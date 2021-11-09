from typing import ContextManager
from django.shortcuts import redirect, render
from .models import Product
from .forms import ClotheForm
from random import sample, randint


def index(request):
    """Página inicial com todos os produtos"""
    page_name = 'Página inicial'
    context = {'page_name': page_name}
    return render(request, 'products/index.html', context)


def products(request, category_id):
    """Todos os produtos"""
    products = Product.objects.all()
    page_name = 'Todos os produtos'
    context = {'page_name': page_name,
               'products': products, 'category_id': category_id}
    return render(request, 'products/products.html', context)


def product(request, category_id, product_id):
    """Página do produto"""
    product_info = Product.objects.get(id=product_id)

    count = Product.objects.filter(category_id=category_id).count()
    index = randint(3, count)
    recommended = Product.objects.all().filter(
        category_id=category_id)[index-3:index]

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
               'recommended': recommended,
               }
    return render(request, 'products/product.html', context)


def subtotal(request):
    """Página de resumo da compra"""
    context = {'title': 'Página de resumo'}
    return render(request, 'products/subtotal.html', context)
