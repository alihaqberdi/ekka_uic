from rest_framework.views import APIView
from simple_product.models import Product, Category, ProductImage
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import serializers


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


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListAPIViewSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductListAPIViewSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductListAPIViewSerializer
    queryset = Product.objects.all()


# def get(self, request, *args, **kwargs):
#     data = Product.objects.all()
#
#     serializer = ProductListAPIViewSerializer(data, many=True)
#
#     return Response(serializer.data, status=200)
