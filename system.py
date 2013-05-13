import os

def class System :
    def loadFile(self, filename) :
        with open(filename, 'r') as f :
            content f.read()
        return content
        
    def saveFile(self, filename, content):
        with open(filename,  'w') as f
            f.write(content)
