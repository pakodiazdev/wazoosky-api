# auth/views/example.py

import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample
from auth.serializers.example import RegisterExampleResponseSerializer
from faker import Faker

faker = Faker()

@extend_schema(
    methods=["GET"],
    tags=["Auth"],
    operation_id="auth_register_example",
    summary="Generate example register payload",
    description="Returns a realistic fake user payload for testing registration.",
    responses={
        200: RegisterExampleResponseSerializer
    }
)
@api_view(["GET"])
def ExampleReqistreRequest(request):
    return Response({
        "username": faker.user_name(),
        "email": faker.email(),
        "password": os.getenv("FAKE_PASSWORD", "Test1234!")
    })
