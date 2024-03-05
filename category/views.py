from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from category.models import Category
from category.paginators import CategoryPagination
from category.serializers import CategorySerializer, SubCategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class = CategoryPagination
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.action == 'get_all_categories':
            return SubCategorySerializer
        return CategorySerializer

    @action(methods=['get'], detail=False)
    def get_all_categories(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
