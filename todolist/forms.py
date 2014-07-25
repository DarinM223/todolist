from django.forms import ModelForm
from django import forms
from todolist import models

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }

class TodoListForm(ModelForm):
    class Meta:
        model = models.TodoList
        fields = ['name']
