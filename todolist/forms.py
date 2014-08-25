from django.forms import ModelForm
from django import forms
from todolist import models

class TodoListForm(ModelForm):
    class Meta:
        model = models.TodoList
        fields = ['name']

