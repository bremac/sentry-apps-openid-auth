from django.conf.urls.defaults import *
from sentry.conf import urls

urlpatterns = patterns('',
    url(r'^login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^google/login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
) + urls.urlpatterns
