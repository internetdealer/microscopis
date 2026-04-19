from django.apps import AppConfig


class StaticSiteConfig(AppConfig):
    """Mini-site for intercepted radio signals (not django.contrib.staticfiles)."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.static"
    label = "static_site"
    verbose_name = "Static (signals)"

    def ready(self):
        import sites.static.admin  # noqa: F401
