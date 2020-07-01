"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/30 18:02
@Filename			: book_test_mixin.py
@Description		: 
@Software           : PyCharm
"""
from django.conf import settings

from demo.utils.demo_help import RequestHelp


class TimeAndAttendanceMixin(object):
    """
    考勤取卡mixin
    """

    def __init__(self, request_obj: RequestHelp, params: dict):
        self.request_obj = request_obj
        self.params = params

    def get_attendance_response(self, url):
        """
        获取请求结果
        :return:
        """
        return self.request_obj.get(url, params=self.params)

    def get_attendance_clock(self):
        """
        获取打卡记录
        :return:
        """

        url = settings.ATTENDANCE + "attendance/test/clock"
        return self.get_attendance_response(url)

    def get_attendance_class(self):
        """
        获取班次
        :return:
        """
        url = settings.ATTENDANCE + "attendance/test/class"
        return self.get_attendance_response(url)

    def get_attendance_leave_data(self):
        """
        获取请假/调休/出差
        :return:
        """
        url = settings.ATTENDANCE + "attendance/test/leavedata"
        return self.get_attendance_response(url)



