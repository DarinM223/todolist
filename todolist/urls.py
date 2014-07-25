from django.conf.urls import url

from todolist import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^adduser/', views.adduser, name='adduser'),
]
