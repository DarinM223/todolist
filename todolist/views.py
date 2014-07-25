from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from todolist import models
from todolist import forms

# Create your views here.

def index(request):
    return render(request, 'todolist/login.html')

class UserCreateView(CreateView):
    model = models.User
    form_class = forms.UserForm
    fields = ['username', 'email', 'password']
    template_name = 'todolist/signup.html'
    success_url = '/todolist'

class UserDetailView(DetailView):
    model = models.User
    template_name = 'todolist/user_detail.html'
