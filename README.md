Sentry OpenID Authorization for Google Apps
===========================================

This is a trivial recipe to add Google Apps authentication via OpenID
to an installation of sentry. Though sentry itself has adopted
[django-social-auth](https://github.com/omab/django-social-auth/),
social auth may be inconvenient to users using multiple Google Accounts,
as the domain of an Apps account isn't checked until _after_ the user
goes through the OpenID workflow.

Instead, this recipe builds off of django-openid-auth and
[adieu's patched version of python-openid](https://github.com/adieu/python-openid)
(as described at http://learnedstuffs.wordpress.com/2012/05/22/django-google-account-authentication/)
to make use of the _hd_ query parameter to Google's OpenID implementation.


Installation
============
It should be sufficient to install this package using pip, which will pull in
sentry and the requisite OpenID packages.


Configuration
=============

To start using OpenID Authorization, first ensure that all of the
users on your sentry server have email addresses which correspond
to those assigned to them in your Google Apps domain. Add the following
to your sentry configuration file, and you're done:

```python
EXTRA_INSTALLED_APPS = (
    'django_openid_auth',
    'sentry_apps_openid_auth',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
OPENID_SSO_SERVER_URL = 'https://google.com/accounts/o8/site-xrds?hd=YOUR-APPS-DOMAIN'

AUTHENTICATION_BACKENDS = (
    'sentry_apps_openid_auth.auth.GoogleBackend',
)

ROOT_URLCONF = 'sentry_apps_openid_auth.urls'
```
