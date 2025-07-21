

from django.db import models

class TrafficPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TrafficData(models.Model):
    traffic_point = models.ForeignKey(TrafficPoint, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    congestion_level = models.IntegerField()  # 1-10 scale
    average_speed = models.FloatField()
    vehicle_count = models.IntegerField()

class TrafficIncident(models.Model):
    traffic_point = models.ForeignKey(TrafficPoint, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_type = models.CharField(max_length=50)
    description = models.TextField()
    severity = models.IntegerField()  # 1-5 scale