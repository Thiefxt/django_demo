"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-29 21:14
@Filename			: demo_help.py
@Description		: 
@Software           : PyCharm
"""
import random
import re
import traceback

from rest_framework.views import exception_handler as drf_exception_handler
from django.db import DatabaseError
from redis.exceptions import RedisError
from django.conf import settings
import logging
from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
import json


logger = logging.getLogger(__name__)


class CstResponse(Response):

    def __init__(self, code, message=None, data=None, **kwargs):
        """
        自定义返回数据
        :param data: 返回数据
        :param code: 返回状态码
        :param message: 返回消息
        """
        if not message:
            message = Language.get(code)

        dic_data = dict(
            code=int(code),
            msg=message
        )
        if data:
            dic_data['data'] = data
        else:
            dic_data['data'] = None
        super(CstResponse, self).__init__(dic_data, **kwargs)


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        msg = '{}-{}\n GET {}\n POST {}'.format(request.path, request.method, json.dumps(request.GET),
                                            request.body.decode('utf8'))
        logger.info(msg)

    def process_response(self, request, response):
        # msg = '{} {}: {}'.format(request.path, request.method, json.dumps(response.data))
        # logger.info(response.content.decode('utf8'))
        logger.info(str(response.content))
        return response


class CstException(Exception):
    """
    业务异常类
    """
    def __init__(self, code, message=None):
        self.code = code
        self.message = message
        super(CstException, self).__init__()


class ValidationError(Exception):
    """
    业务异常类
    """
    def __init__(self, code, message=None):
        self.code = code
        self.message = message
        super(ValidationError, self).__init__()


def exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常
    :param context: 异常上下文
    :return: Response响应对象
    """
    response = drf_exception_handler(exc, context)

    if response is None:
        errmsg = None
        if settings.DEBUG:
            errmsg = str(exc)
        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            # 数据库异常
            logger.error(traceback.format_exc())
            response = CstResponse(RET.DBERR, errmsg)
        elif isinstance(exc, CstException):
            response = CstResponse(exc.code, exc.message)
        elif isinstance(exc, ValidationError):
            response = CstResponse(exc.code, exc.message)
        else:
            logger.error(traceback.format_exc())
            response = CstResponse(RET.SERVERERR, errmsg)

    return response


class RET:
    """
    语言类包
    """
    OK = "200"
    DBERR = "501"
    NODATA = "462"
    DATAEXIST = "503"
    DATAERR = "499"
    SESSIONERR = "411"
    LOGINERR = "412"
    PARAMERR = "503"
    USERERR = "404"
    ROLEERR = "415"
    PWDERR = "416"
    SMSERR = "517"
    REQERR = "521"
    IPERR = "422"
    THIRDERR = "431"
    IOERR = "502"
    SERVERERR = "500"
    UNKNOWERR = "451"
    PERMISSION_ON = "410"
    REQUEST_ERR = "417"
    USER_ERR = "406"
    USER_INFO_ERR = "407"
    MOBILE_ERR = "408"
    EMAIL_ERR = "409"
    ERROR = "466"
    USER_STATUS = "465"


# 元组中第一个为中文，第二个为英文，第三个为繁体
language_pack = {
    RET.OK: ("成功",),
    RET.DBERR: ("数据库查询错误",),
    RET.NODATA: ("无数据",),
    RET.DATAEXIST: ("数据已存在",),
    RET.DATAERR: ("数据格式错误",),
    RET.SESSIONERR: ("用户未登录",),
    RET.LOGINERR: ("用户登录失败",),
    RET.PARAMERR: ("参数错误",),
    RET.USERERR: ("用户不存在或未激活",),
    RET.ROLEERR: ("用户未登录",),
    RET.PWDERR: ("你输入的当前登录密码不正确",),
    RET.REQERR: ("非法请求或请求次数受限",),
    RET.IPERR: ("IP受限",),
    RET.THIRDERR: ("第三方系统错误",),
    RET.IOERR: ("文件读写错误",),
    RET.SERVERERR: ("内部错误",),
    RET.UNKNOWERR: ("未知错误",),
    RET.SMSERR: ("短信失败",),
    RET.PERMISSION_ON: ("没有权限",),
    RET.REQUEST_ERR: ("非法请求或非法地址",),
    RET.USER_ERR: ("用户注册失败，请稍后重试",),
    RET.USER_INFO_ERR: ("用户信息获取失败",),
    RET.MOBILE_ERR: ("手机号已被注册请重新输入",),
    RET.EMAIL_ERR: ("邮箱已被注册请重新输入",),
    RET.USER_STATUS: ("账号已被禁用，如有疑义请联系平台客服",),
    "network_error": ("网络异常，请稍候再试",),
}


class Language(object):

    _lang ='zh_cn'

    @classmethod
    def init(cls, lang):
        cls._lang = lang

    @classmethod
    def get(cls, value):
        lang = language_pack.get(value)
        if not lang:
            return None
        if cls._lang == 'zh_cn' and len(lang) > 0:
            return lang[0]
        elif cls._lang == 'en_US' and len(lang) > 1:
            return lang[1]
        elif cls._lang == 'zh_F' and len(lang) > 2:
            return lang[2]


def random_str(length):
    """
    随机生成长度为 length,范围是 0～9|a-z|A-Z 的字符串
    :param length: 长度
    :return:
    """
    rand_char = list(range(ord('a'), ord('z'))) + list(range(ord('A'), ord('Z'))) + list(range(ord('0'), ord('9')))
    s = []
    for n in range(length):
        x = random.choice(rand_char)
        s.append(chr(x))
    return ''.join(s)


def judge_mobile(mobile):
    if len(mobile) == 11:
        rp = re.compile('^0\d{2,3}\d{7,8}$|^1[3-9]\d{9}$|^147\d{8}$')
        phone_match = rp.match(mobile)
        if phone_match:
            return True
        else:
            return False
    else:
        return False


def judge_email(email):
    re_email = re.compile(r"^[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?$")
    if re_email.match(email):
        return True
    else:
        return False


def random_nick_name():
    """
    获取昵称:前2位小写字母，后两位数字
    :return:
    """
    rand_char = range(ord('a'), ord('z'))
    s = []
    for n in range(2):
        x = random.choice(rand_char)
        s.append(chr(x))
    rand_char = range(0, 9)
    for n in range(6):
        x = random.choice(rand_char)
        s.append(str(x))
    return ''.join(s)


def parameter_check(serializer, request):
    """
    Parameter check
    :param serializer:
    :param request:
    :return:
    """
    if request.method == "GET" or request.method == "DELETE":
        data_req = request.query_params
    elif request.method == "POST" or request.method == "PUT":
        data_req = request.data
    else:
        raise CstException(RET.REQERR)
    serializer = serializer(data=data_req)
    serializer.is_valid(raise_exception=True)
    data_dict = serializer.data
    return data_dict
