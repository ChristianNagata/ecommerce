from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:category_id>/', views.products, name='products'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('subtotal/', views.subtotal, name='subtotal'),
    path('myproducts/', views.myproducts, name='myproducts'),
]
