from django.conf.urls import patterns, include, url
from views import post_new

urlpatterns = patterns('',
    url(r'^$', post_new, name="post_new"),
)