from eea.restapi.interfaces import ILocalSectionMarker
from forests.theme.interfaces import ILocalSectionMarker as IForestLocalMarker
from plone.dexterity.interfaces import IDexterityContainer
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContainer)
def index_title(object):
    try:
        parent = object.restrictedTraverse("../..")
    except AttributeError:
        return object.Title()
    else:
        if ILocalSectionMarker.providedBy(parent) or \
                IForestLocalMarker.providedBy(parent):

            return parent.Title()

    return object.Title()


@indexer(IDexterityContent)
def index_topics(object):
    return object.aq_inner.aq_self.topics
