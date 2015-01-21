"""
Plugin definition for the analytics OPAL plugin
"""
from django.conf import settings
from opal.utils import OpalPlugin

from analytics.urls import urlpatterns

BACKEND = getattr(settings, 'OPAL_ANALYTICS_BACKEND', 'google.analytics')
NODOMAIN = getattr(settings, 'OPAL_ANALYTICS_NODOMAIN', False)

SCRIPTS = {
    'google.analytics': {
        'plugin': 'js/angulartics-0.17.2/angulartics-ga.min.js',
        'snippet': 'analytics/ga.html'
    },
    'piwik': {
        'plugin': 'js/angulartics-0.17.2/angulartics-piwik.min.js',
        'snippet': 'analytics/piwik.html'
    }
}

class AnalyticsPlugin(OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.upstream.deps': [
            'js/angulartics-0.17.2/angulartics.min.js',
            SCRIPTS[BACKEND]['plugin']
        ]
    }
    head_extra = [SCRIPTS[BACKEND]['snippet']]
    angular_module_deps = [
        'angulartics',
        'angulartics.google.analytics'
    ]

    def restricted_teams(self, user):
        """
        Return any restricted teams for particualr users that our
        plugin may define.
        """
        return []

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def flows(self):
        """
        Return any custom flows that our plugin may define
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}
