from django.apps import AppConfig


class ResidueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.residue"
    label = "residue"
    verbose_name = "Residue"

    def ready(self):
        import sites.residue.admin  # noqa: F401
