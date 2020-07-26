from django.shortcuts import render, redirect
from User.forms import SignupForm, SellerForm, ChangePersonalInfoBuyer, ChangePersonalInfoSeller
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main.models import Seller, Buyer
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def Profile_seller(request, seller):
    PersonalInfo = ChangePersonalInfoSeller()
    template_name = 'User/Profile-Seller.html'
    user = Seller.objects.filter(username = seller)
    if len(user) == 0:
        return Profile_buyer(request,seller)
    if request.method == "POST":
        PersonalInfo = ChangePersonalInfoSeller(request.POST)
        if PersonalInfo.is_valid():
            Biography   = PersonalInfo.cleaned_data.get("Bio")
        print(PersonalInfo.is_valid())

    context = {"seller":user[0],  "PersonalInformation": PersonalInfo}
    return render(request,template_name,context)

@login_required
def Profile_buyer(request, buyer):
    PersonalInfo = ChangePersonalInfoBuyer()
    template_name = 'User/Profile-Buyer.html'
    user = Buyer.objects.filter(username = buyer)
    if request.method == "POST":
        PersonalInfo = ChangePersonalInfoBuyer(request.POST)
        print(PersonalInfo.is_valid())
        if PersonalInfo.is_valid():
            first_name   = PersonalInfo.cleaned_dataget.get("first_name")
            last_name   = PersonalInfo.cleaned_dataget.get("last_name")
            Biography   = PersonalInfo.cleaned_data.get("Bio")

    context = {"buyer":user[0], "PersonalInformation":PersonalInfo}
    return render(request,template_name,context)

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
            return redirect('/SignupSeller')
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
            buyer = Buyer(username = username, firstname = first_name, lastname = last_name, email = Email)
            buyer.save()
            login(request,user)
            return redirect('/Home')
        else:
            return redirect('/SignupBuyer')
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
                return redirect('/Home')
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

@login_required
def log_out(request):
    logout(request)
    return render(request,'Main/Base.html')
