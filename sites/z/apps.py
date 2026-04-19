from django.apps import AppConfig


class ZSiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.z"
    label = "z_site"
    verbose_name = "Z"

    def ready(self):
        import sites.z.admin  # noqa: F401
        import sites.z.signals  # noqa: F401
