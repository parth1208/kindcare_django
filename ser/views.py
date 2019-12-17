from django.shortcuts import render
from .utils import *
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from . models import Cart
from seller.models import *
from django.db.models import Sum

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
            return render (request,'index.html')
        else:
            return render(request,'seller/index_admin.html')
    else:
        return render (request,'index.html')

def Product(request):
    product=ProductDetails.objects.all()
    return render (request,'Product.html',{'product':product})
   
def agents(request):
    return render (request,'agents.html')

def about(request):
    return render (request,'about.html')

def blog(request):
    return render (request,'blog.html')

def contact(request):
    return render (request,'contact.html')

def signin(request):
    if request.method!="POST":
        return render(request,'signin.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(username=email,password=password)
        if user:
            login(request,user)

            if request.user.is_seller==False:
                return render(request,'index.html')
            else:
                return render(request,'seller/index_admin.html')
        else:
            return render(request,'signin.html',{'Message':'Email id and password is incorrect'})
  

def signup(request):
    if request.method=='POST':
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('Email')
        name=request.POST.get('name')
        phone_no=request.POST.get('phoneno')
        Sellect=request.POST.get('Type')
        print('the',Sellect)
        if(password1==password2):
            try:
                match=User.objects.get(email=email)
                return render(request,'signup.html',{'Message':'Email id already taken'})
            except :
                if Sellect=='Seller':
                    User.objects.create_user(username=email,email=email,password=password1,first_name=name,phone=phone_no,is_seller=True)
                    user =authenticate(username=email,password=password1)
                    login(request,user)
                    return render(request,'seller/index_admin.html')
                else:
                    User.objects.create_user(username=email,email=email,password=password1,first_name=name,phone=phone_no,is_customer=True)
                
                    user =authenticate(username=email,password=password1)
                    login(request,user)
                    return render(request,'index.html')
        else:
             return render(request,'signup.html',{'Message':'missmatched password'})
    else:
        return render(request,'signup.html')


def Products_li(request,pk):
    obj=ProductDetails.objects.get(pk=pk)
    return render(request,'Product-list.html',{'obj':obj})


def logout_user(request):
    #email=request.user.email
    #email='parthmangukiya1208@gmail.com'
    
    email_subject = 'Interest shown in your property'
    email_from = settings.EMAIL_HOST_USER
    email='parthmangukiya1208@gmail.com'
    sendmail(email_subject,'mail',email,{'name':'logout your account'})
    logout(request)
    return redirect(index)

def forget(request):
    return render(request,'forget.html')

def cart(request,pk):
    obj=ProductDetails.objects.get(pk=pk)
    try:
        obj=Cart.objects.get(product=obj,buyer=request.user)
        obj.Cart_quantity=obj.Cart_quantity+1
        obj.total=obj.Cart_quantity*obj.product.Product_Price
        obj.save()
    except: 
        obj=Cart.objects.create(product=obj,buyer=request.user)
        obj.total=obj.Cart_quantity*obj.product.Product_Price
        obj.save()

    return redirect(Product)
    #hello

def my_cart(request):
    obj=Cart.objects.filter(buyer=request.user)
    cart_total=Cart.objects.aggregate(Sum('total'))
    return render(request,'cart.html',{'cart':obj,'no':len(obj),'total':cart_total['total__sum']})