from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Max, Min, Avg, Count, Q
from django.views import View
from product.models import Product, Size, Category, Color, Price
from django.contrib.postgres.search import TrigramSimilarity


# trigram extension


# Create your views here.


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
        "size_ls": Size.objects.all(),
        "category_ls": Category.objects.all(),
        "color": Color.objects.all()
    }
    return render(request, "product_list.html", context)
