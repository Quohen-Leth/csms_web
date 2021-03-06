from django.urls import path
from rest_framework import routers

from .views import ChargingStationViewSet

router = routers.DefaultRouter()
router.register(r"stations", ChargingStationViewSet)
