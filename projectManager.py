from views.MainWindow import MainWindow
import os, sys
from PyQt4.QtGui import QApplication

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 

globalProject = None

app = QApplication(sys.argv)
f = MainWindow()
f.showMaximized()
app.exec_()
