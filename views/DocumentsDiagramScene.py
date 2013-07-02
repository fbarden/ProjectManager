
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
        print "Vai pro update!"
        rootsList = self.project.getDocumentsList()
        print rootsList
        
        if (len(rootsList) == 0):
            print "Retornou sem nada"
            return 
        self.radius = 180
        offset = 0
        step = 360/len(rootsList)
        for rootName in rootsList :
            self.drawDocNode(rootName, 180 - offset*step)
            print "Criou nodo"
            offset += 1

    def drawDocNode(self, nodeName, degree):
        print "DOCNODE"
        node = self.project.getDocument(nodeName)
        nodeItem = NodeGraphicItem(50, 75)
        nodeItem.setText("")
        #print node.getPrefix()
        nodeItem.setTitle(node.getName())
        print node.getName()
        nodeItem.rotate(degree)
        nodeItem.translate(self.radius, 0)
        nodeItem.rotate(-degree)
        self.addItem(nodeItem)
        return nodeItem
