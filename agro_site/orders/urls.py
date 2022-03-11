from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path(
        'order_list/<str:username>/',
        views.orderlist,
        name='order_list'
    ),
    path(
        'order_list/<int:id>/detail/',
        views.orderlistdetail,
        name='order_list_detail'
    ),
    path(
        'my_sales/<str:username>/',
        views.ordersales,
        name='ordersales'        
    ),
    path(
        'my_sales/<str:username>/',
        views.ordersales,
        name='ordersales'        
    ),
    path('pdf_view/<int:id>/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<int:id>/', views.DownloadPDF.as_view(), name="pdf_download"),
]