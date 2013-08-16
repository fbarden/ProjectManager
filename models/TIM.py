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
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["Tipo", "Card. Descendente", "Dep. Descendente", "Card. Ascendente", "Dep. Ascendente"])
        invisibleRoot = self.invisibleRootItem()
        rootsList = TIM.getRootsList()
        for rootName in rootsList :
            root = self.TIM.getType(rootName)
            invisibleRoot.appendRow(self.prepareType(root, None))

    def prepareType(self, type, parent):
        print "Preparing type " + type.getName()
        typeName = type.getName()
        typeItem = QStandardItem(typeName)
        typeItem.setData(type, Qt.UserRole)
        parentCardinality = "---"
        parentDependency = "---"
        childCardinality = "---"
        childDependency = "---"
        
        if (parent != None) :
            parentCardinality = parent.getChildMinCard(typeName) + " .. " + parent.getChildMaxCard(typeName)
            if (parent.isDependentOf(typeName)) :
                parentDependency = "Sim"
            else :
                parentDependency = "Nao"
            parentName = parent.getName()
            childCardinality = type.getParentMinCard(parentName) + " .. " + type.getParentMaxCard(parentName)
            if (type.isDependentOf(parentName)) :
                childDependency = "Sim"
            else :
                childDependency = "Nao"
        childTypeList = type.getPossibleChildrenList()
        for childName in childTypeList:
            child = self.TIM.getType(childName)
            typeItem.appendRow(self.prepareType(child, type))
        typeItem.setFlags(typeItem.flags() & ~ Qt.ItemIsEditable)
        parentCardItem = QStandardItem(parentCardinality)
        parentDepItem = QStandardItem(parentDependency)
        parentDepItem.setFlags(parentDepItem.flags() & ~ Qt.ItemIsEditable)
        childCardItem = QStandardItem(childCardinality)
        childCardItem.setFlags(childCardItem.flags() & ~ Qt.ItemIsEditable)
        childDepItem = QStandardItem(childDependency)
        childDepItem.setFlags(childDepItem.flags() & ~ Qt.ItemIsEditable)
        return [typeItem, childCardItem, childDepItem, parentCardItem, parentDepItem]