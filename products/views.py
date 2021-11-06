from typing import ContextManager
from django.shortcuts import redirect, render
from .models import Product
from .forms import ClotheForm


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

    if request.method == 'POST':
        form = ClotheForm(request.POST)
        if form.is_valid():
            return redirect('/subtotal/')
    else:
        form = ClotheForm()

    page_name = 'Produto'
    context = {'page_name': page_name,
               'info': product_info,
               'form': form,
               'sub_category': str(product_info.sub_category),
               }
    return render(request, 'products/product.html', context)


def subtotal(request):
    """Página de resumo da compra"""
    context = {'title': 'Página de resumo'}
    return render(request, 'products/subtotal.html', context)


def myproducts(request):
    """Carrinho"""
    pass
