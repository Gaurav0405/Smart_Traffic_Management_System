# traffic_management/services/google_maps_service.py

import googlemaps
from django.conf import settings

class GoogleMapsService:
    def __init__(self):
        self.client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    
    def get_traffic_data(self, latitude, longitude):
        return self.client.traffic_data(
            location=(latitude, longitude),
            radius=1000
        )
    
    def get_distance_matrix(self, origins, destinations):
        return self.client.distance_matrix(
            origins,
            destinations,
            mode="driving",
            departure_time="now",
            traffic_model="best_guess"
        )