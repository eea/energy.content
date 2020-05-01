''' vocabulary module '''
from plone.app.vocabularies.catalog import KeywordsVocabulary as KV
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class KeywordsVocabulary(KV):
    """KeywordsVocabulary."""

    def __init__(self, index):
        self.keyword_index = index


def generic_vocabulary(_terms, sort=True):
    """ Returns a zope vocabulary from a dict or a list
    """

    if _terms and isinstance(_terms, dict):
        _terms = _terms.items()
    elif _terms and isinstance(_terms[0], str):
        _terms = [(x, x) for x in _terms]

    if sort:
        _terms = sorted(_terms, key=lambda x: x[0])

    def factory(context):
        """factory.

        :param context:
        """
        return SimpleVocabulary([
            SimpleTerm(n, n.encode('utf-8'), l) for n, l in _terms
        ])

    return factory


TopicsVocabularyFactory = KeywordsVocabulary('meta_topics')

RESOURCE_TYPES = ['', 'Data', 'Briefing', 'Report', 'Indicator', ]


resource_types_vocabulary = generic_vocabulary(RESOURCE_TYPES)
alsoProvides(resource_types_vocabulary, IVocabularyFactory)
