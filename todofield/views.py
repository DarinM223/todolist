from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from todofield import models
from todofield import forms
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def field_create(request, username, pk):
    if request.user.is_authenticated() and request.user.username == username:
        todolist = get_object_or_404(models.TodoList, pk=pk)
        if request.method == 'POST':
            todofield_form = forms.TodoFieldForm(data=request.POST)
            if todofield_form.is_valid():
                    todofield = todofield_form.save(commit=False)
                    todofield.parentList = todolist
                    todofield.save()
                    return HttpResponseRedirect(reverse('todolist:todolist', args=(request.user.username, pk,)))
        else:
            todofield_form = forms.TodoFieldForm()
        return render(request, 'todofield/field_create.html', { 'form': todofield_form, 'list': todolist })
    else:
        return HttpResponse('You are not authorized to perform this action!')

def field_delete(request, username, pk, field_pk):
    if request.user.is_authenticated() and request.user.username == username:
        todofield = get_object_or_404(models.TodoField, pk=field_pk)
        todofield.delete()
        return HttpResponseRedirect(reverse('todolist:todolist', args=(username, pk,)))
    else:
        return HttpResponse('You are not authorized to perform this action!')

def field_edit(request, username, pk, field_pk):
    if request.user.is_authenticated() and request.user.username == username:
        todofield = get_object_or_404(models.TodoField, pk=field_pk)
        if request.method == 'POST':
            todofield_form = forms.TodoFieldForm(request.POST, instance=todofield)
            if todofield_form.is_valid():
                todofield_form.save()
                return HttpResponseRedirect(reverse('todolist:todolist', args=(username, pk,)))
        else:
            todofield_form = forms.TodoFieldForm(instance=todofield)
        return render(request, 'todofield/field_edit.html', { 'form': todofield_form, 'field': todofield })
    else:
        return HttpResponse('You are not authorized to perform this action!')
