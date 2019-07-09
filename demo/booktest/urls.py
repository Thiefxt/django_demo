"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 6/28/19 22:22
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path
from booktest import views


urlpatterns = [
    path("query", views.MyTest.as_view()),
    path("order", views.CreateOrder.as_view()),
    path("filter", views.FilterTest.as_view()),
]

