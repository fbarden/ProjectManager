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
        description = str(self.ui.descriptionEdit.text())
        filepath = str(self.ui.fileEdit.text())
        self.project.addImportedFile(os.path.basename(filepath), description)
        shutil.copy(filepath, self.project.getLocation() + 'imported/')
        self.fileImportedSignal.emit(os.path.basename(filepath))
