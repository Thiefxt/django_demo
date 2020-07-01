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

from celery_tasks.celery_config import CELERY_BACKEND_URL

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings.dev'


# 1.创建celery客户端对象
celery_app = Celery('app', backend=CELERY_BACKEND_URL)

# 2.加载配置信息(将来的任务存取的仓库)
celery_app.config_from_object("celery_tasks.celery_config", namespace='CELERY')
# celery_app.config_from_object('celery_tasks.config')pip

# 3.自动注册异步任务(将来那些异步任务可以仓库中存放)
celery_app.autodiscover_tasks()