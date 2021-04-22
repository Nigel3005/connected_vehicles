from rest_framework import serializers
from .models import viewVehicleStatus

class viewVehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = viewVehicleStatus
        fields = ('json',)