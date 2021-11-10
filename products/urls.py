from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:category_id>/', views.products, name='products'),
    path('product/<int:category_id>/<int:product_id>/',
         views.product, name='product'),
    path('subtotal//<int:product_id>/', views.subtotal, name='subtotal'),
]
