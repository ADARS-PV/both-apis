from rest_framework import serializers
from api.models import Customers,Merchants,ShopCategories

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'phone_number', 'name', 'latitude', 'longitude']

class ShopCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategories
        fields = ['id', 'category_name']

class MerchantsSerializer(serializers.ModelSerializer):
    
    categories = ShopCategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Merchants
        fields = ['id', 'merchant_name', 'latitude', 'longitude', 'delivery_radius', 'categories']