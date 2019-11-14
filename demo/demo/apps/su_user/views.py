# Create your views here.
import re
import time

from rest_framework.views import APIView

from su_user.models import SuUsers
from su_user.serializers import UserInfoSerializer
from demo.utils.auth_user import PCAuthentication
from demo.utils.demo_help import CstResponse, RET, random_nick_name
from demo.utils.set_jwt import set_token


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


class JwtDemo(APIView):
    """登录"""
    def post(self, request):
        # celery_test.delay(10, 20)
        data = request.data
        mobile = data.get("mobile")
        password = data.get("password")
        if not all([mobile, password]):
            return CstResponse(RET.PARAMERR)
        if not re.match(r"'^0\d{2,3}\d{7,8}$|^1[3-9]\d{9}$|^147\d{8}$'", mobile):
            return CstResponse(RET.DATAERR, "手机号输入错误")

        user = SuUsers.objects.filter(mobile=mobile).first()
        if not user:
            return CstResponse(RET.USERERR)
        if not user.verification_password(password):
            return CstResponse(RET.PWDERR)
        if user.status != 1:
            return CstResponse(RET.USER_STATUS)

        data_dict = set_token(user)
        return CstResponse(RET.OK, "登录成功", data=data_dict)


class UserInfo(APIView):
    authentication_classes = [PCAuthentication]

    def get(self, request):
        """用户信息"""
        user = request.user
        user_info = UserInfoSerializer(user).data
        return CstResponse(RET.OK, data=user_info)


class Register(APIView):
    """注册"""

    def post(self, request):
        mobile = request.data.get("mobile")
        password = request.data.get("password")
        if not all([password, mobile]):
            return CstResponse(RET.PARAMERR)
        if not re.match(r"^0\d{2,3}\d{7,8}$|^1[3-9]\d{9}$|^147\d{8}$", mobile):
            return CstResponse(RET.DATAERR, "手机号输入错误")
        if not re.match(r"[0-9a-zA-Z~!@#$%^&*?\.+\-,/]{6,16}$", password):
            return CstResponse(RET.DATAERR, "密码格式错误")
        user = SuUsers.objects.filter(mobile=mobile).first()
        if user:
            return CstResponse(RET.MOBILE_ERR)
        # with transaction.atomic():
        user = SuUsers.objects.create(
            mobile=mobile,
            nick_name="Thief",
            status="1",                 # 用户状态,1[激活],2[冻结]
            reg_time=int(time.time()),  # 注册时间
            register_source=1           # 注册来源
        )
        user.set_password(password)
        user.save()

        data = set_token(user)
        return CstResponse(RET.OK, "注册成功", data=data)

