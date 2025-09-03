from django.urls import path 
from .views import *

urlpatterns = [
    path('list/<int:id>/', ListNotificationsForUser.as_view()),
    path('create/', CreateNotification.as_view()),
]
