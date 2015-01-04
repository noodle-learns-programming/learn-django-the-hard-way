from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^placeholder/(?P<width>\d+)x(?P<height>\d+)', 'views.angular.placeholder'),
    url(r'^add/(?P<n1>[0-9]+)/(?P<n2>[0-9]+)/$', 'views.angular.add')
)