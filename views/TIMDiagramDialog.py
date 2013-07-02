
from UI import Ui_TIMDiagramDialog



from PyQt4.QtGui import *
from PyQt4.QtCore import *
from views.TIMDiagramScene import TIMDiagramScene

class TIMDiagramDialog(QDialog):

    def __init__(self, parent = None, TIM= None):
        super(TIMDiagramDialog, self).__init__(parent)
        self.ui = Ui_TIMDiagramDialog.Ui_TIMDiagramDialog()
        self.ui.setupUi(self)
        diagramScene = TIMDiagramScene(self.ui.graphicsView, TIM)
        self.ui.graphicsView.setScene(diagramScene)