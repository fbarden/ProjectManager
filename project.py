#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import xml.etree.ElementTree as ET
import os
from link import Link
from tim import TIM, Type
from document import Document

class Project :
    def __init__(self):
        self.name = ""
        self.documents = {}
        self.documentsOrder = []
        self.location = ""
        self.imported_files = {}
        self.consolidationSettings = {}
        self.TIM = None

    def getConsolidationSettings(self):
        return self.consolidationSettings

    def setConsolidationSettings(self, settings):
        self.consolidationSettings = settings
    
    def getType2Clauses(self):
        type2Clauses = {}
        for type in self.TIM.getTypesList():
            type2Clauses[type] = []
        clausesList = self.getAllClauses().values()
        for clause in clausesList :
            typeName = clause.getType().getName()
            type2Clauses[typeName].append(clause)
        return type2Clauses
    
    def loadXML(self,  filename):
        self.location = os.path.dirname(filename) + '/'
        tree = ET.parse(filename)
        XML = tree.getroot()
        self.name = XML.get("name")
        TIMNode= XML.find('tim')
        self.loadTIM(TIMNode)
        self.documents = {}
        self.loadDocuments(XML)
        importedFilesNode = XML.find('imported_files')
        self.loadImportedFiles(importedFilesNode)
        consolidationNode = XML.find('consolidation')
        if consolidationNode is not None :
            self.loadConsolidation(consolidationNode)
        linksList = self.getAllLinks()
        for link in linksList :
            link.consolidateLink(self)
    
    def loadDocuments(self, documentsNode):
        for document_node in documentsNode.findall("document") :
            document = Document()
            document_name = document_node.get("name")
            document.loadXML(self, document_name +".xml")
            self.documents[document_name] = document
            for clauseId in document.getClausesList():
                clause = document.getClause(clauseId)
                clauseType = clause.getType()
                clause.setType(self.TIM.getType(clauseType))
        order = documentsNode.find("order").text
        if order is not None :
            self.documentsOrder = order.split(";")
        else :
            self.documentsOrder = []

    def loadImportedFiles(self, importedFilesNode):
        for fileNode in importedFilesNode.findall('file'):
            self.imported_files[fileNode.get('name')] = fileNode.text

    def loadConsolidation(self, consolidationNode):
        if consolidationNode.get('docPrefix') == 'yes' :
            self.consolidationSettings['docPrefix'] = True
        else :
            self.consolidationSettings['docPrefix'] = False
        if consolidationNode.get('typePrefix') == 'yes' :
            self.consolidationSettings['typePrefix'] = True
        else :
            self.consolidationSettings['typePrefix'] = False
        if consolidationNode.get('unifyDocuments', 'no') == 'yes' :
            self.consolidationSettings['unifyDocuments'] = True
        else :
            self.consolidationSettings['unifyDocuments'] = False
        self.consolidationSettings['order'] = consolidationNode.get('order')
        documents = consolidationNode.find('documents')
        self.consolidationSettings['documents'] = documents.text.split(';')
        documents = consolidationNode.find('types')
        self.consolidationSettings['types'] = documents.text.split(';')
        limitsNode = consolidationNode.find('limits')
        if (limitsNode is not None) :
            limits = {}
            prefixNodes = limitsNode.findall('prefix')
            for prefixNode in prefixNodes :
                limits[prefixNode.get('prefix')] = int(prefixNode.get('limit'))
            self.consolidationSettings['limits'] = limits

    def loadTIM(self, TIMNode):
        self.TIM = TIM()
        self.TIM.loadXML(TIMNode)

    def moveDocument(self, document, step):
        index = self.documentsOrder.index(document)
        newIndex = index+step 
        if ((newIndex >= 0) and (newIndex<len(self.documentsOrder))) :
            self.documentsOrder.insert(newIndex, self.documentsOrder.pop(index))

    def saveDocuments(self, documentsNode):
        for documentName in self.getDocumentsList():
            documentNode = ET.SubElement(documentsNode, 'document')
            documentNode.set('name', documentName)
        orderNode = ET.SubElement(documentsNode, 'order')
        orderText = ""
        for document in self.documentsOrder :
            orderText += document + ";"
        orderNode.text = orderText.strip(";")

    def saveImportedFiles(self, importedFilesNode):
        for file in self.imported_files.keys() :
            fileNode= ET.SubElement(importedFilesNode , 'file')
            fileNode.set('name', file)
            fileNode.text = self.imported_files[file]
    
    def saveConsolidation(self, consolidationsNode):
        docPrefix = ""
        if (self.consolidationSettings['docPrefix']):
            docPrefix = 'yes'
        else :
            docPrefix = 'no'
        typePrefix = ""
        if (self.consolidationSettings['typePrefix']):
            typePrefix = 'yes'
        else:
            typePrefix = 'no'
        if (self.consolidationSettings['unifyDocuments']):
            unifyDocuments = 'yes'
        else:
            unifyDocuments = 'no'
        consolidationsNode.set('order', self.consolidationSettings['order'])
        consolidationsNode.set('docPrefix', docPrefix)
        consolidationsNode.set('typePrefix', typePrefix)
        consolidationsNode.set('unifyDocuments', unifyDocuments)
        documentsNode = ET.SubElement(consolidationsNode, 'documents')
        documentsNode.text = ';'.join(self.consolidationSettings['documents'])
        typesNode = ET.SubElement(consolidationsNode, 'types')
        typesNode.text = ';'.join(self.consolidationSettings['types'])
        limitsNode = ET.SubElement(consolidationsNode, 'limits')
        if 'limits' in self.consolidationSettings.keys() :
            limits = self.consolidationSettings['limits']
            for limit in limits :
                limitNode = ET.SubElement(limitsNode, 'prefix')
                limitNode.set('prefix', limit)
                limitNode.set('limit', str(limits[limit]))

    def save(self):
        projectNode = ET.Element('project')
        projectNode.set('name',  self.name)
        self.saveDocuments(projectNode)
        importedFilesNode = ET.SubElement(projectNode, 'imported_files')
        self.saveImportedFiles(importedFilesNode)
        if (self.consolidationSettings != {}) :
            consolidationsNode = ET.SubElement(projectNode, 'consolidation')
            self.saveConsolidation(consolidationsNode)
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
    
    def getAllClauses(self):
        list = {}
        for documentName in self.getDocumentsList() :
            documentObj = self.getDocument(documentName)
            for clause in documentObj.getClausesList():
                list[clause] = documentObj.getClause(clause)
        return list
    
    def getDocumentsList(self):
        return self.documentsOrder

    def removeDocument(self, documentName):
        document = self.documents[documentName]
        document.destroy()
        del self.documents[documentName]
        self.documentsOrder.remove(documentName)
    
    def getName(self):
        return self.name

    def setName(self,  name):
        self.name = name

    def getLocation(self):
        return self.location

    def setLocation(self,  location):
        os.mkdir(location + 'imported')
        self.location = location
    
    def addDocument(self, document):
        self.documents[document.getName()] = document
        self.documentsOrder.append(document.getName())

    def getAllLinks(self):
        linksList = []
        for documentName in self.getDocumentsList() :
            documentObj = self.getDocument(documentName)
            for clauseName in documentObj.getClausesList() :
                clauseObj = documentObj.getClause(clauseName)
                linksList += clauseObj.getChildLinksList()
        return linksList

    def getDocument2ClausesDict(self):
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
        if file in self.imported_files:
            return self.imported_files[file]
        else:
            return ""

    def setImportedFileDescription(self, file, description):
        self.imported_files[unicode(file)] = description
