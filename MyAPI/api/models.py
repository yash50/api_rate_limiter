from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    request_limits_developer = models.IntegerField(default=-1)
    request_limits_organization = models.IntegerField(default=-1)
    