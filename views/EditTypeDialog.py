from PyQt4.QtGui import *
from PyQt4.QtCore import *
from views.UI import Ui_EditTypeDialog

class EditTypeDialog(QDialog):

    def __init__(self, parent, type, parentType):
        super(EditTypeDialog, self).__init__(parent)
        self.ui = Ui_EditTypeDialog.Ui_EditTypeDialog()
        self.ui.setupUi(self)
        self.type = type
        self.parentType = parentType
        self.loadType(self.type, parentType)
        self.accepted.connect(self.saveChanges)

    def loadType(self, type, parentType):
        self.ui.nameEdit.setText(type.getName())
        self.ui.prefixEdit.setText(type.getPrefix())
        self.ui.descriptionEdit.setText(type.getDescription())
    
    def saveChanges(self):
        print "Salvando Changes"
        self.type.setName(self.ui.nameEdit.text())
        self.type.setPrefix(self.ui.prefixEdit.text())