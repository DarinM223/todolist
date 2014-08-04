from django.forms import ModelForm
from django import forms
from todolist import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# extends default User authentication form to allow for email fields
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        # define widgets as necessary so it can be styled
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

class TodoListForm(ModelForm):
    class Meta:
        model = models.TodoList
        fields = ['name']

class TodoFieldForm(ModelForm):
    class Meta:
        model = models.TodoField
        fields = ['text', 'deadline']
