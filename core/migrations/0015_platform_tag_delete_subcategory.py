# Generated by Django 4.2.9 on 2024-01-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0014_remove_user_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Platform",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "prompts",
                    models.ManyToManyField(related_name="platforms", to="core.prompt"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "prompts",
                    models.ManyToManyField(related_name="tags", to="core.prompt"),
                ),
            ],
        ),
        migrations.DeleteModel(name="Subcategory", ),
    ]
