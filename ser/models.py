from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
    phone=models.IntegerField(default=0)
    is_customer=models.BooleanField(' Is Customer',default=False)
    is_seller=models.BooleanField(' Is seller',default=False)

class Cart(models.Model):
    product=models.ForeignKey('seller.ProductDetails',related_name="Product_Details",on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    buyer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Cart_quantity=models.IntegerField(default=1)
    total=models.IntegerField(default=1)

class Service_Categary(models.Model):
    icon=models.CharField(max_length=25)
    service_Description=models.TextField()
    service_Name=models.CharField(max_length=25)

    def __str__(self):
        return self.service_Name

class servant(models.Model):
    genderchoice=(
        ('M','male'),
        ('F','female')
    )
    service=models.ForeignKey(Service_Categary,related_name='Services',on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    price=models.IntegerField()
    gender=models.CharField(choices=genderchoice,max_length=25)
    
    def __str__(self):
        return self.name
