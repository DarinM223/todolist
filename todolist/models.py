from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    dateCreated = models.DateTimeField('Date created', auto_now_add=True)
    def __unicode__(self):
        return self.name

