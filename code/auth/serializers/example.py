# auth/serializers/example.py

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Register Example",
            value={
                "username": "john_doe87",
                "email": "john.doe87@example.com",
                "password": "Test1234!"
            }
        )
    ]
)
class RegisterExampleResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
