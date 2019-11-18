# -*- coding: utf-8 -*-
from energy.content.behaviors.energy_union_metadata import IEnergyUnionMetadataMarker
from energy.content.testing import ENERGY_CONTENT_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class EnergyUnionMetadataIntegrationTest(unittest.TestCase):

    layer = ENERGY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_energy_union_metadata(self):
        behavior = getUtility(IBehavior, 'energy.content.energy_union_metadata')
        self.assertEqual(
            behavior.marker,
            IEnergyUnionMetadataMarker,
        )
