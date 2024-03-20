from simple_product.views import ShopListView, product_detail
from django.urls import path, include
from simple_product.api_endpoints import ProductListAPIView, ProductRetrieveAPIView, ProductDestroyAPIView, \
    CategoryModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("Category", CategoryModelViewSet)

app_name = 'product'

urlpatterns = [
    path('ProductList/', ShopListView.as_view(), name="shop_list"),
    # path("ProductDetail/<slug:slug>/", product_detail, name='detail'),
]

"""API URL"""
urlpatterns += [
    path("ProductListApiView/", ProductListAPIView.as_view(), name="product_list"),
    path("ProductDetail/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_detail"),
    path("ProductDestroy/<int:pk>/", ProductDestroyAPIView.as_view(), name="product_destroy"),
    path("", include(router.urls))
]
