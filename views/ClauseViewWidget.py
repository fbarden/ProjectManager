import sys
from UI import Ui_ClauseView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project

class ClauseViewWidget(QWidget):
    def __init__(self, clause=None):
        super(ClauseViewWidget, self).__init__()
        self.clause = None
        self.ui = Ui_ClauseView.Ui_clauseViewWidget()
        self.ui.setupUi(self)
        if (clause is not None) :
            self.loadClause(clause)

    def loadClause(self,  clause):
        self.clause = clause
        self.loadTitle()
        self.loadText()
        self.loadUplinks()
        self.loadDownlinks()
        self.loadHistory()
        self.loadRelatedDocs()

    def loadText(self):
        self.ui.textEdit.setText(self.clause.getText())
    
    def loadTitle(self):
        self.ui.titleLabel.setText(self.clause.document + ": " + self.clause.getTitle())
        self.ui.titleEdit.setText(self.clause.getTitle())
    
    def loadUplinks(self):
        pass

    def loadDownlinks(self):
        pass

    def loadHistory(self):
        pass
   
    def loadRelatedDocs(self):
        
        pass
