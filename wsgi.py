#!/usr/bin/python
import os
import sys

virtualenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],
                          'virtenv', 'bin', 'activate_this.py')

try:
    if sys.hexversion < 0x3000000:
        execfile(virtualenv, dict(__file__=virtualenv))
    else:
        exec(compile(open(virtualenv).read(), virtualenv, 'exec'),
             dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings.settings.production'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
