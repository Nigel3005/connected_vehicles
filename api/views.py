from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from api.models import vehicleStatus
from .serializers import viewVehicleStatusSerializer, createVehicleStatusSerializer
from rest_framework.response import Response

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()

class createVehicleStatus(APIView):
    serializer_class = createVehicleStatusSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            json = serializer.data.get('vehicleid')
            vehicle_status = vehicleStatus(json=json)
            vehicle_status.save()
            return Response(viewVehicleStatusSerializer(vehicle_status).data, status=status.HTTP_200_OK)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)