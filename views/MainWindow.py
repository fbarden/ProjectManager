from UI import Ui_MainWindow
from NewProjectDialog import NewProjectDialog
from ProjectViewWidget import ProjectViewWidget
from ClauseViewWidget import ClauseViewWidget
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore

from project import Project

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.project = None
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNewProject.triggered.connect(self.newProject)
        self.ui.actionOpenProject.triggered.connect(self.openProject)
        self.ui.actionSaveProject.triggered.connect(self.saveProject)
#        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)

    def newProject(self):
        projectName, returnOK = QInputDialog.getText(\
            None,
            self.trUtf8("Novo Projeto..."),
            self.trUtf8("Nome do projeto"),
            QLineEdit.Normal)

    def openProject(self):
        projectPath = QFileDialog.getOpenFileName(\
            None,
            self.trUtf8("Open File..."),
            self.trUtf8("."),
            self.trUtf8("*.xml"),
            None)
        self.project = Project()
        self.project.open(str(projectPath))
        self.openProjectWidget(self.project)
    
    def saveProject(self):
        pass

    def openProjectWidget(self,  project):
        projectViewWidget = ProjectViewWidget(project)
        self.setCentralWidget(projectViewWidget)
        self.ui.centralwidget = projectViewWidget
        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)
        self.ui.centralwidget.openClauseSignal.connect(self.openClauseWidget)

    def openDocumentWidget(self, document):
        documentViewWidget = DocumentViewWidget(self, document)
        documentViewWidget.show()
#    
    def openClauseWidget(self, document,  clause):
        clauseObj = self.project.getDocument(str(document)).getClause(str(clause))
        clauseViewWidget = ClauseViewWidget(clauseObj)
        self.setCentralWidget(clauseViewWidget)
        self.ui.centralwidget = clauseViewWidget
    