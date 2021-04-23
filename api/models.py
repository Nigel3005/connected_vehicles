from django.db import models

class vehicleStatus(models.Model):
    vehicleid = models.TextField()
    batterijperc

    def __str__(self):
        return self.vehicleid

    class Meta:
        verbose_name_plural = "vehicle statusses"