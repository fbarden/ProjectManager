from UI import Ui_MainWindow
from NewProjectDialog import NewProjectDialog
from NewDocumentDialog import NewDocumentDialog
from NewClauseDialog import NewClauseDialog
from ProjectViewWidget import ProjectViewWidget
from DocumentViewWidget import DocumentViewWidget
from ClauseViewWidget import ClauseViewWidget
from EditImportedFilesDialog import EditImportedFilesDialog
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project
from document import Document
from clause import Clause

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.project = None
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNewProject.triggered.connect(self.newProject)
        self.ui.actionOpenProject.triggered.connect(self.openProject)
        self.ui.actionSaveProject.triggered.connect(self.saveProject)
        self.ui.actionManageFiles.triggered.connect(self.manageImportedFiles)
#        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)

    def newProject(self):
        self.project = Project()
        newProjectDialog = NewProjectDialog(self,  self.project)
        newProjectDialog .show()
        newProjectDialog.openProjectSignal.connect(self.openProjectWidget)

    def newDocument(self):
        newDocumentDialog = NewDocumentDialog(self,  self.project)
        newDocumentDialog .show()
        newDocumentDialog.openDocumentSignal.connect(self.openDocumentWidget)
#        self.project.addDocument(document)
    
    def newClause(self, documentName):
        document = self.project.getDocument(str(documentName))
        newClauseDialog = NewClauseDialog(self, self.project, document)
        newClauseDialog.show()
        newClauseDialog.openClauseSignal.connect(self.openClauseWidget)

    def openProject(self):
        projectPath = QFileDialog.getOpenFileName(\
            None,
            self.trUtf8("Abrir arquivo..."),
            self.trUtf8("."),
            self.trUtf8("*.prj"),
            None)
        self.project = Project()
        self.project.loadXML(str(projectPath))
        self.openProjectWidget()
    
    def saveProject(self):
        self.project.saveAll()

    def openProjectWidget(self):
        project = self.project
        projectViewWidget = ProjectViewWidget(project)
        self.setCentralWidget(projectViewWidget)
        self.ui.centralwidget = projectViewWidget
        self.ui.centralwidget.newDocumentSignal.connect(self.newDocument)
        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)
        self.ui.centralwidget.openClauseSignal.connect(self.openClauseWidget)

    def openDocumentWidget(self, document):
        if (document == None) :
            documentObj = Document()
        else :
            documentObj = self.project.getDocument(str(document))
        documentViewWidget = DocumentViewWidget(documentObj)
        self.setCentralWidget(documentViewWidget)
        self.ui.centralwidget = documentViewWidget
        self.ui.centralwidget.openProjectSignal.connect(self.openProjectWidget)
        self.ui.centralwidget.newClauseSignal.connect(self.newClause)
        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)
        self.ui.centralwidget.openClauseSignal.connect(self.openClauseWidget)

    def openClauseWidget(self, document,  clause):
        clauseObj = self.project.getDocument(str(document)).getClause(str(clause))
        clauseViewWidget = ClauseViewWidget(self.project, clauseObj)
        self.setCentralWidget(clauseViewWidget)
        self.ui.centralwidget = clauseViewWidget
        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)

    def manageImportedFiles(self):
        if (self.project is not None):
            editImportedFilesDialog = EditImportedFilesDialog(self, self.project)
            editImportedFilesDialog.show()
