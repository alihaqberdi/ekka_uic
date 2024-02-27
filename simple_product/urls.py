from simple_product.views import ShopListView, product_detail
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('ProductList/', ShopListView.as_view(), name="shop_list"),
    path("ProductDetail/<slug:slug>/", product_detail, name='detail'),
]