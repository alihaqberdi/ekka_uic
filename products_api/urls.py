from django.urls import path
from products_api.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view())
]
