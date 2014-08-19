from django.conf.urls import url

from todolist import views
# use django-class-based-auth-views for authentication views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    url(r'^new/$', views.list_create, name='list_create'),
    url(r'^(?P<pk>[-_\w]+)/$', views.list_detail, name='todolist'),
    url(r'^(?P<pk>[-_\w]+)/delete/$', views.list_delete, 
        name='list_delete'),
    url(r'^(?P<pk>[-_\w]+)/new/$', views.field_create, 
        name='field_create'),
    url(r'^(?P<pk>[-_\w]+)/(?P<field_pk>[-_\w]+)/delete/$', 
        views.field_delete, name='field_delete'),
    url(r'^(?P<pk>[-_\w]+)/(?P<field_pk>[-_\w]+)/edit/$', 
        views.field_edit, name='field_edit'),
]
