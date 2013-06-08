from UI import Ui_NewProjectDialog
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class NewProjectDialog(QtGui.QDialog):
    def __init__(self,  project):
        super(NewProjectDialog, self).__init__()
        self.ui = Ui_NewProjectDialog.Ui_NewProjectDialog()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.searchPath())
        self.ui.buttonBox.accepted.connect(self.setProject)

    def setProject(self):
        project.setName(self.ui.projectNameEdit.text())
        project.setFilepath(self.folderEdit.text())
