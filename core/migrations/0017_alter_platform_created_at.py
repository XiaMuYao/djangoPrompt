# Generated by Django 4.2.9 on 2024-01-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_alter_platform_name_alter_tag_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="platform",
            name="created_at",
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
        ),
    ]
