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

from django.contrib.auth.decorators import permission_required, login_required
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
            user.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        user_form = forms.UserCreateForm()

    return render(request, 'todolist/signup.html', { 'form': user_form })

def detail(request, username):
    if not request.user.is_authenticated():
        return HttpResponse('You are not logged in!')
    user = get_object_or_404(User, username=username)
    return render(request, 'todolist/user_detail.html', { 'this_user': user })

def listdetail(request, username, pk):
    if not request.user.is_authenticated():
        return HttpResponse('You are not logged in!')
    my_list = get_object_or_404(models.TodoList, pk=pk)
    return render(request, 'todolist/list_detail.html', { 'list': my_list })

def createlist(request, username):
    if request.user.is_authenticated() and request.user.username == username:
        if request.method == 'POST':
            todolist_form = forms.TodoListForm(data=request.POST)
            if todolist_form.is_valid():
                todolist = todolist_form.save()
                todolist.user = request.user
                todolist.save()
                return HttpResponseRedirect(reverse('index'))
        else:
            todolist_form = forms.TodoListForm()
        return render(request, 'todolist/list_create.html', { 'form': todolist_form })
    else:
        return HttpResponse('You are not authorized to perform this action!')

def listdelete(request, username, pk):
    if request.user.is_authenticated() and request.user.username == username:
        todolist = get_object_or_404(models.TodoList, pk=pk)
        todolist.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse('You are not authorized to perform this action!')

def createfield(request, username, pk):
    if request.user.is_authenticated() and request.user.username == username:
        todolist = get_object_or_404(models.TodoList, pk=pk)
        if request.method == 'POST':
            todofield_form = forms.TodoFieldForm(data=request.POST)
            if todofield_form.is_valid():
                    todofield = todofield_form.save(commit=False)
                    todofield.parentList = todolist
                    todofield.save()
                    return HttpResponseRedirect(reverse('todolist', args=(request.user.username, pk,)))
        else:
            todofield_form = forms.TodoFieldForm()
        return render(request, 'todolist/field_create.html', { 'form': todofield_form, 'list': todolist })
    else:
        return HttpResponse('You are not authorized to perform this action!')

def fielddelete(request, username, pk, field_pk):
    if request.user.is_authenticated() and request.user.username == username:
        todofield = get_object_or_404(models.TodoField, pk=field_pk)
        todofield.delete()
        return HttpResponseRedirect(reverse('todolist', args=(username, pk,)))
    else:
        return HttpResponse('You are not authorized to perform this action!')

def fieldedit(request, username, pk, field_pk):
    if request.user.is_authenticated() and request.user.username == username:
        todofield = get_object_or_404(models.TodoField, pk=field_pk)
        if request.method == 'POST':
            todofield_form = forms.TodoFieldForm(request.POST, instance=todofield)
            if todofield_form.is_valid():
                todofield_form.save()
                return HttpResponseRedirect(reverse('todolist', args=(username, pk,)))
        else:
            todofield_form = forms.TodoFieldForm(instance=todofield)
        return render(request, 'todolist/field_edit.html', { 'form': todofield_form, 'field': todofield })
    else:
        return HttpResponse('You are not authorized to perform this action!')

