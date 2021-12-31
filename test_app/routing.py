from django.urls import path
from .consumer import WSConsumer


ws_urlpatterns = [
    path('ws/url', WSConsumer.as_asgi()),
]
