from dependency_injector import containers, providers
from organizations.services.create_membership import CreateMembershipService


class CoreContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "organizations.views",  # puedes agregar más apps aquí
        ]
    )

    create_membership_service = providers.Factory(CreateMembershipService)
