# -*- coding: utf-8 -*-
''' energy union metadata '''

from plone import schema
from plone.app.dexterity.behaviors.metadata import DCFieldProperty
from plone.app.dexterity.behaviors.metadata import MetadataBase
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IEnergyUnionMetadataMarker(Interface):
    """IEnergyUnionMetadataMarker."""

    pass


@provider(IFormFieldProvider)
class IEnergyUnionMetadata(model.Schema):
    """IEnergyUnionMetadata."""

    resource_type = schema.Choice(
        title=u"Resource Type",
        required=False,
        missing_value='',
        default='',
        vocabulary='energy.resource_types',
    )

    meta_topics = schema.Tuple(
        title=u"Topics",
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )
    form.widget(
        'meta_topics',
        AjaxSelectFieldWidget,
        vocabulary='energy.topics'
    )


@implementer(IEnergyUnionMetadata)
@adapter(IEnergyUnionMetadataMarker)
class EnergyUnionMetadata(MetadataBase):
    """ Metadata behavior implementation
    """

    resource_type = DCFieldProperty(IEnergyUnionMetadata['resource_type'])
    meta_topics = DCFieldProperty(IEnergyUnionMetadata['meta_topics'])
