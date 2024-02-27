from django.shortcuts import render
from simple_product.models import Product, Category
from django.views import View
from django.core.paginator import Paginator


class ShopListView(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        obj = Product.objects.all()
        paginator = Paginator(obj, 12)
        obj = paginator.get_page(page)

        context = {
            "product_ls": obj,
            "category_ls": Category.objects.all(),
            "end_index": [i + 1 for i in range(paginator.num_pages)],
            "item_count": paginator

        }
        return render(request, 'product_list.html', context)


def product_detail(request, slug):
    obj = Product.objects.get(slug=slug)
    context = {
        "product": obj
    }
    return render(request, 'product_detail.html', context)
