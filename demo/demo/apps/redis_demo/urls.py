"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 8/8/19 20:29
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from demo.apps.redis_demo import views

urlpatterns = [
    path("redis", views.RedisExpiredMonitoring.as_view()),
    path("redis/demo", views.RedisDemo.as_view()),


    path("celery_test", views.CeleryTest.as_view()),
    path("redis", views.TestRedis.as_view()),

    path("cycle_analysis", views.ActualCycleAnalysis.as_view()),
]
