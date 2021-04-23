from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from api.models import vehicleStatus
from .serializers import viewVehicleStatusSerializer
from rest_framework.response import Response

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()

# class createVehicleStatus(APIView):
#     serializer_class = createVehicleStatusSerializer
#
#     def post(self, request, format=None):
#         data = request.data[1]
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             vs = serializer.data.get('vs')
#             vehicleid = request.headers.get('vehicleid')
#             vehicle_status = vehicleStatus(vehicleid=vehicleid, vs=vs)
#             vehicle_status.save()
#             return Response(viewVehicleStatusSerializer(vehicle_status).data, status=status.HTTP_200_OK)
#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class createVehicleStatus(APIView):

    def post(self, request, format=None):
        try:
            payload = request.data[1]["vs"]
            vehicleid = request.headers.get('vehicleid')
            vehicle_status = vehicleStatus(vehicleid=vehicleid, payload=payload)
            vehicle_status.save()
            return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
