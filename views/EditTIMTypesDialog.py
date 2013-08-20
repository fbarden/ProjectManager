#!/usr/bin/python
# -*- coding: utf-8 -*-
from UI import Ui_EditTIMTypesDialog
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class EditTIMTypesDialog(QtGui.QDialog):
    def __init__(self,  project):
        super(EditTIMTypesDialog, self).__init__()
        self.ui = Ui_EditTIMTypesDialog.Ui_EditTIMTypesDialog()
        self.ui.setupUi(self)
#        self.ui.searchButton.clicked.connect(self.searchPath())
        self.ui.buttonBox.accepted.connect(self.setProject)

    def setProject(self):
        project.setName(self.ui.projectNameEdit.text())
        project.setFilepath(self.folderEdit.text())
