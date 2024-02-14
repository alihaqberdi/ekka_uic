from common.views import IndexView, ShopListView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('ProductList/', ShopListView.as_view(), name="shop_list")
]