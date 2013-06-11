import xml.etree.ElementTree as ET
import os

class Type():
    def __init__(self):
        self.name = ""
        self.possibles = []
    
    def getName(self):
        return self.name

    def setName(self,  name):
        self.name = name
    
    def addPossibleChild(self,  typeName):
        if typeName not in self.possibles :
            self.possibles += [typeName]
    
    def removePossibleChild(self,  typeName):
        self.possibles.remove(typeName)
    
    def getPossibleChildrenList(self):
        return self.possibles

    def loadXML(self,  XML):
        self.name = XML.get('name')
        print "Carregando Type: " + self.name
        for child in XML.findall("child"):
            print "         - " + child.text
            self.addPossibleChild(child.text)

    def save(self, typesNode, root):
        typeNode = ET.SubElement(typesNode , 'type')
        typeNode.set('name', self.getName())
        if root :
            typeNode.set('root', 'yes')
        for child in self.getPossibleChildrenList() :
            childNode = ET.SubElement(typeNode , 'child')
            childNode.text = child

class TIM():
    def __init__(self):
        self.types = {}
        self.roots = []
    
    def loadXML(self,  XML):
        print "Carregando TIM"
        for typeXML in XML.findall("type") :
            type = Type()
            type.loadXML(typeXML)
            if typeXML.get('root', 'no') == 'yes':
                self.addRoot(type.getName())
            self.addType(type)

    def save(self, TIMNode):
        for typeName in self.getTypesList() :
            root = False
            type = self.getType(typeName)
            if typeName in self.getRootsList():
                root = True
            type.save(TIMNode, root)
    
    def addType(self,  type):
        self.types[type.getName()] = type
    
    def removeType(self,  typeName):
        del self.types[typeName]
    
    def getTypesList(self):
        return sorted(set(self.types.keys()))

    def clearTypesList(self):
        for type in self.getTypesList() :
            self.removeType(type)

    def getType(self,  typeName):
        return self.types[typeName]

    def addRoot(self, typeName):
        if (typeName not in self.roots) :
            self.roots += [typeName]

    def getRootsList(self):
        return self.roots

    def getPossibleParentsList(self, type):
        parentsList = []
        print "*** getPossibleParentsList ***" + type.getName()
        for candidateType in self.getTypesList() :
            print "+ Candidato: " + candidateType
            print "Possible Children"
            print self.getType(candidateType).getPossibleChildrenList()
            if type.getName() in self.getType(candidateType).getPossibleChildrenList():
                parentsList += [candidateType]
        print "ParentList:"
        print parentsList
        return parentsList
