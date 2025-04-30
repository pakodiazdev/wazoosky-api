from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthEndpointTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="admin@wazoosky.dev", username="admin", password="admin123"
        )
        self.login_url = reverse("token_obtain_pair")

    def test_user_can_login_and_receive_tokens(self):
        response = self.client.post(
            self.login_url,
            {"email": "admin@wazoosky.dev", "password": "admin123"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["email"], self.user.email)
        self.assertEqual(response.data["user"]["username"], self.user.username)

    def test_token_refresh_returns_new_access_token(self):
        # Primero, logueamos para obtener el refresh token
        login_response = self.client.post(
            self.login_url,
            {"email": "admin@wazoosky.dev", "password": "admin123"},
            format="json",
        )

        refresh_token = login_response.data["refresh"]

        # Ahora, refrescamos
        refresh_url = reverse("token_refresh")
        response = self.client.post(
            refresh_url, {"refresh": refresh_token}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
