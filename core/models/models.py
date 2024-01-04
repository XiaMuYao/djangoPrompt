# Create your models here.
from django.db import models


class Prompt(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    content = models.TextField()
    un_like = models.IntegerField(null=True, default=0)
    like = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    prompts = models.ManyToManyField('Prompt', related_name='categories')


class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    prompts = models.ManyToManyField('Prompt', related_name='professions')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    prompt = models.ForeignKey('Prompt', related_name='comments', on_delete=models.CASCADE)


class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
