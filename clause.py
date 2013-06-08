import xml.etree.ElementTree as ET
import link

class Clause:
    def __init__(self,  document):
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

    def open(self,  clauseXML):
        self.child_links = {}
        self.parent_links= {}
        self.related_files = {}
        self.XML = clauseXML
        self.id = self.XML .get("id")
        titleXML = self.XML.find("title")
        textXML = self.XML.find("text")
        linksXML = self.XML.find("links")
        related_filesXML = self.XML.find("related_files")
        self.title = titleXML.text
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
        self.text = self.XML.find("text").text
        print "Terminou o coarregamento da clausula"
        print self.parent_links
        print self.child_links

    def getUpdatedNode(self):
        clause_node = ET.Element("clause")
        clause_node.set("id",  self.id)
        clause_node.text = "\n"
        title_node = ET.SubElement(clause_node,  "title")
        title_node.text = self.text
        title_node.tail = "\n"
        links_node = ET.SubElement(clause_node,  "links")
        links_node.text = "\n"
        for child_link in self.child_links :
            link_node = ET.SubElement(links_node,  "link")
            document_link,  clause_link = child_link.getChild().split(":")
            link_node.set("document",  document_link)
            link_node.set("clause",  clause_link)
            link_node.tail = "\n"
        links_node.tail = "\n"
        related_files_node = ET.SubElement(clause_node, "related_files")
        related_files_node.text = "\n"
        for related_file in self.related_files :
            file_node = ET.SubElement(related_files_node, "file")
            file_node.set("filename",  related_file)
            file_node.text = self.related_files[related_file]
            file_node.tail = "\n"
        related_files_node.tail = "\n"
        clause_node.tail = "\n"
        return document_tree

    def save(self):
        document_tree = ET.parse(self.document + ".xml")
        document_node = document_tree.getroot()
        clauses_node= document_node.find("clauses")
        for clause in clauses_node :
            if (clause.get('id') == self.id) :
                clauses_node.remove(clause)
        clause_node = self.getUpdatedNode()
        document_node.append(clause_node)
        document_tree.write(self.document + ".xml")

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

    def addChildLink(self, link):
        if (not link in self.child_links.values()) :
            self.child_links[link.getChildID()] = link
            print self.document.getName() + ":" + self.id + " adicionando link filho " + link.getChildID()
    
    def removeChildLink(self, link_rem):
        if link in self.child_links.values() :
            self.child_links.remove(link.getChildID())
    
    def addParentLink(self, link):
        if (not link in self.parent_links.values()) :
            self.parent_links[link.getParentID()] = link
            print self.document.getName() + ":" + self.id + " adicionando link pai " + link.getParentID()

    def removeParentLink(self, link_rem):
        if link in self.parent_links.values() :
            del self.parent_links[link.getParentID()]

    def getRelatedFilesList(self):
        return self.related_files

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
