# Generated by Django 4.2.9 on 2024-01-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_remove_commentmap_comment_remove_commentmap_prompt_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prompt",
            name="like",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="prompt",
            name="un_like",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
