from django.contrib import admin
from .models import Category, Product, SubCategory


class Products(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'sub_category'
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 10


admin.site.register(Product, Products)
admin.site.register(Category)
admin.site.register(SubCategory)
