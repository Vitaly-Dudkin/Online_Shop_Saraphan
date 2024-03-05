from rest_framework import routers

from cart.views import CartViewSet, ProductCartViewSet
from cart.apps import CartConfig

app_name = CartConfig.name

router = routers.DefaultRouter()

router.register(r'', CartViewSet, basename='cart')
router.register(r'my_cart', ProductCartViewSet, basename='my-cart')


urlpatterns = [

    ] + router.urls
