from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^rosetta/',include('rosetta.urls')),
    url(r'^admin/$','rosetta.tests.views.dummy', name='dummy-login')
)
