"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/10/23 14:36
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from file_demo import views


urlpatterns = [
    path("pdf_demo", views.PdfDemo.as_view()),
]
