from django.shortcuts import render, redirect
from .forms import SignupForm, SellerForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main.models import Seller
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def Profile(request):
    template_name = 'User/Profile-Buyer.html'
    return render(request,template_name)

def Singup_seller(request):
    template_name = 'User/Signup_seller.html'
    if(request.method == "POST"):
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            username   = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            Email      = form.cleaned_data.get("email")
            user = authenticate(username=username, password=raw_password)
            seller = Seller(username = username,Email = Email)
            seller.save()
            login(request,user)
            return redirect('/Home')
        else:
            return redirect('User/Signup_seller.html')
    else :
        form = SellerForm()
    context= {"Form":form}
    return render(request,template_name, context)

def Signup_buyer(request):
    template_name = 'User/Signup_buyer.html'
    if(request.method == "POST"):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username   = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name  = form.cleaned_data.get("last_name")
            raw_password = form.cleaned_data.get("password1")
            Email      = form.cleaned_data.get("email")
            user = authenticate(username=username, password=raw_password)
            Buyer.objects.create(username = username, firstname = first_name, lastname = last_name, email = Email)
            Buyer.save()
            login(request,user)
            return redirect('main/Home.html')
        else:
            return redirect('User/Signup_buyer.html')
    else :
        form = SignupForm()
    context= {"Form":form}
    return render(request,template_name, context)

def Login(request):
    if(request.method == "POST"):
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username   = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if(user is not None):
                login(request, user)
                return redirect('main/Home.html')
            else:
                return HttpResponse(user)
    else:
        form = AuthenticationForm()
    context ={
    "Form":form
    }
    return render(request,"User/Login.html",context)

def Signup(request):

    return render(request,'User/Signup.html')
