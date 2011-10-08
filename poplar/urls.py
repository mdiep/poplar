
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('poplar.views',
    url('^$',                         'activity_feed', name='activity-feed'),
    url('^people/?$',                 'everyone',      name='everyone'),
    url('^people/(\d+)/?$',           'person',        name='person'),
    url('^people/new/?$',             'person_add',    name='person_add'),
    url('^people/(\d+)/notes/new/?$', 'note_add',      name='note_add'),
    url('^groups/([\w-]+)/?$',        'group',         name='group'),
    url('^api/search/?$',             'search',        name='api-search'),
)
