#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
Created on Aug 19, 2013

@author: fbarden
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EditLinksModel(QStandardItemModel):
    '''
    classdocs
    '''


    def __init__(self, clause, option):
        '''
        Constructor
        '''
        super(EditLinksModel, self).__init__()
        self.clause = clause
        self.option = option
        root = self.invisibleRootItem()
        if option == "uplinks" :
            linksList = clause.getParentLinksList()
            for link in linksList :
                parent = link.getParent()
                parentItem = QStandardItem(parent.getDocument().getName() + ":" + parent.getTitle())
                parentItem.setData(parent, Qt.UserRole)
                parentItem.setData(link, Qt.UserRole + 1)
                parentItem.setFlags(parentItem.flags() & ~ Qt.ItemIsEditable)
                root.appendRow(parentItem)
        elif (option == 'downlinks'):
            linksList = clause.getChildLinksList()
            for link in linksList :
                child = link.getChild()
                childItem = QStandardItem(child.getDocument().getName() + ":" + child.getTitle())
                childItem.setData(child, Qt.UserRole)
                childItem.setData(link, Qt.UserRole + 1)
                childItem.setFlags(childItem.flags() & ~ Qt.ItemIsEditable)
                root.appendRow(childItem)

    def removeLink(self, index):
        link = index.data(Qt.UserRole + 1).toPyObject()
        link.remove()
        self.removeRow(index.row())
