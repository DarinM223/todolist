from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

#class User(models.Model):
#    username = models.CharField(max_length=50, primary_key=True)
#    password = models.CharField(max_length=50)
#    email = models.EmailField(unique=True)
#    def __unicode__(self):
#        return self.username

class TodoList(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=50, primary_key=True)
    dateCreated = models.DateTimeField('Date created')
    def __unicode__(self):
        return self.name

class TodoField(models.Model):
    parentList = models.ForeignKey(TodoList)
    text = models.CharField(max_length=200)
    dateCreated = models.DateTimeField('Date created')
    deadline = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.text

