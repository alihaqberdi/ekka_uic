from rest_framework.serializers import ModelSerializer
from simple_product.models import Category
from django.utils.text import slugify
from rest_framework.validators import ValidationError


class CategoryModelViewSetSerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def validate(self, attrs):
        obj = Category.objects.filter(slug=slugify(attrs.get("title")))
        if obj.exists():
            raise ValidationError("slug is exists")
        return attrs
