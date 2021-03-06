from django.db import models
from datetime import datetime
from uuid import uuid4

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    user_name = models.CharField(max_length=40)
    certification = models.CharField(max_length=100)
    register = models.DateField(default=datetime.now)
    phone = models.CharField(max_length=20)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)


class Post(models.Model):
    board_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    date = models.DateField(default=datetime.now)


class Comment(models.Model):
    comment_id = models.UUIDField( primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    date = models.DateField(default=datetime.now)

    class Meta : #기본적으로 필드의 결과를 내림차순으로 정렬하도록
        ordering =['date']

