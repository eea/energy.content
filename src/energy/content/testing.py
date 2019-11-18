# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import energy.content


class EnergyContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=energy.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'energy.content:default')


ENERGY_CONTENT_FIXTURE = EnergyContentLayer()


ENERGY_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ENERGY_CONTENT_FIXTURE,),
    name='EnergyContentLayer:IntegrationTesting',
)


ENERGY_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ENERGY_CONTENT_FIXTURE,),
    name='EnergyContentLayer:FunctionalTesting',
)


ENERGY_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ENERGY_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EnergyContentLayer:AcceptanceTesting',
)
