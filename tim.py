import xml.etree.ElementTree as ET
import os

class Type():
    def __init__(self):
        self.name = ""
        self.prefix = ""
        self.description = ""
        self.acceptsRecursion = False
        self.possibleChildren = {}
        self.possibleParents = {}

    def getPrefix(self):
        return self.prefix

    def getDescription(self):
        return self.description

    def setPrefix(self, value):
        self.prefix = unicode(value)

    def setDescription(self, value):
        self.description = unicode(value)
    
    def getName(self):
        return self.name

    def setName(self,  name):
        print "Setando nome " + name
        self.name = unicode(name)
    
    def addPossibleChild(self, typeName, minCard, maxCard, dependency):
        if typeName not in self.possibleChildren.keys() :
            self.possibleChildren[typeName] = (minCard, maxCard, dependency)

    def getChildMinCard(self, childName):
        return self.possibleChildren[childName][0]

    def getChildMaxCard(self, childName):    
        return self.possibleChildren[childName][1]

    def getParentMinCard(self, parentName):
        return self.possibleParents[parentName][0]

    def getParentMaxCard(self, parentName):
        return self.possibleParents[parentName][1]
    
    def removePossibleChild(self, typeName):
        del self.possibleChildren[typeName]
    
    def getPossibleChildrenList(self):
        return self.possibleChildren.keys()
    
    def isDependentOf(self, typeName):
        if typeName in self.getPossibleChildrenList():
            return self.possibleChildren[typeName][2]
        elif typeName in self.getPossibleParentsList():
            return self.possibleParents[typeName][2]
        else:
            return False

    def addPossibleParent(self, typeName, minCard, maxCard, dependency):
        if typeName not in self.possibleParents.keys() :
            self.possibleParents[typeName] = (minCard, maxCard, dependency)
    
    def removePossibleParent(self, typeName):
        del self.possibleParents[typeName]
    
    def getPossibleParentsList(self):
        return self.possibleParents.keys()

    def loadXML(self,  XML):
        self.name = XML.get('name')
        self.prefix = XML.get('prefix')
        for child in XML.findall("child"):
            name = child.get('name')
            minCard = child.get('minCard')
            maxCard = child.get('maxCard')
            dependency = (child.get('dependent') == 'yes')
            self.addPossibleChild(name, minCard, maxCard, dependency)
        for parent in XML.findall("parent"):
            name = parent.get('name')
            minCard = parent.get('minCard')
            maxCard = parent.get('maxCard')
            dependency = (parent.get('dependent') == 'yes')
            self.addPossibleParent(name, minCard, maxCard, dependency)

    def save(self, typesNode, root):
        typeNode = ET.SubElement(typesNode , 'type')
        typeNode.set('name', self.getName())
        typeNode.set('prefix', self.getPrefix())
        if root :
            typeNode.set('root', 'yes')
        for child in self.getPossibleChildrenList() :
            childNode = ET.SubElement(typeNode , 'child')
            childNode.set('name', child)
            childNode.set('minCard', self.possibleChildren[child][0])
            childNode.set('maxCard', self.possibleChildren[child][1])
            if (self.possibleChildren[child][1]):
                childNode.set('dependent', 'yes')
            else:
                childNode.set('dependent', 'no')
        for parent in self.getPossibleParentsList() :
            parentNode = ET.SubElement(typeNode , 'parent')
            parentNode.set('name', parent)
            parentNode.set('minCard', self.possibleParents[parent][0])
            parentNode.set('maxCard', self.possibleParents[parent][1])
            if (self.possibleParents[parent][1]):
                parentNode.set('dependent', 'yes')
            else:
                parentNode.set('dependent', 'no')

class TIM():
    def __init__(self):
        self.types = {}
        self.roots = []
    
    def loadXML(self,  XML):
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

    def getType(self, typeName):
        return self.types[unicode(typeName)]

    def addRoot(self, typeName):
        if (typeName not in self.roots) :
            self.roots += [typeName]

    def getRootsList(self):
        return self.roots

    def getPossibleParentsList(self, type):
        parentsList = []
        for candidateType in self.getTypesList() :
            if type.getName() in self.getType(candidateType).getPossibleChildrenList():
                parentsList += [candidateType]
        return parentsList
