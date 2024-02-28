from django.shortcuts import render
from django.views.generic import TemplateView
from simple_product.models import Category
from django.contrib.postgres.search import TrigramSimilarity


def all_pages_view(request):
    if request.user.is_authenticated:
        return {
            "cart": None
        }
    else:
        cart = request.session.get('cart')
        data = request.POST
        if cart:
            if data.get('product') in cart:
                val = cart[data.get('product')]
                cart[data.get('product')] = int(val) + int(data.get("num"))
                request.session["cart"] = cart
                return {
                    "cart": cart,
                    "item_count": cart[data.get('product')]
                }
        else:
            cart[data.get('product')] = data.get("num")
            return {
                "cart": None,
                "item_count": cart[data.get('product')]
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
