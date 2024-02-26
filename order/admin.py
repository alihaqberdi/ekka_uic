from django.contrib import admin
from order.models import Cart, CartItem, OrderDiscount
# Register your models here.
admin.site.register([Cart, CartItem, OrderDiscount])