import sys
from UI import Ui_ProjectView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project

class ProjectViewWidget(QWidget):

    openDocumentSignal = pyqtSignal(str);
    openClauseSignal = pyqtSignal(str, str);

    def __init__(self, project = None):
        super(ProjectViewWidget, self).__init__()
        self.ui = Ui_ProjectView.Ui_projectViewWidget()
        self.ui.setupUi(self)
        self.ui.documentsListWidget.itemActivated.connect(self.openSelect)
        self.clausesDict  = {}
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
                self.clausesDict[documentName + clause.getTitle()] = clause.getID()
                widgetList += [clauseWidgetItem]
        self.ui.documentsListWidget.addTopLevelItems(widgetList)

    def openSelect(self, selectedItem, column):
        if (selectedItem.parent() is None) :
            self.openDocumentSignal.emit(selectedItem.text(0))
        else :
            self.openClauseSignal.emit(selectedItem.parent().text(0),  self.clausesDict[str(selectedItem.parent().text(0) + selectedItem.text(0))])
