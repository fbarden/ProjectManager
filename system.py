import os

class System :
    def loadFile(self, filename) :
        content = ""
        with open(filename, 'r') as f :
            content = f.read()
        return content
        
    def saveFile(self, filename, content):
        with open(filename,  'w') as f
            f.write(content)

    def openBrowser(self,  filetype,  initialPath):
        fileNames = QtGui.QFileDialog.getOpenFileNames(parent, ("Open File"),paths.get_testcases_path(),("All Files (pd*.txt)"));
