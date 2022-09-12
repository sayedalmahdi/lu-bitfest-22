from django.contrib import admin
from .models import BusInventory, Stoppage, Route
# Register your models here.

admin.site.register(BusInventory)
admin.site.register(Stoppage)
admin.site.register(Route)
