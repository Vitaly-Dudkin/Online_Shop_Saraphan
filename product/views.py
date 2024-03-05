from rest_framework import viewsets

from product.models import Product
from product.paginators import ProductPagination
from product.serializers import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
