"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-29 21:13
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from su_user import views


urlpatterns = [
    path("demo", views.DemoEn.as_view()),
    path("demo1", views.DemoEnt.as_view()),

    path("login", views.JwtDemo.as_view()),         # 生成jwt
    path("user_info", views.UserInfo.as_view()),
    path("register", views.Register.as_view()),
]
