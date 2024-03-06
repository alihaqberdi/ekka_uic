from rest_framework import serializers
from simple_product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'text', 'price', 'count', 'category')
