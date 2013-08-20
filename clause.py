#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import xml.etree.ElementTree as ET
import link

class Clause:
    def __init__(self,  document=None):
        self.document = document
        self.id = "-1"
        self.consolidatedID = ""
        self.IDHistory = []
        self.title = ""
        self.text = ""
        self.comments = ""
        self.child_links = {}
        self.child_types = {}
        self.parent_links= {}
        self.parent_types = {}
        self.related_files = {}
        self.XML = None
        self.type = None
        self.tags = {}
        self.tags['suspect'] = []
        self.tags['minCard'] = []
        self.tags['maxCard'] = []
        self.tags['orphan'] = ["Orphan"]
        self.tags['window'] = ["Window"]

    def getComments(self):
        return self.comments

    def setComments(self, comments):
        self.comments = unicode(comments)

    def getConsolidatedID(self):
        return self.consolidatedID
    
    def clearIDHistory(self):
        self.IDHistory = []

    def setConsolidatedID(self, consolidatedID):
        if (self.consolidatedID != ""):
            self.IDHistory.append(self.consolidatedID)
        self.consolidatedID = unicode(consolidatedID)

    def getIDHistory(self):
        length = len(self.IDHistory)
        if length != 0 :
            return self.IDHistory[length - 1] + " -> " + self.consolidatedID
        else :
            return None

    def destroy(self):
        for link in self.child_links.values() :
            link.remove()
        for link in self.parent_links.values() :
            link.remove() 

    def loadXML(self,  clauseXML):
        self.child_links = {}
        self.parent_links= {}
        self.related_files = {}
        self.XML = clauseXML
        self.id = self.XML .get("id") 
        self.consolidatedID = self.XML.get("consolidated", "")
        self.type = self.XML .get("type")
        suspectsXML = self.XML.find("suspects")
        titleXML = self.XML.find("title")
        textXML = self.XML.find("text")
        commentsXML = self.XML.find("comments")
        linksXML = self.XML.find("links")
        related_filesXML = self.XML.find("related_files")
        historyNode = self.XML.find("consolidation_history")
        if historyNode is not None :
            if historyNode.text is not None :
                self.IDHistory = historyNode.text.split(';')
        if suspectsXML is not None :
            for suspect in suspectsXML.findall('suspect'):
                if suspect.text not in self.tags['suspect']:
                    self.tags['suspect'].append(suspect.text)
        if (titleXML.text is not None) :
            self.title = titleXML.text
        if (textXML.text is not None):
            self.text = textXML.text
        if (commentsXML.text is not None):
            self.comments = commentsXML.text
        for child_link in linksXML.findall("link") :
            document  = child_link.get("document")
            clause = child_link.get("clause")
            newLink = link.Link()
            newLink.addParent(self.getID())
            newLink.addChild(document + ":" + clause)
            self.child_links[newLink.getChildID()] = newLink
        for related_file in related_filesXML.findall("file") :
            self.related_files[related_file.get("filename")] = related_file.text

    def save(self, clausesNode):
        clauseNode = ET.SubElement(clausesNode , 'clause')
        clauseNode.set("id",  self.id)
        clauseNode.set("consolidated",  self.consolidatedID)
        historyNode = ET.SubElement(clauseNode,  "consolidation_history")
        historyNode.text = ';'.join(self.IDHistory)
        clauseNode.set("type",  self.type.getName())
        clauseNode.text = "\n"
        suspectsNode = ET.SubElement(clauseNode,  "suspects")
        for suspect in self.tags['suspect'] :
            suspectNode = ET.SubElement(suspectsNode,  "suspect")
            suspectNode.text = suspect
        titleNode = ET.SubElement(clauseNode,  "title")
        titleNode.text = self.title
        titleNode.tail = "\n"
        textNode = ET.SubElement(clauseNode,  "text")
        textNode.text = self.text
        commentsNode = ET.SubElement(clauseNode,  "comments")
        commentsNode.text = self.comments
        linksNode = ET.SubElement(clauseNode,  "links")
        linksNode.text = "\n"
        for childLink in self.getChildLinksList() :
            linkNode = ET.SubElement(linksNode,  "link")
            documentLink,  clauseLink = childLink.getChildID().split(":")
            linkNode.set("document",  documentLink)
            linkNode.set("clause",  clauseLink)
            linkNode.tail = "\n"
        linksNode.tail = "\n"
        relatedFilesNode = ET.SubElement(clauseNode, "related_files")
        relatedFilesNode.text = "\n"
        for related_file in self.related_files :
            file_node = ET.SubElement(relatedFilesNode, "file")
            file_node.set("filename",  related_file)
            file_node.text = self.related_files[related_file]
            file_node.tail = "\n"
        relatedFilesNode.tail = "\n"
        clauseNode.tail = "\n"

    def evaluateOrphan(self):
        if (len(self.parent_links) == 0):
            if(not self.type.canBeOrphan()):
                return True
        return False

    def evaluateWindow(self):
        if (len(self.child_links) == 0):
            if(not self.type.canBeWindow()):
                return True
        return False

    def evaluateSuspect(self, clause):
        otherType = clause.getType()
        if self.type.isDependentOf(otherType.getName()) :
            if clause.getID() not in self.tags['suspect']:
                self.tags['suspect'].append(clause.getID())
    
    def isDependentOf(self, clause):
        return self.getType().isDependentOf(clause.getType().getName())
    
    def emitChange(self):
        self.tags['suspect'] = []
        for childClauseID in self.getChildClausesList():
            childClause = self.getChildLinkClause(childClauseID)
            childClause.evaluateSuspect(self)
        for parentClauseID in self.getParentClausesList():
            parentClause = self.getParentLinkClause(parentClauseID)
            parentClause.evaluateSuspect(self)

    def isSuspect(self):
        return (len(self.tags['suspect']) > 0)

    def getID(self):
        return unicode((self.getDocument().getName() + ":" + self.id))

    def setID(self, id):
        self.id = unicode(id)
    
    def getTitle(self): 
        return self.title
    
    def setTitle(self, title):
        self.title = unicode(title)

    def getText(self): 
        return self.text
    
    def setText(self, text):
        self.text = unicode(text)
    
    def getDocument(self):
        return self.document

    def setDocument(self, document):
        self.document = document

    def getWarnings(self):
        warnings = []
        self.tags['minCard'] = []
        self.tags['maxCard'] = []
        childCard = self.evaluateChildrenCardinality()
        self.tags['minCard'] += childCard['minCard']
        self.tags['maxCard'] += childCard['maxCard']
        parentCard = self.evaluateParentsCardinality()
        self.tags['minCard'] += parentCard['minCard']
        self.tags['maxCard'] += parentCard['maxCard']
        for key in self.tags.keys() :
            if len(self.tags[key]) > 0:
                reason = ", ".join(self.tags[key])
                if (key == 'minCard'):
                    warnings.append("Card. Baixa(" + reason + ")")
                elif (key == 'maxCard'):
                    warnings.append("Card. Alta(" + reason + ")")
                elif (key == "suspect"):
                    warnings.append("Suspeita(" + reason + ")")
        if (self.evaluateOrphan()):
            warnings.append("Órfã")
        if (self.evaluateWindow()):
            warnings.append("Incompleta")
        return warnings
    
    def evaluateChildrenCardinality(self):
        self.child_types = {}
        warnings = {}
        warnings['minCard'] = []
        warnings['maxCard'] = []
        for childLink in self.child_links.values():
            childClause = childLink.getChild()
            childTypeName = childClause.getType().getName()
            if childTypeName in self.child_types :
                self.child_types[childTypeName] += 1
            else :
                self.child_types[childTypeName] = 1
        for type in self.child_types :
            ret = self.evaluateChildCardinality(type)
            if (ret < 0) :
                warnings['minCard'].append(type)
            elif (ret > 0):
                warnings['maxCard'].append(type)
        return warnings

    def evaluateParentsCardinality(self):
        self.parent_types = {}
        warnings = {}
        warnings['minCard'] = []
        warnings['maxCard'] = []
        for parentLink in self.parent_links.values():
            parentClause = parentLink.getParent()
            parentTypeName = parentClause.getType().getName()
            if parentTypeName in self.parent_types :
                self.parent_types[parentTypeName] += 1
            else :
                self.parent_types[parentTypeName] = 1
        for type in self.parent_types :
            ret = self.evaluateParentCardinality(type)
            if (ret < 0) :
                warnings['minCard'].append(type)
            elif (ret > 0):
                warnings['maxCard'].append(type)
        return warnings

    def evaluateChildCardinality(self, typeName):
        cardinality = self.type.checkChildCardinality(typeName, self.child_types[typeName])
        return cardinality
    
    def evaluateParentCardinality(self, typeName):
        cardinality = self.type.checkParentCardinality(typeName, self.parent_types[typeName])
        return cardinality

    def addChildLink(self, link):
        if (not link in self.child_links.values()) :
            child = link.getChild()
            childID = child.getID()
            self.child_links[childID] = link

    def removeChildLink(self, link_rem):
        if link_rem in self.child_links.values() :
            self.child_links.remove(link_rem.getChildID())
    
    def addParentLink(self, link):
        if (not link in self.parent_links.values()) :
            parent = link.getParent()
            parentID = parent.getID()
            self.parent_links[parentID] = link

    def removeParentLink(self, link_rem):
        if link_rem in self.parent_links.values() :
            parent = link_rem.getParentID()
            del self.parent_links[parent]

    def getRelatedFilesList(self):
        return self.related_files

    def addRelatedFile(self, file, observation):
        self.related_files[file] = observation

    def getRelatedFileObservation(self, file):
        return self.related_files[file]

    def getChildLinksList(self):
        return self.child_links.values()
    
    def getParentLinksList(self):
        return self.parent_links.values()
    
    def getParentLinksDoc2Clause(self):
        documentsList = {}
        for link in self.getParentLinksList() :
            documentsList[link.getParentDocumentID()] = []
        for link in self.getParentLinksList() :
            documentsList[link.getParentDocumentID()].append(link.getParentClauseID())
        return documentsList
    
    def getChildLinksDoc2Clause(self):
        documentsList = {}
        for link in self.getChildLinksList() :
            documentsList[link.getChildDocumentID()] = []
        for link in self.getChildLinksList() :
            documentsList[link.getChildDocumentID()].append(link.getChildClauseID())
        return documentsList

    def getParentLinkClause(self, clause):
        return self.parent_links[clause].getParent()
    
    def getParentClausesList(self):
        return self.parent_links.keys()
    
    def getChildClausesList(self):
        return self.child_links.keys()
        
    def getChildLinkClause(self,  clause):
        return self.child_links[clause].getChild()

    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type

    def getCode(self, docPrefix=False, typePrefix=False):
        code = ""
        if docPrefix :
            code += self.getDocument().getPrefix() + ":"
        if typePrefix :
            code += self.getType().getPrefix()
        code += self.id
        return code
