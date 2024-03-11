from rest_framework.serializers import ModelSerializer
from simple_product.models import Category


class CategoryModelViewSetSerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
