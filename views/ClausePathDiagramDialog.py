
from UI import Ui_DiagramDialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from views.ClauseDiagramScene import ClauseDiagramScene

class ClausePathDiagramDialog(QDialog):

    def __init__(self, parent = None, clause = None):
        super(ClausePathDiagramDialog, self).__init__(parent)
        self.ui = Ui_DiagramDialog.Ui_DiagramDialog()
        self.ui.setupUi(self)
        diagramScene = ClauseDiagramScene(self.ui.graphicsView, clause)
        self.ui.graphicsView.setScene(diagramScene)