import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DriftglassImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(db_index=True, max_length=128, unique=True)),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image_url", models.URLField(max_length=500)),
                ("image_credit", models.CharField(blank=True, help_text="Attribution line (e.g. Unsplash photographer).", max_length=255)),
                ("source_host", models.CharField(blank=True, help_text="Origin host label for telemetry (e.g. images.unsplash.com).", max_length=120)),
                ("probe_agent", models.CharField(default="fetch-agent-v3", help_text="Synthetic agent id shown in the UI.", max_length=64)),
                ("is_featured", models.BooleanField(db_index=True, default=False)),
                ("created_at", models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Driftglass image",
                "verbose_name_plural": "Driftglass images",
                "ordering": ["-created_at", "slug"],
            },
        ),
    ]
