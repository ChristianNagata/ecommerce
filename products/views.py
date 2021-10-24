from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)


def product(request, product_id):
    product_info = Product.objects.get(id=product_id)
    context = {'info': product_info}
    return render(request, 'products/product.html', context)
