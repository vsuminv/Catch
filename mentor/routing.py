# chat/routing.py
from django.urls import re_path

from . import consumers
# from Catch.mentor import consumers

websocket_urlpatterns = [
    re_path(r'ws/mentor/mentor_chatrooms/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]