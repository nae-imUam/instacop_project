# screensharing/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/screen_sharing/(?P<room_name>\w+)/$', consumers.ScreenSharingConsumer.as_asgi()),
]
