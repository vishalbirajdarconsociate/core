from django.db import models
from useradmin.models import *
# Create your models here.
class Customer(models.Model):
    firstName=models.CharField(null=True, max_length=50)
    lastName=models.CharField( max_length=50, null=True)
    email=models.CharField( max_length=50)
    phoneNumber=models.CharField(max_length=20)
    shippingAddress=models.TextField()
    billingAddress=models.TextField()
    Vendor=models.ForeignKey(VendorLog, on_delete=models.CASCADE)
