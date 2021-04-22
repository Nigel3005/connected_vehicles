from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from api.models import vehicleStatus

class viewapi(generics.ListAPIView):
    queryset = vehicleStatus.objects.all()