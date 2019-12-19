from eea.restapi.interfaces import ILocalSectionMarker
from forests.theme.interfaces import ILocalSectionMarker as IForestLocalMarker
from plone.dexterity.interfaces import IDexterityContainer
from plone.indexer import indexer


@indexer(IDexterityContainer)
def index_title(object):
    parent = object.aq_parent

    if ILocalSectionMarker.providedBy(parent) or \
            IForestLocalMarker.providedBy(parent):

        return parent.Title()

    return object.Title()
