from django.shortcuts import render

# Create your views here.
from .forms import UserLoginForm


def login(request):
    context = {
        'title': 'Geetshop | Вход',
        'form': UserLoginForm(),
    }
    return render(request,'authapp/login.html',context)

def register(request):
    context={
        'title':'Geetshop | Регистрация'
    }
    return render(request,'authapp/register.html',context)

def profile(request):
    context = {
        'title': 'Geetshop | Профиль'
    }
    return render(request, 'authapp/profile.html')