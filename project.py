import xml.etree.ElementTree as ET
import os
from link import Link
from document import Document

class Project :
    def __init__(self):
        self.name = ""
        self.documents = {}
        self.XML = None
    
    def open(self,  filename):
        tree = ET.parse(filename)
        self.XML = tree.getroot()
        self.name = self.XML.get("name")
        self.documents = {}
        for document_node in self.XML.findall("document") :
            document = Document()
            document_name = document_node.get("name")
            document.open(document_name +".xml")
            self.documents[document_name] = document
        linksList = self.getAllLinks()
        for link in linksList :
            link.consolidateChild(self)
        for link in linksList :
            print link.getParentID() + " --> " + link.getChildID()

    def save(self):
        project = ET.Element('project')
        project.set('name',  self.name)
        project.tail = "\n"
        tree = ET.ElementTree(element=project)
        try :
            os.mkdir(name)
        except :
            pass
        tree.write(self.name + "/" + self.name + "Project.xml")
        
    def saveAll(self):
        self.save()
        for document_name in self.documents :
            self.documents[document_name].save()

    def getDocument(self, name):
        return self.documents[name]
    
    def getDocumentsList(self):
        list = []
        for document in self.documents :
            list += [document]
        return list
    
    def addDocument(self,  document):
        self.documents[document.getName] = document
    
    def removeDocument(self,  document):
        del self.documents[document.getName]
    
    def getName(self):
        return self.name

    def setName(self,  name):
        self.name = name

    def getAllLinks(self):
        linksList = []
        for documentName in self.getDocumentsList() :
            documentObj = self.getDocument(documentName)
            for clauseName in documentObj.getClausesList() :
                clauseObj = documentObj.getClause(clauseName)
                linksList += clauseObj.getChildLinksList()
        return linksList
