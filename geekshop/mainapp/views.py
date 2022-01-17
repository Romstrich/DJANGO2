import json
import os

from mainapp.models import Product,ProductCategory



MODULE_DIR=os.path.dirname(__file__)
from django.shortcuts import render


# Create your views here.

def index(request):
    context={
        'title':'Geekshop | Главная',
    }
    return render(request,'mainapp/index.html',context)

def products(request):
    #load from file
    bd_products=Product.objects.all()
    bd_categories=ProductCategory.objects.all()


    json_products=os.path.join(MODULE_DIR,'fixtures/products.json')
    json_categories=os.path.join(MODULE_DIR,'fixtures/categories.json')
    context = {
        'title': 'Geekshop | Товары',
        'products': bd_products,#json.load(open(json_products,encoding='utf-8')),
        'categories':bd_categories,#json.load(open(json_categories,encoding='utf-8')),
    }



    return render(request,'mainapp/products.html',context)