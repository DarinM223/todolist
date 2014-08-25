from django.db import models

from todolist.models import TodoList

# Create your models here.

class TodoField(models.Model):
    parentList = models.ForeignKey(TodoList)
    text = models.CharField(max_length=200)
    dateCreated = models.DateTimeField('Date created', auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.text

