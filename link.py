#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

class Link :
    def __init__ (self):
        self.parent_id = ""
        self.child_id = ""
        self.parent = None
        self.child = None
    
    def addParent(self, clause, clauseObj = None):
        self.parent_id = clause
        if (clauseObj is not None) :
            self.parent = clauseObj
            self.parent.addChildLink(self)
    
    def addChild(self, clause, clauseObj = None):
        self.child_id = clause
        if (clauseObj is not None) :
            self.child = clauseObj
            self.child.addParentLink(self)
    
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
        return self.parent_id
    
    def getChildDocumentID(self):
        document, clause = self.child_id.split(":")
        return document
    
    def getChildClauseID(self): 
        return self.child_id

    def remove(self):
        child_id = self.child.getID()
        parent_id = self.parent.getID()
        del self.parent.child_links[child_id]
        del self.child.parent_links[parent_id]
        self.parent.removeChildLink(child_id)
        self.child.removeParentLink(parent_id)

    def consolidateLink(self, project):
        if self.parent is None:
            parent_document,  parent = self.parent_id.split(":")
            self.parent = project.getDocument(parent_document).getClause(self.parent_id)
        if self.child is None:  
            child_document, child = self.child_id.split(":")
            self.child = project.getDocument(child_document).getClause(self.child_id)
        self.parent.addChildLink(self)
        self.child.addParentLink(self)
