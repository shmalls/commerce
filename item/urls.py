from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.item, name='item'),
    url(r'add/$', views.add_to_cart, name='add'),
	url(r'review/$', views.add_review, name='review'),
]