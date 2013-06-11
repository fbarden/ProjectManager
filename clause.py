import xml.etree.ElementTree as ET
import link

class Clause:
    def __init__(self,  document=None):
        self.document = document
        self.id = "-1"
        self.title = ""
        self.text = ""
        self.child_links = {}
        self.parent_links= {}
        self.related_files = {}
        self.XML = None
        self.type = None
        self.tags = []

    def loadXML(self,  clauseXML):
        self.child_links = {}
        self.parent_links= {}
        self.related_files = {}
        self.XML = clauseXML
        self.id = self.XML .get("id")
        self.type = self.XML .get("type")
        titleXML = self.XML.find("title")
        textXML = self.XML.find("text")
        linksXML = self.XML.find("links")
        related_filesXML = self.XML.find("related_files")
        if (titleXML.text is not None) :
            self.title = titleXML.text
        if (textXML.text is not None):
            self.text = textXML.text
        for child_link in linksXML.findall("link") :
            document  = child_link.get("document")
            clause = child_link.get("clause")
            newLink = link.Link()
            newLink.addParent(self.document.getName(),  self.id)
            newLink.addChild(document,  clause)
            self.child_links[newLink.getChildID()] = newLink
        for related_file in related_filesXML.findall("file") :
            self.related_files[related_file.get("filename")] = related_file.text

    def save(self, clausesNode):
        clauseNode = ET.SubElement(clausesNode , 'clause')
        clauseNode.set("id",  self.id)
        clauseNode.set("type",  self.type)
        clauseNode.text = "\n"
        titleNode = ET.SubElement(clauseNode,  "title")
        titleNode.text = self.title
        titleNode.tail = "\n"
        textNode = ET.SubElement(clauseNode,  "text")
        textNode.text = self.text
        linksNode = ET.SubElement(clauseNode,  "links")
        linksNode.text = "\n"
        for childLink in self.getChildLinksList() :
            linkNode = ET.SubElement(linksNode,  "link")
            documentLink,  clauseLink = childLink.getChild().split(":")
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
    
    def getID(self):
        return self.id
    
    def setID(self,  id):
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
            documentsList[link.getParentDocumentID()] += link.getParentClauseID()
        return documentsList
    
    def getChildLinksDoc2Clause(self):
        documentsList = {}
        for link in self.getChildLinksList() :
            documentsList[link.getChildDocumentID()] = []
        for link in self.getChildLinksList() :
            documentsList[link.getChildDocumentID()] += link.getChildClauseID()
        return documentsList

    def getParentLinkClause(self,  document,  clause):
        ID = document + ":" + clause
        return self.parent_links[ID].getParent()
        
    def getChildLinkClause(self,  document,  clause):
        ID = document + ":" + clause
        return self.child_links[ID].getChild()

    def getType(self):
        return self.type
    
    def setType(self,  type):
        self.type = type
