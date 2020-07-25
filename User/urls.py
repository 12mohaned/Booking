from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'User'
urlpatterns = [
path('Profile',views.Profile, name = 'Profile'),
path('SignupSeller', views.Singup_seller, name = 'Signup-Seller'),
path('SignupBuyer',views.Signup_buyer, name = 'Signup-Buyer'),
path('Signup',views.Signup, name = 'Signup'),
path('Login', views.Login, name = 'Login'),
path('Logout',views.log_out, name = 'Logout'),
]
