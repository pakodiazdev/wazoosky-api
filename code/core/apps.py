from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        from .containers import CoreContainer
        container = CoreContainer()
        container.wire(modules=[
            "organizations.views.organization",  # views que usarán inyección
        ])
