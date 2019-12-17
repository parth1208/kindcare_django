from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from . forms import *
from . models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request,'seller/index_admin.html')

def addproducts(request):
    
    if request.method!='POST':
        form=ProductForm()
    
        return render(request,'seller/addproduct.html',{'form':form})
    else:
        form=ProductForm(request.POST ,request.FILES)
        if form.is_valid:
            f=form.save(commit=False)
            f.owned_by=request.user
            f.save()

            return redirect(index)

def display_product(request):
    # product_list=ProductDetails.objects.filter(owned_by=request.user)
    product_list=ProductDetails.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 10)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    return render(request,'seller/dispalyProduct.html',{'obj':obj})

