#!/usr/bin/python
import os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings.settings.production'
application = django.core.handlers.wsgi.WSGIHandler()
