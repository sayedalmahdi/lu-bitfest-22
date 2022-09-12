from .models import BusInventory, Stoppage, Route
from rest_framework import serializers

class BusInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusInventory
        fields = ('id', 'license_number', 'codename', 'capacity', 'driver_name', 'driver_contact', 'is_active')

class StoppageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stoppage
        fields = ('id', 'label', 'latitude', 'longitude')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('route_no', 'label', 'start_location')