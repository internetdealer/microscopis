from django.apps import AppConfig


class SableConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.sable"
    label = "sable"
    verbose_name = "Sable"

    def ready(self):
        import sites.sable.admin  # noqa: F401
