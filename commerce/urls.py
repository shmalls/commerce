from django.conf.urls import include, url
from django.contrib import admin
from commerce import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'commerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^item/', include('item.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'logout.html'}, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^search/', include('search.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^cart/', include('cartapp.urls')),
]
