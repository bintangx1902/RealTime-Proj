from django.urls import path
from .consumer import WSConsumer


ws_urlpatterns = [
    path('ws', WSConsumer.as_asgi()),
]
