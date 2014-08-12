from __future__ import unicode_literals, absolute_import

"""Production settings and globals."""

import os
import dj_database_url

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def env(setting, default=None):
    """ Get the environment setting or return exception """
    key = os.environ.get(setting, default)

    if key is None:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

    return key

# HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [env('OPENSHIFT_APP_DNS')]
# END HOST CONFIGURATION

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = env('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
DATABASES = {}
DATABASES['default'] = dj_database_url.config("OPENSHIFT_POSTGRESQL_DB_URL")
DATABASES['default']['NAME'] = env('OPENSHIFT_APP_NAME')
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION


# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('OPENSHIFT_SECRET_TOKEN')
# END SECRET CONFIGURATION


# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = join(env('OPENSHIFT_DATA_DIR'), 'media')

# END MEDIA CONFIGURATION


# THIRD PARTY CONFIGURATION
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': join(env('OPENSHIFT_DATA_DIR', 'whoosh_index')),
    }
}

# END THIRD PARTY CONFIGURATION


# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = join(env('OPENSHIFT_REPO_DIR'), 'wsgi', 'static')
# END STATIC FILE CONFIGURATION


# SECURITY CONFIGURATION
# http://django-secure.readthedocs.org/en/latest/settings.html#secure-ssl-redirect
MIDDLEWARE_CLASSES += (
    'djangosecure.middleware.SecurityMiddleware',
)

SECURE_SSL_REDIRECT = True

# http://django-secure.readthedocs.org/en/latest/settings.html#secure-frame-deny
SECURE_FRAME_DENY = True

# https://docs.djangoproject.com/en/1.6/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# http://django-secure.readthedocs.org/en/latest/settings.html#secure-hsts-seconds
SECURE_HSTS_SECONDS = True

# http://django-secure.readthedocs.org/en/latest/settings.html#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAIN = True

# END SECURITY CONFIGURATION
