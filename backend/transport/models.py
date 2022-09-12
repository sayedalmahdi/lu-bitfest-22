from django.db import models


class BusInventory(models.Model):
    license_number = models.CharField(max_length=50)
    codename = models.CharField(max_length=50)
    capacity = models.IntegerField()
    driver_name = models.CharField(max_length=50)
    driver_contact = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.bus_id


class Route(models.Model):
    route_no = models.CharField(max_length=50, primary_key=True)
    label = models.CharField(max_length=50)
    start_location = models.ForeignKey('Stoppage', on_delete=models.CASCADE, related_name='start_location')

class Stoppage(models.Model):
    label = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.label