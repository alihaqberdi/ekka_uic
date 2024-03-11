from rest_framework.viewsets import ModelViewSet
from simple_product.models import Category
from .serializers import CategoryModelViewSetSerializers


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelViewSetSerializers
