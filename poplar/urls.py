
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('poplar.views',
    url('^$',         'activity_feed',  name='activity-feed'),
    url('^people/?$', 'everyone',       name='everyone'),
)
