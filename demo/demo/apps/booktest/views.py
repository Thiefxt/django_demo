import json
import time

from django_redis import get_redis_connection
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from booktest.models import SoOrderGoods, SoOrder
from booktest.serializers import SoOrderSerializer, SoOrderSerializerTset, SoOrderSerializerCher
from demo.utils.my_page import Standard


class UserBrowseHistoryView(GenericAPIView):
    """浏览记录"""
    def get(self, request):
        redis_conn = get_redis_connection("history")
        pl = redis_conn.pipeline()
        user_id = request.query_params.get("user_id")
        goods_id = request.query_params.get("goods_id")
        data_time_now = time.strftime("%Y-%m-%d", time.localtime())
        if redis_conn.hexists("history_%s" % user_id, key=goods_id):
            pl.hmset("history_%s" % user_id, {goods_id: data_time_now})
            # pl.expire("history_%s" % user_id, 60*60*24)  # 设置过期时长
            pl.execute()
        a = redis_conn.hgetall("history_%s" % user_id)
        return Response({"code": 200, "msg": "ok"})


class MyTest(APIView):
    def get(self, request):
        buyer_id = request.query_params.get("buyer_id")
        if not buyer_id:
            return Response({"code": 400, "msg": "参数错误"})
        order = SoOrder.objects.filter(buyer_id=buyer_id)
        serializer = SoOrderSerializer(order, many=True)
        return Response({"code": 200, "msg": "OK", "data": serializer.data})


class CreateOrder(APIView):
    def get(self, request):
        a = {"a": "", "b": ""}
        order = SoOrder.objects.create(
            buyer_id="91",
            shop_id="2",
            parent_id=453453534,
            order_sn=json.dumps([1, 2, 3]),
            order_type="1",
            charge_id="1",
            shopping_id="1",
            status="0",
            goods_count="8",
            is_frozen="0",
            create_time=int(time.time())
        )
        SoOrderGoods.objects.create(
            order=order,
            goods_name=a.get("c", ""),
            count="1",
            money="1.00"
        )

        return Response({"code": 200})


class FilterTest(ListAPIView):

    queryset = SoOrder.objects.filter(buyer_id="2").all()
    serializer_class = SoOrderSerializer

    filter_backends = [OrderingFilter]  # 指定过滤后端为排序过滤
    ordering_fields = ["id", "buyer_id"]    # 指定排序字段


class CheckWXPay(APIView):
    def post(self, request):
        data = request.data
        serializer = SoOrderSerializerTset(data=data)
        serializer.is_valid(raise_exception=True)
        print(data)
        return Response({"data": data})


class Cher(APIView):
    def post(self, request):
        data = SoOrder.objects.filter(buyer_id="99").all()
        serializer = SoOrderSerializerCher(data, many=True)
        return Response(serializer.data)


class MyPage(ListAPIView):
    queryset = SoOrder.objects.all()
    pagination_class = Standard
    serializer_class = SoOrderSerializer