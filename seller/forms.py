from django import forms
from . models import *
from ser.models import *
from django.forms import DateTimeField

class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.DateInput):
    input_type='time'


class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductDetails
        fields='__all__'
        exclude=('owned_by','Product_type')
    
    field_order = ['Tagline','product_name', 'cat', 'cat_sub', 'Product_Price','quantity','discount','Product_image','Product_Description']

class servant_detail(forms.ModelForm):
    class Meta:
        model=ServantBook
        fields='__all__'
        exclude=('customer','servant','ordered_at','status')

        field_order=['address','phone_no','data','time']
        widgets={

        'data':DateInput(),
        'time':TimeInput()
        }

class User_detail(forms.ModelForm):
    class Meta:
        model=User_account
        fields='__all__'
        
        field_order=['Image','Fullname','Email_id','Phone_number','Address','Gender','City']