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
    # Cтраница создания товара для продавца
    path('create/', views.create_product, name='create_product'),
    # Страница отправки формы продавца Сергею
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('denied/', views.get_denied, name='denied'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('products/<int:id>/comment/', views.add_comment, name='add_comment'),
]
