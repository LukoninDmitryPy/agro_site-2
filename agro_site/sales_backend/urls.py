from django.urls import path

from . import views


app_name = 'sales_backend'

urlpatterns = [
    # Главная страница, каталог выбора мета-групп и категорий товаров
    path('', views.index, name='index'),
    # Страница с выбранной категорией товаров + список этих самых товаров
    path('product_group/<slug:slug>/', views.product_group, name='product_group'),
    # Отдельная страница о товаре, карточка товара
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product')
]
