from django.conf.urls import url

from todolist import views

urlpatterns = [
    url(r'^new/$', views.create, name='create'),
    url(r'^(?P<pk>[-_\w]+)/$', views.detail, name='todolist'),
    url(r'^(?P<pk>[-_\w]+)/delete/$', views.delete, 
        name='delete'),
]
