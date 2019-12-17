from django import forms
from . models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductDetails
        fields='__all__'
        exclude=('owned_by','Product_type')
    
    field_order = ['Tagline','product_name', 'cat', 'cat_sub', 'Product_Price','quantity','discount','Product_image','Product_Description']