from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenRequestSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sobrescribe los campos creados dinámicamente
        self.fields["email"] = serializers.EmailField(
            default="admin@wazoosky.dev",
            help_text="Email del usuario para iniciar sesión",
        )
        self.fields["password"] = serializers.CharField(
            write_only=True, default="admin123", help_text="Contraseña del usuario"
        )

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = {
            "id": self.user.id,
            "email": self.user.email,
            "username": self.user.username,
        }
        return data
