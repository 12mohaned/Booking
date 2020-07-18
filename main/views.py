from django.shortcuts import render
from .forms import InquiryForm
from .models import Buyer, Seller, Service, Booking, Inquiry,Seller_Service
from django.http import HttpResponse
from datetime import datetime
# Return all services
def Home(request):
    Services = Service.objects.all()
    context = {"Services":Services,}
    return render(request,"main/Home.html",context)

#Return all service providers
def Services(request,service):
    service = Seller_Service.objects.filter(servicename = service)
    if len(service) == 0:
        return HttpResponse("Url Can't be found")

    context = {"Services":service}
    return render(request,"main/Reserve.html",context)

#Reserve Service Providers
def reserve_provider(request, provider):
    Provider = Seller_Service.objects.filter(sellername = provider)
    print(Provider)
    if len(Provider) == 0:
        return HttpResponse("Url Can't be found")
    if request.method == "POST":
        Date = request.POST["Date"]
        print(Date)
        print(datetime.strptime(Date,'%m/%d/%y'))
        #if len(Date) > 0:
        #    Booking = Booking(Sellername  = Seller.objects.get(username = 'BookingApp'), Buyername  = Buyer.objects.get(username = 'mohaned.mashaly'), service    = Service.objects.get(name = 'BootCamp'))
        #    Booking.save()
    return render(request,"main/Slot.html")

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
