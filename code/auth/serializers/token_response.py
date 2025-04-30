from rest_framework import serializers

from auth.serializers.user_mini import UserMiniSerializer


class TokenResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = UserMiniSerializer()
