#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *
from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem
from project import Project

class DocumentsDiagramScene(QGraphicsScene):

    def __init__(self,  parent, project=None):
        super(DocumentsDiagramScene, self).__init__(parent)
        self.project = project
        self.updateDocsImage()

    def updateDocsImage(self):
        docsList = self.project.getDocument2ClausesDict()
        docLinks = {}
        doc2NodeDict = {}
        if (len(docsList) == 0):
            return 
        self.radius = 180
        offset = 0
        step = 360/len(docsList)
        for docName in docsList.keys() :
            doc2NodeDict[docName] = self.drawDocNode(docName, 180 - offset*step)
            offset += 1
        for docName in docsList.keys():
            document = self.project.getDocument(docName)
            for clauseName in docsList[docName]:
                clause = document.getClause(clauseName)
                linksDoc2Clause = clause.getChildLinksDoc2Clause()
                if docName in docLinks.keys() :
                    docLinks[docName] += linksDoc2Clause.keys()
                else :
                    docLinks[docName] = linksDoc2Clause.keys()
        for docName in docLinks.keys():
            docParam = {}
            docNode = doc2NodeDict[docName]
            docParam['node'] = docNode
            for linkName in docLinks[docName]:
                if linkName != docName :
                    linkParam = {}
                    linkNode = doc2NodeDict[linkName]
                    linkParam['node'] = linkNode
                    linkParam['arrow'] = True
                    line = LineGraphicItem(docParam, linkParam)
                    self.addItem(line)
                

    def drawDocNode(self, nodeName, degree):
        node = self.project.getDocument(nodeName)
        nodeItem = NodeGraphicItem(50, 75)
        nodeItem.setText("")
        nodeItem.setTitle(node.getTitle())
        nodeItem.rotate(degree)
        nodeItem.translate(self.radius, 0)
        nodeItem.rotate(-degree)
        self.addItem(nodeItem)
        return nodeItem
