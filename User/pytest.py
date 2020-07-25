import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django import urls
from main.models import Buyer, Seller, Service, Booking, Inquiry, Seller_Service
from main.pytest import seller

@pytest.fixture
def authenticated_user(client):
    """ create authenticated user for the test """
    user = User(username = 'misho.mashaly')
    user.set_password('my_password1')
    user.save()
    client.login(username = user.username)
    assert user != None
    return user


@pytest.mark.django_db
def test_login(client):
    url = urls.reverse('User:Login')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup(client):
    url = urls.reverse('User:Signup')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup_seller(client):
    signup_url = urls.reverse('User:Signup-Seller')
    response = client.post(signup_url, {'username':'mohaned.mashaly',
                                   'password1':'pass123456/',
                                   'password2':'pass123456/'})
    assert response.status_code == 302
    assert response.url == urls.reverse('main:Home')

@pytest.mark.django_db
def test_login(client):
    login_url = urls.reverse('User:Login')
    response = client.post(login_url, {'username' : 'mohaned.mashaly',
                                      'password1' :'pass123456/'})
    assert response.status_code == 200
    assert response.url == urls.reverse('main:Home')

"""@pytest.mark.django_db
def test_home(authenticated_user, client):
    url = urls.reverse('main:Home')
    response = client.get(url)
    assert response.status_code == 200"""
