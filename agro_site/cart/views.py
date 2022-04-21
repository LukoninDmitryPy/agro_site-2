from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from sales_backend.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import CartAddProductFrom
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductFrom(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['Количество'] <= product.count:
            amount = cd['Количество']
        else:
            amount = product.count
        cart.add(
            product=product,
            count=product.count,
            quantity=amount,
        )
    return redirect(
        'sales_backend:product_detail',
        id=id
        )


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail')

# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart:cart_detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart:cart_detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart:cart_detail")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")

@login_required(login_url="/users/login")
def cart_detail(request):
    cart = Cart(request)
    return render(
        request,
        'cart/cart_detail.html',
        {
            'cart': cart,
        }
    )