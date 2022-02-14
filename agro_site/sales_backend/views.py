from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Product, ProductGroup
from cart.forms import CartAddProductFrom


def index(request):
    product_group_list = ProductGroup.objects.all()
    paginator = Paginator(product_group_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'sales_backend/index.html', context)


def product_group(request, slug):
    product_group = get_object_or_404(ProductGroup, slug=slug)
    product_list = product_group.product.all()
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'product_group': product_group,
        'page_obj': page_obj,
    }
    return render(request, 'sales_backend/product_group.html', context)


def product_detail(request, id):
    product_pk = get_object_or_404(Product, pk=id)
    product_group = product_pk.product_group
    cart_product_form = CartAddProductFrom()
    context = {
        'product_pk': product_pk,
        'product_group': product_group,
        'cart_product_form': cart_product_form
    }
    return render(request, 'sales_backend/product_detail.html', context)
