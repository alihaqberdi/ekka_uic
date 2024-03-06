from django.db import models
from users.models import CustomUser
from simple_product.models import Product


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    finger_print = models.CharField(max_length=255, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=18, decimal_places=2)
    session_id = models.CharField(max_length=255, default='')


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    price_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitems')
    count = models.PositiveSmallIntegerField()
