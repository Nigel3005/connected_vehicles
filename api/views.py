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
            #Decode Message
            payload_enc = request.data[1]["vs"]
            payload = bytes.fromhex(payload_enc).decode('utf-8')

            #Split message
            values = []
            for i in range(0, len(payload), 2):
                value_enc = payload[i:i + 2]
                value = int(value_enc, 16)
                values.append(value)

            alarm_enc = values[0]
            vermogen = values[1]
            batterij_percentage = values[2]
            actieradius = values[3]
            batterijspanning_minimum  = values[4]
            batterijspanning_gemiddeld  = values[5]
            batterijspanning_maximum  = values[6]
            snelheid = values[7]
            info_enc = values[8]
            motor_temperatuur = values[9]
            controller_temperatuur = values[10]
            spanning_12v = values[11]

            gemiddeld_verbruik = values[13]
            satelliet_enc = values[14]
            batterij_temperatuur = values[15]
            kabine_temperatuur = values[16]
            kabine_ingestelde_temperatuur = values[17]
            olie_temperatuur = values[18]
            versnelling_x_richting = values[19]
            versnelling_y_richting = values[20]
            versnelling_z_richting = values[21]
            bedrijfstijd_lowbyte = values[22]
            bedrijfstijd_highbyte = values[23]


            # decode alarm
            alarm = '{0:08b}'.format(int(alarm_enc))
            laden =  alarm[0]
            error_g = alarm[1]
            tanken = alarm[2]
            baterij_temp = alarm[4]
            batterij_span_laag = alarm[5]
            batterij_span_hoog = alarm[6]

            # decode info
            info = '{0:08b}'.format(int(info_enc))
            airco_actief = info[1]
            error_12v = info[2]
            hoogspanningserror = info[3]
            motor_temperatuur_alarm = info[5]
            controller_temperatuur_alarm = info[6]
            airco_aan = info[7]

            # decode satalliet
            satelliet = '{0:08b}'.format(int(satelliet_enc))
            aantal_satellieten = int(satelliet[0:7], 2)

            # decode bedrijfstijd
            bedrijfstijd_lowbyte = '{0:08b}'.format(int(bedrijfstijd_lowbyte))
            bedrijfstijd_highbyte = '{0:08b}'.format(int(bedrijfstijd_highbyte))
            bedrijfstijd = int(bedrijfstijd_highbyte + bedrijfstijd_lowbyte, 2)

            vehicle_id = request.headers.get('vehicleid').upper()
            vehicle_status = vehicleStatus(vehicle_id=vehicle_id, laden=laden, snelheid=snelheid,
                                           vermogen=vermogen, batterij_percentage=batterij_percentage, batterij_temperatuur=batterij_temperatuur,
                                           motor_temperatuur=motor_temperatuur, controller_temperatuur=controller_temperatuur, actieradius=actieradius,
                                           batterijspanning_minimum=batterijspanning_minimum, batterijspanning_gemiddeld=batterijspanning_gemiddeld,
                                           batterijspanning_maximum=batterijspanning_maximum, spanning_12v=spanning_12v,
                                           gemiddeld_verbruik=gemiddeld_verbruik,satelliet=satelliet,kabine_temperatuur=kabine_temperatuur,
                                           kabine_ingestelde_temperatuur=kabine_ingestelde_temperatuur,olie_temperatuur=olie_temperatuur,
                                           versnelling_x_richting=versnelling_x_richting, versnelling_y_richting=versnelling_y_richting,
                                           versnelling_z_richting=versnelling_z_richting,
                                           bedrijfstijd_lowbyte=bedrijfstijd_lowbyte,bedrijfstijd_highbyte=bedrijfstijd_highbyte,
                                           error_g=error_g,tanken=tanken,baterij_temp=baterij_temp,batterij_span_laag=batterij_span_laag,
                                           batterij_span_hoog=batterij_span_hoog,airco_actief=airco_actief,error_12v=error_12v,
                                           hoogspanningserror=hoogspanningserror,motor_temperatuur_alarm=motor_temperatuur_alarm,
                                           controller_temperatuur_alarm=controller_temperatuur_alarm,airco_aan=airco_aan,
                                           aantal_satellieten=aantal_satellieten,bedrijfstijd=bedrijfstijd,
                                           )
            vehicle_status.save()
            return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'Failed': 'bad request'}, status=status.HTTP_409_CONFLICT)



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
