from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'title':'Geekshop | Главная',
    }
    return render(request,'mainapp/index.html',context)

def products(request):
    return render(request,'mainapp/products.html')