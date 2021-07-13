from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *;

class LocationList(APIView):
    def get(self, request):
        model = Location.objects.all()
        serializer = LocationSerializer(model, many=True)
        return Response(serializer.data)

class OwnerList(APIView):
    def get(self, request):
        model = Owner.objects.all()
        serializer = OwnerSerializer(model, many=True)
        return Response(serializer.data)

class StoreList(APIView):
    def get(self, request):
        model = Store.objects.all()
        serializer = StoreSerializer(model, many=True)
        return Response(serializer.data)

# class ProductList(APIView):
#     def get(self, request):
#         model= Product.objects.all()
#         serializer = ProductSerializer(model, many=True)
#         return Response(serializer.data)

# class FeaturedProductList(APIView):
#     def get(self, request):
#         model = FeaturedProduct.objects.all()
#         serializer = FeaturedProductSerializer(model, many=True)
#         return Response(serializer.data)