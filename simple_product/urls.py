from simple_product.views import ShopListView, product_detail
from django.urls import path
from simple_product.api import ProductListAPIView

app_name = 'product'

urlpatterns = [
    path('ProductList/', ShopListView.as_view(), name="shop_list"),
    path("ProductDetail/<slug:slug>/", product_detail, name='detail'),
]

"""API URL"""
urlpatterns += [
    path("ProductListApiView/",ProductListAPIView.as_view())
]
