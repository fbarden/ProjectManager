from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_NewDocumentDialog

from document import Document

class NewDocumentDialog(QDialog):
    
    openDocumentSignal = pyqtSignal(object)
    
    def __init__(self,  parent,  project, document):
        super(NewDocumentDialog, self).__init__(parent)
        self.project = project
        self.document = document
        self.ui = Ui_NewDocumentDialog.Ui_NewDocumentDialog()
        self.ui.setupUi(self)
        self.accepted.connect(self.setDocument)
    
    def setDocument(self):
        title = str(self.ui.titleEdit.text())
        initials = str(self.ui.initialsEdit.text())
        name = str(self.ui.nameEdit.text())
        self.document.setTitle(title)
        self.document.setInitials(initials)
        self.document.setName(name)
        self.project.addDocument(self.document)
        self.openDocumentSignal.emit(self.document.getName())
