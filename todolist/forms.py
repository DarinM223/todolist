from django.forms import ModelForm
from django import forms
from todolist import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap3_datetime.widgets import DateTimePicker

class TodoListForm(ModelForm):
    class Meta:
        model = models.TodoList
        fields = ['name']

class TodoFieldForm(ModelForm):
    class Meta:
        model = models.TodoField
        fields = ['text', 'deadline']
        widgets = {
                'deadline': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                    "pickseconds": False})
        }
