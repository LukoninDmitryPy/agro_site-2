from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/products/', ProductViewSet),
    path('v1/api-token-auth/', views.obtain_auth_token,
         name='auth_token'),
]
