import xml.etree.ElementTree as ET
from clause import Clause
import os

class Document :
    def __init__(self):
        self.project = None
        self.title = ""
        self.clauses = {}
        self.name = ""
        self.initials = ""

    def loadXML(self, project, filename):
        self.project = project
        self.clauses = {}
        self.name = filename[0:len(filename)-4]
        tree = ET.parse(self.project.getLocation() + filename)
        XML = tree.getroot()
        self.title = XML.get("title")
        self.initials = XML.get("initials")
        clauses_node = XML.find("clauses")
        self.loadClauses(clauses_node)

    def save(self):
        documentNode = ET.Element('document')
        documentNode.set('title',  self.title)
        documentNode.set('name',  self.name)
        documentNode.set('initials',  self.initials)
        clausesNode = ET.SubElement(documentNode, 'clauses')
        self.saveClauses(clausesNode)
        documentNode.tail = "\n"
        tree = ET.ElementTree(element=documentNode)
        tree.write(self.project.getLocation()+ self.getName() + ".xml")

    def loadClauses(self, clauses_node):
        for item in clauses_node.findall("clause") :
            clause = Clause(self)
            id = item.get("id")
            clause.loadXML(item)
            self.clauses[id] = clause

    def saveClauses(self, clausesNode):
        for clause in self.getClausesList():
            self.getClause(clause).save(clausesNode)

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
        return sorted(set(self.clauses))

    def getClause(self,  id):
        return self.clauses[id]
    
    def addClause(self,  clause):
        list = self.getClausesList()
        if (list == []) :
            newID = '1'
        else :
            newID = str(int(max(list))+1)
        clause.setID(newID)
        clause.setDocument(self)
        self.clauses[clause.getID()] = clause
    
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

    def setTitle(self, newTitle):
        self.title = newTitle

    def getInitials(self):
        return self.initials

    def setInitials(self, initials):
        self.initials = initials
