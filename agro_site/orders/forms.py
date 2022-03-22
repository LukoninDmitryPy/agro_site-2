from django import forms
from .models import Order, Message


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'address',
            'postal_code',
            'city',
        ]
        labels = {
            'address': 'Укажите Ваш полный адрес',
            'postal_code': 'Укажите почтовый индекс',
            'city': 'Укажите Ваш город'
        }
        help_texts = {
            'address': 'Страна, область, город, улица/проспект/иное, дом/строение/иное, квартира/офис/иное'
        }

class OrderCollectingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'status_order',
        ]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}
