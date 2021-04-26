from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=200, null=True)
    vehicleid = models.CharField(max_length=11, null=True)
    test_1 = models.CharField(max_length=200, null=True)
    test_2 = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.user.username