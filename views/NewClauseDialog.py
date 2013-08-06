from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_NewClauseDialog

from clause import Clause
from link import Link

class NewClauseDialog(QDialog):
    
    openElementSignal = pyqtSignal(str)
    
    def __init__(self,  parent,  project, document=None, parentClause=None):
        super(NewClauseDialog, self).__init__(parent)
        self.project = project
        self.document = document
        self.ui = Ui_NewClauseDialog.Ui_NewClauseDialog()
        self.ui.setupUi(self)
        documentList = self.project.getDocumentsList()
        self.ui.documentBox.addItems(documentList)
        if (self.document is not None):
            self.ui.documentBox.setCurrentIndex(self.ui.documentBox.findText(self.document.getName()))
        if (parentClause is not None):
            type = parentClause.getType()
            typeList = type.getPossibleChildrenList()
        else :
            typeList = self.project.getTIM().getTypesList()
        self.ui.typeBox.addItems(typeList)
        currentType = self.ui.typeBox.currentText()
        self.updateParentClauses()
        if (parentClause is not None):
            parentClauseName = parentClause.getID()
            self.ui.parentBox.setCurrentIndex(self.ui.parentBox.findText(parentClauseName))
        self.accepted.connect(self.setClause)
        self.ui.typeBox.currentIndexChanged.connect(self.updateParentClauses)

    def updateParentClauses(self):
        currentType = self.ui.typeBox.currentText()
        self.clausesList = {}
        self.ui.parentBox.clear()
        clausesDict = self.project.getAllClauses()
        type = self.project.getTIM().getType(unicode(currentType))
        parentTypeList = self.project.getTIM().getPossibleParentsList(type)
        for clauseID in clausesDict.keys():
            clause = clausesDict[clauseID]
            if self.isType(clause, parentTypeList):
                self.clausesList[(clause.getDocument().getName() + ": " + clause.getTitle())] = clauseID 
        self.ui.parentBox.addItems(self.clausesList.keys())
        if currentType in self.project.getTIM().getRootsList() :
            self.ui.parentBox.insertItem(0, "Sem Clausula Pai" )
        if (unicode(self.ui.parentBox.currentText()) is ""):
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def isType(self, clause, typeList):
        if (clause.getType().getName() in typeList) :
            return True
        else :
            return False

    def setClause(self):
        title = unicode(self.ui.titleEdit.text())
        parent = unicode(self.ui.parentBox.currentText())
        self.clause = Clause()
        self.clause.setTitle(title)
        self.clause.setType(self.project.getTIM().getType(unicode(self.ui.typeBox.currentText())))
        self.document = self.project.getDocument(unicode(self.ui.documentBox.currentText()))
        self.document.addClause(self.clause)
        if (parent != "Sem Clausula Pai") :
            parentClause = self.clausesList[unicode(self.ui.parentBox.currentText())]
            link = Link()
            link.addChild(self.clause.getID())
            link.addParent(parentClause)
            link.consolidateLink(self.project)
        self.openElementSignal.emit("clause:" + self.clause.getID())
