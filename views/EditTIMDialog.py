from UI import Ui_EditTIMDialog
import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import *
from views.EditTypeDialog import EditTypeDialog
from models.TIM import TIMModel

class EditTIMDialog(QDialog):
    def __init__(self, parent, project):
        super(EditTIMDialog, self).__init__(parent)
        self.ui = Ui_EditTIMDialog.Ui_EditTIMDialog()
        self.ui.setupUi(self)
        self.project = project
        self.TIM = project.getTIM()
        model = TIMModel(self.TIM)
        self.ui.TIMTreeView.setModel(model)
        #self.loadTIM(self.TIM)
        self.ui.buttonBox.accepted.connect(self.saveChanges)
        self.ui.TIMTreeView.activated.connect(self.openType)

    def loadTIM(self, TIM):
        self.ui.TIMTreeView.clear()
        addItem = QTreeWidgetItem(self.ui.TIMTreeView)
        addItem.setText(0, "<adicionar tipo>")
        rootsList = TIM.getRootsList()
        for root in rootsList :
            self.prepareType(root, self.ui.TIMTreeView)

    def prepareType(self, typeName, parentItem):
        typeItem = QTreeWidgetItem(parentItem)
        typeItem.setText(0, typeName)
        type = self.TIM.getType(typeName)
        addItem = QTreeWidgetItem(typeItem)
        addItem.setText(0, "<adicionar tipo>")
        childTypeList = type.getPossibleChildrenList()
        for child in childTypeList:
            self.prepareType(child, typeItem)
        self.ui.TIMTreeView.expandAll()

    def openType(self):
        selectedItem = self.ui.TIMTreeView.selectedItems()[0]
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
    
    
    