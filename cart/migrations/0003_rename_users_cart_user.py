# Generated by Django 5.0.2 on 2024-03-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='users',
            new_name='user',
        ),
    ]
