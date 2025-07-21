from django.contrib import admin
from .models import TrafficPoint, TrafficData, TrafficIncident

@admin.register(TrafficPoint)
class TrafficPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(TrafficData)
class TrafficDataAdmin(admin.ModelAdmin):
    list_display = ('traffic_point', 'timestamp', 'congestion_level', 'average_speed', 'vehicle_count')
    list_filter = ('timestamp', 'congestion_level')
    search_fields = ('traffic_point__name',)

@admin.register(TrafficIncident)
class TrafficIncidentAdmin(admin.ModelAdmin):
    list_display = ('traffic_point', 'timestamp', 'incident_type', 'severity')
    list_filter = ('timestamp', 'incident_type', 'severity')
    search_fields = ('description', 'traffic_point__name')
