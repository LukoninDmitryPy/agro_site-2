import re
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.user = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    seller=item['product'].product_seller,
                    user=request.user,
                    product=item['product'],
                    price=item['total_price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(
                request,
                'orders/success.html',
                {'order': order}
            )
    else:
        form = OrderCreateForm
    return render(
        request,
        'orders/create.html',
        {'cart': cart, 'form': form}
    )


def orderlist(request, username):
    template = 'orders/order_list.html'
    user = get_object_or_404(
        User,
        username=username
    )
    order = user.user.all()
    return render(
        request,
        template,
        {'order': order}
    )


def orderlistdetail(request, id):
    template = 'orders/order_list_detail.html'
    order = get_object_or_404(Order,pk=id)
    order_details = order.items.all()
    return render(
        request,
        template, 
        {
            'order_details': order_details,
            'order': order
        }
    )


def ordersales(request, username):
    template = 'orders/order_for_sales.html'
    seller = get_object_or_404(
        User,
        username=username
    )
    order_for_sale = OrderItem.objects.filter(seller__seller__user=seller)
    return render(
        request,
        template,
        {'order_for_sale': order_for_sale}
    )
