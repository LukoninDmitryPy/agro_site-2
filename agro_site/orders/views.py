import re
from unittest import result
from django.shortcuts import get_object_or_404
from users.models import MyUser as User

from .models import OrderItem, Order, Chat, Message
from .forms import OrderCreateForm, OrderCollectingForm, MessageForm
from cart.cart import Cart

from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django import template
from django.conf import settings
from django.urls import reverse

register = template.Library()


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
            'order': order,
        }
    )


def ordersales(request, username,):
    template = 'orders/order_for_sales.html'
    seller = get_object_or_404(User,username=username)
    order_for_sale = OrderItem.objects.filter(seller_id=seller)
    return render(request, template, {'order_for_sale': order_for_sale,})


def ordersales_detail(request, id):
    template = 'orders/order_for_sales_detail.html'
    order_for_sale = OrderItem.objects.filter(order_id=id)
    order = Order.objects.get(pk=id)
    form = OrderCollectingForm(instance=order)
    
    if request.method == 'POST':
        form = OrderCollectingForm(request.POST, instance=order)
        if form.is_valid():

            form.save()
            return redirect('orders:create_dialog', order.user.id,)
    return render(request, template, {'order_for_sale': order_for_sale, 'form': form})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("latin1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


#Opens up page as PDF
class ViewPDF(View):
    def get(self, request, id, *args, **kwargs):
        order = get_object_or_404(Order,pk=id)
        order_details = order.items.all()
        data = {
            'order_details': order_details
        }
        pdf = render_to_pdf('orders/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, id, *args, **kwargs):
        order = get_object_or_404(Order,pk=id)
        order_details = order.items.all()
        data = {
            'order_details': order_details
        }
        pdf = render_to_pdf('orders/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response


class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'orders/list_of_chats.html', {'user_profile': request.user, 'chats': chats})

    @register.simple_tag
    def get_companion(user, chat):
        for u in chat.members.all():
            if u != user:
                return u
        return None


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None
 
        return render(
            request,
            'orders/usersmessages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )
 
    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('orders:messages', kwargs={'chat_id': chat_id}))

class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('orders:messages', kwargs={'chat_id': chat.id}))


import os

from fpdf import FPDF

from agro_site.settings import BASE_DIR


class Constant:
    DT_CAPTION = 1
    DT_TEXT = 2
    DT_EMPTYLINE = 3
    DT_FOOTER = 4

class PDFMaker(FPDF):
    font_regular_name = 'DejaVuSansCondensed.ttf'
    font_regular_family = 'DejaVu'
    font_bold_family = 'DejaVuBold'
    font_bold_name = 'DejaVuSansCondensed-Bold.ttf'
    font_dir = 'static/fonts/'
    default_font_size = 12
    font_sizes = {
        Constant.DT_CAPTION: 14,
        Constant.DT_TEXT: 12,
        Constant.DT_FOOTER: 10
    }

    data: {}
    footer_text = ''

    line_height = 9  # in mm

    a4_height_mm = 297
    a4_width_mm = 210
    footer_padding = 15

    def __init__(self, orientation='P', unit='mm', format='A4', data=''):
        super().__init__(orientation=orientation, unit=unit, format=format)

        self.data = data

        self.__pdf_init()

    def set_footer_text(self, text):
        self.footer_text = text

    def footer(self):
        if self.footer_text:
            self.set_text_color(70, 70, 70)
            self.set_font(
                self.font_regular_family,
                size=self.__font_size(Constant.DT_FOOTER))
            self.set_y(-self.footer_padding)
            self.line(0, 0, 300, 0)
            self.cell(
                200, self.line_height, txt=self.footer_text, ln=1, align='C')

    def __pdf_init(self):
        font_regular = os.path.join(
            BASE_DIR, self.font_dir, self.font_regular_name)

        font_bold = os.path.join(
            BASE_DIR, self.font_dir, self.font_bold_name)

        self.set_auto_page_break(1)
        self.add_page()
        self.add_font(self.font_regular_family, '', font_regular, uni=True)
        self.add_font(self.font_bold_family, '', font_bold, uni=True)

    def __font_size(self, line_type):
        return self.font_sizes.get(line_type, self.default_font_size)

    def pdf_render(self):
        for line_type, line in self.data:
            self.set_text_color(40, 40, 40)

            if self.a4_height_mm - self.get_y() <= 2 * self.footer_padding:
                self.ln(self.a4_height_mm - self.get_y())

            if line_type == Constant.DT_CAPTION:
                self.set_font(
                    self.font_bold_family, size=self.__font_size(line_type),
                    style='U')
                self.cell(200, self.line_height, txt=line, ln=1, align='C')
            elif line_type == Constant.DT_TEXT:
                self.set_font(
                    self.font_regular_family, size=self.__font_size(line_type))
                self.cell(200, self.line_height, txt=line, ln=1, align='L')
            elif line_type == Constant.DT_EMPTYLINE:
                self.ln(self.line_height)

        self.close()

        return self.__pdf_output()

    def __pdf_output(self):
        return self.output(dest='S').encode('latin1')