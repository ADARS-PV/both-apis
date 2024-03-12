from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from geopy.distance import geodesic
from api.models import ShopCategories,Customers,Merchants
from api.serializers import ShopCategoriesSerializer,CustomersSerializer,MerchantsSerializer


# Create your views here.
class merchantView(APIView):

    def get(self, request, customer_id, customer_lat, customer_long, *args, **kwargs):

        customer_location = (float(customer_lat), float(customer_long))

        nearby_merchants = []
        all_categories = set()

        for merchant in Merchants.objects.all():
            merchant_location = (merchant.latitude, merchant.longitude)
            distance = geodesic(customer_location, merchant_location).kilometers
            if distance <= merchant.delivery_radius:
                serializer = MerchantsSerializer(merchant)
                nearby_merchants.append({
                    "merchant_name": merchant.merchant_name,
                    "distance": distance,
                    "categories": [category.category_name for category in merchant.categories.all()]
                })
                all_categories.update(merchant.categories.all())

        response_data = {
            "customer_id": customer_id,
            "lat": customer_lat,
            "long": customer_long,
            "merchants": nearby_merchants,
            "shop_categories": [category.category_name for category in all_categories]
        }
        return Response(response_data)
   
       