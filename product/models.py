from django.db import models
from pytils.translit import slugify

from category.models import Category, NULLABLE


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField(verbose_name='description', **NULLABLE)
    slug = models.SlugField(unique=True, verbose_name='slug')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    image_small = models.ImageField(upload_to='product_images/small/', **NULLABLE)
    image_medium = models.ImageField(upload_to='product_images/medium/', **NULLABLE)
    image_large = models.ImageField(upload_to='product_images/large/', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')

    def save(self, *args, **kwargs):
        if not self.slug:  # Если slug пустой
            self.slug = slugify(self.title)  # Генерируем slug из custom_field
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['title']
