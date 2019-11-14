"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-9-19 21:02
@Filename			: set_jwt.py
@Description		: 
@Software           : PyCharm
"""
import time

import jwt

from demo import settings


def set_token(user):
    token_dict = {
        "user_id": user.user_id,
        'iat': int(time.time()),
        'user_name': user.nick_name,
        'exp': int(time.time() + 60 * 60)
    }
    token = jwt.encode(token_dict, settings.SECRET_KEY, algorithm='HS256')

    return {"user_id": user.user_id, "user_name": user.nick_name, "token": token}
