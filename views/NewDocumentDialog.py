#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_NewDocumentDialog

from project import Project
from document import Document

class NewDocumentDialog(QDialog):
    
    openElementSignal = pyqtSignal(str)
    
    def __init__(self,  parent,  project, document=None):
        super(NewDocumentDialog, self).__init__(parent)
        self.project = project
        self.document = document
        self.ui = Ui_NewDocumentDialog.Ui_NewDocumentDialog()
        self.ui.setupUi(self)
        self.accepted.connect(self.setDocument)
    
    def setDocument(self):
        title = unicode(self.ui.titleEdit.text())
        prefix = unicode(self.ui.prefixEdit.text())
        name = unicode(self.ui.nameEdit.text())
        if (self.document is None):
            self.document = Document()
        self.document.setTitle(title)
        self.document.setPrefix(prefix)
        self.document.setName(name)
        self.project.addDocument(self.document)
        self.document.setProject(self.project)
        self.openElementSignal.emit("document:" + self.document.getName())
