from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^profile/$', views.userprofile, name='userprofile'),
   url(r'^editprofile/$', views.editprofile, name='editprofile'),
]