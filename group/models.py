from django.db import models
from user.models import User

class Group(models.Model):
    name = models.CharField(max_length=20, null=False)
    users = models.ManyToManyField('user.User')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()