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
        for clause in self.getClausesList():
            self.getClause(clause).save(clausesNode)
        orderNode = ET.SubElement(clausesNode, 'order')
        orderText = ""
        for id in self.clauses:
            orderText+= id + ";"
        orderNode.text = orderText.strip(";")

    def saveClause(self,  id):
        document_tree= ET.parse(self.project + "/" + self.name + ".xml")
        document_node = document_tree.getroot()
        clauses_node= document_node.find("clauses")
        for clause in clauses_node :
            if (clause.get('id') == str(id)) :
                clauses_node.remove(clause)
        clause_node = self.getUpdatedNode()
        document_node.append(clause_node)
        document_tree.write(self.name + ".xml")
    
    def getClausesList(self):
        return self.clausesOrder

    def getClause(self, id):
        print "BAH " + str(id)
        return self.clauses[id.split(':')[1]]
    
    def addClause(self,  clause):
        list = self.clauses
        if (list == []) :
            newID = '1'
        else :
            newID = str(int(max(list))+1)
        clause.setID(newID)
        clause.setDocument(self)
        self.clausesOrder.append(clause.getID())
        self.clauses[newID] = clause

    def destroy(self):
        for clauseID in self.clauses:
            clause = self.clauses.pop(clauseID)
            clause.destroy()
        os.remove(self.project.getLocation() + self.name + ".xml")
    
    def removeClause(self, clause):
        del self.clauses[clause.getID()]
        clause.remove()

    def getProject(self):
        return self.project
    
    def setProject(self, project):
        self.project = project

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getPrefix(self):
        return self.prefix

    def setPrefix(self, prefix):
        self.prefix = prefix
