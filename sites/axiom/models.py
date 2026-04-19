from django.db import models
from django.utils import timezone


class AxiomLaw(models.Model):
    LAW_TYPES = [
        ("constitution", "Founding principle"),
        ("statute", "Binding requirement"),
        ("ruling", "Interpretive guidance"),
        ("amendment", "Amendment / update"),
    ]

    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    civilization_name = models.CharField(
        max_length=120,
        verbose_name="instrument",
        help_text="Regulatory or standards source (e.g. EU AI Act, NIST AI RMF).",
    )
    law_type = models.CharField(max_length=20, choices=LAW_TYPES)
    title = models.CharField(max_length=200)
    body = models.TextField()
    article_number = models.CharField(max_length=20, blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    enacted_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        app_label = "core"
        ordering = ["-enacted_at"]
        verbose_name = "Axiom law"
