from PyQt4.QtGui import *
from PyQt4.QtCore import *
from views.UI import Ui_EditTypeDialog

class EditTypeDialog(QDialog):

    def __init__(self, parent, type, parentType, TIM):
        super(EditTypeDialog, self).__init__(parent)
        self.ui = Ui_EditTypeDialog.Ui_EditTypeDialog()
        self.ui.setupUi(self)
        self.type = type
        self.parentType = parentType
        self.TIM = TIM
        self.loadType(self.type, parentType)
        self.accepted.connect(self.saveChanges)

    def loadType(self, type, parentType):
        self.ui.nameEdit.setText(type.getName())
        self.ui.prefixEdit.setText(type.getPrefix())
        self.ui.descriptionEdit.setText(type.getDescription())
        if (parentType is not None) :
            parentName = parentType.getName()
            self.ui.minCardChildEdit.setText(type.getParentMinCard(parentName))
            self.ui.maxCardChildEdit.setText(type.getParentMaxCard(parentName))
            self.ui.childDependencyCheckBox.setChecked(type.isDependentOf(parentName))
            typeName = type.getName()
            self.ui.minCardParentEdit.setText(parentType.getChildMinCard(typeName))
            self.ui.maxCardParentEdit.setText(parentType.getChildMaxCard(typeName))
            self.ui.parentDependencyCheckBox.setChecked(parentType.isDependentOf(typeName))
        else :
            self.ui.minCardChildEdit.setEnabled(False)
            self.ui.maxCardChildEdit.setEnabled(False)
            self.ui.childDependencyCheckBox.setEnabled(False)
            self.ui.minCardParentEdit.setEnabled(False)
            self.ui.maxCardParentEdit.setEnabled(False)
            self.ui.parentDependencyCheckBox.setEnabled(False)
    
    def saveChanges(self):
        parentName = self.parentType.getName()
        minChildCard = self.ui.minCardChildEdit.text()
        maxChildCard = self.ui.maxCardChildEdit.text()
        childDependency =  self.ui.childDependencyCheckBox.isChecked()
        self.type.removePossibleParent(parentName)
        self.type.addPossibleParent(parentName, minChildCard, maxChildCard, childDependency)

        childName = self.type.getName()
        minParentCard = self.ui.minCardParentEdit.text()
        maxParentCard = self.ui.maxCardParentEdit.text()
        parentDependency = self.ui.parentDependencyCheckBox.isChecked()
        self.parentType.removePossibleChild(childName)
        self.parentType.addPossibleChild(childName, minParentCard, maxParentCard, parentDependency)

        newName = self.ui.nameEdit.text()
        self.TIM.renameType(childName, newName)
        self.type.setPrefix(self.ui.prefixEdit.text())
        self.type.setDescription(self.ui.descriptionEdit.text())