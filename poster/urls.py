from django.conf.urls import patterns, include, url
from views import create

urlpatterns = patterns('',
    url(r'^$', create, name="create"),
)