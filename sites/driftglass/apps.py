from django.apps import AppConfig


class DriftglassConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.driftglass"
    label = "driftglass"
    verbose_name = "Driftglass"

    def ready(self):
        import sites.driftglass.admin  # noqa: F401
