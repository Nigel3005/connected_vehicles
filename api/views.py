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
            payload_enc = request.data[1]["vs"]
            payload = bytes.fromhex(payload_enc).decode('utf-8')
            laden =  payload[0]
            cell_spanning = int(payload[1:2])/100+2
            accu_spanning = int(payload[3:5])/10
            cell_percentage = int(payload[6:7])
            motor_temperatuur = int(payload[8:9])-100
            vehicle_id = request.headers.get('vehicleid').upper()
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
