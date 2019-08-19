"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 8/8/19 20:29
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from redis_demo import views


urlpatterns = [
    path("redis", views.RedisExpiredMonitoring.as_view()),
]
