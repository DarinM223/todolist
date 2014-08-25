from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from users import forms

from django.core.urlresolvers import reverse

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponseRedirect(reverse('main_app:index'))
    else:
        return HttpResponseRedirect(reverse('main_app:index'))

def login(request):
    if request.method == 'POST':
        authform = AuthenticationForm(data=request.POST)

        if authform.is_valid():
            auth_login(request, authform.get_user())
            return HttpResponseRedirect(reverse('users:user', args=(authform.get_user().username,)))
    else: 
        authform = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': authform })


def signup(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()
            return HttpResponseRedirect(reverse('main_app:index'))
    else:
        user_form = forms.UserCreateForm()

    return render(request, 'users/signup.html', { 'form': user_form })

def detail(request, username):
    if not request.user.is_authenticated():
        return HttpResponse('You are not logged in!')
    user = get_object_or_404(User, username=username)
    return render(request, 'users/detail.html', { 'this_user': user })
