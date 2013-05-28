import sys
from UI import Ui_ClauseView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project

class ClauseViewWidget(QWidget):
    def __init__(self,  parent,  project = None):
        super(ClauseViewWidget, self).__init__()
        self.parent = parent
        self.ui = Ui_ClauseView.Ui_clauseViewWidget()
        self.ui.setupUi(self.parent)
