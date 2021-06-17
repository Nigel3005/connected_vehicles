from rest_framework import generics, status
from rest_framework.views import APIView

from .models import vehicleStatus
from .serializers import viewVehicleStatusSerializer
from rest_framework.response import Response

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()

class createVehicleStatus(APIView):

    def post(self, request, format=None):
        try:
            #get message
            payload_enc = request.data[1]["vs"]
            payload = bytes.fromhex(payload_enc).decode('utf-8')
            alarm_enc = payload[0:3]
            snelheid = int(payload[3:6])/100+2
            trilling = int(payload[6:9])/10
            vermogen = int(payload[9:10])
            airco = int(payload[1:4])
            verwarming = int(payload[3:6])
            batterij_percentage = int(payload[6:7])
            batterij_gemiddeld = int(payload[7:8])
            accu_spanning = int(payload[8:9])
            batterij_temperatuur = int(payload[2:3])
            motor_temperatuur = int(payload[4:5])-100
            controller_temperatuur = int(payload[2:4])
            actieradius = int(payload[4:6])
            error = int(payload[6:8])

            # decode
            alarm = '{0:08b}'.format(int(alarm_enc))
            laden =  alarm[0]
            vehicle_id = request.headers.get('vehicleid').upper()






            vehicle_status = vehicleStatus(vehicle_id=vehicle_id, laden=laden, snelheid=snelheid, trilling=trilling,
                                           vermogen=vermogen, airco=airco, verwarming=verwarming, batterij_percentage=batterij_percentage,
                                           batterij_gemiddeld=batterij_gemiddeld, accu_spanning=accu_spanning, batterij_temperatuur=batterij_temperatuur,
                                           motor_temperatuur=motor_temperatuur, controller_temperatuur=controller_temperatuur, actieradius=actieradius, error=error,)
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
