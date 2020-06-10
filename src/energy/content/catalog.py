''' catalog module '''
from plone.dexterity.interfaces import IDexterityContainer
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer
from forests.theme.interfaces import ILocalSectionMarker as IForestLocalMarker
from eea.restapi.interfaces import ILocalSectionMarker


@indexer(IDexterityContainer)
def index_title(ob):
    """index_title.

    :param ob:
    """
    try:
        parent = ob.restrictedTraverse("../..")
    except AttributeError:
        return ob.Title()
    else:
        if ILocalSectionMarker.providedBy(parent) or \
                IForestLocalMarker.providedBy(parent):

            return parent.Title()

    return ob.Title()


@indexer(IDexterityContent)
def index_topics(ob):
    """index_topics.

    :param ob:
    """
    return ob.aq_inner.aq_self.topics
