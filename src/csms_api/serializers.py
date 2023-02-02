from rest_framework_gis.serializers import GeoModelSerializer

from .models import ChargingStation


class ChargingStationSerializer(GeoModelSerializer):
    class Meta:
        model = ChargingStation
        geo_field = 'location'
        auto_bbox = True
        fields = ["station_id", "location", "configuration"]
