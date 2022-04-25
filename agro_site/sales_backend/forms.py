from django import forms

from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'product_group',
            'price',
            'description',
            'count',
            'discount',
            'on_sale'
        )
        labels = {
            'name': 'Наименование товара',
            'product_group': 'Категория товара',
            'price': 'Цена',
            'description': 'Описание',
            'count': 'Наличие',
            'discount': 'Скидка',
        }
        help_texts = {
            'discount': 'Введите условие выполнение Вашей скидки'
        }


class SellerForm(forms.Form):
    from_email = forms.EmailField(
        label='Email',
        required=True,
        help_text='Ваша электронная почта')
    subject = forms.CharField(
        label='Тема',
        required=True,
        help_text='''
        В теме письма укажите название Вашей компании с
        организационно-правовой-формой,
        также укажите пометку "Хочу стать продавцом"
        '''
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea, 
        required=True,
        help_text='''
        Укажите, пожалуйста, Имя, Фамилию,
        Телефон, ИНН организации или ИП
        ''')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'rating',)
        help_texts = {
            'text': 'Запиши свои мысли',
        }
        labels = {
            'text': 'Текст комментарии',
        }