from rest_framework import viewsets, permissions

from .models import ChargingStation
from .serializers import ChargingStationSerializer


class ChargingStationViewSet(viewsets.ModelViewSet):
    queryset = ChargingStation.objects.all()
    serializer_class = ChargingStationSerializer
    # permission_classes = [permissions.IsAuthenticated]
