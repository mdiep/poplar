from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'',        include('poplar.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sign-in/?',  'django.contrib.auth.views.login',             name='sign-in'),
    url(r'^sign-out/?', 'django.contrib.auth.views.logout_then_login', name='sign-out'),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
