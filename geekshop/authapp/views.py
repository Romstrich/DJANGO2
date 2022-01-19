from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import UserLoginForm,UserRegisterForm


def login(request):
    if request.method=='POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password = request.POST.get('password')
            user=auth.authenticate(username=username,password=password)
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('mainapp:index'))
        else:
            print(form.errors)
    else:
        form=UserLoginForm()

    context = {
        'title': 'Geetshop | Вход',
        'form': form,
    }
    return render(request,'authapp/login.html',context)

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form=UserRegisterForm()

    context={
        'title':'Geetshop | Регистрация',
        'form':form,
    }
    return render(request,'authapp/register.html',context)

def logout(request):
    auth.logout(request)
    return render(request,'mainapp/index.html')

def profile(request):
    context = {
        'title': 'Geetshop | Профиль'
    }
    return render(request, 'authapp/profile.html')