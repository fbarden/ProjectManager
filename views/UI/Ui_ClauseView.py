# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fbarden/Documents/ProjectManager/views/UI/ClauseView.ui'
#
# Created: Sat Jun  1 13:24:03 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_clauseViewWidget(object):
    def setupUi(self, clauseViewWidget):
        clauseViewWidget.setObjectName(_fromUtf8("clauseViewWidget"))
        clauseViewWidget.resize(1025, 713)
        self.verticalLayout_4 = QtGui.QVBoxLayout(clauseViewWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previousButton = QtGui.QToolButton(clauseViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.horizontalLayout.addWidget(self.previousButton)
        self.line_2 = QtGui.QFrame(clauseViewWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.returnButton = QtGui.QToolButton(clauseViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnButton.sizePolicy().hasHeightForWidth())
        self.returnButton.setSizePolicy(sizePolicy)
        self.returnButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.returnButton.setObjectName(_fromUtf8("returnButton"))
        self.horizontalLayout.addWidget(self.returnButton)
        self.titleLabel = QtGui.QLabel(clauseViewWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.horizontalLayout.addWidget(self.titleLabel)
        self.upButton = QtGui.QToolButton(clauseViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMaximumSize(QtCore.QSize(50, 50))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.horizontalLayout.addWidget(self.upButton)
        self.deleteButton = QtGui.QToolButton(clauseViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.line_3 = QtGui.QFrame(clauseViewWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.nextButton = QtGui.QToolButton(clauseViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(clauseViewWidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.editTab = QtGui.QWidget()
        self.editTab.setObjectName(_fromUtf8("editTab"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.editTab)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.uplinksLayout = QtGui.QVBoxLayout()
        self.uplinksLayout.setObjectName(_fromUtf8("uplinksLayout"))
        self.line = QtGui.QFrame(self.editTab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.uplinksLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.showUplinksCheckBox = QtGui.QCheckBox(self.editTab)
        self.showUplinksCheckBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showUplinksCheckBox.sizePolicy().hasHeightForWidth())
        self.showUplinksCheckBox.setSizePolicy(sizePolicy)
        self.showUplinksCheckBox.setText(_fromUtf8(""))
        self.showUplinksCheckBox.setChecked(True)
        self.showUplinksCheckBox.setObjectName(_fromUtf8("showUplinksCheckBox"))
        self.horizontalLayout_2.addWidget(self.showUplinksCheckBox)
        self.uplinksLabel = QtGui.QLabel(self.editTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uplinksLabel.sizePolicy().hasHeightForWidth())
        self.uplinksLabel.setSizePolicy(sizePolicy)
        self.uplinksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uplinksLabel.setObjectName(_fromUtf8("uplinksLabel"))
        self.horizontalLayout_2.addWidget(self.uplinksLabel)
        self.uplinksLayout.addLayout(self.horizontalLayout_2)
        self.uplinksTreeWidget = QtGui.QTreeWidget(self.editTab)
        self.uplinksTreeWidget.setObjectName(_fromUtf8("uplinksTreeWidget"))
        self.uplinksTreeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.uplinksLayout.addWidget(self.uplinksTreeWidget)
        self.horizontalLayout_6.addLayout(self.uplinksLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fontComboBox = QtGui.QFontComboBox(self.editTab)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        self.fontSizeComboBox = QtGui.QComboBox(self.editTab)
        self.fontSizeComboBox.setObjectName(_fromUtf8("fontSizeComboBox"))
        self.horizontalLayout_4.addWidget(self.fontSizeComboBox)
        self.boldButton = QtGui.QToolButton(self.editTab)
        self.boldButton.setArrowType(QtCore.Qt.NoArrow)
        self.boldButton.setObjectName(_fromUtf8("boldButton"))
        self.horizontalLayout_4.addWidget(self.boldButton)
        self.italicButton = QtGui.QToolButton(self.editTab)
        self.italicButton.setObjectName(_fromUtf8("italicButton"))
        self.horizontalLayout_4.addWidget(self.italicButton)
        self.underlineButton = QtGui.QToolButton(self.editTab)
        self.underlineButton.setObjectName(_fromUtf8("underlineButton"))
        self.horizontalLayout_4.addWidget(self.underlineButton)
        self.imageButton = QtGui.QToolButton(self.editTab)
        self.imageButton.setObjectName(_fromUtf8("imageButton"))
        self.horizontalLayout_4.addWidget(self.imageButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.titleEdit = QtGui.QLineEdit(self.editTab)
        self.titleEdit.setEnabled(False)
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        self.horizontalLayout_5.addWidget(self.titleEdit)
        self.titleCheckBox = QtGui.QCheckBox(self.editTab)
        self.titleCheckBox.setObjectName(_fromUtf8("titleCheckBox"))
        self.horizontalLayout_5.addWidget(self.titleCheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.textEdit = QtGui.QTextEdit(self.editTab)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.downlinksLayout = QtGui.QVBoxLayout()
        self.downlinksLayout.setObjectName(_fromUtf8("downlinksLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.downlinksCheckBox = QtGui.QCheckBox(self.editTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downlinksCheckBox.sizePolicy().hasHeightForWidth())
        self.downlinksCheckBox.setSizePolicy(sizePolicy)
        self.downlinksCheckBox.setText(_fromUtf8(""))
        self.downlinksCheckBox.setChecked(True)
        self.downlinksCheckBox.setObjectName(_fromUtf8("downlinksCheckBox"))
        self.horizontalLayout_3.addWidget(self.downlinksCheckBox)
        self.downlinksLabel = QtGui.QLabel(self.editTab)
        self.downlinksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.downlinksLabel.setObjectName(_fromUtf8("downlinksLabel"))
        self.horizontalLayout_3.addWidget(self.downlinksLabel)
        self.downlinksLayout.addLayout(self.horizontalLayout_3)
        self.downlinksTreeWidget = QtGui.QTreeWidget(self.editTab)
        self.downlinksTreeWidget.setObjectName(_fromUtf8("downlinksTreeWidget"))
        self.downlinksTreeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.downlinksLayout.addWidget(self.downlinksTreeWidget)
        self.editDownlinksButton = QtGui.QPushButton(self.editTab)
        self.editDownlinksButton.setObjectName(_fromUtf8("editDownlinksButton"))
        self.downlinksLayout.addWidget(self.editDownlinksButton)
        self.horizontalLayout_6.addLayout(self.downlinksLayout)
        self.tabWidget.addTab(self.editTab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(clauseViewWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.titleCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.titleEdit.setEnabled)
        QtCore.QObject.connect(self.showUplinksCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.uplinksTreeWidget.setVisible)
        QtCore.QObject.connect(self.showUplinksCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.uplinksLabel.setVisible)
        QtCore.QMetaObject.connectSlotsByName(clauseViewWidget)

    def retranslateUi(self, clauseViewWidget):
        clauseViewWidget.setWindowTitle(QtGui.QApplication.translate("clauseViewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("clauseViewWidget", "<--", None, QtGui.QApplication.UnicodeUTF8))
        self.returnButton.setText(QtGui.QApplication.translate("clauseViewWidget", "<]", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("clauseViewWidget", "Documento: Título da Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setText(QtGui.QApplication.translate("clauseViewWidget", "î", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("clauseViewWidget", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("clauseViewWidget", "-->", None, QtGui.QApplication.UnicodeUTF8))
        self.uplinksLabel.setText(QtGui.QApplication.translate("clauseViewWidget", "Uplinks", None, QtGui.QApplication.UnicodeUTF8))
        self.boldButton.setText(QtGui.QApplication.translate("clauseViewWidget", "Negrito", None, QtGui.QApplication.UnicodeUTF8))
        self.italicButton.setText(QtGui.QApplication.translate("clauseViewWidget", "Itálico", None, QtGui.QApplication.UnicodeUTF8))
        self.underlineButton.setText(QtGui.QApplication.translate("clauseViewWidget", "Sublinhado", None, QtGui.QApplication.UnicodeUTF8))
        self.imageButton.setText(QtGui.QApplication.translate("clauseViewWidget", "Imagem", None, QtGui.QApplication.UnicodeUTF8))
        self.titleEdit.setText(QtGui.QApplication.translate("clauseViewWidget", "Título da Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.titleCheckBox.setText(QtGui.QApplication.translate("clauseViewWidget", "Alt. Título", None, QtGui.QApplication.UnicodeUTF8))
        self.downlinksLabel.setText(QtGui.QApplication.translate("clauseViewWidget", "Downlinks", None, QtGui.QApplication.UnicodeUTF8))
        self.editDownlinksButton.setText(QtGui.QApplication.translate("clauseViewWidget", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTab), QtGui.QApplication.translate("clauseViewWidget", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("clauseViewWidget", "Histórico", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("clauseViewWidget", "Documentos Relacionados", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    clauseViewWidget = QtGui.QWidget()
    ui = Ui_clauseViewWidget()
    ui.setupUi(clauseViewWidget)
    clauseViewWidget.show()
    sys.exit(app.exec_())

