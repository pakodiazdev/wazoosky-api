from django.shortcuts import render
from django.http import JsonResponse
from core.serializers.health_check_serializer import HealthCheckSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view


@extend_schema(
    summary="Health Check",
    description="Returns a simple status check to verify if the API is running.",
    responses=HealthCheckSerializer
)
@api_view(['GET'])
def health_check(request):
    return JsonResponse({
        "status": "ok",
        "message": "Where’s your paperwork, Wazoosky? 🧾 (coming soon...)"
    })
