from UI import Ui_AddTypeDialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *

class AddTypeDialog(QDialog):

    def __init__(self,  parent,  TIM,  item):
        super(AddTypeDialog, self).__init__(parent)
        self.TIM = TIM
        self.item = item
        self.ui = Ui_AddTypeDialog.Ui_AddTypeDialog()
        self.ui.setupUi(self)
        self.loadTypes()
        self.accepted.connect(self.addType)
        isRoot = (self.item.parent() is not None)
        self.ui.minCardChildEdit.setEnabled(isRoot)
        self.ui.maxCardChildEdit.setEnabled(isRoot)
        self.ui.childDependencyCheckBox.setEnabled(isRoot)
        self.ui.minCardParentEdit.setEnabled(isRoot)
        self.ui.maxCardParentEdit.setEnabled(isRoot)
        self.ui.parentDependencyCheckBox.setEnabled(isRoot)

    def addType(self):
        if (self.ui.existingTypeButton.isChecked()):
            typeName = unicode(self.ui.typeComboBox.currentText())
            type = self.TIM.getType(typeName)
        elif (self.ui.newTypeButton.isChecked()):
            type = Type()
            typeName = unicode(self.ui.newTypeEdit.text())
            typePrefix = unicode(self.ui.prefixEdit.text())
            typeDescription = unicode(self.ui.descriptionEdit.text())
            type.setName(typeName)
            type.setPrefix(typePrefix)
            type.setDescription(typeDescription)
            self.TIM.addType(type)
        if (self.item.parent() is None) :
            self.TIM.addRoot(typeName)
        else :
            minCardChild = unicode(self.ui.minCardChildEdit.text())
            maxCardChild = unicode(self.ui.maxCardChildEdit.text())
            childDependency = self.ui.childDependencyCheckBox.isChecked()
            minCardParent = unicode(self.ui.minCardParentEdit.text())
            maxCardParent = unicode(self.ui.maxCardParentEdit.text())
            parentDependency = self.ui.parentDependencyCheckBox.isChecked()
            parentName = unicode(self.item.parent().text(0))
            parentType = self.TIM.getType(parentName)
            parentType.addPossibleChild(typeName, minCardChild, maxCardChild, parentDependency)
            type.addPossibleParent(parentName, minCardParent, maxCardParent, childDependency)
        self.addTypeSignal.emit(type.getName(),  self.item)

    def loadTypes(self):
        typesList = self.TIM.getTypesList()
        for type in typesList:
            self.ui.typeComboBox.addItem(type)
