# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_redis import get_redis_connection


class RedisExpiredMonitoring(GenericAPIView):
    """redis key 过期监控事件"""

    def get(self, request):
        redis_conn = get_redis_connection("user_ex")
        pl = redis_conn.pipeline()
        access_token = redis_conn.get("WX_BASE_ACCESS_TOKEN")
        jsapi = redis_conn.get("WEIXIN_JS_API_TICKET")
        if access_token:
            print(access_token.decode())
        if jsapi:
            print(jsapi.decode())
        # pl.setex("name", 10, "xiao")
        # pl.execute()
        # name = redis_conn.get("name")
        # print(name.decode())
        return Response({"test": None})
