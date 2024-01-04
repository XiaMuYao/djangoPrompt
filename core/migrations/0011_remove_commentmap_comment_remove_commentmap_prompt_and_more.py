# Generated by Django 4.2.9 on 2024-01-04 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_remove_comment_prompt_remove_commentmap_comment_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="commentmap", name="comment", ),
        migrations.RemoveField(model_name="commentmap", name="prompt", ),
        migrations.RemoveField(model_name="professionmap", name="profession", ),
        migrations.RemoveField(model_name="professionmap", name="prompt", ),
        migrations.AddField(
            model_name="category",
            name="prompts",
            field=models.ManyToManyField(related_name="categories", to="core.prompt"),
        ),
        migrations.AddField(
            model_name="comment",
            name="prompt",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="core.prompt",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profession",
            name="prompts",
            field=models.ManyToManyField(related_name="professions", to="core.prompt"),
        ),
        migrations.DeleteModel(name="CategoryMap", ),
        migrations.DeleteModel(name="CommentMap", ),
        migrations.DeleteModel(name="ProfessionMap", ),
    ]
