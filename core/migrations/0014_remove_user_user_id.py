# Generated by Django 4.2.9 on 2024-01-05 15:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_user_remove_comment_user_id_comment_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="user_id", ),
    ]