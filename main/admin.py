from django.contrib import admin
from .models import Buyer, Seller, Booking, Service, Inquiry, Seller_Service
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    fields = ["username", "firstname", "lastname", "email", "Bio"]
admin.site.register(Buyer,BuyerAdmin)

class SellerAdmin(admin.ModelAdmin):
    fields = ["username","Email", "Bio"]
admin.site.register(Seller, SellerAdmin)

class BookingAdmin(admin.ModelAdmin):
    fields = ["Sellername","Buyername", "service", "date"]
admin.site.register(Booking,BookingAdmin)

class ServiceAdmin(admin.ModelAdmin):
    fields = ["name","content","service_provider"]
admin.site.register(Service,ServiceAdmin)

class InquiryAdmin(admin.ModelAdmin):
    fields = ["Message"]
admin.site.register(Inquiry, InquiryAdmin)

class SelleServiceAdmin(admin.ModelAdmin):
    fields = ['sellername','servicename']
admin.site.register(Seller_Service,SelleServiceAdmin)
