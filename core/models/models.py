# Create your models here.
from django.db import models


class Prompt(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    content = models.TextField()
    in_put = models.TextField()
    out_put = models.TextField()
    un_like = models.IntegerField(null=True, default=0)
    like = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    prompts = models.ManyToManyField('Prompt', related_name='categories')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)


class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    prompts = models.ManyToManyField('Prompt', related_name='platforms')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    prompts = models.ManyToManyField('Prompt', related_name='tags')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)


class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    prompts = models.ManyToManyField('Prompt', related_name='professions')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    prompt = models.ForeignKey('Prompt', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_type = models.IntegerField()
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)
