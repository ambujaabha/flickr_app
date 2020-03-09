from django.db import models
from flicker_user.models import FlickerUser

class Group(models.Model):
    name = models.CharField(max_length=20, null=False)
    users = models.ManyToManyField('flicker_user.FlickerUser')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()