import xml.etree.ElementTree as ET

class Link :
    def __init__ (self):
        self.parent_id = ""
        self.child_id = ""
        self.parent = None
        self.child = None
    
    def addParent(self,  document,  clause):
        self.parent_id = document + ":" + str(clause)
#        if (object is not None) :
#            self.parent = object
#            self.parent.addChildLink(self)
#            print "Adicionado link PAI com " + self.parent_id
    
    def addChild(self,  document,  clause):
        self.child_id = document + ":" + str(clause)
#        if (object is not None) :
#            self.child = object
#            self.child.addParentLink(self)
    
    def getChildID(self):
        return self.child_id

    def getParentID(self):
        return self.parent_id
    
    def getParent(self):
        return self.parent
    
    def getChild(self):
        return self.child

    def getParentDocumentID(self):
        document,  clause = self.parent_id.split(":")
        return document

    def getParentClauseID(self):
        document,  clause = self.parent_id.split(":")
        return clause
    
    def getChildDocumentID(self):
        document,  clause = self.child_id.split(":")
        return document
    
    def getChildClauseID(self):
        document,  clause = self.child_id.split(":")
        return clause

    def remove(self):
        self.parent.removeChildLink(self)
        self.parent.removeParentLink(self)

    def consolidateParent(self,  project):
        if self.parent is None:
            parent_document,  parent = self.parent_id.split(":")
            self.parent = project.getDocument(parent_document).getClause(parent)
            self.parent.addChildLink(self)

    def consolidateChild(self,  project):
        if self.child is None:
            child_document, child = self.child_id.split(":")
            self.child = project.getDocument(child_document).getClause(child)
            self.child.addParentLink(self)
