import json
import time

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView

from orders.models import SoOrder, SoOrderGoods
from utils.demo_help import parameter_check


class OrderSettlementView(GenericAPIView):
    """结算订单"""
    serializer_class = ""

    def post(self, request):
        pass


class CommitOrderView(GenericAPIView):
    """保存订单"""
    serializer_class = ""
    permission_classes = []

    def post(self, request):
        request_data = parameter_check(self.get_serializer, request)
        user_id = request.user.user_id
        order = SoOrder.objects.create(
            buyer_id=user_id,
            shop_id="2",
            parent_id=453453534,
            order_sn=SoOrder.create_order_sn(),
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
            goods_name="",
            count="1",
            money="1.00"
        )
