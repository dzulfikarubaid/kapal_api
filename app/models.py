from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    position = models.CharField(max_length=40, blank=False, null=False)
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=60, blank=False, null=False)