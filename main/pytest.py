import pytest
from .models import  Buyer, Seller, Service, Booking, Inquiry,Seller_Service

@pytest.mark.django_db
def test_Buyer_model():
    buyer = Buyer(username = 'mohaned.mashaly',
                  firstname = 'mohaned',
                  lastname = 'mashaly',
                  email = 'mohaned.mashaly12@gmail.com')
    buyer.save()
    assert buyer != None and Buyer.objects.count() == 1

@pytest.mark.django_db
def test_Seller_model():
    seller = Seller(username = 'mohaned.mashaly',
              Email = 'mohaned')
    seller.save()
    assert seller != None and Seller.objects.count() == 1

@pytest.mark.django_db
def test_Service_model():

    seller = Seller(username = 'mohaned.mashaly',Email = 'mohaned')
    seller.save()

    service = Service(name = 'Advertising Agency',content = 'a very good service.....',service_provider = seller)
    service.save()
    assert service != None and Service.objects.count() == 1


@pytest.mark.django_db
def test_Booking_model():

    seller = Seller(username = 'mohaned.mashaly',Email = 'mohaned')
    seller.save()

    service = Service(name = 'Advertising Agency',content = 'a very good service.....',service_provider = seller)
    service.save()

    buyer = Buyer(username = 'mohaned.mashaly',
              firstname = 'mohaned',
              lastname = 'mashaly',
              email = 'mohaned.mashaly12@gmail.com')
    buyer.save()

    booking = Booking(Sellername = seller,
                      Buyername = buyer,
                      service   = service,
                      date = '2020-09-09')
    booking.save()
    assert booking != None and Booking.objects.count() == 1

@pytest.mark.django_db
def test_Inquiry_model():
    size = Inquiry.objects.count()
    inquiry = Inquiry(Message = 'I had problem with.....')
    inquiry.save()
    assert inquiry != None and Inquiry.objects.count() == 1

@pytest.mark.django_db
def test_Seller_Service_model():
    seller = Seller(username = 'mohaned.mashaly',Email = 'mohaned')
    seller.save()

    service = Service(name = 'Advertising Agency',
                      content = 'a very good service.....',
                      service_provider = seller)
    service.save()

    seller_service = Seller_Service(
              sellername = seller,
              servicename = service)
    seller_service.save()
    assert seller_service != None and Seller_Service.objects.count() == 1
