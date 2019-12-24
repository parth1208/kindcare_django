from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
User=get_user_model()
# Register your models here.
admin.site.register(User)
admin.site.register(Service_Categary)
admin.site.register(servant)