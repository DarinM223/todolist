from django.conf.urls import url

from todolist import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.UserCreateView.as_view(), name='signup'),
    url(r'^users/(?P<username>[-_\w]+)/', views.UserDetailView.as_view(), name='user'),
]
