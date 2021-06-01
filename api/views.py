from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from api.models import vehicleStatus
from .serializers import viewVehicleStatusSerializer
from rest_framework.response import Response

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()

class createVehicleStatus(APIView):

    def post(self, request, format=None):
        try:
            payload = request.data[1]["vs"]
            laden = payload[0]
            cell_spanning = 12 #int(payload[1:2])/100+2
            accu_spanning = 12#int(payload[3:4])/10
            cell_percentage = 12#int(payload[5:6])
            motor_temperatuur = 12#int(payload[7:8])-100
            vehicle_id = request.headers.get('vehicle_id').upper()
            vehicle_status = vehicleStatus(vehicle_id=vehicle_id, laden=laden, cell_spanning=cell_spanning, accu_spanning=accu_spanning, cell_percentage=cell_percentage, motor_temperatuur=motor_temperatuur)
            vehicle_status.save()
            return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)









# class createVehicleStatus(APIView):
#
#     def post(self, request, format=None):
#         try:
#             payload = request.data[1]["vs"]
#
#             battery_perc = payload[2:4]
#             battery_perc = int(payload[2:3])-30
#
#             vehicle_id = request.headers.get('vehicle_id')
#             vehicle_status = vehicleStatus(vehicle_id=vehicle_id, payload=payload)
#             vehicle_status.save()
#             return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
#         except:
#             return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
