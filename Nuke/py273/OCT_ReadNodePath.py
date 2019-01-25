# -*- coding: utf-8 -*-
import nuke
import os
class  myFindFrame():
    def __init__(self):
        self.panelResult = ''
        self.allReadPaths = []

    def myFindPanel(self):
        self.fileName = nuke.root().knob("name").value() 
        if not self.fileName:
            nuke.message('\xe8\xaf\xb7\xe5\x85\x88\xe4\xbf\x9d\xe5\xad\x98nuke\xe6\x96\x87\xe4\xbb\xb6\xef\xbc\x81')
            return

        i = 1
        p = nuke.Panel('input save txt path')
        p.setWidth(250)
        p.addSingleLineInput('Input Path', '')  
        p.addButton('Cancel')
        p.addButton('OK')
        self.panleResult = p.show() 
        path = p.value('Input Path') 
        self.readPath(path)

    def readPath(self, inPath):
        if not os.path.isdir(inPath):
            os.makedirs(inPath)
        self.myReads = nuke.selectedNodes('Read')
        if len(self.myReads) == 0:
            self.myReads= nuke.allNodes('Read')
        if self.myReads:
            for eachRead in self.myReads:
                readFilePath = eachRead['file'].value()
                readFileDir = os.path.dirname(readFilePath)
                if not readFileDir in self.allReadPaths:
                    self.allReadPaths.append(readFileDir)

        txtName = os.path.basename(self.fileName)
        txtName = txtName.replace('nk', 'txt')
        txtPath = os.path.join(inPath, txtName)
        f = open(txtPath, 'wt') 
        if self.allReadPaths:
            for eachPath in self.allReadPaths:
                try:
                    f.write(eachPath+'\n')
                except:
                    print "read Path error"
                
        f.close()

# myFindFrame().myFindPanel()