from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elkyrtools.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fake_api_gen/', include('fake_api_gen.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
