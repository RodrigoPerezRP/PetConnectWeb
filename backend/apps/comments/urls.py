from django.urls import path
from .views import *

urlpatterns = [
    path('list/<int:id>/', ListCommentsPost.as_view(), name="list"),
    path('create/', CreateComment.as_view(), name="create"),
    path('edit/<int:id>/', EditComment.as_view(), name="edit"),
    path('delete/<int:id>/', DeleteComment.as_view(), name="delete"),
]
