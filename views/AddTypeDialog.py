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
        isRoot = (self.item.parent() is not None)
        self.ui.minCardChildEdit.setEnabled(isRoot)
        self.ui.maxCardChildEdit.setEnabled(isRoot)
        self.ui.childDependencyCheckBox.setEnabled(isRoot)
        self.ui.minCardParentEdit.setEnabled(isRoot)
        self.ui.maxCardParentEdit.setEnabled(isRoot)
        self.ui.parentDependencyCheckBox.setEnabled(isRoot)

    def addType(self):
        if (self.ui.existingTypeButton.isChecked()):
            typeName = str(self.ui.typeComboBox.currentText())
            type = self.TIM.getType(typeName)
        elif (self.ui.newTypeButton.isChecked()):
            type = Type()
            typeName = str(self.ui.newTypeEdit.text())
            typePrefix = str(self.ui.prefixEdit.text())
            typeDescription = str(self.ui.descriptionEdit.text())
            type.setName(typeName)
            type.setPrefix(typePrefix)
            type.setDescription(typeDescription)
            self.TIM.addType(type)
        if (self.item.parent() is None) :
            self.TIM.addRoot(typeName)
        else :
            minCardChild = str(self.ui.minCardChildEdit.text())
            maxCardChild = str(self.ui.maxCardChildEdit.text())
            childDependency = self.ui.childDependencyCheckBox.isChecked()
            minCardParent = str(self.ui.minCardParentEdit.text())
            maxCardParent = str(self.ui.maxCardParentEdit.text())
            parentDependency = self.ui.parentDependencyCheckBox.isChecked()
            parentName = str(self.item.parent().text(0))
            parentType = self.TIM.getType(parentName)
            parentType.addPossibleChild(typeName, minCardChild, maxCardChild, childDependency)
            type.addPossibleParent(parentName, minCardParent, maxCardParent, parentDependency)
        self.addTypeSignal.emit(type.getName(),  self.item)

    def loadTypes(self):
        typesList = self.TIM.getTypesList()
        for type in typesList:
            self.ui.typeComboBox.addItem(type)
