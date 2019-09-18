import re

from django.shortcuts import render

# Create your views here.
from raven.utils.wsgi import get_client_ip
from rest_framework.views import APIView

from su_user.models import SuUsers
from utils.demo_help import CstResponse, RET, Language, judge_mobile, random_nick_name


class Enrollment(APIView):
    """注册单步"""

    def post(self, request):
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        password = request.data.get('password')
        device = request.data.get('device', 'web')
        source = request.META.get('HTTP_SOURCE', 1)
        if not all([mobile, password, code, device]):
            return CstResponse(RET.PARAMERR)
        if not re.match(r"[0-9a-zA-Z~!@#$%^&*?\.+\-,/]{6,16}$", password):
            return CstResponse(RET.DATAERR, Language.get("password_err"))
        if judge_mobile(mobile):
            ct = SuUsers.objects.filter(mobile=mobile).count()
        else:
            return CstResponse(RET.PARAMERR)
        if ct > 0:
            return CstResponse(400, Language.get('user_registered'))
        user_data = {'mobile': mobile}
        # cst_func.verification_code(mobile, code)
        nickname = random_nick_name()
        remote_addr = get_client_ip(request.META)

        return CstResponse(RET.OK, Language.get('register_success'))


class Sign(object):
    __single = None

    def __init__(self):
        self.headers = {}

    def __new__(cls, *args, **kwargs):
        if not cls.__single:
            cls.__single = super().__new__(cls, *args, **kwargs)
        return cls.__single

    def kw(self, **kwargs):
        self.headers.update(kwargs)
        return self.headers


class DemoEn(APIView):
    def get(self, request):
        sign1 = Sign()
        print(sign1.kw(a=random_nick_name()))
        print(id(sign1))
        return CstResponse(RET.OK)


class DemoEnt(APIView):
    def get(self, request):
        sign1 = Sign()
        print(sign1.kw(b=random_nick_name()))
        print(id(sign1))
        return CstResponse(RET.OK)
