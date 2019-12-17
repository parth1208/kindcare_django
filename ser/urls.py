
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('Product/',views.Product, name='Product' ),
    path('Agents/',views.agents, name='agents' ),
    path('About/',views.about, name='about' ),
    path('Blog/',views.blog, name='blog' ),
    path('Contact/',views.contact, name='contact' ),
    path('Sign-In/',views.signin, name='signin' ),
    path('Sign-up/',views.signup, name='signup' ),
    path('Products-list/<int:pk>',views.Products_li,name='Products-list'),
    path('logout/',views.logout_user,name='logout'),
    path('forgot/',views.forget,name='forget'),
    path('cart/<int:pk>',views.cart,name='cart'),
    path('mycart/',views.my_cart,name='my_cart')
]