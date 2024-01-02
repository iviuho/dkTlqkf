from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(models.Model):
    username_validator = UnicodeUsernameValidator()

    created_at = models.DateTimeField(auto_now_add=True)
    login_id = models.CharField(
        max_length=30, unique=True, validators=[username_validator]
    )
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id} - {self.login_id}"


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

    def __str__(self) -> str:
        return self.content
