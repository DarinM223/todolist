from django.conf.urls import url

from todofield import views

urlpatterns = [
    url(r'new/$', views.create, name='create'),
    url(r'^(?P<field_pk>[-_\w]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<field_pk>[-_\w]+)/edit/$', views.edit, name='edit'),
]
