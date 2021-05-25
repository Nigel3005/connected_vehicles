from django.db import models

class vehicleStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    vehicle_name = models.CharField(max_length=200)
    vehicleid = models.CharField(max_length=11)
    payload = models.CharField(max_length=200)
    laden = models.CharField(max_length=200)
    cell_spanning = models.CharField(max_length=200)
    accu_spanning = models.CharField(max_length=200)
    cell_perc = models.CharField(max_length=200)
    motor_temp = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicleid

    class Meta:
        verbose_name_plural = "vehicle statusses"