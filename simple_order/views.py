from django.shortcuts import render
from simple_product.models import Product
from django.urls import reverse
from django.shortcuts import redirect
from simple_order.models import CartItem, Cart


# Create your views here.


def cart_view(request):
    cart = Cart.objects.get(session_id=_cart)
    cart_item = CartItem.objects.filter(user=request.user)

    context = {
        'cart_item': cart_item

    }
    return render(request, 'cart.html', context)


def add_cart_view(request):
    if request.method == "POST":
        product_id = request.POST.get('product')
        count = request.POST.get('num')
        product_obj = Product.objects.get(id=product_id)
        cart = request.session.get('cart', {})
        if str(product_obj.id) in cart:
            cart[str(product_obj.id)] += int(count)
        else:
            cart[str(product_obj.id)] = int(count)
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(reverse('product:detail', kwargs={'slug': product_obj.slug}))






def remove_cart_view(request):
    if request.method == "POST":
        product_id = request.POST.get('product')
        count = request.POST.get('num')
