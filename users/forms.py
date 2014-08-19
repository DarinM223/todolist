from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# extends default User authentication form to allow for email fields
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        # define widgets as necessary so it can be styled
        widgets = {
                'username': forms.TextInput(),
                'email': forms.TextInput(),
                'password1': forms.PasswordInput(),
                'password2': forms.PasswordInput()
        }
