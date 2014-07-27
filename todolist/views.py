from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, FormView
from todolist import models
from todolist import forms
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user', args=(request.user.username,)))
    else: 
        return render(request, 'todolist/index.html')

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse('You have to login before you can log out!')

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
