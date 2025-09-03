from django.urls import path 
from .views import GetMessagesOfChat

urlpatterns = [
    path('get/<int:id>/', GetMessagesOfChat.as_view(), name="get-messages-of-chat"),
]
