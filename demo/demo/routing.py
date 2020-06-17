"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/17 16:29
@Filename			: routing.py
@Description		: 
@Software           : PyCharm
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})