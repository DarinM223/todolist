from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from todolist import models
from todolist import forms
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'todolist/login.html')

class UserCreateView(CreateView):
    form_class = forms.UserCreateForm
    model = User
    template_name = 'todolist/signup.html'
    # redirects to user detail page
    def get_success_url(self):
        return reverse('user', args=(self.object.username,))

class UserDetailView(DetailView):
    # model = models.User
    model = User
    template_name = 'todolist/user_detail.html'
    # gets object from username parameter in url string
    def get_object(self):
        return self.get_queryset().get(username=self.kwargs.get("username"))
