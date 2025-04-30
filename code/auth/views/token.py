from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.serializers.token import TokenRequestSerializer
from auth.serializers.token_response import TokenResponseSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenRequestSerializer  # type: ignore[assignment]

    @extend_schema(
        tags=["Auth"],
        operation_id="login",
        summary="User login (JWT)",
        description="Authenticates the user and returns access and refresh tokens.",
        request=TokenRequestSerializer,
        responses={
            200: OpenApiResponse(
                response=TokenResponseSerializer,
                description="Token pair returned on successful login",
            ),
            401: OpenApiResponse(description="Invalid credentials"),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AuthRefreshView(TokenRefreshView):
    @extend_schema(
        tags=["Auth"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
