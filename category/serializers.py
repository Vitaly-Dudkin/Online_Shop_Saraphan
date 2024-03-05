from rest_framework import serializers

from category.models import Category


class SubCategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategory', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Category
        fields = '__all__'
