
from django.test import TestCase
from .models import TrafficPoint, TrafficData
from .services.traffic_analyzer import TrafficAnalyzer

class TrafficAnalyzerTests(TestCase):
    def setUp(self):
        self.analyzer = TrafficAnalyzer()
        self.traffic_point = TrafficPoint.objects.create(
            latitude=12.34,
            longitude=56.78,
            name="Test Point"
        )

    def test_traffic_analysis(self):
        result = self.analyzer.analyze_traffic_point(self.traffic_point)
        self.assertIsNotNone(result)