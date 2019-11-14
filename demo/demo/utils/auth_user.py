"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-29 21:43
@Filename			: auth_user.py
@Description		: 
@Software           : PyCharm
"""
import jwt
from rest_framework import authentication

from demo import settings
from su_user.models import SuUsers
from demo.utils.demo_help import CstException, RET


class PCAuthentication(authentication.BaseAuthentication):
    """
    PC Login authentication
    """
    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION')

        if not authorization:
            raise CstException(RET.SESSIONERR)
        try:
            token_dict = jwt.decode(authorization, settings.SECRET_KEY, algorithms=['HS256'])
        except Exception as e:
            raise CstException(RET.SESSIONERR)

        user = SuUsers.objects.filter(user_id=token_dict.get("user_id")).first()
        if not user:
            raise CstException(RET.USERERR)

        return user, None
