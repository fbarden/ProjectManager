import xml.etree.ElementTree as ET
from clause import Clause
import os

class Document :
    def __init__(self):
        self.project = None
        self.title = ""
        self.clauses = {}
        self.clausesOrder = []
        self.name = ""
        self.prefix = ""

    def moveClause(self, clause, step):
        index = self.clausesOrder.index(clause)
        newIndex = index+step
        print "movendo clausula "
        print "ANTES"
        print self.clausesOrder
        if ((newIndex >= 0) and (newIndex<len(self.clausesOrder))) :
            self.clausesOrder.insert(newIndex, self.clausesOrder.pop(index))
        print "DEPOIS"
        print self.clausesOrder
        
    def loadXML(self, project, filename):
        self.project = project
        self.clauses = {}
        self.name = filename[0:len(filename)-4]
        tree = ET.parse(self.project.getLocation() + filename)
        XML = tree.getroot()
        self.title = XML.get("title")
        self.prefix = XML.get("prefix")
        clauses_node = XML.find("clauses")
        self.loadClauses(clauses_node)

    def save(self):
        documentNode = ET.Element('document')
        documentNode.set('title',  self.title)
        documentNode.set('name',  self.name)
        documentNode.set('prefix',  self.prefix)
        clausesNode = ET.SubElement(documentNode, 'clauses')
        self.saveClauses(clausesNode)
        documentNode.tail = "\n"
        tree = ET.ElementTree(element=documentNode)
        tree.write(self.project.getLocation()+ self.getName() + ".xml")

    def loadClauses(self, clausesNode):
        for item in clausesNode.findall("clause") :
            clause = Clause(self)
            id = item.get("id")
            clause.loadXML(item)
            self.clauses[id] = clause
        order = clausesNode.find('order').text
        clausesOrder = []
        if (order is not None) :
            clausesOrder = order.split(';')
        for clauseID in clausesOrder :
            self.clausesOrder.append(self.getName() + ":" + clauseID)

    def saveClauses(self, clausesNode):
        print self.clausesOrder
        for clause in self.getClausesList():
            self.getClause(clause).save(clausesNode)
        orderNode = ET.SubElement(clausesNode, 'order')
        orderText = ""
        for id in self.clausesOrder:
            orderText+= id.split(':', 1)[1] + ";"
        orderNode.text = orderText.strip(";")
        print orderText

    def getClausesList(self):
        return self.clausesOrder

    def getClause(self, id):
        return self.clauses[id.split(':')[1]]
    
    def addClause(self, clause):
        list = self.clauses.keys()
        if (list == []) :
            newID = '1'
        else :
            newID = unicode(int(max(list))+1)
        clause.setID(newID)
        clause.setDocument(self)
        self.clausesOrder.append(clause.getID())
        self.clauses[newID] = clause

    def destroy(self):
        for clauseID in self.clauses:
            clause = self.clauses[clauseID]
            clause.destroy()
        os.remove(self.project.getLocation() + self.name + ".xml")
    
    def removeClause(self, clauseID):
        id = clauseID.split(":")[1]
        clause = self.clauses[id]
        clause.destroy()
        self.clausesOrder.remove(clauseID)
        del self.clauses[id]

    def getProject(self):
        return self.project
    
    def setProject(self, project):
        self.project = project

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = unicode(name)

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = unicode(title)

    def getPrefix(self):
        return self.prefix

    def setPrefix(self, prefix):
        self.prefix = unicode(prefix)

    def setOrder(self, list):
        self.clausesOrder = list