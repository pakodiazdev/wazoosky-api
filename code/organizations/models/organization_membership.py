from django.db import models
from django.conf import settings

class OrganizationMembership(models.Model):
    ROLE_CHOICES = [
      ("owner", "Owner"),
      ("admin", "Admin"),
      ("member", "Member"),
      ("reader", "Reader"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "organization")
