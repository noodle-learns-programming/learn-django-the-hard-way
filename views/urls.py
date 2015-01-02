from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^add/(?P<n1>[0-9]+)/(?P<n2>[0-9]+)/$', 'views.angular.add')
)