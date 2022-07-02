from rest_framework import serializers

from .models import ChargingStation


class ChargingStationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChargingStation
        fields = ["station_id", "location", "configuration"]