"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 6/28/19 22:22
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path
from demo.apps.booktest import views

urlpatterns = [
    path("query", views.MyTest.as_view()),
    path("order", views.CreateOrder.as_view()),
    path("filter", views.FilterTest.as_view()),

    path("wx/pay", views.CheckWXPay.as_view()),
    path("order_sn", views.Cher.as_view()),
    path("my/page", views.MyPage.as_view()),
    path("history", views.UserBrowseHistoryView.as_view()),    # 浏览记录
    path("test_values_list", views.TestValuesList.as_view()),

    path("time_attendance", views.TimeAndAttendance.as_view()),
]

