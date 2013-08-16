import sys
from UI import Ui_ProjectView
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re

from project import Project
from views.DocumentsDiagramScene import DocumentsDiagramScene
from models.ProjectViewModel import ProjectViewModel

class ProjectViewWidget(QWidget):

    newDocumentSignal = pyqtSignal();
    openElementSignal = pyqtSignal(str);
    closeProjectSignal = pyqtSignal();
    backHistorySignal = pyqtSignal();

    def __init__(self, project = None):
        super(ProjectViewWidget, self).__init__()
        self.ui = Ui_ProjectView.Ui_projectViewWidget()
        self.ui.setupUi(self)
        
        model = ProjectViewModel(project)
        self.ui.documentsListWidget.setModel(model)
        documentDiagramScene = DocumentsDiagramScene(self.ui.graphicsView, project)
        self.ui.graphicsView.setScene(documentDiagramScene)
        self.ui.documentsListWidget.expandAll()
        self.ui.documentsListWidget.setFocus()
        
        for column in range(model.columnCount()):
            self.ui.documentsListWidget.resizeColumnToContents(column)
        
        self.ui.documentsListWidget.activated.connect(self.openSelect)
        self.closeProjectAction = QAction('Fechar Projeto', self)
        self.closeProjectAction.setShortcut('CTRL+W')
        self.closeProjectAction.triggered.connect(self.closeProject)
        self.addAction(self.closeProjectAction)
        self.backHistoryAction = QAction(QString('Voltar'), self)
        self.backHistoryAction.setShortcut('ALT+Backspace')
        self.backHistoryAction.triggered.connect(self.backHistory)
        self.addAction(self.backHistoryAction)
        self.moveUpAction = QAction('Mover para cima', self)
        self.moveUpAction.setShortcut('ALT+Up')
        self.moveUpAction.triggered.connect(self.moveUpElement)
        self.addAction(self.moveUpAction)
        self.moveDownAction = QAction('Move para baixo', self)
        self.moveDownAction.setShortcut('ALT+Down')
        self.moveDownAction.triggered.connect(self.moveDownElement)
        self.addAction(self.moveDownAction)
        self.deleteAction = QAction('Excluir', self)
        self.deleteAction.setShortcut('Delete')
        self.deleteAction.triggered.connect(self.deleteElement)
        self.addAction(self.deleteAction)
        self.newDocumentAction = QAction('Criar novo documento', self)
        self.ui.newDocumentButton.setDefaultAction(self.newDocumentAction)
        self.newDocumentAction.triggered.connect(self.newDocument)
        self.deleteAction.setShortcut('Delete')
        self.deleteAction.triggered.connect(self.deleteElement)
        self.addAction(self.deleteAction)
        self.ui.moveUpButton.clicked.connect(self.moveUpElement)
        self.ui.moveDownButton.clicked.connect(self.moveDownElement)
        self.ui.deleteButton.clicked.connect(self.deleteElement)

    def moveUpElement(self):
        model = self.ui.documentsListWidget.model()
        index =  self.ui.documentsListWidget.selectedIndexes()[0]
        self.moveElement(-1)
    
    def moveDownElement(self):
        self.moveElement(1)

    def moveElement(self, step):
        model = self.ui.documentsListWidget.model()
        index =  self.ui.documentsListWidget.selectedIndexes()[0]
        model.moveElement(index, step)
        self.ui.documentsListWidget.expandAll()
        self.ui.documentsListWidget.setFocus()

    def deleteElement(self):
        model = self.ui.documentsListWidget.model()
        index =  self.ui.documentsListWidget.selectedIndexes()[0]
        model.deleteElement(index)
        return

    def backHistory(self):
        self.backHistorySignal.emit()

    def closeProject(self):
        self.closeProjectSignal.emit()

    def openSelect(self, index):
        elementIndex = index.sibling(index.row(), 0)
        type = elementIndex.data(Qt.UserRole).toPyObject()
        id = elementIndex.data(Qt.UserRole + 1).toPyObject()
        if (type == 'newDocument'):
            self.newDocument();
        else :
            if (type == "document") :
                self.openElementSignal.emit(type + ":" + id.getName())
            elif (type == "clause") :
                self.openElementSignal.emit(type + ":" + id.getID())

    def newDocument(self):
        self.newDocumentSignal.emit()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        #----- position = self.ui.documentsListWidget.mapFrom(self, event.pos())
        #--------- if (self.ui.documentsListWidget.indexAt(position).isValid()):
            #--------------------------------- menu.addAction(self.moveUpAction)
            #------------------------------- menu.addAction(self.moveDownAction)
            #--------------------------------- menu.addAction(self.deleteAction)
        #----------------------------------------------------------------- else:
        menu.addAction(self.newDocumentAction)
        menu.popup(event.globalPos())