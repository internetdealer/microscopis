"""Celery application; workers should set DJANGO_SETTINGS_MODULE."""
from __future__ import annotations

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "microscopis.settings")

app = Celery("microscopis")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
