import xml.etree.ElementTree as ET

#all_links_list = []

#def resetLinksList ():
#    all_links_list = []

class Link :
    def __init__ (self):
        self.parent_node = ""
        self.child_node = ""
        self.parent_clause = None
        self.child_clause = None
#        all_links_list += [self]
    
    def addParent(self,  document,  clause):
        self.parent_node = document + ":" + str(clause)
    
    def addChild(self,  document,  clause):
        self.child_node = document + ":" + str(clause)
    
    def getChild(self):
        return self.child_node

    def getParent(self):
        return self.parent_node

    def getParentDocument(self):
        document,  clause = self.parent_node.split(":")
        return document
        
    def getParentClause(self):
        document,  clause = self.parent_node.split(":")
        return clause
    
    def getChildDocument(self):
        document,  clause = self.child_node.split(":")
        return document
    
    def getChildClause(self):
        document,  clause = self.child_node.split(":")
        return clause

    def remove(self):
        self.parent_clause.removeChildLink(self)
        self.parent_clause.removeParentLink(self)

    def consolidate(self,  project):
        parent_document,  parent_clause = self.parent_node.split(":")
        child_document, child_clause = self.child_node.split(":")
        self.parent_clause = project.getDocument(parent_document).getClause(parent_clause)
        self.child_clause = project.getDocument(child_document).getClause(child_clause)
        self.parent_clause.addChildLink(self)
        self.child_clause.addParentLink(self)
