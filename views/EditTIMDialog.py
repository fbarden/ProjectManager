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
        self.ui.TIMTreeView.setExpandsOnDoubleClick(False)
        self.ui.TIMTreeView.expandAll()
        self.ui.TIMTreeView.activated.connect(self.openType)
        self.ui.buttonBox.accepted.connect(self.saveChanges)

    def openType(self, index):
        type = index.data(Qt.UserRole).toPyObject()
        if (index.parent().isValid()) :
            parentType = index.parent().data(Qt.UserRole).toPyObject()
        else:
            parentType = None
        editType = EditTypeDialog(self, type, parentType)
        editType.show()
        editType.accepted.connect(lambda : self.loadTIM(self.TIM))
    
    def saveChanges(self):
        pass

    def contextMenuEvent(self, event):
        print event.pos()