"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-10-20 21:41
@Filename			: config.py
@Description		: 
@Software           : PyCharm
"""
from celery.schedules import crontab


# celery配置文件
# 指定任务队列存取位置
CELERY_BROKER_URL = "redis://127.0.0.1:6379/7"

# # 使用redis存储结果
BACKEND_URL = 'redis://127.0.0.1:6379/6'      # 结果存储


CELERY_BACKEND_URL = 'redis://127.0.0.1:6379/8'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# # 时区设置
# timezone = 'Asia/Shanghai'
# celery默认开启自己的日志
# False表示不关闭
# worker_hijack_root_logger = False
# # 存储结果过期时间，过期后自动删除
# # 单位为秒
# result_expires = 60 * 60 * 24
#
# imports = [
#     'celery_tasks.celery_demo.tasks'
# ]
#
# beat_schedule = {
#     'tasks': {
#         # 具体需要执行的函数
#         # 该函数必须要使用@app.task装饰
#         'task': 'celery_tasks.celery_demo.tasks.celery_test',
#         # 定时时间
#         # 每分钟执行一次，不能为小数
#         'schedule': crontab(minute='*/1'),
#         # 或者这么写，每小时执行一次
#         # "schedule": crontab(minute=0, hour="*/1")
#         # 执行的函数需要的参数
#         'args': (1, 2)
#     }
# }