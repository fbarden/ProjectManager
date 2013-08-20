#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Jul 27, 2013

@author: fbarden
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ProjectViewModel(QStandardItemModel):
    
    def __init__(self, project):
        super(ProjectViewModel, self).__init__()
        self.project = project
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["Documentos", "Prefixos", "Tipos", "ID consolidado", "Avisos"])
        invisibleRoot = self.invisibleRootItem()
        documentsList = project.getDocumentsList()
        for documentName in documentsList :
            document = self.project.getDocument(documentName)
            invisibleRoot.appendRow(self.prepareDocument(document))

    def prepareDocument(self, document):
        itemLabel = document.getTitle()
        documentItem = QStandardItem(itemLabel)
        clausesList = document.getClausesList()
        documentItem.setData("document", Qt.UserRole)
        documentItem.setData(document, Qt.UserRole + 1)
        for clauseId in clausesList :
            clause = document.getClause(clauseId)
            documentItem.appendRow(self.prepareClause(clause))
        documentItem.setFlags(documentItem.flags() & ~ Qt.ItemIsEditable)
        
        prefixItem = QStandardItem(document.getPrefix())
        prefixItem.setFlags(prefixItem.flags() & ~ Qt.ItemIsEditable)
    
        return [documentItem, prefixItem]
        
    def prepareClause(self, clause):
        itemLabel = clause.getTitle()
        warnings = ' | '.join(clause.getWarnings())
        warningsItem = QStandardItem(warnings)
        warningsItem.setFlags(warningsItem.flags() & ~ Qt.ItemIsEditable)
        
        clauseItem = QStandardItem(itemLabel)
        clauseItem.setData("clause", Qt.UserRole)
        clauseItem.setData(clause, Qt.UserRole + 1)
        clauseItem.setData(warnings, Qt.UserRole + 2)            
        clauseItem.setFlags(clauseItem.flags() & ~ Qt.ItemIsEditable)
        
        typeItem = QStandardItem(clause.getType().getName())
        typeItem.setFlags(typeItem.flags() & ~ Qt.ItemIsEditable)
        
        consolidateItem = QStandardItem(clause.getConsolidatedID())
        consolidateItem.setFlags(consolidateItem.flags() & ~ Qt.ItemIsEditable)
        
        return [clauseItem, None, typeItem, consolidateItem, warningsItem]
    
    def moveElement(self, index, step):
        movedItem = self.itemFromIndex(index)
        parentItem = movedItem.parent()
        movedRow = index.row()
        if (parentItem is None) :
            parentItem = self

        newRow = movedRow + step
        if (newRow < 0):
            newRow = 0
        elif (newRow >= parentItem.rowCount()) :
            newRow = parentItem.rowCount() - 1
        moved = parentItem.takeRow(movedRow)
        parentItem.insertRow(newRow, moved)

        type = movedItem.data(Qt.UserRole).toPyObject()
        element = movedItem.data(Qt.UserRole + 1).toPyObject()
        if (type == "document") :
            self.project.moveDocument(element.getName(), step)
        elif (type == "clause") :
            doc = element.getDocument()
            doc.moveClause(element.getID(), step)

    def moveUpElement(self, index):
        self.moveElement(index, -1)

    def moveDownElement(self, index):
        self.moveElement(index, 1)

    def deleteElement(self, index):
        item = self.itemFromIndex(index)
        type = item.data(Qt.UserRole).toPyObject()
        element = item.data(Qt.UserRole + 1).toPyObject()
        if (type == 'document'):
            self.project.removeDocument(element.getName())
        elif (type == 'clause'):
            doc = element.getDocument()
            doc.removeClause(element.getID())
        self.removeRow(item.row(), index.parent())
