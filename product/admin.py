from django.contrib import admin

from product.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'slug', 'image_small', 'image_medium', 'image_large', 'price')