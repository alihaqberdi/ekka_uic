from simple_common.views import IndexView, search_view, testviy_view, hello_world, HelloWorldAPIView
from django.urls import path

app_name = 'common'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('SearchView/', search_view, name='search'),
    path("testviy/", testviy_view),
    path("api/v1/hello-world/", hello_world),
    path("api/v2/hello-world/", HelloWorldAPIView.as_view())
]
