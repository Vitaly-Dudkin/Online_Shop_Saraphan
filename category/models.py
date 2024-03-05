from django.db import models
from pytils.translit import slugify

NULLABLE = {
    'null': True,
    'blank': True
}


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='name')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='category_images/', verbose_name='image', **NULLABLE)
    category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='parent',
                                 related_name='subcategory', **NULLABLE)

    description = models.TextField(verbose_name='description', **NULLABLE)

    def save(self, *args, **kwargs):
        if not self.slug:  # Если slug пустой
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Category{self.name}'if self.category else f'SubCategory {self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']



