"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-10-20 21:53
@Filename			: tasks.py
@Description		: 
@Software           : PyCharm
"""
from celery_tasks.main import celery_app


@celery_app.task(name='celery_demo')
def celery_test(num1, num2):
    print("celery 被执行了", num1, num2)
