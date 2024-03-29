# Generated by Django 4.2.9 on 2024-01-04 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_prompt_like_alter_prompt_un_like"),
    ]

    operations = [
        migrations.RemoveField(model_name="categorymap", name="category_id", ),
        migrations.RemoveField(model_name="categorymap", name="prompt_id", ),
        migrations.RemoveField(model_name="comment", name="prompt_id", ),
        migrations.AddField(
            model_name="categorymap",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.category",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="categorymap",
            name="prompt",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="core.prompt"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="prompt",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="core.prompt"
            ),
            preserve_default=False,
        ),
    ]
