from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_id = models.CharField(max_length=11, null=True)


    def __str__(self):
        return self.user.username