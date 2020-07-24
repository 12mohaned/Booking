from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main import models

def Profile(request):
    template_name = 'User/Profile-Buyer.html'
    return render(request,template_name)

def Singup(request):
    template_name = 'User/Signup.html'
    if(request.method == "POST"):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username   = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            Email      = form.cleaned_data.get("email")
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('main/Home.html')
        else:
            return redirect('User/SignUp.html')
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
