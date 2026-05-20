from django.shortcuts import render, redirect
from myapp.models import Products
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_required 
from django.contrib.auth.decorators import login_required
from myapp.forms import *

def register(request):
    if request.method == "POST":
        form = CustomForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect("login/")

    else:
        form = CustomForm() 
    return render(request, "register.html", {"form" : form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get("username") 
            pswrd = form.cleaned_data.get("password")
            user = authenticate(username = u_name, password = pswrd)
            if user is not None:
                auth_required(request, user)
                return redirect("products")

    else:
        form = AuthenticationForm() 
    return render(request, "login.html", {"form": form})


@login_required(login_url="login")
def product(request):
    products = Products.objects.all()
    return render(request, 'home.html', {'products':products})
