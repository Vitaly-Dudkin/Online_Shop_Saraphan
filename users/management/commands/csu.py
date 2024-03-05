from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email=input('Введите email: '),
                                   is_staff=True,
                                   is_superuser=True,
                                   )

        user.set_password('qwerty')
        user.save()
