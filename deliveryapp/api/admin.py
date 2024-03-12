# admin.py
from django.contrib import admin
from api.models import Customers,ShopCategories,Merchants

# Register your models here.

admin.site.register(Customers)

admin.site.register(ShopCategories)

admin.site.register(Merchants)
