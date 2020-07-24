import pytest
from .models import  Buyer, Seller, Service, Booking, Inquiry,Seller_Service
from django.urls import reverse
from django import urls
from django.test import TestCase
from main.models import Buyer, Seller, Service, Booking, Inquiry, Seller_Service

@pytest.fixture
def buyer():
    return Buyer.objects.create(username = 'mohaned.mashaly',
                  firstname = 'mohaned',
                  lastname = 'mashaly',
                  email = 'mohaned.mashaly12@gmail.com')

@pytest.fixture
def seller():
    return Seller.objects.create(username = 'mohaned.mashaly',Email = 'mohaned')

@pytest.fixture
def service(seller):
    return Service.objects.create(name = 'Advertising Agency', content = 'a very good service.....', service_provider = seller)

@pytest.fixture
def booking(seller,buyer,service):
    return Booking.objects.create(Sellername = seller,Buyername = buyer,service = service, date = '2020-09-09')

@pytest.fixture
def seller_service(seller, service):
    return Seller_Service.objects.create(sellername = seller,servicename = service)

@pytest.fixture
def inquiry():
    return Inquiry.objects.create(Message = 'I had problem with.....')

@pytest.mark.django_db
def test_Buyer_model(buyer):
    buyer.save()
    assert buyer != None and Buyer.objects.count() == 1

@pytest.mark.django_db
def test_Seller_model(seller):
    seller.save()
    assert seller != None and Seller.objects.count() == 1

@pytest.mark.django_db
def test_Service_model(seller, service):

    seller.save()
    service.save()
    assert service != None and Service.objects.count() == 1

@pytest.mark.django_db
def test_Booking_model(seller,service,buyer,booking):
    seller.save()
    service.save()
    buyer.save()
    booking.save()
    assert booking != None and Booking.objects.count() == 1

@pytest.mark.django_db
def test_Inquiry_model(inquiry):
    inquiry.save()
    assert inquiry != None and Inquiry.objects.count() == 1

@pytest.mark.django_db
def test_Seller_Service_model(seller, service, seller_service):
    seller.save()
    service.save()
    seller_service.save()
    assert seller_service != None and Seller_Service.objects.count() == 1

@pytest.mark.django_db
def test_home(client):
    url = urls.reverse('main:Home')
    response = client.get(url)
    assert response.status_code == 200
