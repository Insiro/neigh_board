from datetime import datetime
from uuid import uuid4
from django.db import models


# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    certification = models.CharField(max_length=100)
    register = models.DateField(default=datetime.now())
    phone = models.CharField(max_length=20)
    region = models.ForeignKey(Region, null=False)
    salt = models.TextField()


class Post(models.Model):
    board_id = models.UUIDField(primary_key=True, uuid=uuid4, editable=False)
    author = models.ForeignKey(User, null=False)
    title = models.CharField(max_length=30)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    region = models.ForeignKey(Region, null=False)


class Comment(models.Model):
    pk = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True)
    comment = models.TextField()
    date = models.DateField(default=datetime.now())
