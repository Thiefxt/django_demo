"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-29 21:43
@Filename			: auth_user.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework import authentication

from utils.demo_help import CstException, RET


class PCAuthentication(authentication.BaseAuthentication):
    """
    PC Login authentication
    """
    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION')

        if not authorization:
            raise CstException(RET.SESSIONERR)
        # TODO
