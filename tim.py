#!/usr/bin/python
# -*- coding: utf-8 -*-
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
        self.name = unicode(name)
    
    def checkChildCardinality(self, typeName, value):
        minCard = self.getChildMinCard(typeName)
        maxCard = self.getChildMaxCard(typeName)
        if (minCard != '*'):
            if (value < int(minCard)):
                return -1
        if (maxCard != '*') :
            if (value > int(maxCard)):
                return 1
        return 0

    def checkParentCardinality(self, typeName, value):
        minCard = self.getParentMinCard(typeName)
        maxCard = self.getParentMaxCard(typeName)
        if (minCard != '*') :
            if (value < int(minCard)):
                return -1
        if (maxCard != '*'):
            if (value > int(maxCard)):
                return 1
        return 0

    def canBeOrphan(self):
        ret = True
        for type in self.possibleParents:
            if self.getParentMinCard(type) > 0:
                ret = False
        return ret

    def canBeWindow(self):
        ret = True
        for type in self.possibleChildren:
            if self.getChildMinCard(type) > 0:
                ret = False
        return ret

    def addPossibleChild(self, typeName, minCard, maxCard, dependency):
        if typeName not in self.possibleChildren.keys() :
            self.possibleChildren[typeName] = (unicode(minCard), unicode(maxCard), dependency)

    def getChildMinCard(self, childName):
        return self.possibleChildren[childName][0]

    def getChildMaxCard(self, childName):    
        return self.possibleChildren[childName][1]

    def getParentMinCard(self, parentName):
        return self.possibleParents[parentName][0]

    def getParentMaxCard(self, parentName):
        return self.possibleParents[parentName][1]
    
    def removePossibleChild(self, typeName):
        return self.possibleChildren.pop(typeName)
    
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
            self.possibleParents[typeName] = (unicode(minCard), unicode(maxCard), dependency)
    
    def removePossibleParent(self, typeName):
        return self.possibleParents.pop(typeName)
    
    def getPossibleParentsList(self):
        return self.possibleParents.keys()

    def loadXML(self,  XML):
        self.name = XML.get('name')
        descriptionNode = XML.find("description")
        self.description = descriptionNode.text
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
        descriptionNode = ET.SubElement(typeNode , 'description')
        descriptionNode.text = self.getDescription()
        typeNode.set('name', self.getName())
        typeNode.set('prefix', self.getPrefix())
        if root :
            typeNode.set('root', 'yes')
        for child in self.getPossibleChildrenList() :
            childNode = ET.SubElement(typeNode , 'child')
            childNode.set('name', child)
            childNode.set('minCard', self.possibleChildren[child][0])
            childNode.set('maxCard', self.possibleChildren[child][1])
            if (self.possibleChildren[child][2]):
                childNode.set('dependent', 'yes')
            else:
                childNode.set('dependent', 'no')
        for parent in self.getPossibleParentsList() :
            parentNode = ET.SubElement(typeNode , 'parent')
            parentNode.set('name', parent)
            parentNode.set('minCard', self.possibleParents[parent][0])
            parentNode.set('maxCard', self.possibleParents[parent][1])
            if (self.possibleParents[parent][2]):
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
    
    def renameType(self, typeName, newName):
        typeName = unicode(typeName)
        newName = unicode(newName)
        type = self.getType(typeName)
        parentsList = type.getPossibleParentsList()
        for parentName in parentsList :
            parentType = self.getType(parentName)
            childInfo = parentType.removePossibleChild(typeName)
            parentType.addPossibleChild(newName, *childInfo)
        childrenList = type.getPossibleChildrenList()
        for childName in childrenList :
            childType = self.getType(childName)
            parentInfo = childType.removePossibleParent(typeName)
            childType.addPossibleParent(newName, *parentInfo)
        if typeName in self.roots :
            self.roots.remove(typeName)
            self.roots.append(newName)
        if typeName in self.types :
            self.removeType(typeName)
            type.setName(newName)
            self.addType(type)
