from django import forms


class CartAddProductFrom(forms.Form):
    Количество = forms.IntegerField()
