from django.shortcuts import redirect, render
from rest_framework import authentication
from rest_framework import permissions
from products.serializer import ProductSerializer
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .forms import ClotheForm
from random import randint
from django.contrib.auth.decorators import login_required


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


@login_required
def subtotal(request, product_id):
    """Página de resumo da compra"""
    cart = Product.objects.all().filter(id=product_id)
    context = {
        'title': 'Página de resumo',
        'cart': cart,
    }
    return render(request, 'products/subtotal.html', context)


class ProductViewSet(viewsets.ModelViewSet):
    """Define o comportamento da view da API"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #authentication_classes = [BaseAuthentication]
    #permission_classes = [IsAuthenticated]
