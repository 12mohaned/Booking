from django.shortcuts import render
from .forms import DateForm, InquiryForm
from .models import Buyer, Seller, Service, Booking, Inquiry
from django.http import HttpResponse

# Return all services
def Home(request):
    Services = Service.objects.all()
    context = {"Services":Services,}
    return render(request,"main/Home.html",context)

#Return all service providers
def Services(request,service):
    service = Seller_Service.objects.filter(service = service)
    if len(service) == 0:
        return HttpResponse("Url Can't be found")

    context = {"Services":service}
    return render(request,"main/Reserve.html",context)

#Reserve Service Providers
def reserve_provider(request, provider):
    Provider = Seller_Service.objects.filter(username = provider)
    if len(Provider) == 0:
        return HttpResponse("Url Can't be found")

    return render(request,"main/Home.html")

#submit Inquiry
def Inquiry(request):
    Inquiryform = InquiryForm()
    if request.method == "POST":
        Inquiryform = InquiryForm(request.POST)
        if Inquiryform.is_valid():
            inquiry = Inquiryform.save(commit=False)
            inquiry.save()
    context = { "InquiryForm":Inquiryform}
    return render(request,"main/inquiry.html",context)
