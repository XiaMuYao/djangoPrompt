# Generated by Django 4.2.9 on 2024-01-04 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_remove_categorymap_category_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="professionmap", name="profession_id", ),
        migrations.RemoveField(model_name="professionmap", name="prompt_id", ),
        migrations.AddField(
            model_name="professionmap",
            name="profession",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.profession",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="professionmap",
            name="prompt",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="core.prompt"
            ),
            preserve_default=False,
        ),
    ]
