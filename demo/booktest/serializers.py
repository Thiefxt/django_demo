"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 6/28/19 23:40
@Filename			: serializers.py
@Description		: 
@Software           : PyCharm
"""
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



