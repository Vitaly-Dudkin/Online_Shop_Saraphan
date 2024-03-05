from django.db import models

from product.models import Product
from users.models import User


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='users')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return f'Cart for: {self.user}'

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ['-created_at']


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')

    class Meta:
        verbose_name = 'product cart'
        verbose_name_plural = 'product carts'
        ordering = ['product']