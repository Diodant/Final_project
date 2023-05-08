from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from backend.views import MyLogin

schema_view = get_schema_view(
    openapi.Info(
        title="API documentations",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/login/', MyLogin.as_view()),
    path('accounts/', include('allauth.urls')),

    path('', include('backend.urls')),
]
