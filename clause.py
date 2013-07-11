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
        self.parent_links= {}
        self.related_files = {}
        self.XML = None
        self.type = None
        self.suspects = []
        self.tags = []

    def getComments(self):
        return self.comments

    def setComments(self, comments):
        self.comments = comments

    def getConsolidatedID(self):
        return self.consolidatedID

    def setConsolidatedID(self, consolidatedID):
        if (self.consolidatedID is None):
            self.IDHistory += self.consolidatedID + "->" + consolidatedID
        self.consolidatedID = consolidatedID
            

    def destroy(self):
        for link in self.parent_links:
            self.removeParentLink(link)
        for child in self.child_links:
            self.removeChildLink(link)

    def removeParentLink(self, link):
        del self.parent_links[link]

    def removeChildLink(self, link):
        del self.child_links[link]

    def loadXML(self,  clauseXML):
        self.child_links = {}
        self.parent_links= {}
        self.related_files = {}
        self.XML = clauseXML
        self.id = self.XML .get("id")
        #self.consolidatedID = self.XML.get("consolidated")
        self.type = self.XML .get("type")
        suspectsXML = self.XML.find("suspects")
        titleXML = self.XML.find("title")
        textXML = self.XML.find("text")
        commentsXML = self.XML.find("comments")
        linksXML = self.XML.find("links")
        related_filesXML = self.XML.find("related_files")
        if suspectsXML is not None :
            for suspect in suspectsXML.findall('suspect'):
                if suspect.text not in self.suspects:
                    self.suspects.append(suspect)
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
        #clauseNode.set("consolidated",  self.consolidatedID)
        clauseNode.set("type",  self.type.getName())
        clauseNode.text = "\n"
        suspectsNode = ET.SubElement(clauseNode,  "supects")
        for suspect in self.suspects :
            suspectNode = ET.SubElement(suspectsNode,  "supect")
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

    def remove(self):
        document_tree = ET.parse(self.document + ".xml")
        document_node = document_tree.getroot()
        clauses_node = document_node.find("clauses")
        for clause in clauses_node :
            if (clause.get('id') == self.id) :
                clauses_node.remove(clause)
        for link in self.child_links :
            link.remove()

    def evaluateSuspect(self, clause):
        otherType = clause.getType()
        if self.type.isDependentOf(otherType.getName()) :
            if clause.getID() not in self.suspects:
                self.suspects.append(clause.getID())
    
    def isDependentOf(self, clause):
        return self.getType().isDependentOf(clause.getType().getName())
    
    def emitChange(self):
        for childClauseID in self.getChildClausesList():
            childClause = self.getChildLinkClause(childClauseID)
            childClause.evaluateSuspect(self)
        for parentClauseID in self.getParentClausesList():
            parentClause = self.getParentLinkClause(parentClauseID)
            parentClause.evaluateSuspect(self)

    def isSuspect(self):
        return (len(self.suspects) > 0)

    def getID(self):
        return self.getDocument().getName() + ":" + self.id

    def setID(self, id):
        self.id = id
    
    def getTitle(self): 
        return self.title
    
    def setTitle(self, title):
        self.title = title

    def getText(self): 
        return self.text
    
    def setText(self, text):
        self.text = text
    
    def getDocument(self):
        return self.document

    def setDocument(self, document):
        self.document = document

    def addChildLink(self, link):
        if (not link in self.child_links.values()) :
            self.child_links[link.getChildID()] = link
    
    def removeChildLink(self, link_rem):
        if link in self.child_links.values() :
            self.child_links.remove(link.getChildID())
    
    def addParentLink(self, link):
        if (not link in self.parent_links.values()) :
            self.parent_links[link.getParentID()] = link

    def removeParentLink(self, link_rem):
        if link in self.parent_links.values() :
            del self.parent_links[link.getParentID()]

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
            