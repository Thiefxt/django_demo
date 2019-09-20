# Create your views here.
import time

import jwt
from rest_framework.views import APIView

from demo import settings
from su_user.models import SuUsers
from su_user.serializers import UserInfoSerializer
from utils.auth_user import PCAuthentication
from utils.demo_help import CstResponse, RET, random_nick_name
from utils.set_jwt import set_token


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

    def post(self, request):
        token_dict = {
            "user_id": 1,
            'iat': int(time.time()),
            'user_name': 'lowman',
            'exp': int(time.time() + 60*60)
        }
        token = jwt.encode(token_dict, settings.SECRET_KEY, algorithm='HS256')
        return CstResponse(RET.OK, data={"user_id": 1, "user_name": "lowman", "token": token})


class UserInfo(APIView):
    authentication_classes = [PCAuthentication]

    def get(self, request):
        user = request.user
        user_info = UserInfoSerializer(user).data
        return CstResponse(RET.OK, data=user_info)


class Register(APIView):

    def post(self, request):
        mobile = request.data.get("mobile")
        password = request.data.get("password")
        if not all([password, mobile]):
            return CstResponse(RET.PARAMERR)
        user = SuUsers.objects.filter(mobile=mobile).first()
        if user:
            return CstResponse(RET.MOBILE_ERR)
        user = SuUsers.objects.create(
            mobile=mobile,
            nick_name="Thief",
            status="1",
            reg_time=int(time.time()),
            register_source=1
        )
        user.set_password(password)
        user.save()

        data = set_token(user)
        return CstResponse(RET.OK, data=data)

