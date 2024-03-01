from django.shortcuts import render
from django.views.generic import TemplateView
from simple_product.models import Category
from django.contrib.postgres.search import TrigramSimilarity
from simple_common.forms import TestviyForm


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


def testviy_view(request):
    form = TestviyForm()
    if request.method == "POST":
        request.POST
        form = TestviyForm(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    context['form'] = form
    return render(request, 'testviy.html', context)
