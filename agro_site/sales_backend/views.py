from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from . import models, forms
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from agro_site.settings import DEFAULT_FROM_EMAIL

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


@permission_required('sales_backend.add_product')
def create_product(request):
    form = forms.ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        return redirect('sales_backend:index')
    return render(request, 'sales_backend/create_product.html', {'form': form})


def contact_view(request):
    if request.method == 'GET':
        form = forms.SellerForm()
    elif request.method == 'POST':
        form = forms.SellerForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    f'{subject} от {from_email}',
                    message,
                    DEFAULT_FROM_EMAIL, 
                    (from_email,)
                )
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('sales_backend:success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'sales_backend/email.html', {'form': form})


def success_view(request):
    return render(request, 'sales_backend/success.html')
