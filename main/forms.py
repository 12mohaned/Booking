
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Buyer, Seller, Service, Booking, Inquiry
from django.contrib.auth.models import User

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('Message',)
