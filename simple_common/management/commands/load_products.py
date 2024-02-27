from django.core.management.base import BaseCommand
from simple_product.models import Product, Category
import json


class Command(BaseCommand):
    help = 'Load products from a csv file'

    def handle(self, *args, **options):
        with open('data/products.json', 'r') as file:
            data = json.load(file)
            for item in data:
                category = Category.objects.get(id=item['category'])
                Product.objects.create(
                    category=category,
                    title=item['title'],
                    text=item['text'],
                    count=item['count'],
                    price=item['price'],
                    main_image=item['main_image']

                )

        return 'Products loaded'