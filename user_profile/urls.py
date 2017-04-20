from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.profile, name='profile'),
	url(r'^view-profile$', views.view_profile, name='view_profile'),
	url(r'^edit-profile$', views.edit_profile, name='edit_profile'),
	url(r'^view-payment$', views.view_payment, name='view_payment'),
	url(r'^edit-payment$', views.edit_payment, name='edit_payment'),

]