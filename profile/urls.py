from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'profile/login.html','redirect_field_name':'redirect_to'}),
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/profile/'}),
        url(r'^signup/$',views.signup)
)
