from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *;

class LocationList(APIView):
    def get(self, request):
        model = Location.objects.all()
        serializer = LocationSerializer(model, many=True)
        return Response(serializer.data)