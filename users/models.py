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
