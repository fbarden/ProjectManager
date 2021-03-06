#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, shutil

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_ImportFileDialog

class ImportFileDialog(QDialog):
    
    fileImportedSignal = pyqtSignal(str)
    
    def __init__(self, parent, project):
        super(ImportFileDialog, self).__init__(parent)
        self.project = project
        self.ui = Ui_ImportFileDialog.Ui_ImportFileDialog()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.searchFile)
        self.accepted.connect(self.completeImport)

    def searchFile(self):
        filepath = QFileDialog.getOpenFileName(\
            None,
            self.trUtf8("Importar arquivo"),
            QString(),
            QString(),
            None)
        if (filepath != "") :
            self.ui.fileEdit.setText(filepath)

    def completeImport(self):
        description = unicode(self.ui.descriptionEdit.text())
        filepath = unicode(self.ui.fileEdit.text())
        if (filepath != '') :
            try :
                shutil.copy(filepath, self.project.getLocation() + 'imported/')
                self.project.addImportedFile(os.path.basename(filepath), description)
                self.fileImportedSignal.emit(os.path.basename(filepath))
            except:
                QMessageBox.warning(None,
                                    self.trUtf8("Erro"),
                                    self.trUtf8("""Erro ao importar arquivo!"""),
                                    QMessageBox.StandardButtons(QMessageBox.Ok))

