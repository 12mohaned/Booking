from django.shortcuts import render
from .forms import InquiryForm
from .models import Buyer, Seller, Service, Booking, Inquiry,Seller_Service
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

booking = Booking()
# Return all services
def Home(request):
    Services = Service.objects.all()
    context = {"Services":Services,}
    return render(request,"main/Home.html",context)

#Return all service providers
def Services(request,service):
    services = Seller_Service.objects.filter(servicename = service)
    booking.service = Service.objects.get(name = service)

    if len(service) == 0:
        return HttpResponse("Url Can't be found")

    context = {"Services":services}
    return render(request,"main/Reserve.html",context)

#Reserve Service Providers
def reserve_provider(request, provider):
    user_name = request.user
    booking.Sellername  = Seller.objects.get(username = provider)
    booking.Buyername  = Buyer.objects.get(username = user_name)
    booking.Provider = Seller_Service.objects.filter(sellername = provider)
    if len(provider) == 0:
        return HttpResponse("Url Can't be found")
    if request.method == "POST":
        Date = request.POST["Date"]
        if len(Date) == 0:
            return HttpResponse("Enter a valid Date")
        else:
            dt = datetime.strptime(Date, '%m/%d/%Y')
            booking.date = dt
            payment_method(request)
            booking.save()
    return render(request,"main/Slot.html")

def payment_method(request):
    return render(request, "main/Payment_method.html")
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

def process_payment(request):
    service_name = request.session.get('servicename')
    service = Service.objects.get(name = 'Trip-Advisor')
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % 100,
        'item_name': 'Order {}'.format(service.name),
        'invoice': str(service.name),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,'paypal-ipn'),
        'return_url': 'http://{}{}'.format(host,'payment_done'),
        'cancel_return': 'http://{}{}'.format(host,'payment_cancelled'),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"PaypalForm" : form}
    return render(request,'main/process_payment.html',context)

@csrf_exempt
def payment_done(request):
    return render(request, 'main/payment_done.html')

@csrf_exempt
def payment_cancelled(request):
    return render(request, 'main/payment_cancel.html')
