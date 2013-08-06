from UI import Ui_EditDocumentDialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditDocumentDialog(QDialog):

    def __init__(self, parent, document):
        super(EditDocumentDialog, self).__init__(parent)
        self.ui = Ui_EditDocumentDialog.Ui_EditDocumentDialog()
        self.ui.setupUi(self)
        self.document = document
        self.ui.titleEdit.setText(self.document.getTitle())
        self.ui.prefixEdit.setText(self.document.getPrefix())
        self.accepted.connect(self.saveChanges)
    
    def saveChanges(self):
        self.document.setTitle(self.ui.titleEdit.text())
        self.document.setPrefix(self.ui.prefixEdit.text())