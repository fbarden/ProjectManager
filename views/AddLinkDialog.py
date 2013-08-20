#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
Created on Aug 19, 2013

@author: fbarden
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from views.UI.Ui_AddLinkDialog import Ui_AddLinkDialog
from numpy.core.setup_common import type2def

class AddLinkDialog(QDialog):
    '''
    classdocs
    '''


    def __init__(self, parent, project, clause, option):
        '''
        Constructor
        '''
        super(AddLinkDialog, self).__init__(parent)
        self.ui = Ui_AddLinkDialog()
        self.ui.setupUi(self)
        self.type2Clause = project.getType2Clauses()
        self.loadTypes(clause, option)
        self.ui.typeComboBox.currentIndexChanged.connect(self.loadClauses)
    
    def loadTypes(self, clause, option):
        linkTypesList = []
        if (option == "downlinks"):
            linkTypesList = clause.getType().getPossibleChildrenList()
        elif (option == "uplinks"):
            linkTypesList = clause.getType().getPossibleParentsList()
        self.ui.typeComboBox.addItems(linkTypesList)
        self.loadClauses()

    def loadClauses(self):
        self.ui.clauseComboBox.clear()
        currentType = unicode(self.ui.typeComboBox.currentText())
        if currentType != "" :
            for clause in self.type2Clause[currentType] :
                self.ui.clauseComboBox.addItem(clause.getDocument().getName() + ":" + clause.getTitle(), clause)
        okButton = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        okButton.setEnabled(self.ui.clauseComboBox.count() > 0)

    def getClause(self):
        index = self.ui.clauseComboBox.currentIndex()
        return self.ui.clauseComboBox.itemData(index).toPyObject()
