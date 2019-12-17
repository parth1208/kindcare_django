from django.urls import path, include
from . import views
urlpatterns = [
path('',views.index,name='index_admin'),
path('AddProducts',views.addproducts,name='addproducts'),
path('displayproduct',views.display_product,name='display_pro')
]