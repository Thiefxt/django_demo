"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-10-20 21:53
@Filename			: tasks.py
@Description		: 
@Software           : PyCharm
"""
import time

from celery_tasks.main import celery_app
from celery_tasks.celery_demo.callback_test import MyTask


@celery_app.task(base=MyTask)
def test_celery(num):

    time.sleep(5)
    return num * 100
