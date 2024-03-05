from django.contrib.auth.models import AbstractUser
from django.db import models

from category.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone_number', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='image', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Country', **NULLABLE)
    verification_code = models.CharField(unique=True, **NULLABLE, verbose_name='verification_code')
    is_active = models.BooleanField("active",
                                    default=True,
                                    help_text=(
                                        "Designates whether this users should be treated as active. "
                                        "Unselect this instead of deleting accounts."
                                    ),
                                    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
