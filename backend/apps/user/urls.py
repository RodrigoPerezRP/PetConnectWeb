from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import (
    CreateUser,
    ListUsers,
    GetUser,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="access_token"),
    path('refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('verify/', TokenVerifyView.as_view(), name="verify-token"),
    path('register/', CreateUser.as_view(), name="register"),
    path('list/', ListUsers.as_view(), name="list-users"),
    path('get/<slug:slug>/', GetUser.as_view(),name="get-user"),
]
