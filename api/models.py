from django.db import models

class vehicleStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    vehicle_id = models.CharField(max_length=11)

    # CAN_ID 400
    laden = models.BooleanField()
    error_g = models.BooleanField()
    tanken = models.BooleanField()
    baterij_temp = models.BooleanField()
    batterij_span_laag = models.BooleanField()
    batterij_span_hoog = models.BooleanField()
    vermogen = models.IntegerField()
    batterij_percentage = models.IntegerField()
    actieradius = models.IntegerField()
    batterijspanning_minimum = models.IntegerField()
    batterijspanning_gemiddeld = models.IntegerField()
    batterijspanning_maximum = models.IntegerField()
    snelheid = models.IntegerField()

    #CAN_ID 401
    airco_actief = models.IntegerField()
    error_12v = models.IntegerField()
    hoogspanningserror = models.IntegerField()
    motor_temperatuur_alarm = models.IntegerField()
    controller_temperatuur_alarm = models.IntegerField()
    airco_aan = models.IntegerField()
    motor_temperatuur = models.IntegerField()
    controller_temperatuur = models.IntegerField()
    spanning_12v = models.IntegerField()
    gemiddeld_verbruik = models.IntegerField()
    aantal_satellieten  = models.IntegerField()
    batterij_temperatuur = models.IntegerField()

    #CAN_ID 402
    kabine_temperatuur = models.IntegerField()
    kabine_ingestelde_temperatuur = models.IntegerField()
    olie_temperatuur = models.IntegerField()
    versnelling_x_richting = models.IntegerField()
    versnelling_y_richting = models.IntegerField()
    versnelling_z_richting = models.IntegerField()
    bedrijfstijd = models.IntegerField()

    def __str__(self):
        return self.vehicle_id

    # def chartdata(self):
    #     return [
    #         self.laden,
    #         self.snelheid,
    #         self.trilling,
    #         self.vermogen,
    #         self.airco,
    #         self.verwarming,
    #         self.batterij_percentage,
    #         self.batterij_gemiddeld,
    #         self.batterij_temperatuur,
    #         self.motor_temperatuur,
    #         self.controller_temperatuur,
    #         self.actieradius,
    #         self.error
    #     ]

    class Meta:
        verbose_name_plural = "vehicle statusses"
