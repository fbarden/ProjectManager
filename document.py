import xml.etree.ElementTree as ET
from clause import Clause
import os

class Document :
    def __init__(self):
        self.project = ""
        self.title = ""
        self.clauses = {}
        self.name = ""
        self.XML = None

    def open(self, filename):
        self.clauses = {}
        self.name = filename[0:len(filename)-4]
        tree = ET.parse("./" + filename)
        self.XML = tree.getroot()
        self.title = self.XML.get("title")
        clauses_node = self.XML.find("clauses")
        for item in clauses_node.findall("clause") :
            clause = Clause(self)
            id = item.get("id")
            clause.open(item)
            self.clauses[id] = clause

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
        self.clauses[clause.getID] = clause
    
    def removeClause(self, clause):
        del self.clauses[clause.getID()]
        clause.remove()
    
    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle
