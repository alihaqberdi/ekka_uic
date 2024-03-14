from rest_framework.viewsets import ModelViewSet
from simple_product.models import Category
from .serializers import CategoryModelViewSetSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from simple_product.api_endpoints.product.serializers import ProductListAPIViewSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelViewSetSerializers

    @action(detail=True, methods=["GET"])
    def get_products(self, request, pk=None):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductListAPIViewSerializer(products, many=True)
        return Response(serializer.data)
