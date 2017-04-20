from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.profile, name='profile'),
	url(r'^view$', views.view_profile, name='view_profile'),
	url(r'^edit$', views.edit_profile, name='edit_profile'),
]