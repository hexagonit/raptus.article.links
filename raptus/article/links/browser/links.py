from Acquisition import aq_inner
from zope import interface, component

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize

from raptus.article.core import RaptusArticleMessageFactory as _
from raptus.article.core import interfaces
from raptus.article.links.interfaces import ILinks as ILinksRetriever

class ILinks(interface.Interface):
    """ Marker interface for the attachments viewlet
    """

class Component(object):
    """ Component which lists attachments of an article
    """
    interface.implements(interfaces.IComponent)
    component.adapts(interfaces.IArticle)
    
    title = _(u'Links')
    description = _(u'List of links contained in the article.')
    image = '++resource++links.gif'
    interface = ILinks
    viewlet = 'raptus.article.links'
    
    def __init__(self, context):
        self.context = context

class Viewlet(ViewletBase):
    """ Viewlet listing the links contained in the article
    """
    index = ViewPageTemplateFile('links.pt')

    @property
    @memoize
    def links(self):
        provider = ILinksRetriever(self.context)
        manageable = interfaces.IManageable(self.context)
        items = manageable.getList(provider.getLinks())
        for item in items:
            item.update({'title': item['brain'].Title,
                         'description': item['brain'].Description,
                         'url': item['brain'].getRemoteUrl})
        return items
