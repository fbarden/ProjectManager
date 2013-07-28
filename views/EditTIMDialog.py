from UI import Ui_EditTIMDialog
import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import *
from views.EditTypeDialog import EditTypeDialog

class EditTIMDialog(QDialog):
    def __init__(self, parent, project):
        super(EditTIMDialog, self).__init__(parent)
        self.ui = Ui_EditTIMDialog.Ui_EditTIMDialog()
        self.ui.setupUi(self)
        self.project = project
        self.TIM = project.getTIM()
        self.loadTIM(self.TIM)
        self.ui.buttonBox.accepted.connect(self.saveChanges)
        self.ui.TIMTreeWidget.activated.connect(self.openType)

    def loadTIM(self, TIM):
        self.ui.TIMTreeWidget.clear()
        addItem = QTreeWidgetItem(self.ui.TIMTreeWidget)
        addItem.setText(0, "<adicionar tipo>")
        rootsList = TIM.getRootsList()
        for root in rootsList :
            self.prepareType(root, self.ui.TIMTreeWidget)

    def prepareType(self, typeName, parentItem):
        typeItem = QTreeWidgetItem(parentItem)
        typeItem.setText(0, typeName)
        type = self.TIM.getType(typeName)
        addItem = QTreeWidgetItem(typeItem)
        addItem.setText(0, "<adicionar tipo>")
        childTypeList = type.getPossibleChildrenList()
        for child in childTypeList:
            self.prepareType(child, typeItem)
        self.ui.TIMTreeWidget.expandAll()

    def openType(self):
        selectedItem = self.ui.TIMTreeWidget.selectedItems()[0]
        type = self.TIM.getType(selectedItem.text(0))
        if (selectedItem.parent() is not None) :
            parentType = self.TIM.getType(selectedItem.parent().text(0))
        else:
            parentType = None
        editType = EditTypeDialog(self, type, parentType)
        editType.show()
        editType.accepted.connect(lambda : self.loadTIM(self.TIM))
    
    def saveChanges(self):
        pass
    
    
    