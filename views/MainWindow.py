from UI import Ui_MainWindow
from NewProjectDialog import NewProjectDialog
from ProjectViewWidget import ProjectViewWidget
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore

from project import Project

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNewProject.triggered.connect(self.newProject)
        self.ui.actionOpenProject.triggered.connect(self.openProject)
        self.ui.actionSaveProject.triggered.connect(self.saveProject)

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
        project = Project()
        project.open(str(projectPath))
        self.openProjectWidget(project)
    
    def saveProject(self):
        pass

    def openProjectWidget(self,  project):
        self.ui.centralwidget.openProjectWidget(project)
