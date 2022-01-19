import json
import os
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

from authapp.models import User


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
            for i in prod:
                print(i,prod[i])
            new_category=Product(**prod)
            new_category.save()
        print(Product.objects.count())

        #users = load_from_json('authapp/fixtures/User.json')

        User.objects.all().delete()
        #print(os.getcwd())
        if os.path.isfile(os.getcwd()+'/authapp/fixtures/User.json'):
            print('file does exist')
            my_users=os.getcwd()+'/authapp/fixtures/User.json'
            os.system(f'python manage.py loaddata {my_users}')
