from django.shortcuts import render
from product.models import Product, Size, Category, Color, Price
from django.views import View
from django.core.paginator import Paginator


class ShopListView(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        print(page, "page")
        # paginator product
        obj = Product.objects.all()
        paginator = Paginator(obj, 1)
        obj = paginator.get_page(page)

        context = {
            "product_ls": obj,
            "size_ls": Size.objects.all(),
            "category_ls": Category.objects.all(),
            "color": Color.objects.all(),
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