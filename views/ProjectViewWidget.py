import sys
from UI import Ui_ProjectView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project

class ProjectViewWidget(QWidget):
    def __init__(self,  parent,  project = None):
        super(ProjectViewWidget, self).__init__()
        self.parent = parent
        self.ui = Ui_ProjectView.Ui_projectViewWidget()
        self.ui.setupUi(self.parent)
        self.ui.documentsListWidget.itemActivated.connect(self.parent.openSelect)
        if (project is not None) :
            self.loadProject(project)
    
    def loadProject(self,  project):
        documentsList = project.getDocumentsList()
        widgetList = []
        for documentName in documentsList :
            documentWidgetItem = QTreeWidgetItem()
            documentWidgetItem.setText(0,  documentName)
            widgetList += [documentWidgetItem]
            document = project.getDocument(documentName)
            clausesList = document.getClausesList()
            for clauseId in clausesList :
                clauseWidgetItem = QTreeWidgetItem(documentWidgetItem)
                clause = document.getClause(clauseId)
                clauseWidgetItem.setText(0,  clause.getTitle())
                widgetList += [clauseWidgetItem]
        self.ui.documentsListWidget.addTopLevelItems(widgetList)
