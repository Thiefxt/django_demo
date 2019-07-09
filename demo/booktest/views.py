import time

from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

# Create your views here.
from booktest.models import SoOrderGoods, SoOrder
from booktest.serializers import SoOrderSerializer


class MyTest(APIView):
    def get(self, request):
        order = SoOrder.objects.filter(buyer_id="2")
        serializer = SoOrderSerializer(order, many=True)
        return Response(serializer.data)


class CreateOrder(APIView):
    def get(self, request):
        order = SoOrder.objects.create(
            buyer_id="2",
            shop_id="2",
            parent_id=1234567894,
            order_sn="5468435151",
            order_type="1",
            charge_id="1",
            shopping_id="1",
            status="1",
            goods_count="8",
            is_frozen="0",
            create_time=int(time.time())
        )
        SoOrderGoods.objects.create(
            order=order,
            goods_name="名片",
            count="1",
            money="1.00"
        )

        return Response({"code": 200})


class FilterTest(ListAPIView):

    queryset = order = SoOrder.objects.filter(buyer_id="2").all()
    serializer_class = SoOrderSerializer

    filter_backends = [OrderingFilter]  # 指定过滤后端为排序过滤
    ordering_fields = ["id", "buyer_id"]    # 指定排序字段
