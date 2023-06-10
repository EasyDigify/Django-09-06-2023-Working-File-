from django.contrib import admin
from .models import *

model_list = [User,Customer,Worksheet,Credentials,Renewal]
admin.site.register(model_list)
