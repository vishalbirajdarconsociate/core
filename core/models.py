from django.db import models
from useradmin.models import VendorLog

# Create your models here.

class Product(models.Model):
    SKU=models.CharField( max_length=50)
    productName=models.CharField( max_length=50)
    productDesc=models.TextField()
    productThumb=models.ImageField( upload_to='static/images/product/', height_field=None, width_field=None, max_length=None)
    productPrice=models.FloatField()
    productQty=models.IntegerField(default=0)
    Unlimited=models.IntegerField(default=0)
    productStatus=models.IntegerField(default=0)
    vendorId=models.ForeignKey(VendorLog, on_delete=models.CASCADE)
    preparationTime=models.DurationField(null=True,blank=True)
    def __str__(self):
        return self.productName
    
class ProductImages(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/images/product_images/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.product.productName+" | image "+str(self.pk)
    
    
class Category(models.Model):
    categoryName=models.CharField( max_length=50)
    categoryParentId=models.IntegerField(default=0,null=True,blank=True)
    categoryDescription=models.TextField()
    categoryStatus=models.IntegerField(default=0,null=True,blank=True)
    categorySortOrder=models.IntegerField(default=0,null=True,blank=True)
    categoryImgage=models.ImageField(upload_to='static/images/Category/', height_field=None, width_field=None, max_length=None)
    categoryCreatedAt=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    categoryUpdatedAt=models.DateTimeField(auto_now=True,null=True,blank=True)
    vendorId=models.ForeignKey(VendorLog, on_delete=models.CASCADE)
    def __str__(self):
        return self.categoryName


class ProductCategory(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.product.productName+" | "+self.category.categoryName
