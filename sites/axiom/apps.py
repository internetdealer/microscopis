from django.apps import AppConfig


class AxiomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.axiom"
    label = "axiom"
    verbose_name = "Axiom"

    def ready(self):
        import sites.axiom.admin  # noqa: F401
