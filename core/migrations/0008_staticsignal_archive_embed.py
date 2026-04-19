from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_axiom_instrument_verbose"),
    ]

    operations = [
        migrations.AddField(
            model_name="staticsignal",
            name="archive_embed_file",
            field=models.CharField(
                blank=True,
                help_text="Optional file inside the item (e.g. tcp_d1_01_track.mp3) to start that track in the embed.",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="staticsignal",
            name="archive_embed_id",
            field=models.CharField(
                blank=True,
                help_text="Internet Archive item id for embedded player, e.g. ird059 → archive.org/embed/ird059",
                max_length=80,
            ),
        ),
    ]
