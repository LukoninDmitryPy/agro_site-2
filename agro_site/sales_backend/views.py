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
from django.views.generic import ListView
from django.db.models import Q
from agroblog.models import Post
from users.models import MyUser as User



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

def product_detail_for_sale(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.product_seller != request.user:
        return redirect('sales_backend:product_detail', product.id)
    form = forms.ProductForSellerForm(
        request.POST or None,
        files=request.FILES or None,
        instance=product
    )
    if form.is_valid():
        form.save
        return redirect('sales_backend:product_detail', product.id)
    context = {
        'form': form,
        'id': id
    }
    return render(request, 'sales_backend/product_detail_for_seller.html', context)

def products_of_seller(request, username):
    seller = get_object_or_404(User,username=username)
    product1 = get_object_or_404(Product, product_seller=seller)
    product = Product.objects.filter(product_seller=seller)
    if product1.product_seller != request.user:
        return redirect('sales_backend:index')
    context = {
        'product': product,
    }
    return render(request, 'sales_backend/products_of_seller.html', context)


@permission_required('sales_backend.add_product', login_url='sales_backend:denied')
def create_product(request):
    form = forms.ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.product_seller = request.user
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


def get_denied(request):
    template = 'sales_backend/not_has_permission.html'
    return render(request, template)


class SearchResultsView(ListView):
    template_name = 'sales_backend/search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = (
        Product.objects.filter(
            Q(name__icontains=query)),
        Post.objects.filter(
            Q(text__icontains=query)),
        ProductGroup.objects.filter(
            Q(title__icontains=query))
        )
        return object_list

def ofert(request):
    template = 'sales_backend/ofert.html'
    return render(request, template)

def politic(request):
    template = 'sales_backend/politic.html'
    return render(request, template)

def dostavka_i_oplata(request):
    template = 'sales_backend/dostavka_i_oplata.html'
    return render(request, template)

def poryadok_oplati(request):
    template = 'sales_backend/poryadok_oplati.html'
    return render(request, template)

def rekuisits(request):
    template = 'sales_backend/rekuisits.html'
    return render(request, template)
