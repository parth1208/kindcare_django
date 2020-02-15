from django.shortcuts import render
from .utils import *
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from . models import *
from seller.models import *
from django.db.models import Sum
from seller.forms import *
# Create your views here.

def index(request):
    last_ten=ProductDetails.objects.all().order_by('-id')[:4]
    last_ten_in_ascending_order=reversed(last_ten)
    print(last_ten_in_ascending_order)
    #obj=Service_Categary.objects.all()
    Product=Category.objects.all()
    service=Category.objects.filter(category_type='service')
    if request.user.is_authenticated:
        if request.user.is_customer:
            return render (request,'index.html',{'obj':service,'product':Product,'last_four':last_ten_in_ascending_order})
        else:
            return render(request,'seller/index_admin.html',{'last_four':last_ten_in_ascending_order})
    else:
        return render (request,'index.html',{'obj':service,'product':Product,'last_four':last_ten_in_ascending_order})

def Product(request):
    product=ProductDetails.objects.all()
    return render (request,'Product.html',{'product':product})
   

def myorders(request):
    order_list=ServantBook.objects.filter(customer=request.user)
    product_list=OrderItem.objects.filter(customer=request.user)
    order=ProductOrder.objects.filter(customer=request.user)
    page = request.GET.get('page', 1)
    '''
    paginator = Paginator(order_list, 10)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:5
    obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    '''
    return render(request,'myorder.html',{'obj':order_list ,'product_list':product_list,'order':order})

def orders(request):
    cart=Cart.objects.filter(buyer=request.user)
    cart_total=cart.aggregate(Sum('total'))
    order_id=ProductOrder.objects.create(customer=request.user,status='Pending',total_price=cart_total['total__sum'])
    for i in cart:
        OrderItem.objects.create(order_id=order_id,customer=request.user,quantity=i.Cart_quantity,product=i.product)
    cart.delete()

def ordershow(request):
    products_list=Cart.objects.filter(custommer=request.user)
    return render(request,'myorder.html',{'orde':orde})



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
                return redirect(index)
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
                    return redirect(index)
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
    email=request.user.email
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
    cart_total=Cart.objects.filter(buyer=request.user).aggregate(Sum('total'))
    return render(request,'cart.html',{'cart':obj,'no':len(obj),'total':cart_total['total__sum']})

def servantf(request,pk):
    cat=Category.objects.get(pk=pk)
    ser=servant.objects.filter(service=cat)
    return render(request,'servant-list.html',{'ser':ser})

#@login_required(login_url='/login/')
def book_servant(request,pk):
    if request.method=='POST':
        obj=servant.objects.get(pk=pk)
        form=servant_detail(request.POST)

        if form.is_valid():
            form=form.save(commit=False)
            form.customer=request.user
            form.servant=obj
            form.status='Pending'
            form.save()
            return redirect(myorders)
    else:
        obj=servant.objects.get(pk=pk)
        form=servant_detail()
        print('hello')
        return render(request,'servant_detail.html',{'form':form})




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})






def Account(request):
    form=User_detail()
    return render(request, 'account.html',{'form':form})
