from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)