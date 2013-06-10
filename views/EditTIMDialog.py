from UI import Ui_EditTIMDialog
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class EditTIMDialog(QtGui.QDialog):
    def __init__(self,  project):
        super(EditTIMDialog, self).__init__()
        self.ui = Ui_EditTIMDialog.Ui_EditTIMDialog()
        self.ui.setupUi(self)
#        self.ui.searchButton.clicked.connect(self.searchPath())
        self.ui.buttonBox.accepted.connect(self.setProject)

    def setProject(self):
        project.setName(self.ui.projectNameEdit.text())
        project.setFilepath(self.folderEdit.text())
