from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'todolist/login.html')

def signup(request):
    return render(request, 'todolist/signup.html')

def adduser(request):
    return HttpResponseRedirect('signup/')
