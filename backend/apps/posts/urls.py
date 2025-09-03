from django.urls import path 
from .views import *

urlpatterns = [
    path('all/', ListAllPost.as_view(), name="list-all-posts"),
    path('create/', CreatePost.as_view(), name="create-post"),
    path('edit/<int:id>/', EditPost.as_view(), name="edit-post"),
    path('delete/<int:id>/', DeletePost.as_view(), name="delete-post"),
    
    path('list/<int:id>/', ListPostsForUser.as_view(), name="list-posts-user"),
    

]
