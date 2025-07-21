# traffic_management/serializers.py

from rest_framework import serializers
from .models import TrafficPoint, TrafficData, TrafficIncident

class TrafficPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficPoint
        fields = '__all__'

class TrafficDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficData
        fields = '__all__'