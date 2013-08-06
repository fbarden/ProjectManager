'''
Created on Jul 27, 2013

@author: fbarden
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TIMModel(QStandardItemModel):
    
    def __init__(self, TIM):
        super(TIMModel, self).__init__()
        self.TIM = TIM
        invisibleRoot = self.invisibleRootItem()
        rootsList = TIM.getRootsList()
        for root in rootsList :
            invisibleRoot.appendRow(self.prepareType(root))

    def prepareType(self, typeName):
        typeItem = QStandardItem(typeName)
        type = self.TIM.getType(typeName)
        typeItem.setData(type, Qt.UserRole)
        childTypeList = type.getPossibleChildrenList()
        for child in childTypeList:
            typeItem.appendRow(self.prepareType(child))
        typeItem.setFlags(typeItem.flags() & ~ Qt.ItemIsEditable)
        return typeItem