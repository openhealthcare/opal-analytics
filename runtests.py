"""
Standalone test runner for OPAL plugin
"""
import os
import sys

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE = 'analytics.tests.dummy_options_module',
                   ROOT_URLCONF='analytics.urls',
                   INTEGRATING=False,
                   DEFAULT_DOMAIN='localhost',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'opal',
                                   'analytics'
                               ))

from analytics.tests import dummy_options_module
from analytics.tests import dummy_opal_application

from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['analytics', ])
if failures:
    sys.exit(failures)
