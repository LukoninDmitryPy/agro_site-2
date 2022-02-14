from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('sales_backend.urls', namespace='sales_backend')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
]
