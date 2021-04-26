from rest_framework import serializers
from .models import vehicleStatus

class viewVehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleStatus
        fields = ('vehicle_name','vehicleid','payload','test_1','test_2')
