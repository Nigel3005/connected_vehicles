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
            laden = payload[2:4]
            cell_spanning = int(payload[2:3])-30
            accu_spanning = int(payload[2:3])-30
            cell_perc = int(payload[2:3])-30
            motor_temp = int(payload[2:3])-30
            vehicleid = request.headers.get('vehicleid')
            vehicle_status = vehicleStatus(vehicleid=vehicleid, payload=payload, laden=laden, cell_spanning=cell_spanning, accu_spanning=accu_spanning, cell_perc=cell_perc, motor_temp=motor_temp)
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
#             vehicleid = request.headers.get('vehicleid')
#             vehicle_status = vehicleStatus(vehicleid=vehicleid, payload=payload)
#             vehicle_status.save()
#             return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
#         except:
#             return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
