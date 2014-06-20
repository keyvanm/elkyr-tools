from django.conf.urls import patterns, include, url

urlpatterns = patterns('fake_api_gen.views',
	url(r'^fakeapi/(?P<api_slug>[\w-]+)/$', 'apiview'),
)