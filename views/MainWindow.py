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
from views.TIMDiagramDialog import TIMDiagramDialog
from verification import Verification
from views.ClausePathDiagramDialog import ClausePathDiagramDialog
from views.ProjectConsolidationWizard import ProjectConsolidationWizard
from Consolidator import Consolidator

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
        self.ui.actionTIMDiagram.triggered.connect(self.showTIMDiagram)
        self.ui.actionPathDiagram.triggered.connect(self.showClausePathDiagram)
        self.ui.actionNewDocument.triggered.connect(self.newDocument)
        self.ui.actionNewClause.triggered.connect(lambda : self.newClause())
        self.ui.actionCheckSpaces.triggered.connect(self.checkSpaces)
        self.ui.actionProjectConsolidation.triggered.connect(self.projectConsolidation)

    def projectConsolidation(self):
        projectConsolidationWizard = ProjectConsolidationWizard(self, self.project)
        projectConsolidationWizard.show()
        projectConsolidationWizard.consolidateProjectSignal.connect(self.consolidateProject)
    
    def consolidateProject(self, settings):
        consolidator = Consolidator(self.project, settings)
        consolidator.toPDF()

    def showClausePathDiagram(self):
        clauseList = []
        title2ClauseDict = {}
        doc2Clause = self.project.getDocument2ClausesDict()
        for docName in doc2Clause.keys():
            doc = self.project.getDocument(docName)
            for clauseID in doc2Clause[docName]:
                clause = doc.getClause(clauseID)
                exibitionName = doc.getPrefix() + " - " + clause.getTitle()
                clauseList.append(exibitionName)
                title2ClauseDict[exibitionName] = clause
        choiceID, returnOK = QInputDialog.getItem(None,
                             self.trUtf8("Diagrama de Caminho"),
                             self.trUtf8("Escolha a clausula base:"),
                             clauseList,
                             0, False)
        diagramDialog = ClausePathDiagramDialog(self, title2ClauseDict[str(choiceID)])
        diagramDialog.show()

    def showTIMDiagram(self):
        diagramDialog = TIMDiagramDialog(self, self.project.getTIM())
        diagramDialog.show() 
        
    def newProject(self):
        self.project = Project()
        newProjectDialog = NewProjectDialog(self,  self.project)
        newProjectDialog.show()
        newProjectDialog.openProjectSignal.connect(self.openProjectWidget)
        self.history = []
        self.history.insert(0, 'project:root')

    def newDocument(self):
        newDocumentDialog = NewDocumentDialog(self,  self.project)
        newDocumentDialog.show()
        newDocumentDialog.openDocumentSignal.connect(self.openDocumentWidget)
#        self.project.addDocument(document)

    def checkSpaces(self):
        verification = Verification()
        verification.checkSpaces(self.project)

    def newClause(self, paramDict = {}):
        document = None
        parentClause = None
        type = None
        for param in paramDict:
            if (param is 'document'):
                documentName = paramDict['document']
                document = self.project.getDocument(documentName)
            elif (param is 'parentClause'):
                parentClause = paramDict['parentClause']
        newClauseDialog = NewClauseDialog(self, self.project, document, parentClause)
        newClauseDialog.show()
        newClauseDialog.openClauseSignal.connect(self.openClauseWidget)

    def openProject(self):
        projectPath = str(QFileDialog.getOpenFileName(\
            None,
            self.trUtf8("Abrir arquivo..."),
            self.trUtf8("."),
            self.trUtf8("*.prj"),
            None))
        if (projectPath != ""):
            self.project = Project()
            self.project.loadXML(str(projectPath))
            self.history = []
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
        self.ui.centralwidget.closeProjectSignal.connect(self.closeProject)
        self.ui.centralwidget.backHistorySignal.connect(self.backHistory)
        self.ui.actionNewDocument.setEnabled(True)
        self.ui.actionNewClause.setEnabled(len(self.project.getDocumentsList()) > 0)
        self.history.insert(0, 'project:project')

    def closeProject(self):
        self.project = None
        self.centralwidget = None
        self.setCentralWidget(self.centralwidget)
        self.ui.actionNewDocument.setEnabled(False)
        self.ui.actionNewClause.setEnabled(False)

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
        self.ui.centralwidget.backHistorySignal.connect(self.backHistory)
        self.ui.actionNewClause.setEnabled(len(self.project.getDocumentsList()) > 0)
        self.history.insert(0, 'document:' + str(document))

    def openClauseWidget(self, clauseID):
        documentName = clauseID.split(":")[0]
        clauseObj = self.project.getDocument(str(documentName)).getClause(str(clauseID))
        clauseViewWidget = ClauseViewWidget(self.project, clauseObj)
        self.setCentralWidget(clauseViewWidget)
        self.ui.centralwidget = clauseViewWidget
        self.ui.centralwidget.openDocumentSignal.connect(self.openDocumentWidget)
        self.ui.centralwidget.openClauseSignal.connect(self.openClauseWidget)
        self.ui.centralwidget.newClauseSignal.connect(self.newClause)
        self.ui.centralwidget.backHistorySignal.connect(self.backHistory)
        self.history.insert(0, 'clause:' + str(clauseID))

    def backHistory(self):
        if len(self.history) == 1:
            return
        del self.history[0]
        print '-----------------'
        print self.history[0]
        type, id = self.history[0].split(":", 1)
        if (type == "clause"):
            print "Carregando clausula " + id
            self.openClauseWidget(id)
        elif (type == "document"):
            print "Carregando documento " + id
            self.openDocumentWidget(id)
        elif (type == "project"):
            print 'Carregando projeto'
            self.openProjectWidget()

    def manageImportedFiles(self):
        if (self.project is not None):
            editImportedFilesDialog = EditImportedFilesDialog(self, self.project)
            editImportedFilesDialog.show()
