from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from simple_product.models import Product
from .serializers import ProductListAPIViewSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListAPIViewSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', "text", "price", "category__title"]
    filterset_fields = ["category", "price", "count"]

    def get_queryset(self):
        return self.queryset


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductListAPIViewSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductListAPIViewSerializer
    queryset = Product.objects.all()


__all__ = ["ProductListAPIView", "ProductRetrieveAPIView", "ProductDestroyAPIView"]
