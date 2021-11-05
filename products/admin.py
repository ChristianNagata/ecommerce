from django.contrib import admin
from .models import Category, Clothe, Product, SubCategory, Supplement


admin.site.register(Clothe)
admin.site.register(Supplement)
admin.site.register(Category)
admin.site.register(SubCategory)
