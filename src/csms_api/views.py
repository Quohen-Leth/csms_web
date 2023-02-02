from rest_framework import viewsets, permissions
from rest_framework_gis.filters import InBBoxFilter

from .models import ChargingStation
from .serializers import ChargingStationSerializer


class ChargingStationViewSet(viewsets.ModelViewSet):
    queryset = ChargingStation.objects.all()
    serializer_class = ChargingStationSerializer
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    # permission_classes = [permissions.IsAuthenticated]
