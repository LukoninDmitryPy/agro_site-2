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
<<<<<<< HEAD
    path('edit_product/<int:id>/', product_detail_for_sale, name='edit_product'),
    path('my_products/<str:username>/', views.products_of_seller, name='products_of_seller'),
    path('ofert/', views.ofert, name='ofert'),
    path('politic/', views.politic, name='politic'),
    path('dost_i_oplat/', views.dostavka_i_oplata, name='d_i'),
    path('por_opl/', views.poryadok_oplati, name='p_o'),
    path('requi/', views.rekuisits, name='req'),
    path('pay/', views.pay, name='pay'),
=======
>>>>>>> d00c9fc93965c49c7aaae998056b093707bf610a
]
