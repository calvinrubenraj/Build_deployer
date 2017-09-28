'''
Created on Sep 15, 2017

@author: calvin
'''
# Build_deployer/urls.py
from django.conf.urls import url
from Build_deployer import views


urlpatterns = [
    url(r'^$', views.login_validation),
    url(r'^login.jsp$', views.login_validation),
    url(r'^temp$', views.TemplatesView.as_view()),
    url(r'^test$', views.TestView.as_view()),
    #url(r'^about/$', views.AboutPageView.as_view()),
#    url(r'^login_failed/$', views.login_validation),
 #   url(r'^get_login/$', views.get_name, name='get_name'),
]