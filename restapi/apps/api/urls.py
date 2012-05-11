from django.conf.urls.defaults import patterns, include, url


from apps.api.views import *

urlpatterns = patterns('',
    url(r'^teams/', teams),
)
