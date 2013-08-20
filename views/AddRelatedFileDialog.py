#!/usr/bin/python
# -*- coding: utf-8 -*-
import shutil

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_AddRelatedFileDialog

class AddRelatedFileDialog(QDialog):

    updateFileTreeSignal = pyqtSignal();

    def __init__(self, parent, project, clause):
        super(AddRelatedFileDialog, self).__init__(parent)
        self.project = project
        self.clause = clause
        self.ui = Ui_AddRelatedFileDialog.Ui_AddRelatedFileDialog()
        self.ui.setupUi(self)
        self.loadFiles()
        self.accepted.connect(self.setClause)

    def loadFiles(self):
        importedFiles = self.project.getImportedFilesList()
        for file in importedFiles :
            item = QTreeWidgetItem(self.ui.filesTreeWidget)
            item.setText(0, file)
            item.setText(1, self.project.getImportedFileDescription(file))

    def setClause(self):
        file = unicode(self.ui.filesTreeWidget.currentItem().text(0))
        observation = unicode(self.ui.observationEdit.text())
        self.clause.addRelatedFile(file, observation)
        self.updateFileTreeSignal.emit()
