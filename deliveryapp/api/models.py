from django.db import models

# Create your models here.

class Customers(models.Model):

    phone_number = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):

        return self.name

class ShopCategories(models.Model):

   
    category_name = models.CharField(max_length=200)

    def __str__(self):

        return self.category_name
    
class Merchants(models.Model):

  
    merchant_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    delivery_radius = models.FloatField()
    categories = models.ManyToManyField(ShopCategories)

    def __str__(self):
        return self.merchant_name

