=================
django-kb-example
=================

Example of the app `django-kb <https://github.com/eliostvs/django-kb>`_ running on Openshift.


Installation
------------

#. Create an account at `Openshift <https://www.openshift.com>`_.

#. Install rhc command line tools and login: ::

    $ rhc setup

#. Create a python aplication: ::

    $ rhc create-app knowledge python-3.3 postgresql-9.2

#. Add this upstream repository: ::

    $ cd knowledge
    $ git remote add upstream -m master git://github.com/eliostvs/django-kb-example.git
    $ git pull -s recursive -X theirs upstream master

#. Them push to repo upstream: ::

    $ git push

#. That's it. You can now checkout your application at: ::

    http://knowledge-$yournamespace.rhcloud.com

