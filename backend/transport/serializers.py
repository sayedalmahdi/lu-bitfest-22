from .models import BusInventory
from rest_framework import serializers

class BusInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusInventory
        fields = ('license_number', 'codename', 'capacity', 'driver_name', 'driver_contact', 'is_active')

