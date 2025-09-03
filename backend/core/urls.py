from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.user.urls')),
    path('api/chats/', include('apps.chats.urls')),
    path('api/comments/', include('apps.comments.urls')),
    path('api/followers/', include('apps.followers.urls')),
    path('api/likes/', include('apps.likes.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/posts/', include('apps.posts.urls')),
]
