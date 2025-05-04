# views/organization.py

from rest_framework import viewsets, permissions
from organizations.models import Organization
from organizations.serializers.organization import OrganizationCreateSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(memberships__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
