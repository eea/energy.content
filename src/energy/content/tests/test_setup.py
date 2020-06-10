# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from energy.content.testing import ENERGY_CONTENT_INTEGRATION_TESTING


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that energy.content is properly installed."""

    layer = ENERGY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if energy.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'energy.content'))

    def test_browserlayer(self):
        """Test that IEnergyContentLayer is registered."""
        from energy.content.interfaces import (
            IEnergyContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IEnergyContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):
    """TestUninstall."""

    layer = ENERGY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['energy.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if energy.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'energy.content'))

    def test_browserlayer_removed(self):
        """Test that IEnergyContentLayer is removed."""
        from energy.content.interfaces import \
            IEnergyContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IEnergyContentLayer,
            utils.registered_layers())
