# serializers/organization.py

from rest_framework import serializers
from organizations.models import Organization
from organizations.models import OrganizationMembership

class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'slug', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        org = super().create(validated_data)
        OrganizationMembership.objects.create(
            user=user,
            organization=org,
            role="owner"
        )
        return org
