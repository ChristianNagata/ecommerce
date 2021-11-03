from django.shortcuts import render
from .models import Product


def index(request):
    """Página inicial com todos os produtos"""
    page_name = 'Página inicial'
    context = {'page_name': page_name}
    return render(request, 'products/index.html', context)


def products(request):
    """Todos os produtos"""
    products = Product.objects.all()
    page_name = 'Todos os produtos'
    context = {'page_name': page_name, 'products': products}
    return render(request, 'products/products.html', context)


def product(request, product_id):
    """Página do produto"""
    product_info = Product.objects.get(id=product_id)
    page_name = 'Produto'
    context = {'page_name': page_name, 'info': product_info}
    return render(request, 'products/product.html', context)


def myproducts(request):
    """Refere-se ao chamado 'carrinho'"""
    pass
