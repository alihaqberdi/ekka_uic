from django.core.management.base import BaseCommand
from simple_product.models import Category
import json


class Command(BaseCommand):
    help = "Load category from csv file"

    def handle(self, *args, **options):
        with open('data/category.json', 'r') as file:
            data = json.load(file)
            for item in data:
                Category.objects.get_or_create(
                    **item
                )
