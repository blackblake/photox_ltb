# image_repo_backend/urls.py
from django.contrib import admin
from django.urls import path, include
# 用于开发环境处理媒体文件访问
from django.conf import settings
from django.conf.urls.static import static

# --- Swagger ---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Photox API",
        default_version='v1',
        description="Photox 项目 API 文档",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@example.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), # 允许任何人访问 API 文档
)
# --- Swagger End ---

urlpatterns = [
    path('admin/', admin.site.urls),

    # 包含 users 应用的 URL，并添加 'api/v1/auth/' 前缀
    path('api/v1/auth/', include('users.urls', namespace='users')), # 使用 namespace='users'

    # 你之后可以添加其他应用的 URL
    # path('api/v1/images/', include('images.urls', namespace='images')),
    # path('api/v1/albums/', include('albums.urls', namespace='albums')),
    # path('api/v1/community/', include('community.urls', namespace='community')),

    # Swagger API 文档路由
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

# 开发环境下，允许 Django 托管用户上传的媒体文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)