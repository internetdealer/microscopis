from django.apps import AppConfig


class CodexConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sites.codex"
    label = "codex"
    verbose_name = "Codex"

    def ready(self):
        import sites.codex.admin  # noqa: F401
