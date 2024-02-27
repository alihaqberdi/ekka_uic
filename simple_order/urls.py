from simple_order.views import cart_view, add_cart_view
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('Cart/', cart_view, name="cart"),
    path('AddProduct/', add_cart_view, name="add_cart"),
]