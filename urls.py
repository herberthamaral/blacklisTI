from django.conf.urls.defaults import patterns, include, url
import settings
import home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home.views.index, name='home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^profile/', include('profile.urls')),
    (r'^review/', include('review.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
