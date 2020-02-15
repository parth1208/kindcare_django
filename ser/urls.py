
from django.urls import path, include
from . import views
from django.contrib.auth import views as v


urlpatterns = [
    path('',views.index, name='index' ),
    path('Product/',views.Product, name='Product' ),
    path('myorder/',views.myorders, name='myorder' ),
    path('About/',views.about, name='about' ),
    path('Blog/',views.blog, name='blog' ),
    path('Contact/',views.contact, name='contact' ),
    path('login/',views.signin, name='signin' ),
    path('Sign-up/',views.signup, name='signup' ),
    path('Products-list/<int:pk>',views.Products_li,name='Products-list'),
    path('logout/',views.logout_user,name='logout'),
    path('order/',views.orders,name='order'),
    path('Account/',views.Account,name='Account'),

    path('servant_detail/<int:pk>',views.book_servant,name='servant_detail'),

    path('forgot/',views.forget,name='forget'),
    path('cart/<int:pk>',views.cart,name='cart'),
    path('mycart/',views.my_cart,name='my_cart'),
    path('servant-list/<int:pk>',views.servantf,name='servantf'),
    path('change_password',views.change_password,name='change_password'),

    path('password-reset/', v.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html',subject_template_name='password_reset_email_subject.txt'),name='password_reset'),
    path('password-reset-done/', v.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', v.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', v.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
]
