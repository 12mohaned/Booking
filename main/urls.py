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
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
