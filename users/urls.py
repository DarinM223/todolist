from django.conf.urls import url, include

from users import views
urlpatterns = [
    url(r'^login$', views.login, name="login"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<username>[-_\w]+)/$', views.detail, name='user'),
]
