from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from simple_product.models import Product
from .serializers import ProductListAPIViewSerializer


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
