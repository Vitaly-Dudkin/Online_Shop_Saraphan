from django.db.models import Sum, F
from rest_framework import serializers

from cart.models import Cart, ProductCart


class CartSummarySerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    def get_total_quantity(self, instance):
        request = self.context.get('request')
        queryset = Cart.objects.filter(user=request.user)
        total_quantity = queryset.aggregate(total_quantity=Sum('productcart__quantity'))['total_quantity']
        return total_quantity

    def get_total_price(self, instance):
        request = self.context.get('request')
        queryset = Cart.objects.filter(user=request.user)
        total_price = queryset.annotate(
            product_total_price=F('productcart__product__price') * F('productcart__quantity')
        ).aggregate(total_price=Sum('product_total_price'))['total_price']
        return total_price

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'total_quantity', 'total_price']


class MyCartSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductCart
        fields = ['cart', 'product_id', 'product', 'quantity']
