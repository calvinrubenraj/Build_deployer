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
    url(r'^CygFileProf.html$', views.CygnetFileProfPageView),
    url(r'^M6FileProf.html$', views.M6FileProfPageView.as_view()),
    url(r'^M6EnctFileProf.html$', views.M6EncrptyFileProfPageView.as_view()),
    url(r'^CygAddFileProf.html$', views.CygnetAddFileProfPageView),
    url(r'^CygAddFileVal$',views.cyg_add_prof_validation),
    url(r'^M6AddFileProf.html$', views.M6AddFileProfPageView.as_view()),
    url(r'^M6EnctAddFileProf.html$', views.M6EnctAddFileProfPageView.as_view()),
    url(r'^Complete.html$', views.CompleteView.as_view()),
    #url(r'^about/$', views.AboutPageView.as_view()),
#    url(r'^login_failed/$', views.login_validation),
 #   url(r'^get_login/$', views.get_name, name='get_name'),
]