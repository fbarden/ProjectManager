import sys
from UI import Ui_ProjectView, Ui_DocumentView, Ui_ClauseView
from ProjectViewWidget import ProjectViewWidget
#from DocumentViewWidget import DocumentViewWidget
from ClauseViewWidget import ClauseViewWidget
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CentralWidget(QWidget):
    def __init__(self,  parent):
        super(CentralWidget, self).__init__(parent)
        self.parent = parent
#        parent.setCentralWidget(self)
        self.currentWidget = None
        
    def openProjectWidget(self, project) :
        projectViewWidget = ProjectViewWidget(None, project)
        self.currentWidget = projectViewWidget
        projectViewWidget.show()
    
#    def openDocumentWidget(self, document):
#        documentViewWidget = DocumentViewWidget(self, document)
#        documentViewWidget.show()
#    
    def openClauseWidget(self, clause):
        clauseViewWidget = ClauseViewWidget(self, clause)
        self.currentWidget = clauseViewWidget
        clauseViewWidget.show()
    
    def openSelect(self, selectedItem, column):
#        print "CHega!"
        if (selectedItem.parent() is None) :
#            print "Eh documento "
            print selectedItem.text(0)
            self.openDocumentWidget(selectedItem.text(0))
        else :
#            print "Eh clausula "
            self.openClauseWidget(selectedItem.text(0))
            
