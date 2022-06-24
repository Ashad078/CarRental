#from ast import Or
#from os import curdir
from django.contrib import admin
from .models import Customer, Orders

admin.site.register(Customer)
admin.site.register(Orders)
