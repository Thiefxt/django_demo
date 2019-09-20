"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-29 21:21
@Filename			: serializers.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework import serializers

from su_user.models import SuUsers


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuUsers
        fields = "__all__"
