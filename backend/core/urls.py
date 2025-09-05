from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PetConnect API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de tus apps
    path('api/auth/', include('apps.user.urls')),
    path('api/chats/', include('apps.chats.urls')),
    path('api/comments/', include('apps.comments.urls')),
    path('api/followers/', include('apps.followers.urls')),
    path('api/likes/', include('apps.likes.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/posts/', include('apps.posts.urls')),

    # Solo Swagger UI (sin redoc y sin info personalizada)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]