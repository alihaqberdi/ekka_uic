from django.shortcuts import render
from simple_product.models import Product
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.


def cart_view(request):
    context = {

    }
    return render(request, 'cart.html', context)


def add_cart_view(request):
    if request.method == "POST":
        print(request.session.get('cart'))
        product_id = request.POST.get('product')
        product_obj = Product.objects.get(id=product_id)

        return redirect(reverse('product:detail', kwargs={'slug': product_obj.slug}))
