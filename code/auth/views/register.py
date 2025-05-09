from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from auth.serializers.registre import RegisterRequestSerializer
from auth.serializers.token_response import TokenResponseSerializer

User = get_user_model()


class RegisterView(APIView):
    @extend_schema(
        tags=["Auth"],
        auth=[],
        operation_id="registre",
        summary="resgistre and user and login (JWT)",
        description=(
            "Registre and Authenticates the user and returns access "
            "and refresh tokens..."
        ),
        request=RegisterRequestSerializer,
        examples=[
            OpenApiExample(
                name="Generated Example",
                value=RegisterRequestSerializer.get_example(),
                request_only=True,
            )
        ],
        responses={
            200: OpenApiResponse(
                response=TokenResponseSerializer,
                description="Token pair returned on successful login",
            ),
            401: OpenApiResponse(description="Invalid credentials"),
        },
    )
    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #            dispatch('user_registered', user=user)  # 🔥 evento lanzado
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "username": user.username,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
