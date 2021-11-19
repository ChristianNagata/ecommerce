from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from products.views import ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products-vs', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('user/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
