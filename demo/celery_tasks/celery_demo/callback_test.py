"""
@Author				: Thief
@Email				: 18773993654@163.com
@Lost modifid		: 20-4-28 03:38
@Filename			: callback_test.py
@Description		: 
@Software           : PyCharm
"""
import celery


class MyTask(celery.Task):

    #  # 任务失败时执行
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    # # 任务成功时执行
    def on_success(self, retval, task_id, args, kwargs):
        print(task_id, retval, "-----------------")

    # 任务重试时执行
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass
