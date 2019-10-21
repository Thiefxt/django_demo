"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-10-20 21:38
@Filename			: main.py
@Description		: 
@Software           : PyCharm
"""
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

# 1.创建celery客户端对象
celery_app = Celery('app')

# 2.加载配置信息(将来的任务存取的仓库)
celery_app.config_from_object('celery_tasks.config')

# 3.自动注册异步任务(将来那些异步任务可以仓库中存放)
celery_app.autodiscover_tasks(['celery_tasks.celery_demo'])