from organizations.models import OrganizationMembership
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateMembershipService:
    def __call__(self, user: User, organization, role="owner") -> OrganizationMembership:
        return OrganizationMembership.objects.create(
            organization=organization,
            user=user,
            role=role
        )


# Alias limpio y directo: 💥 `create_membership(user, org)`
create_membership = CreateMembershipService()
