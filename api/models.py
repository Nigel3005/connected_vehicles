from django.db import models

class vehicleStatus(models.Model):
    json = models.TextField()

    def __str__(self):
        return self.json

    class Meta:
        verbose_name_plural = "vehicle statusses"