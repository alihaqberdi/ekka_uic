from django.shortcuts import render
from django.views.generic import TemplateView
from simple_product.models import Category
from django.contrib.postgres.search import TrigramSimilarity
from simple_common.forms import TestviyForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from simple_common import tasks


def all_pages_view(request):
    if request.user.is_authenticated:
        return {
            "item_count_1": 0
        }
    else:
        cart = request.session.get('cart', None)
        if cart:
            return {
                "item_count_1": len(cart)
            }
        else:
            return {
                "item_count_1": 0
            }


class IndexView(TemplateView):
    template_name = 'index.html'


def search_view(request):
    q = request.POST.get("q")
    products = Category.objects.all()
    if q:
        products = products.annotate(
            similarity=TrigramSimilarity('title', q),
        ).oreder_by('-similarity')

    context = {
        "product_ls": products,
        "category_ls": Category.objects.all(),
    }
    return render(request, "product_list.html", context)


def more_time_task():
    for i in range(10000000):
        print(i)


def testviy_view(request):
    form = TestviyForm()
    if request.method == "POST":
        request.POST
        form = TestviyForm(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    tasks.add.delay()
    context['form'] = form
    return render(request, 'testviy.html', context)


@api_view(['GET', "POST"])
def hello_world(request):
    if request.method == "POST":
        data = request.body
        return Response(
            {
                "salom": data
            },
            status=204
        )

    return Response(
        {"message": "Hello, world!"},
        status=200
    )


class HelloWorldAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "message": "Hello APIView"
            }
        )
