from django.db import models

class vehicleStatus(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    vehicle_id = models.CharField(max_length=11)
    laden = models.CharField(max_length=200)
    cell_spanning = models.CharField(max_length=200)
    accu_spanning = models.CharField(max_length=200)
    cell_percentage = models.CharField(max_length=200)
    motor_temparatuur = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicle_id

    class Meta:
        verbose_name_plural = "vehicle statusses"


