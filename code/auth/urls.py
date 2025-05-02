from django.urls import path

from .views.token import AuthRefreshView, CustomTokenObtainPairView
from .views.register import RegisterView;
from .views.example_reqistre_request import ExampleReqistreRequest

urlpatterns = [
    path("auth/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", AuthRefreshView.as_view(), name="token_refresh"),
    path('auth/registre', RegisterView.as_view(), name='register'),
    path('auth/registre/example', ExampleReqistreRequest, name='register_example'),
]
