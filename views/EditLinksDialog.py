#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
Created on Aug 19, 2013

@author: fbarden
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from models.EditLinksModel import EditLinksModel
from views.UI.Ui_EditLinksDialog import Ui_EditLinksDialog
from views.AddLinkDialog import AddLinkDialog
from link import Link

class EditLinksDialog(QDialog):
    '''
    classdocs
    '''


    def __init__(self, parent, project, clause, option):
        '''
        Constructor
        '''
        super(EditLinksDialog, self).__init__(parent)
        self.project = project
        self.clause = clause
        self.option = option
        self.ui = Ui_EditLinksDialog()
        self.ui.setupUi(self)
        model = EditLinksModel(clause, option)
        self.ui.linksView.setModel(model)
        self.ui.addLinkButton.clicked.connect(self.addLink)
        self.removeAction = QAction('Remover', self)
        self.removeAction.setShortcut('Delete')
        self.removeAction.triggered.connect(lambda : model.removeLink(self.ui.linksView.currentIndex()))
        self.ui.removeLinkButton.setDefaultAction(self.removeAction)
    
    def addLink(self):
        addLinkDialog = AddLinkDialog(self, self.project, self.clause, self.option)
        if (addLinkDialog.exec_()):
            clause = addLinkDialog.getClause()
            link = Link()
            if (self.option=="uplinks") :
                link.parent = clause
                link.parent_id = clause.getID()
                link.child = self.clause
                link.child_id = self.clause.getID()
                link.addParent(clause.getID(), clause)
                link.addChild(self.clause.getID(), self.clause)
            elif (self.option=="downlinks") :
                link.child = clause
                link.child_id = clause.getID()
                link.parent = self.clause
                link.parent_id = self.clause.getID()
                link.addChild(clause.getID(), clause)
                link.addParent(self.clause.getID(), self.clause)
            model = EditLinksModel(self.clause, self.option)
            self.ui.linksView.setModel(model)
        
