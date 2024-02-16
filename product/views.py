from django.shortcuts import render
from product.models import Product, Size, Category, Color, Price
from django.views import View


class ShopListView(View):
    def get(self, request, *args, **kwargs):
        father_category = Category.objects.filter(parent__isnull=True)
        last_category = Category.objects.get(id=13)

        def find_father(categor):
            avlodi = []
            otasi = categor.parent
            while otasi:
                avlodi.append(otasi)
                otasi = otasi.parent
            return avlodi
        for i, t in enumerate(find_father(last_category), start=1):
            print(i*"    ",t.title)



        # for i in  father_category:
        #     print(i.title)
        #     for j in i.category_set.all():
        #         print(f"\t{j.title}")
        #         for k in j.category_set.all():
        #             print(f"\t\t{k.title}")
        #             for f in k.category_set.all():
        #                 print(f"\t\t\t{f.title}")

        context = {
            "product_ls": Product.objects.all(),
            "size_ls": Size.objects.all(),
            "category_ls": Category.objects.all(),
            "color": Color.objects.all()

        }
        return render(request, 'product_list.html', context)
