import sys
from UI import Ui_ProjectView
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re

from project import Project
from views.DocumentsDiagramScene import DocumentsDiagramScene

class ProjectViewWidget(QWidget):

    newDocumentSignal = pyqtSignal();
    openDocumentSignal = pyqtSignal(str);
    openClauseSignal = pyqtSignal(str);
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
        self.clausesDict  = {}
        self.docsDict = {}
        if (project is not None) :
            self.loadProject(project)
        self.ui.documentsListWidget.expandAll()
        self.ui.documentsListWidget.setFocus()
        

    def backHistory(self):
        self.backHistorySignal.emit()

    def closeProject(self):
        self.closeProjectSignal.emit()

    def loadProject(self,  project):
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

    def openSelect(self, selectedItem, column):
        if (selectedItem.parent() is None) :
            if (self.ui.documentsListWidget.indexOfTopLevelItem(selectedItem) == 0):
                self.newDocument();
            else :
                #documentName = self.docsDict[str(selectedItem.text(0))]
                documentParse = re.search(".*\((?P<documentName>.*)\)", str(selectedItem.text(0)))
                self.openDocumentSignal.emit(documentParse.group('documentName'))
        else :
            #documentName = self.docsDict[str(selectedItem.parent().text(0))]
            documentParse = re.search(".*\((?P<documentName>.*)\)", str(selectedItem.parent().text(0)))
            self.openClauseSignal.emit(self.clausesDict[documentParse.group('documentName') + str(selectedItem.text(0))])

    def newDocument(self):
        self.newDocumentSignal.emit()
