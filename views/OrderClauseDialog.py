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
        self.ui.moveUpButton.clicked.connect(self.moveUpClause)
        self.ui.moveDownButton.clicked.connect(self.moveDownClause)
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
        index = self.ui.clausesListWidget.currentRow()
        newIndex = index + step
        if ((newIndex < 0) or (newIndex > self.ui.clausesListWidget.count())):
            return
        clauseID = self.item2Clause[selectedItem].getID()
        self.document.moveClause(clauseID, step)
        self.ui.clausesListWidget.takeItem(index)
        self.ui.clausesListWidget.insertItem(newIndex, selectedItem)