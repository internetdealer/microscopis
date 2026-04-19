from django.apps import AppConfig


class ParlorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.parlor"
    label = "parlor"
    verbose_name = "Parlor"

    def ready(self):
        import sites.parlor.admin  # noqa: F401
