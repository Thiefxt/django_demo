"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/17 16:20
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]