from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from index.views import profile
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # enable the admin
    url(r'^admin/', include(admin.site.urls)),

    # index page
    url(r'^home/$', include('index.urls')),

    # login-logout, login on index page
    url(r'^$', login),
    url(r'^accounts/logout/$', logout, {'next_page':'/'}),

    # profile
    url(r'^accounts/profile/$', profile),

    #post
    url(r'^post/$', include('post.urls')),

    #news
    url(r'^actu/$', TemplateView.as_view(template_name="news.html")),

    #trombinoscope
    url(r'^trombinoscope/$', TemplateView.as_view(template_name="trombinoscope.html")),

)
