from django.urls import path 
from .views import *

urlpatterns = [
    path('create/', CreateFollow.as_view(), name="create-follow"),
    path('list/<str:username>/', ListFollowsUser.as_view(), name="list-my-followers"),
    path('delete/<int:id>/', UnFollowUser.as_view(), name="delete-follower"),
]
