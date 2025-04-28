from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from core.serializers.health_check_serializer import HealthCheckSerializer

@extend_schema(
    summary="Health Check",
    description="Returns a simple status check to verify if the API is running.",
    responses=HealthCheckSerializer,
)
@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "ok",
        "message": "API running correctly."
    })
