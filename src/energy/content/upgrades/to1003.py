''' upgrade to 1003 '''


import logging
from plone import api


logger = logging.getLogger('energy.content')


def run_upgrade(setup_context):
    """run_upgrade.

    :param setup_context:
    """
    setup_context.runImportStepFromProfile(
        "profile-energy.content:default",
        "catalog",
        run_dependencies=False,
        purge_old=False,
    )

    catalog = api.portal.get_tool("portal_catalog")

    for brain in catalog.searchResults(lxlxl=True):     # gets all brains
        obj = brain.getObject().aq_inner.aq_self

        if hasattr(obj, 'topics'):
            # import pdb
            # pdb.set_trace()
            obj.meta_topics = obj.topics
            del obj.topics
            obj.reindexObject()
            logger.warn("Migrated %s topics storage: %r", brain.getURL(),
                        obj.meta_topics)
