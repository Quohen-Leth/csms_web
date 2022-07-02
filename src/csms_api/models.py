from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class ChargingStation(TimeStampedModel, models.Model):
    station_id = models.CharField(max_length=255, null=False, verbose_name=_("Station ID"))
    location = models.PointField(verbose_name=_("Station coordinates"), null=False)
    configuration = models.JSONField(verbose_name=_("Station configuration"), null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name_plural = "ChargingStations"

    def __str__(self):
        return f"{self.station_id}"
