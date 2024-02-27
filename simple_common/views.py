from django.shortcuts import render
from django.views.generic import TemplateView
from simple_product.models import Category
from django.contrib.postgres.search import TrigramSimilarity


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
