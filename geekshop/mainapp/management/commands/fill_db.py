import json
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product


def load_from_json(filename):
    with open(filename,encoding='utf-8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories=load_from_json('mainapp/fixtures/Categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat=category.get('fields')
            cat['id']=category.get('pk')
            new_category=ProductCategory(**cat)
            new_category.save()

        print(ProductCategory.objects.count())

        products=load_from_json('mainapp/fixtures/Products.json')

        Product.objects.all().delete()
        for product in products:
            prod=product.get('fields')
            prod['id']=product.get('pk')
            category=prod.get('category')
            _category=ProductCategory.objects.get(id=category)
            prod['category']=_category
            new_category=Product(**prod)
            new_category.save()
        print(Product.objects.count())