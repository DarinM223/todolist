from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, FormView
from todolist import models
from todolist import forms
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user', args=(request.user.username,)))
    else: 
        return render(request, 'todolist/index.html')

def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

def login(request):
    if request.method == 'POST':
        authform = AuthenticationForm(data=request.POST)

        if authform.is_valid():
            auth_login(request, authform.get_user())
            return HttpResponseRedirect(reverse('user', args=(authform.get_user().username,)))
    else: 
        authform = AuthenticationForm()
    return render(request, 'todolist/login.html', { 'form': authform })


def register(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            authuser = authenticate(username=user.username, password=user.password)
            return HttpResponseRedirect(reverse('user', args=(user.username,)))
    else:
        user_form = forms.UserCreateForm()

    return render(request, 'todolist/signup.html', { 'form': user_form })

def detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'todolist/user_detail.html', { 'object': user })
