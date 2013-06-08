import os

class Type():
    def __init__(self):
        self.name = ""
        self.possibles = []
    
    def getName(self):
        return self.name

    def setName(self,  name):
        self.name = name
    
    def addPossibleChid(self,  typeName):
        self.possibles += typeName
    
    def removePossibleChild(self,  typeName):
        self.possibles.temove(typeName)
    
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
    
    def loadXML(self,  XML):
        for typeXML in XML.findall("type") :
            type = Type()
            type.loadXML(typeXML)
            self.addType(type)
    
    def addType(self,  type):
        self.types[type.getName()] = type
    
    def removeType(self,  typeName):
        del self.types[typeName]
    
    def getTypesList(self):
        return self.types.keys()

    def getType(self,  typeName):
        return self.type[typeName]

    
