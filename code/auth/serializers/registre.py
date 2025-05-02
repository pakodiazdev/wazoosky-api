import os

from django.contrib.auth import get_user_model
from faker import Faker
from rest_framework import serializers

User = get_user_model()
faker = Faker()


class RegisterRequestSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    @staticmethod
    def get_example():
        return {
            "username": "username",
            "email": "email@serv.com",
            "password": os.getenv("FAKE_PASSWORD", "Test1234!"),
        }
