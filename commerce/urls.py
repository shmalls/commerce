from django.conf.urls import include, url
from django.contrib import admin
from commerce import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'commerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^item/', include('item.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
