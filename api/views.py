from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from api.models import vehicleStatus
from .serializers import viewVehicleStatusSerializer

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()