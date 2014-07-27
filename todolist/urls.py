from django.conf.urls import url

from todolist import views
from class_based_auth_views.views import LoginView

# use django-class-based-auth-views for authentication views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(form_class=AuthenticationForm, template_name='todolist/login.html', success_url='/todolist'), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/', views.UserCreateView.as_view(), name='signup'),
    url(r'^users/(?P<username>[-_\w]+)/', views.UserDetailView.as_view(), name='user'),
]
