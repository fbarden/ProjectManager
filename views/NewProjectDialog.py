from UI import Ui_NewProjectDialog
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class NewProjectDialog(QtGui.QDialog):
    def __init__(self):
        super(NewProjectDialog, self).__init__()
        self.ui = Ui_NewProjectDialog.Ui_NewProjectDialog()
        self.ui.setupUi(self)
