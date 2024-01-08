from django.contrib.auth.models import User
from django.db import models


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
