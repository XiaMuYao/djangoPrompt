# Generated by Django 4.2.9 on 2024-01-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_category_name_alter_profession_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prompt", name="description", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="prompt", name="title", field=models.TextField(),
        ),
    ]
