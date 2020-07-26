from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Buyer, Seller
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30,required = False,help_text='Optional.')
    last_name = forms.CharField(max_length = 30,required = False, help_text='Optional.')
    email = forms.EmailField(max_length =100,required = True, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","password1","password2")

class SellerForm(UserCreationForm):
    class Meta :
        model = User
        fields = ("username","email","password1","password2")

class ChangePersonalInfoBuyer(forms.Form):
    firstname = forms.CharField(max_length = 30, help_text = "First Name", required = False)
    lastname = forms.CharField(max_length = 30, help_text  = "Last Name",  required = False)
    Bio = forms.CharField(max_length = 300, help_text = "We are interest to get to know you more, max number of words is 300", required = False)


class ChangePersonalInfoSeller(forms.Form):
    Bio = forms.CharField(max_length = 300, required = False)
