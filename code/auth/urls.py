from django.urls import path

from .views.example_registre_request import example_reqistre_request
from .views.register import RegisterView
from .views.token import AuthRefreshView, CustomTokenObtainPairView

urlpatterns = [
    path("auth/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", AuthRefreshView.as_view(), name="token_refresh"),
    path("auth/registre", RegisterView.as_view(), name="register"),
    path("auth/registre/example", example_reqistre_request, name="register_example"),
]
