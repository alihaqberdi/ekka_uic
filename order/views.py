from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from product.models import Product


# Create your views here.


def cart_view(request):
    context = {

    }
    return render(request, 'cart.html', context)


def add_cart_view(request):
    request.session.get('cart', [])
    print(request.POST, "post")
    print(request.POST.get('product'))
    obj = Product.objects.get(slug=request.POST.get('product'))

    return reverse("product:detail", kwargs={"slug": obj.slug})
