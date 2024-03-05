from rest_framework import routers

from category.apps import CategoryConfig
from category.views import CategoryViewSet

app_name = CategoryConfig.name

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [

    ] + router.urls
