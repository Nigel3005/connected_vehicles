from rest_framework import serializers
from .models import vehicleStatus

class viewVehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleStatus
        fields = ('json',)

class createVehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleStatus
        fields = ('json',)