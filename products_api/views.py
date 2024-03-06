from rest_framework.generics import ListAPIView
from simple_product.models import Product

from products_api.serializers import ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
