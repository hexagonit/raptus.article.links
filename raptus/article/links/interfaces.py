from zope import interface

class ILinks(interface.Interface):
    """ Provider for links contained in an article
    """
    
    def getLinks():
        """ Returns a list of links (catalog brains)
        """
