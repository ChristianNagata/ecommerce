from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    page_name = 'Página inicial'
    context = {'page_name': page_name, 'products': products}
    return render(request, 'products/index.html', context)


def product(request, product_id):
    product_info = Product.objects.get(id=product_id)
    page_name = 'Produto'
    context = {'page_name': page_name, 'info': product_info}
    return render(request, 'products/product.html', context)
