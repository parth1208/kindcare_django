from django.db import models 
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    cat_type=(
        ('sell','sell'),
        ('service','service')
    )
    icon=models.CharField(max_length=25,null=True)
    category_type=models.CharField(choices=cat_type,max_length=25)
    category_name=models.CharField(max_length=25)
    category_desc=models.TextField()

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name=models.CharField(max_length=25)
    sub_category_desc=models.TextField()
    sub=models.ForeignKey(Category,related_name='subcategory',on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name




class ProductDetails(models.Model):
    product_name=models.CharField(max_length=25,default="mi")
    Product_type=models.CharField(max_length=25)
    Product_Price=models.IntegerField()
    Product_Description=models.TextField()
    Product_image=models.ImageField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)
    modified_at=models.DateTimeField(auto_now_add=True)
    owned_by=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    discount=models.FloatField()
    cat=models.ForeignKey(Category,related_name='Category',on_delete=models.CASCADE)
    cat_sub=models.ForeignKey(SubCategory,related_name="Subcategory",on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    Tagline=models.CharField(max_length=25,default="miii")

    def __str__(self):
        return self.product_name



