from django.apps import AppConfig


class GiltConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.gilt"
    label = "gilt"
    verbose_name = "Gilt"

    def ready(self):
        import sites.gilt.admin  # noqa: F401
