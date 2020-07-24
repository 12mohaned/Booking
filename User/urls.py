from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'User'
urlpatterns = [
path('Profile',views.Profile, name = 'Profile'),
path('Signup', views.Singup, name = 'Signup'),
path('Login', views.Login, name = 'Login'),

]
