from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
#from seller import models
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

class State(models.Model):
    state_name=models.CharField(max_length=30)

    def __str__(self):
        return self.state_name

class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city=models.CharField(max_length=30)
    district=models.CharField(max_length=30,null=True)
    def __str__(self):
        s=str(self.city)+' '+str(self.district)
        return s




class servant(models.Model):
    genderchoice=(
        ('M','male'),
        ('F','female')
    )
    service=models.ForeignKey('seller.Category',related_name='Services',on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=25)
    price=models.IntegerField()
    gender=models.CharField(choices=genderchoice,max_length=25)
    location=models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    phone=models.BigIntegerField(default=0)
    image=models.ImageField(upload_to='Worker Image',null=True)

    def __str__(self):
        return self.name




class ServantBook(models.Model):
    servant=models.ForeignKey(servant,on_delete=models.CASCADE)
    customer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    address=models.TextField()
    phone_no=models.BigIntegerField()
    data=models.DateField()
    time=models.TimeField()
    ordered_at=models.DateTimeField(auto_now_add=True)
    
    status=models.CharField(max_length=20,choices=(('Pending','Pending'),('Approve','Approve'),('Cancel','Cancel')))


class ProductOrder(models.Model):
    customer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=(('Pending','Pending'),('Approve','Approve'),('Cancel','Cancel')))
    ordered_date=models.DateTimeField(auto_now=True)
    total_price=models.IntegerField()

class OrderItem(models.Model):
    order_id=models.ForeignKey(ProductOrder,on_delete=models.CASCADE)
    customer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    quantity=models.IntegerField()
    product=models.ForeignKey('seller.ProductDetails',on_delete=models.CASCADE)

class User_account(models.Model):
    usergender=(
        ('M','male'),
        ('F','female')
    )
    Image=models.ImageField(upload_to='User Image',null=True)
    Fullname=models.CharField(max_length=25)
    Email_id=models.EmailField()
    Phone_number=models.BigIntegerField(default=0)
    Address=models.TextField()
    Gender=models.CharField(choices=usergender,max_length=25)
    City=models.CharField(max_length=25)
    

    def __str__(self):
        return self.Fullname
