from product.views import ShopListView
from django.urls import path

urlpatterns = [
    path('ProductList/', ShopListView.as_view(), name="shop_list")
]