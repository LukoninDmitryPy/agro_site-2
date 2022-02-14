from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('remove/<int:id>/', views.cart_remove, name='cart_remove'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
]
