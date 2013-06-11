from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_EditImportedFilesDialog

from ImportFileDialog import ImportFileDialog

from project import Project
from document import Document

class EditImportedFilesDialog(QDialog):
    
    openDocumentSignal = pyqtSignal(str)
    
    def __init__(self,  parent,  project):
        super(EditImportedFilesDialog, self).__init__(parent)
        self.changedIndexes = []
        self.project = project
        self.ui = Ui_EditImportedFilesDialog.Ui_EditImportedFilesDialog()
        self.ui.setupUi(self)
        self.updateFilesTree()
        self.ui.filesTree.itemActivated.connect(self.editImportedFile)
        self.accepted.connect(self.setImportedFiles)

    def updateFilesTree(self):
        filesList = self.project.getImportedFilesList()
        for fileName in filesList :
            fileItem = QTreeWidgetItem(self.ui.filesTree)
            fileItem.setText(0, fileName)
            fileItem.setText(1, self.project.getImportedFileDescription(fileName))

    def editImportedFile(self, item):
        index = self.ui.filesTree.indexOfTopLevelItem(item)
        if index == 0 :
            self.importFile()
        else:
            newDescription, returnOK = QInputDialog.getText(\
                None,
                self.trUtf8("Editar Descricao"),
                self.trUtf8("Insira nova descricao para o arquivo:"),
                QLineEdit.Normal,
                item.text(1))
            if returnOK :
                item.setText(1, newDescription)
                if index not in self.changedIndexes :
                    self.changedIndexes += [index]

    def setImportedFiles(self):
        for index in self.changedIndexes :
            item = self.ui.filesTree.topLevelItem(index)
            self.project.setImportedFileDescription(str(item.text(0)), str(item.text(1)))

    def importFile(self):
        importFileDialog = ImportFileDialog(self, self.project)
        importFileDialog.show()
        importFileDialog.fileImportedSignal.connect(self.addImportedFile)

    def addImportedFile(self, fileName):
        item = QTreeWidgetItem(self.ui.filesTree)
        item.setText(0, fileName)
        item.setText(1, self.project.getImportedFileDescription(str(fileName)))
