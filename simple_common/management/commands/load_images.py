from django.core.management.base import BaseCommand
from simple_product.models import ProductImage, Product
import json




class Command(BaseCommand):
    help = 'Load images from a csv file'

    def handle(self, *args, **options):
        with open('data/productimages.json', 'r') as file:
            data = json.load(file)
            for item in data:
                print("ok")
                try:
                    product = Product.objects.filter(id=item['product'])
                    ProductImage.objects.create(
                        product=product.first(),
                        image=item['main_image']
                    )
                except:
                    print("Error")
        return 'Images loaded'