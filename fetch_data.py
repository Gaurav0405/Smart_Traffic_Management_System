# model/fetch_data.py
import googlemaps
from datetime import datetime, timedelta
import csv

API_KEY = 'AIzaSyBHW9Xwg7YYGEXxIcUFdCuD2h0CA2sS72E'  # Replace key
gmaps = googlemaps.Client(key=API_KEY)

def fetch_traffic_data(origin, destination, time_window):
    data = []
    for time_offset in range(0, time_window, 3600):  # Every hour
        timestamp = datetime.now() - timedelta(days=30) + timedelta(seconds=time_offset)
        directions_result = gmaps.directions(
            origin,
            destination,
            departure_time=timestamp
        )
        traffic_info = directions_result[0]['legs'][0]['duration_in_traffic']['value']
        data.append([timestamp, traffic_info])
    return data

with open('traffic_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Traffic_Duration'])
    writer.writerows(fetch_traffic_data("Location A", "Location B", 30 * 24 * 3600))
