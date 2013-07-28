import sys
from UI import Ui_ProjectView
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re

from project import Project
from views.DocumentsDiagramScene import DocumentsDiagramScene

class ProjectViewWidget(QWidget):

    newDocumentSignal = pyqtSignal();
    openElementSignal = pyqtSignal(str);
    closeProjectSignal = pyqtSignal();
    backHistorySignal = pyqtSignal();

    def __init__(self, project = None):
        super(ProjectViewWidget, self).__init__()
        self.ui = Ui_ProjectView.Ui_projectViewWidget()
        self.ui.setupUi(self)
        self.ui.documentsListWidget.itemActivated.connect(self.openSelect)
        self.closeProjectShortcut = QShortcut('CTRL+W', self)
        self.closeProjectShortcut.activated.connect(self.closeProject)
        self.backHistoryShortcut = QShortcut('ALT+Backspace', self)
        self.backHistoryShortcut.activated.connect(self.backHistory)
        self.moveUpShortcut = QShortcut('ALT+Up', self)
        self.moveUpShortcut.activated.connect(self.moveUpElement)
        self.moveDownShortcut = QShortcut('ALT+Down', self)
        self.moveDownShortcut.activated.connect(self.moveDownElement)
        self.ui.moveUpButton.clicked.connect(self.moveUpElement)
        self.ui.moveDownButton.clicked.connect(self.moveDownElement)
        self.ui.deleteButton.clicked.connect(self.deleteElement)
        self.deleteShortcut = QShortcut('Delete', self)
        self.deleteShortcut.activated.connect(self.deleteElement)
        self.clausesDict  = {}
        self.docsDict = {}
        if (project is not None) :
            self.project = project
            self.loadProject(project)
        self.ui.documentsListWidget.setFocus()

    def moveUpElement(self):
        self.moveElement(-1)
    
    def moveDownElement(self):
        self.moveElement(1)

    def moveElement(self, step):
        selectedItem = self.ui.documentsListWidget.selectedItems()[0]
        type, id = self.parseSelection(selectedItem)
        if (type == 'document'):
            widget = self.ui.documentsListWidget
            index = widget.indexOfTopLevelItem(selectedItem)
            newIndex = index + step
            if (newIndex<1) or (newIndex>=widget.topLevelItemCount()):
                return
            self.project.moveDocument(id, step)
            self.ui.documentsListWidget.takeTopLevelItem(index)
            self.ui.documentsListWidget.insertTopLevelItem(newIndex, selectedItem)
        elif (type == 'clause'):
            parent = selectedItem.parent()
            index = parent.indexOfChild(selectedItem)
            newIndex = index + step
            if (newIndex<0) or (newIndex >= parent.childCount()) :
                return
            documentName = id.split(":", 1)[0]
            document = self.project.getDocument(documentName)
            document.moveClause(id, step)
            parent.takeChild(index)
            parent.insertChild(newIndex, selectedItem)
        selectedItem.setExpanded(True)
        auxItem = self.ui.documentsListWidget.selectedItems()
        if auxItem != [] :
            auxItem[0].setSelected(False)
        selectedItem.setSelected(True)
            

    def deleteElement(self):
        selectedItem = self.ui.documentsListWidget.selectedItems()[0]
        type, id = self.parseSelection(selectedItem)
        if (type == 'document'):
            self.project.removeDocument(id)
        elif (type == 'clause'):
            documentName = id.split(":", 1)[0]
            document = self.project.getDocument(documentName)
            document.removeClause(id)
        self.loadProject(self.project)

    def backHistory(self):
        self.backHistorySignal.emit()

    def closeProject(self):
        self.closeProjectSignal.emit()

    def loadProject(self,  project):
        self.ui.documentsListWidget.clear()
        documentsList = project.getDocumentsList()
        widgetList = []
        for documentName in documentsList :
            document = project.getDocument(documentName)
            documentWidgetItem = QTreeWidgetItem()
            documentWidgetItem.setText(0,  document.getTitle() + " (" + documentName + ")")
            self.docsDict[document.getTitle()] = documentName
            widgetList += [documentWidgetItem]
            document = project.getDocument(documentName)
            clausesList = document.getClausesList()
            for clauseId in clausesList :
                clauseWidgetItem = QTreeWidgetItem(documentWidgetItem)
                clause = document.getClause(clauseId)
                exibitionName = clause.getTitle()
                if clause.isSuspect() :
                    exibitionName += "    (supeita!)"
                clauseWidgetItem.setText(0, exibitionName)
                self.clausesDict[documentName + clause.getTitle()] = clause.getID()
                widgetList += [clauseWidgetItem]
        self.ui.documentsListWidget.addTopLevelItems(widgetList)
        documentDiagramScene = DocumentsDiagramScene(self.ui.graphicsView, project)
        self.ui.graphicsView.setScene(documentDiagramScene)
        self.ui.documentsListWidget.expandAll()

    def parseSelection(self, selectedItem):
        if (selectedItem.parent() is None) :
            if (self.ui.documentsListWidget.indexOfTopLevelItem(selectedItem) == 0):
                return "newDocument", None
            documentParse = re.search(".*\((?P<documentName>.*)\)", unicode(selectedItem.text(0)))
            return 'document', documentParse.group('documentName')
        else :
            documentParse = re.search(".*\((?P<documentName>.*)\)", unicode(selectedItem.parent().text(0)))
            return "clause", self.clausesDict[documentParse.group('documentName') + unicode(selectedItem.text(0))]

    def openSelect(self, selectedItem, column):
        type, id = self.parseSelection(selectedItem)
        if (type == 'newDocument'):
            self.newDocument();
        else :
            self.openElementSignal.emit(type + ":" + id)

    def newDocument(self):
        self.newDocumentSignal.emit()
