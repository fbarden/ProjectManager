# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fbarden/Documents/ProjectManager/views/UI/ClauseView_v2.ui'
#
# Created: Tue May 28 02:22:41 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1036, 677)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.toolButton = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.toolButton_4 = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton_5 = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout.addWidget(self.toolButton_5)
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.toolButton_3 = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.label_2 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.treeWidget = QtGui.QTreeWidget(self.tab)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fontComboBox = QtGui.QFontComboBox(self.tab)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.toolButton1 = QtGui.QToolButton(self.tab)
        self.toolButton1.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton1.setObjectName(_fromUtf8("toolButton1"))
        self.horizontalLayout_4.addWidget(self.toolButton1)
        self.toolButton_6 = QtGui.QToolButton(self.tab)
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.horizontalLayout_4.addWidget(self.toolButton_6)
        self.toolButton_7 = QtGui.QToolButton(self.tab)
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_4.addWidget(self.toolButton_7)
        self.kcolorcombo = KColorCombo(self.tab)
        self.kcolorcombo.setObjectName(_fromUtf8("kcolorcombo"))
        self.horizontalLayout_4.addWidget(self.kcolorcombo)
        self.toolButton_8 = QtGui.QToolButton(self.tab)
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_4.addWidget(self.toolButton_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.treeWidget_2 = QtGui.QTreeWidget(self.tab)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        self.verticalLayout_2.addWidget(self.treeWidget_2)
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Dialog", "<--", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Dialog", "<]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Documento: Título da Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("Dialog", "î", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_5.setText(QtGui.QApplication.translate("Dialog", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("Dialog", "-->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Uplinks", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton1.setText(QtGui.QApplication.translate("Dialog", "Negrito", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_6.setText(QtGui.QApplication.translate("Dialog", "Itálico", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_7.setText(QtGui.QApplication.translate("Dialog", "Sublinhado", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_8.setText(QtGui.QApplication.translate("Dialog", "Imagem", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Downlinks", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Histórico", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "Documentos Relacionados", None, QtGui.QApplication.UnicodeUTF8))

from kcolorcombo import KColorCombo

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

