from django.urls import path 
from .views import *

urlpatterns = [
    path('list/<int:id>/', ListLikeForPost.as_view(), name="list-likes"),
    path('create/', CreateLike.as_view(), name="create-like"),
    path('delete/<int:id>/', DeleteLike.as_view(), name="delete-like"),
]
