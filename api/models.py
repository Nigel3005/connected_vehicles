from django.db import models

class vehicleStatus(models.Model):
    vehicleid = models.CharField(max_length=11)
    payload = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicleid

    class Meta:
        verbose_name_plural = "vehicle statusses"