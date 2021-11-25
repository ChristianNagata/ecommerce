from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import base
from products.views import ProductViewSet
from user.views import UserViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Energym",
        default_version='v1',
        description="Ecommerce for fit products",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='Products')
router.register(r'users', UserViewSet, basename='Users')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('ctrlcenter/', admin.site.urls),
    path('', include('products.urls')),
    path('user/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('root/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
