from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import ChargingStation


@admin.register(ChargingStation)
class ChargingStationAdmin(GISModelAdmin):
    list_display = ("station_id", "location", "configuration")
