from django.db import models

class vehicleStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    vehicle_id = models.CharField(max_length=11)
    laden = models.CharField(max_length=20)
    snelheid = models.CharField(max_length=20)
    trilling = models.CharField(max_length=20)
    vermogen = models.CharField(max_length=20)
    airco = models.CharField(max_length=20)
    verwarming = models.CharField(max_length=20)
    batterij_percentage = models.CharField(max_length=20)
    batterij_gemiddeld = models.CharField(max_length=20)
    accu_spanning = models.CharField(max_length=20)
    batterij_temperatuur = models.CharField(max_length=20)
    motor_temperatuur = models.CharField(max_length=20)
    controller_temperatuur = models.CharField(max_length=20)
    actieradius = models.CharField(max_length=20)
    error = models.CharField(max_length=20)


    def __str__(self):
        return self.vehicle_id

    def chartdata(self):
        return [
            self.laden,
            self.snelheid,
            self.trilling,
            self.vermogen,
            self.airco,
            self.verwarming,
            self.batterij_percentage,
            self.batterij_gemiddeld,
            self.batterij_temperatuur,
            self.motor_temperatuur,
            self.controller_temperatuur,
            self.actieradius,
            self.error
        ]

    def logboekdata(self):
        return [
            self.time,
            self.vehicle_id,
            self.laden,
            self.snelheid,
            self.trilling,
            self.vermogen,
            self.airco,
            self.verwarming,
            self.batterij_percentage,
            self.batterij_gemiddeld,
            self.batterij_temperatuur,
            self.motor_temperatuur,
            self.controller_temperatuur,
            self.actieradius,
            self.error
        ]

    class Meta:
        verbose_name_plural = "vehicle statusses"


