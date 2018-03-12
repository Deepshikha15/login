from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login



urlpatterns = [
    # post views
    #url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    #url(r'^login/$','django.contrib.auth.views.login',name='login'),
    #url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
    #url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^login/$', login, name='login'),
    url(r'^login/$', logout, name='logout'),
    url(r'^login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),


]