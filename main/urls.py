from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'main'

urlpatterns = [
path("Home",views.Home,name = "Home"),
path("Home/<slug:service>",views.Services,name = "service"),
path("Home/Reserve/<slug:provider>",views.reserve_provider,name = "reserve_provider"),
path("inquiry",views.Inquiry,name = "inquiry"),
path('payment-method/process-payment/', views.process_payment, name='process_payment'),
path('payment-done/', views.payment_done, name='payment_done'),
path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
path('payment-method/',views.payment_method,name = 'payment-method')
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
