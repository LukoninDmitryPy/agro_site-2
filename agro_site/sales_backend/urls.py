from django.urls import path

from . import views


app_name = 'sales_backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_group/<slug:slug>/', views.product_group, name='product_group'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
