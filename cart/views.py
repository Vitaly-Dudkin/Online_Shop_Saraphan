from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status

from cart.models import Cart, ProductCart
from cart.serializers import CartSummarySerializer, MyCartSerializer
from product.models import Product


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSummarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(methods=['POST'], detail=False)
    def add_to_cart(self, request):
        queryset = self.get_queryset()
        user = request.user
        if queryset.filter(user=user).exists():
            cart = queryset.get(user=user)
        else:
            cart = Cart.objects.create(user=user)

        product = request.data['product']
        product = Product.objects.get(id=product)

        if ProductCart.objects.filter(cart=cart, product=product).exists():
            product_cart = ProductCart.objects.get(cart=cart, product=product)
            product_cart.quantity += 1
            product_cart.save()
        else:
            ProductCart.objects.create(cart=cart, product=product, quantity=1)

        return Response({'detail': 'Product added to cart successfully'},
                        status=status.HTTP_200_OK)


class ProductCartViewSet(viewsets.ModelViewSet):
    queryset = ProductCart.objects.all()
    serializer_class = MyCartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)
