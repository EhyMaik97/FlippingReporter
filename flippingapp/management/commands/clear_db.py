from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction

class Command(BaseCommand):
    help = 'Clears the database'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            for model in apps.get_models():
                if model._meta.app_label != 'contenttypes':
                    model.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Database cleared'))
