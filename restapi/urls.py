from django.conf.urls.defaults import patterns, include, url

# enables the lovely Django admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
