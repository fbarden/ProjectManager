import xml.etree.ElementTree as ET
from clause import Clause
import os

class Document :
    def __init__(self):
        self.title = ""
        self.clauses = {}
        self.filename = ""
        self.XML = None

    def open(self,  filename):
        self.clauses = {}
        self.filename = filename
        tree = ET.parse(filename)
        self.XML = tree.getroot()
        self.title = self.XML.get("title")
        clauses_node = self.XML.find("clauses")
        for item in clauses_node.findall("clause") :
            clause = Clause()
            clause.open(filename,  item.get("id"))
            self.clauses[id] = clause

    def saveClause(self,  id):
        document_tree= ET.parse(self.filename)
        document_node = document_tree.getroot()
        clauses_node= document_node.find("clauses")
        for clause in clauses_node :
            if (clause.get('id') == str(id)) :
                clauses_node.remove(clause)
        clause_node = self.getUpdatedNode()
        document_node.append(clause_node)
        document_tree.write(self.document + ".xml")
        
    def getClause(self,  id):
        return self.clauses[id]
    
    def addClause(self,  clause):
        self.clauses[clause.getId] = clause
    
    def removeClause(self, clause):
        del self.clauses[clause.getId()]
        clause.remove()
