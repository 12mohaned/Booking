from django.db import models

# Create your models here.
class Buyer(models.Model):
    username = models.CharField(max_length = 100,primary_key = True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email    = models.EmailField()
    def __str__(self):
        return self.username

class Seller(models.Model):
    username = models.CharField(max_length = 100, primary_key = True)
    Email = models.EmailField()
    def __str__(self):
        return self.username

class Service(models.Model):
    name = models.CharField(max_length = 100,primary_key = True)
    content = models.TextField()
    service_provider = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    book_id    = models.AutoField(primary_key = True)
    Sellername = models.ForeignKey(Seller, on_delete=models.CASCADE)
    Buyername = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()

#Improved later to include the user
class Inquiry(models.Model):
    Message = models.TextField()

class Seller_Service(models.Model):
    sellername = models.ForeignKey(Seller,on_delete = models.CASCADE)
    servicename = models.ForeignKey(Service, on_delete = models.CASCADE)
