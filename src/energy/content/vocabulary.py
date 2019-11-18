from plone.app.vocabularies.catalog import KeywordsVocabulary as KV
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory


@implementer(IVocabularyFactory)
class KeywordsVocabulary(KV):
    def __init__(self, index):
        self.keyword_index = index


TopicsVocabularyFactory = KeywordsVocabulary('topics')
ResourceTypeVocabularyFactory = KeywordsVocabulary('resource_type')
