from django.conf.urls import url

from todolist import views

urlpatterns = [
    url(r'^new/$', views.list_create, name='list_create'),
    url(r'^(?P<pk>[-_\w]+)/$', views.list_detail, name='todolist'),
    url(r'^(?P<pk>[-_\w]+)/delete/$', views.list_delete, 
        name='list_delete'),
]
