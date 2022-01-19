# зарезервировать бд
from django.core.management import BaseCommand
from os import system as cmd
from geekshop.settings import BASE_DIR
from os import path as dir


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
        print('Здесь  будет скрипт резервтрования бд Product, ProductCategory, User')
        print(f'Корневая папка пректа: {BASE_DIR}')

        if file_exists('\\db.sqlite3'):
            print('Uploading Users')
            cmd(f'python -X utf8 manage.py dumpdata authapp.User -o {str(BASE_DIR)}\\authapp\\fixtures\\User.json')
            print('+Uploading Users')
            print('Uploading Products')
            cmd(f'python -X utf8 manage.py dumpdata mainapp.Product -o {str(BASE_DIR)}\\mainapp\\fixtures\\Products.json')
            print('+Uploading Products')
            print('Uploading Categories')
            cmd(f'python -X utf8 manage.py dumpdata mainapp.ProductCategory -o {str(BASE_DIR)}\\mainapp\\fixtures\\Categories.json')
            print('+Uploading Categories')


