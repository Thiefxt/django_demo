# Create your views here.
import json
import time

from celery.result import AsyncResult
from django.db import connections
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_redis import get_redis_connection

from celery_tasks.celery_demo.tasks import test_celery
from celery_tasks.main import celery_app
from demo.utils.db_utils import dict_fetchall
from demo.utils.demo_help import CstResponse, RET


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
        sql = f"""select Circle from Plc_MinStatistics  where Itemcode = 'ZWP12284A' and PassTime between '2020-06-04 20:00:00' and '2020-06-05 08:00:00'order by PassTime desc"""
        with connections['mes'].cursor() as cursor:
            cursor.execute(sql)  # -- 产品编号，实际出模数，机台号，产品名称,  生产总数
            rows = dict_fetchall(cursor)
        print(rows)
        return CstResponse(RET.OK)
