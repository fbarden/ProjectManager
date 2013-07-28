from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI import Ui_OrderClausesDialog

class OrderClauseDialog(QDialog):
    
    reloadDocumentSignal = pyqtSignal()

    def __init__(self, parent, document):
        super(OrderClauseDialog, self).__init__(parent)
        self.ui = Ui_OrderClausesDialog.Ui_OrderClausesDialog()
        self.ui.setupUi(self)
        self.item2Clause = {}
        self.document = document
        actionsList = []
        self.moveUpClauseAction = QAction(self.ui.clausesListWidget)
        self.moveUpClauseAction.triggered.connect(self.moveUpClause)
        self.moveUpClauseAction.setShortcut('Alt+Up')
        actionsList.append(self.moveUpClauseAction)
        self.ui.moveUpButton.clicked.connect(self.moveUpClause)
        self.moveDownClauseAction = QAction(self.ui.clausesListWidget)
        self.moveDownClauseAction.triggered.connect(self.moveDownClause)
        self.moveDownClauseAction.setShortcut('Alt+Down')
        actionsList.append(self.moveDownClauseAction)
        self.ui.moveDownButton.clicked.connect(self.moveDownClause)
        self.deleteClauseAction = QAction(self.ui.clausesListWidget)
        self.deleteClauseAction.triggered.connect(self.deleteClause)
        self.deleteClauseAction.setShortcut('Delete')
        actionsList.append(self.deleteClauseAction)
        self.ui.deleteButton.clicked.connect(self.deleteClause)
        self.ui.clausesListWidget.addActions(actionsList)
        self.loadClauses()
        
    def loadClauses(self):
        clausesList = self.document.getClausesList()
        for clauseID in clausesList:
            clause = self.document.getClause(clauseID)
            item = QListWidgetItem(clause.getTitle(), self.ui.clausesListWidget)
            self.item2Clause[item] = clause

    def moveUpClause(self):
        self.moveClause(-1)
    
    def moveDownClause(self):
        self.moveClause(1)

    def moveClause(self, step):
        selectedItem = self.ui.clausesListWidget.selectedItems()[0]
        index = self.ui.clausesListWidget.row(selectedItem)
        newIndex = index + step
        if ((newIndex < 0) or (newIndex > self.ui.clausesListWidget.count())):
            return
        clauseID = self.item2Clause[selectedItem].getID()
        self.document.moveClause(clauseID, step)
        self.ui.clausesListWidget.takeItem(index)
        self.ui.clausesListWidget.insertItem(newIndex, selectedItem)
        print "Inserindo na posicao " + str(newIndex)
        auxItem = self.ui.clausesListWidget.selectedItems()
        if auxItem != [] :
            auxItem[0].setSelected(False)
        selectedItem.setSelected(True)
    
    def deleteClause(self):
        selectedItem = self.ui.clausesListWidget.selectedItems()[0]
        clauseID = self.item2Clause[selectedItem].getID()
        self.document.removeClause(clauseID)
        index = self.ui.clausesListWidget.row(selectedItem)
        self.ui.clausesListWidget.takeItem(index)