
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Buyer, Seller, Service, Booking, Inquiry
from django.contrib.auth.models import User

class DateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date',)

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('Message',)
