from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Country API",
        default_version="v1.0.0",
        description="An API Sysytem to get all details about countries.",
        contact= openapi.Contact(email=""),
        license= openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('country.urls')),
    
    path('', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc'), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)