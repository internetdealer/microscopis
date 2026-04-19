from django.apps import AppConfig


class VestigeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.vestige"
    label = "vestige"
    verbose_name = "Vestige"

    def ready(self):
        import sites.vestige.admin  # noqa: F401
