import xml.etree.ElementTree as ET

class Link :
    def __init__ (self):
        self.parent_node = ""
        self.child_node = ""
    
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
        pass
