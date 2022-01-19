#скрипт восстановления бд
from django.core.management import BaseCommand

from geekshop.settings import BASE_DIR
from os import path as dir
from os import system as cmd

from authapp.models import User
from mainapp.models import ProductCategory, Product


def file_exists(file_way):
    full_way=str(BASE_DIR)+file_way
    if dir.isfile(full_way):
        print(f'+ exists:{file_way} ')
        return True
    else:
        print(f'! does not exists:{file_way} ')
        return False



class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Cкрипт восстановления в бд Product, ProductCategory, User')
        print(f'Корневая папка пректа: {BASE_DIR}')

        if file_exists('\\db.sqlite3'):
            print('+ DB exists')
            print('->Applying migrations:')
            cmd((f'python manage.py migrate'))
            print('->Clear table ProductCategory')
            ProductCategory.objects.all().delete()
            print('Ok')
            print('->Clear table Product')
            Product.objects.all().delete()
            print('Ok')
            print('->Clear table User')
            User.objects.all().delete()
            print('Ok')
        else:
            print('-> DB does not exists...rise_up')
            cmd((f'python manage.py migrate'))
            print('+ DB rised up')

        print('->Start rise_up')

        if file_exists('\\authapp\\fixtures\\User.json'):
            print('->Loading Users')
            cmd(f'python manage.py loaddata {str(BASE_DIR)}\\authapp\\fixtures\\User.json')
            print('+ Loading Users')
        if file_exists('\\mainapp\\fixtures\\Categories.json'):
            print('->Loading Categories')
            cmd(f'python manage.py loaddata {str(BASE_DIR)}\\mainapp\\fixtures\\Categories.json')
            print('+ Loading Categories')
        if file_exists('\\mainapp\\fixtures\\Products.json'):
            print('->Loading Products')
            cmd(f'python manage.py loaddata {str(BASE_DIR)}\\mainapp\\fixtures\\Products.json')
            print('+ Loading Products')
            print('Ok rise_up')

