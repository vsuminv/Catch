import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import mentor.routing
# from .. import mentor
# from .. import mentor
# from .. import mentor
# from ..mentor import routing
# from Catch import mentor
# from Catch.mentor import routing


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            mentor.routing.websocket_urlpatterns
        )
    ),
})