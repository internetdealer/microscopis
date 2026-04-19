from django.apps import AppConfig


class ErrataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.errata"
    label = "errata"
    verbose_name = "Errata"

    def ready(self):
        import sites.errata.admin  # noqa: F401
