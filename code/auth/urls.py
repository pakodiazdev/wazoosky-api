from django.urls import path

from .views.token import AuthRefreshView, CustomTokenObtainPairView

urlpatterns = [
    path("auth/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", AuthRefreshView.as_view(), name="token_refresh"),
]
