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
        for child in XML.findall("child"):
            addPossibleChild(child.text())

    def getXML(self):
        pass

class TIM():
    def __init__(self):
        self.types = {}
        self.roots = []
    
    def loadXML(self,  XML):
        for typeXML in XML.findall("type") :
            type = Type()
            type.loadXML(typeXML)
            self.addType(type)
    
    def addType(self,  type):
        self.types[type.getName()] = type
        print "Adicionando tipo " + type.getName()
        print "Lista total: "
        print self.getTypesList()
    
    def removeType(self,  typeName):
        del self.types[typeName]
    
    def getTypesList(self):
        return sorted(set(self.types.keys()))

    def clearTypesList(self):
        for type in self.getTypesList() :
            self.removeType(type)

    def getType(self,  typeName):
        print "Lista"
        print self.types
        print "Tipo Desejado"
        print typeName
        return self.types[typeName]

    def addRoot(self, typeName):
        if (typeName not in self.roots) :
            self.roots += [typeName]

    def getRootsList(self):
        return self.roots
