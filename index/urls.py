from django.conf.urls import patterns, include, url
from views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
)

urlpatterns += staticfiles_urlpatterns()
