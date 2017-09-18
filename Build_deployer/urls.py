'''
Created on Sep 15, 2017

@author: calvin
'''
# Build_deployer/urls.py
from django.conf.urls import url
from Build_deployer import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
]