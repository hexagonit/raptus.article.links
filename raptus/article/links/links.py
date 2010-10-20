from zope import interface, component

from Products.CMFCore.utils import getToolByName

from raptus.article.core.interfaces import IArticle
from raptus.article.links.interfaces import ILinks

class Links(object): 
    """ Provider for links contained in an article
    """
    interface.implements(ILinks)
    component.adapts(IArticle)
    
    def __init__(self, context):
        self.context = context
        
    def getLinks(self):
        """ Returns a list of links (catalog brains)
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        return catalog(portal_type='Link', path={'query': '/'.join(self.context.getPhysicalPath()),
                                                 'depth': 1}, sort_on='getObjPositionInParent')
