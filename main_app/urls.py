from django.conf.urls import url

from main_app import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
];
