from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=10, null=True)



