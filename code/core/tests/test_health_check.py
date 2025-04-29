from django.urls import reverse
from rest_framework.test import APITestCase


class TestHealthCheck(APITestCase):
    def test_health_check_returns_ok(self):
        url = reverse("health-check")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.data)
        self.assertEqual(response.data["status"], "ok")
