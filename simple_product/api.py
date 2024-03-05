from rest_framework.views import APIView
from simple_product.models import Product
from rest_framework.response import Response
from rest_framework import serializers


class ProductListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "category",
            "title",
            "slug",
            "text",
            "main_image",
            "price",
            "count"
        )


class ProductListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = Product.objects.first()

        serializer = ProductListAPIViewSerializer(data)

        return Response(serializer.data, status=200)
