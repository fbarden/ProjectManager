import xml.etree.ElementTree as ET
import os
from link import Link
from tim import TIM, Type
from document import Document

class Project :
    def __init__(self):
        self.name = ""
        self.documents = {}
        self.location = ""
        self.imported_files = {}
        self.TIM = None
    
    def loadXML(self,  filename):
        self.location = os.path.dirname(filename) + '/'
        tree = ET.parse(filename)
        XML = tree.getroot()
        self.name = XML.get("name")
        self.documents = {}
        self.loadDocuments(XML)
        importedFilesNode = XML.find('imported_files')
        self.loadImportedFiles(importedFilesNode)
        TIMNode= XML.find('tim')
        self.loadTIM(TIMNode)
        linksList = self.getAllLinks()
        for link in linksList :
            link.consolidateChild(self)
            link.consolidateParent(self)
    
    def loadDocuments(self, documentsNode):
        for document_node in documentsNode.findall("document") :
            document = Document()
            document_name = document_node.get("name")
            document.loadXML(self, document_name +".xml")
            self.documents[document_name] = document

    def loadImportedFiles(self, importedFilesNode):
        for fileNode in importedFilesNode.findall('file'):
            self.imported_files[fileNode.get('name')] = fileNode.text

    def loadTIM(self, TIMNode):
        self.TIM = TIM()
        self.TIM.loadXML(TIMNode)
#        for typeNode in TIMNode.findall('type'):
#            type = Type()
#            type.setName(typeNode.get('name'))
#            for childNode in typeNode.findall('child'):
#                type.addPossibleChild(childNode.get('name'))
#            self.TIM.addType(type)
#            if (typeNode.get('root', 'no') == 'yes'):
#                self.TIM.addRoot(type.getName())

    def saveDocuments(self, documentsNode):
        for documentName in self.getDocumentsList():
            documentNode = ET.SubElement(documentsNode, 'document')
            documentNode.set('name', documentName)

    def saveImportedFiles(self, importedFilesNode):
        for file in self.imported_files.keys() :
            fileNode= ET.SubElement(importedFilesNode , 'file')
            fileNode.set('name', file)
            fileNode.text = self.imported_files[file]

    def save(self):
        projectNode = ET.Element('project')
        projectNode.set('name',  self.name)
        self.saveDocuments(projectNode)
        importedFilesNode = ET.SubElement(projectNode, 'imported_files')
        self.saveImportedFiles(importedFilesNode)
        TIMNode= ET.SubElement(projectNode, 'tim')
        self.TIM.save(TIMNode)
        projectNode.tail = "\n"
        tree = ET.ElementTree(element=projectNode)
        tree.write(self.getLocation()+ self.getName() + ".prj")
        
    def saveAll(self):
        self.save()
        for document_name in self.documents :
            self.documents[document_name].save()

    def getDocument(self, name):
        return self.documents[name]
    
    def getDocumentsList(self):
        return sorted(set(self.documents))
    
    def addDocument(self,  document):
        self.documents[document.getName] = document
        document.setProject(self)

    def removeDocument(self,  document):
        del self.documents[document.getName]
    
    def getName(self):
        return self.name

    def setName(self,  name):
        self.name = name

    def getLocation(self):
        return self.location

    def setLocation(self,  location):
        self.location = location
    
    def addDocument(self, document):
        self.documents[document.getName()] = document

    def getAllLinks(self):
        linksList = []
        for documentName in self.getDocumentsList() :
            documentObj = self.getDocument(documentName)
            for clauseName in documentObj.getClausesList() :
                clauseObj = documentObj.getClause(clauseName)
                linksList += clauseObj.getChildLinksList()
        return linksList

    def getAllDocument2Clauses(self):
        list = {}
        for documentName in self.getDocumentsList() :
            documentObj = self.getDocument(documentName)
            list[documentName] = documentObj.getClausesList()
        return list

    def setTIM(self, TIM):
        self.TIM = TIM
    
    def getTIM(self):
        return self.TIM

    def getImportedFilesList(self):
        return sorted(set(self.imported_files.keys()))

    def addImportedFile(self, file, description):
        self.imported_files[file] = description

    def getImportedFileDescription(self, file):
        print [file]
        if file in self.imported_files:
            return self.imported_files[file]
        else:
            return ""

    def setImportedFileDescription(self, file, description):
        self.imported_files[str(file)] = description
