from django.conf.urls import url

from todolist import views
from class_based_auth_views.views import LoginView

# use django-class-based-auth-views for authentication views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name="login"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^users/(?P<username>[-_\w]+)/$', views.detail, name='user'),
    url(r'^users/(?P<username>[-_\w]+)/(?P<pk>[-_\w]+)/$', views.listdetail, name='todolist')
]
