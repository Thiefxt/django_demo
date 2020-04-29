# Create your views here.
import time

from celery.result import AsyncResult
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_redis import get_redis_connection

from celery_tasks.celery_demo.tasks import test_celery
from celery_tasks.main import celery_app


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
