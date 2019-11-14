"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 6/28/19 23:40
@Filename			: serializers.py
@Description		: 
@Software           : PyCharm
"""
import json

from rest_framework import serializers

from booktest.models import SoOrderGoods, SoOrder


class SoOrderGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoOrderGoods
        fields = "__all__"


class SoOrderSerializer(serializers.ModelSerializer):
    # order 命名必须是model里面related_name的值否则就要为模型名小写_set如soordergoods_set
    order = SoOrderGoodsSerializer(many=True)

    class Meta:
        model = SoOrder
        fields = "__all__"


class SoOrderSerializerTset(serializers.Serializer):
    buyer_id = serializers.IntegerField(required=False)

    def validate(self, attrs):
        return attrs


class SoOrderSerializerCher(serializers.ModelSerializer):
    order_sn = serializers.SerializerMethodField()

    def get_order_sn(self, obj):
        return json.loads(obj.order_sn)

    class Meta:
        model = SoOrder
        exclude = ["resource"]


class UserBrowseHistorySerializer(serializers.Serializer):
    """用户浏览记录序列化器"""
    goods_id = serializers.IntegerField(label="商品id", min_value=1)

    def create(self, validated_data):
        pass
