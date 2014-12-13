from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homeport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'homeport.views.home', name='home'),
    url(r'^on', 'homeport.views.on', name='on'),
    url(r'^off', 'homeport.views.off', name='off'),
    url(r'^log', 'homeport.views.log', name='log'),
    url(r'^gettemp', 'homeport.views.gettemp', name='gettemp'),
)
