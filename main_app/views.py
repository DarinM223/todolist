from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:user', 
            args=(request.user.username,)))
    else: 
        return render(request, 'main_app/index.html')
