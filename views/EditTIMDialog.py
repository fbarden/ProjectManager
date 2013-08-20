#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
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
        for column in range(model.columnCount()):
            self.ui.TIMTreeView.resizeColumnToContents(column)

    def openType(self, index):
        typeIndex = index.sibling(index.row(), 0)
        type = typeIndex.data(Qt.UserRole).toPyObject()
        if (typeIndex.parent().isValid()) :
            parentType = typeIndex.parent().data(Qt.UserRole).toPyObject()
        else:
            parentType = None
        editType = EditTypeDialog(self, type, parentType, self.TIM)
        if(editType.exec_()) :
            self.loadTIM(self.TIM)
            self.ui.TIMTreeView.update(index)

    def loadTIM(self, TIM):
        model = TIMModel(TIM)
        self.ui.TIMTreeView.setModel(model)
        self.ui.TIMTreeView.expandAll()
        for column in range(model.columnCount()):
            self.ui.TIMTreeView.resizeColumnToContents(column)
    
    def saveChanges(self):
        pass

#    def contextMenuEvent(self, event):
#        print event.pos()
