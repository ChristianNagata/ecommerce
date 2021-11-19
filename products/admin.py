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


class Categories(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id', 'category')
    search_fields = ('id', 'category')
    list_per_page = 10


class SubCategories(admin.ModelAdmin):
    list_display = ('id', 'sub_category')
    list_display_links = ('id', 'sub_category')
    search_fields = ('id', 'sub_category')
    list_per_page = 10


admin.site.register(Product, Products)
admin.site.register(Category, Categories)
admin.site.register(SubCategory, SubCategories)
