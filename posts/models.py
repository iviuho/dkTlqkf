from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(models.Model):
    username_validator = UnicodeUsernameValidator()

    created_at = models.DateTimeField(auto_now_add=True)
    login_id = models.CharField(
        max_length=30, unique=True, validators=[username_validator]
    )
    password = models.CharField(max_length=100)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    content = models.CharField(max_length=500)
    view_count = models.PositiveIntegerField(blank=True, default=0)
    parent = models.ForeignKey(
        "self",
        on_delete=models.RESTRICT,
        related_name="comments",
        null=True,
        blank=True,
    )
