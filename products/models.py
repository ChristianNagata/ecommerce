from django.db import models


class Product(models.Model):
    """Todos os tributos de um produto"""
    name = models.CharField(max_length=40)
    details = models.TextField()
    category = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
