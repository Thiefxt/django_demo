# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class RedisExpiredMonitoring(GenericAPIView):
    """redis key 过期监控事件"""

    def get(self, request):
        return Response({})
