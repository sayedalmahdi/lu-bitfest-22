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