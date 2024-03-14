from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from simple_product.models import Product
from .serializers import ProductListAPIViewSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListAPIViewSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', "text", "price", "category__title"]
    authentication_classes = [TokenAuthentication]
    filterset_fields = ["category", "price", "count"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all().select_related("category").prefetch_related("images")
        return queryset


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductListAPIViewSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductListAPIViewSerializer
    queryset = Product.objects.all()


__all__ = ["ProductListAPIView", "ProductRetrieveAPIView", "ProductDestroyAPIView"]
