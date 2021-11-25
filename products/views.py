from rest_framework import serializers, status, viewsets, filters, permissions, authentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from products.serializer import ProductSerializer
from .models import Product
from .forms import ClotheForm
from random import randint


def index(request):
    """Página inicial com todos os produtos"""
    page_name = 'Home'

    context = {'page_name': page_name}
    return render(request, 'products/index.html', context)


def products(request, category_id):
    """Todos os produtos"""
    products = Product.objects.all()
    page_name = 'Products'

    context = {'page_name': page_name,
               'products': products, 'category_id': category_id}
    return render(request, 'products/products.html', context)


def product(request, category_id, product_id):
    """Página do produto"""
    product_info = Product.objects.get(id=product_id)
    page_name = 'Product'

    # Faz a seleção de produtos recomendados
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

    context = {
        'page_name': page_name,
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
    page_name = 'Subtotal'

    context = {
        'title': 'Página de resumo',
        'cart': cart,
        'page_name': page_name
    }
    return render(request, 'products/subtotal.html', context)


class ProductViewSet(viewsets.ModelViewSet):
    """Define o comportamento da view da API"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', ]
    search_fields = ['name', ]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(
                serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
