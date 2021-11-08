from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from .forms import ClotheForm


class Category(models.Model):
    """Categoria proncipal do produto"""
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.category


class SubCategory(models.Model):
    """Categoria de cada produto produtos"""
    sub_category = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'sub-categories'

    def __str__(self) -> str:
        return self.sub_category


class Product(models.Model):
    """Todos os tributos de um produto"""

    category = models.ForeignKey(
        Category, on_delete=CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=CASCADE, blank=True)
    name = models.CharField(max_length=40)
    details = models.TextField()
    price = models.FloatField()
    image = models.ImageField(
        upload_to='images/%d/%m/%Y', blank=True)

    def __str__(self) -> str:
        return self.name
