from django.db import models


class User(models.Model):
    created_at = models.DateTimeField()
    login_id = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


class Post(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
