from rest_framework import serializers
from simple_product.models import Product, Category, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "id",
            "product",
            "image"
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "parent"
        )


class ProductListAPIViewSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "title",
            "slug",
            "text",
            "main_image",
            "price",
            "count",
            "images",
            "total_amount"
        )

    def get_total_amount(self, vals):
        return vals.price * vals.count
