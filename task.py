from celery import shared_task
from .models import TrafficPoint
from .services.traffic_analyzer import TrafficAnalyzer
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def update_traffic_data():
    """
    Periodic task to update traffic data for all traffic points
    """
    analyzer = TrafficAnalyzer()
    traffic_points = TrafficPoint.objects.all()
    
    for point in traffic_points:
        try:
            analyzer.analyze_traffic_point(point)
            logger.info(f"Successfully updated traffic data for point: {point.name}")
        except Exception as e:
            logger.error(f"Error updating traffic data for point {point.name}: {str(e)}")

@shared_task
def analyze_traffic_patterns(point_id):
    """
    Task to analyze traffic patterns for a specific point
    """
    try:
        point = TrafficPoint.objects.get(id=point_id)
        analyzer = TrafficAnalyzer()
        analysis = analyzer.analyze_patterns(point)
        logger.info(f"Completed traffic pattern analysis for point: {point.name}")
        return analysis
    except Exception as e:
        logger.error(f"Error analyzing traffic patterns: {str(e)}")
        raise

@shared_task
def cleanup_old_traffic_data(days=30):
    """
    Task to clean up old traffic data
    """
    from django.utils import timezone
    from datetime import timedelta
    
    cutoff_date = timezone.now() - timedelta(days=days)
    try:
        from .models import TrafficData
        old_data = TrafficData.objects.filter(timestamp__lt=cutoff_date)
        count = old_data.count()
        old_data.delete()
        logger.info(f"Cleaned up {count} old traffic data records")
    except Exception as e:
        logger.error(f"Error cleaning up old traffic data: {str(e)}")