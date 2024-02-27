from django.contrib import admin
from simple_order.models import Cart, CartItem

admin.site.register([Cart, CartItem])