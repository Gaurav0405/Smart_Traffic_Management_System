from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TrafficPoint, TrafficData
from .serializers import TrafficPointSerializer, TrafficDataSerializer
from .services.traffic_analyzer import TrafficAnalyzer

class TrafficPointViewSet(viewsets.ModelViewSet):
    queryset = TrafficPoint.objects.all()
    serializer_class = TrafficPointSerializer

@api_view(['GET'])
def get_traffic_analysis(request, point_id):
    analyzer = TrafficAnalyzer()
    traffic_point = TrafficPoint.objects.get(id=point_id)
    analysis = analyzer.analyze_traffic_point(traffic_point)
    return Response(analysis)