import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="KhulaCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(db_index=True, max_length=64, unique=True)),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
                ("sort_order", models.SmallIntegerField(db_index=True, default=0)),
            ],
            options={
                "verbose_name_plural": "Khula categories",
                "ordering": ["sort_order", "slug"],
            },
        ),
        migrations.CreateModel(
            name="KhulaArticle",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(db_index=True, max_length=128, unique=True)),
                ("title", models.CharField(max_length=255)),
                ("excerpt", models.TextField()),
                ("body", models.TextField()),
                ("author", models.CharField(max_length=128)),
                ("published_at", models.DateField(db_index=True)),
                ("read_minutes", models.PositiveSmallIntegerField(default=8)),
                ("is_featured", models.BooleanField(db_index=True, default=False)),
                ("image_url", models.URLField(blank=True, help_text="Hero image (HTTPS URL, e.g. Unsplash).", max_length=500)),
                ("image_credit", models.CharField(blank=True, help_text="Attribution line under the image.", max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="articles",
                        to="khula.khulacategory",
                    ),
                ),
            ],
            options={
                "ordering": ["-published_at", "-is_featured", "slug"],
            },
        ),
    ]
