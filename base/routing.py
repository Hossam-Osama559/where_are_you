from django.urls import re_path

from . import consumers
websocket_urlpatterns=[

 re_path("new_connection/",consumers.handle_new_client.as_asgi()),

 
]