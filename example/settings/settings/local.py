from __future__ import unicode_literals, absolute_import

"""Development settings and globals."""

from os.path import join, normpath

from .base import *


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# END EMAIL CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(SITE_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION


# TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
# END TOOLBAR CONFIGURATION

# TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#template-string-if-invalid
TEMPLATE_STRING_IF_INVALID = 'INVALID VARIABLE: (%s)'

# http://django-crispy-forms.readthedocs.org/en/latest/crispy_tag_forms.html#make-crispy-forms-fail-loud
CRISPY_FAIL_SILENTLY = False
# END TEMPLATE CONFIGURATION

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': join(SITE_ROOT, 'whoosh_index'),
    }
}
