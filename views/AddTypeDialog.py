from UI import Ui_AddTypeDialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *

class AddTypeDialog(QDialog):

    addTypeSignal = pyqtSignal(str,  QTreeWidgetItem);

    def __init__(self,  parent,  TIM,  item):
        super(AddTypeDialog, self).__init__(parent)
        self.TIM = TIM
        self.item = item
        self.ui = Ui_AddTypeDialog.Ui_AddTypeDialog()
        self.ui.setupUi(self)
        self.loadTypes()
        self.accepted.connect(self.addType)
        self.ui.existingTypeButton.toggled.connect(self.ui.typeComboBox.setEnabled)
        self.ui.newTypeButton.toggled.connect(self.ui.newTypeEdit.setEnabled)

    def addType(self):
        if (self.ui.existingTypeButton.isChecked()):
            typeName = str(self.ui.typeComboBox.currentText())
            type = self.TIM.getType(typeName)
        elif (self.ui.newTypeButton.isChecked()):
            type = Type()
            typeName = str(self.ui.newTypeEdit.text())
            type.setName(typeName)
            self.TIM.addType(type)
        if (self.item.parent() is None) :
            self.TIM.addRoot(typeName)
        else :
            parentName = str(self.item.parent().text(0))
            parentType = self.TIM.getType(parentName)
            parentType.addPossibleChild(typeName)
        self.addTypeSignal.emit(type.getName(),  self.item)

    def loadTypes(self):
        typesList = self.TIM.getTypesList()
        for type in typesList:
            self.ui.typeComboBox.addItem(type)
