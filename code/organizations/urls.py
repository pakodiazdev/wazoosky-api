# organizations/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from organizations.views.organization import OrganizationViewSet

# Si planeas tener vistas adicionales (como invitaciones, miembros, etc.)
# puedes importarlas aquí conforme las vayas creando
# from organizations.views.membership import InviteMemberView

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet, basename='organizations')

urlpatterns = [
    path('', include(router.urls)),

    # Aquí puedes registrar rutas adicionales fuera del router
    # path('organizations/<int:org_id>/invite/', InviteMemberView.as_view(), name='invite-member'),
]
