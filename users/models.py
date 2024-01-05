from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = "username"
