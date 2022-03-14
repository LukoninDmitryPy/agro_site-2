from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('sales_backend.urls', namespace='sales_backend')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('auth/', include('users.urls', namespace='user')),
    path('auth/', include('django.contrib.auth.urls')), 
    path('account/', include('users.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('blog/', include('agroblog.urls', namespace='posts')),
]
