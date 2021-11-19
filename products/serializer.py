from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'sub_category'
        )

    def validate_name(self, name):
        if not name.isalpha():
            raise serializers.ValidationError('Product name should be alpha')
        return name

    def validate_price(self, price):
        if not price.isdecimal():
            raise serializers.ValidationError(
                'Product price should be decimal')
        return price
