from UI import Ui_NewProjectDialog
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *
from project import Project
from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem
from TIMDiagramScene import TIMDiagramScene

from AddTypeDialog import AddTypeDialog

class NewProjectDialog(QWizard):
    
    openProjectSignal = pyqtSignal()
    
    def __init__(self,  parent,  project=None):
        super(NewProjectDialog, self).__init__(parent)
        self.project = project
        self.parent = parent
        self.TIM = TIM()
        self.ui = Ui_NewProjectDialog.Ui_NewProjectDialog()
        self.ui.setupUi(self)
        self.setButtonText(QWizard.BackButton,  "Anterior")
        self.setButtonText(QWizard.NextButton,  "Proximo")
        self.setButtonText(QWizard.CancelButton,  "Cancelar")
        self.setButtonText(QWizard.FinishButton,  "Finalizar")
        self.ui.wizardPage1.registerField("projectName*",  self.ui.projectNameEdit)
        self.ui.wizardPage1.registerField("locationName*",  self.ui.folderEdit)
        self.accepted.connect(self.setProject)
        self.currentIdChanged.connect(self.updatePages)
        self.ui.TIMTreeWidget.itemActivated.connect(self.typeTreeAction)
        self.ui.searchButton.clicked.connect(self.openSearchFolder)
        self.scene = TIMDiagramScene(self.ui.graphicsView, self.TIM)    
        self.ui.graphicsView.setScene(self.scene)

    def openSearchFolder(self):
        location = QFileDialog.getExistingDirectory(\
            None,
            self.trUtf8("Diretorio do projeto"),
            self.trUtf8("."),
            QFileDialog.Options(QFileDialog.ShowDirsOnly))
        if (location != ""):
            self.ui.folderEdit.setText(location)

    def typeTreeAction(self, item):
        if (item.text(0) == "<adicionar tipo>") :
            addTypeDialog = AddTypeDialog(self, self.TIM, item)
            addTypeDialog.show()
            addTypeDialog.addTypeSignal.connect(self.updateTIMTree)

    def setProject(self):
        if (self.project is None) :
            self.project = None
        self.project.setName(str(self.ui.projectNameEdit.text()))
        self.project.setLocation(os.path.normpath(str(self.ui.folderEdit.text())) + '/')
        self.project.TIM = self.TIM
        self.parent.project = self.project
        self.openProjectSignal.emit()

    def updatePages(self, page):
        if (page == 2):
            self.scene.updateTIMImage()

    def updateTIMTree(self):
        self.ui.TIMTreeWidget.clear()
        addItem = QTreeWidgetItem(self.ui.TIMTreeWidget)
        addItem.setText(0, "<adicionar tipo>")
        rootsList = self.TIM.getRootsList()
        for root in rootsList :
            self.printType(root, self.ui.TIMTreeWidget)

    def printType(self, typeName, parentItem):
        typeItem = QTreeWidgetItem(parentItem)
        typeItem.setText(0, typeName)
        type = self.TIM.getType(typeName)
        addItem = QTreeWidgetItem(typeItem)
        addItem.setText(0, "<adicionar tipo>")
        childTypeList = type.getPossibleChildrenList()
        for child in childTypeList:
            self.printType(child, typeItem)
