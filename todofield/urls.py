from django.conf.urls import url

from todofield import views

urlpatterns = [
    url(r'new/$', views.field_create, 
        name='field_create'),
    url(r'^(?P<field_pk>[-_\w]+)/delete/$', 
        views.field_delete, name='field_delete'),
    url(r'^(?P<field_pk>[-_\w]+)/edit/$', 
        views.field_edit, name='field_edit'),
]
