# Create your views here.
import datetime
import json
import time
import uuid
from pprint import pprint

from celery.result import AsyncResult
from django.db import connections
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_redis import get_redis_connection

from celery_tasks.celery_demo.tasks import test_celery
from celery_tasks.main import celery_app
from demo.utils.db_utils import dict_fetchall, cursor_execute
from demo.utils.demo_help import CstResponse, RET
from lib_algorithm.data_process import data_filtering


class RedisDistributedLocks(GenericAPIView):
    """redis 分布式"""

    def post(self, request):
        goods_id = request.data.get("goods_id")

        redis_conn = get_redis_connection("inventory")
        pl = redis_conn.pipeline()
        client_id = str(uuid.uuid1())
        pl.setnx(goods_id, client_id)
        pl.expire(goods_id, 10)
        result = pl.execute()        # 执行管道
        if not result[0]:
            return Response("网络异常，请稍后重试")
        try:
            stock = int(redis_conn.get("stock").decode("utf-8"))
            if stock > 0:
                stock -= 1
                redis_conn.set("stock", stock)
                print("扣减成功，库存剩余：{}".format(stock))
            else:
                print("库存不足，扣减失败")
        finally:
            goods_id_bit = redis_conn.get(goods_id)
            if goods_id_bit:
                client_id_str = goods_id_bit.decode("utf-8")
                if client_id == client_id_str:
                    redis_conn.delete(goods_id)

        return Response("ok")


class RedisExpiredMonitoring(GenericAPIView):
    """redis key 过期监控事件"""

    def get(self, request):

        redis_conn = get_redis_connection("user_ex")
        # pl = redis_conn.pipeline()
        access_token = redis_conn.get("name")
        jsapi = redis_conn.get("WEIXIN_JS_API_TICKET")
        if access_token:
            print(access_token.decode())
        if jsapi:
            print(jsapi.decode())
        redis_conn.setex("name", 60, "tao")
        # pl.execute()
        name = redis_conn.get("name")
        print(name.decode())
        return Response({"test": None})


class RedisDemo(GenericAPIView):

    def get(self, request):
        redis_conn = get_redis_connection("user_ex")
        key = 'VERIFICATE_CODE' + "18773993654"
        redis_conn.set(key, {"expire_time": (time.time() + 60,), "code": "123456"})
        a = redis_conn.get(key)
        print(a)
        redis_conn.delete(key)
        return Response({"code": 200})


class CeleryTest(GenericAPIView):

    def get(self, request):
        res = test_celery.delay(10)
        for i in range(10):
            time.sleep(0.5)
            async_task = AsyncResult(id=res.id, app=celery_app)
            print("async_task.id", async_task.id)
            if async_task.successful():
                result = async_task.get()
                print(result)
                print("执行成功")
                break
            else:
                print("任务还未执行完成")

        return Response({"code": 200, "msg": "ok"})


class TestRedis(GenericAPIView):

    def get(self, request):
        machine_loss_time = 0
        remarks = ""
        line_name = "p3"
        under_loss_time = 1
        under_remarks = "我的"
        under_item_code = "b-31"
        redis_conn = get_redis_connection('default')
        time_redis = redis_conn.hget(line_name, under_item_code)
        if time_redis:
            time_redis = json.loads(time_redis.decode("utf-8"))
            machine_loss_time += float(time_redis.get("under_loss_time"))
            remarks += time_redis.get("under_remarks")
            redis_conn.hdel(line_name, under_item_code)
        if under_loss_time:
            redis_conn.hset(line_name, under_item_code,
                            json.dumps({"under_loss_time": under_loss_time, "under_remarks": under_remarks}))
            redis_conn.expire(line_name, 60 * 60)
        return Response("ok")


class ActualCycleAnalysis(GenericAPIView):
    """
    实际周期分析
    """

    def get(self, request):
        # sql = f"""-- select Circle from Plc_MinStatistics  where Itemcode = 'ZWP12063A' and PassTime between '2020-06-04 20:00:00' and '2020-06-05 08:00:00'order by PassTime desc"""
        sql = f"""select  Circle from Plc_MinStatistics  where Itemcode = '16057-B05' and Circle <> 0 and Circle is not null order by PassTime desc"""
        with connections['mes'].cursor() as cursor:
            cursor.execute(sql)
            rows = [list(i) for i in cursor.fetchall()]
        a = data_filtering(rows)
        print(a / 10)
        return CstResponse(RET.OK)
