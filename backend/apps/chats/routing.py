from django.urls import path 
from .consumers import WSConsumer


ws_urlpatterns = [
    path('ws/send-message/', WSConsumer.as_asgi())
]