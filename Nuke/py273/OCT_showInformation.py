# *-* coding: utf-8 *-*
import nuke
import os
import OCT_newMergCamTool_YH
import pyseq

OCTV_DIR="//octvision.com//cg"

doSetUps = OCT_newMergCamTool_YH.newMergeCam()
class OCT_ReformatTexts():
    def __init__(self):
        self.panleResult=''
        self.selectedNode = ''
     
    def createNode(self, option, type):
        if type == 2:
            withNodeReformat = self.selectedNode['width'].value()
            heightNodeReformat = self.selectedNode['height'].value()

        nodeText = nuke.nodes.Text2()
        if type == 2:
            nodeText['box'].setValue(withNodeReformat*0.5*float(option))
            nodeText['font_size'].setValue(heightNodeReformat/10)
        nodeText['message'].setValue('[frame]')

        nodeReformat = nuke.nodes.Reformat()
        nodeReformat.setInput(0, self.selectedNode)
        nodeReformat['type'].setValue('scale')
        nodeReformat['scale'].setValue(float(option))

        nodeText.setInput(0,nodeReformat)

        self.nodeWrite = nuke.nodes.Write()
        self.nodeWrite.setInput(0,nodeText)
        self.nodeWrite['channels'].setValue("rgb")
        self.nodeWrite['file_type'].setValue('png')

    def checkSequece(self):
        self.fileName = nuke.root().knob("name").value() 
        if not self.fileName:
            nuke.message('\xe8\xaf\xb7\xe5\x85\x88\xe4\xbf\x9d\xe5\xad\x98nuke\xe6\x96\x87\xe4\xbb\xb6\xef\xbc\x81')
            return

        self.selectedNode = nuke.selectedNodes()[0]
        if self.selectedNode:
            p=nuke.Panel('reformatTextUI')
            p.addSingleLineInput('scale:','0.5')
            p.addButton('Cancel')
            p.addButton('OK')
            p.setWidth(10)

            self.panleResult=p.show()
            if self.panleResult:
                option = p.value('scale:')
                if option:
                    self.createNode(option, 1)
                    myDir = os.path.dirname(self.fileName)
                    myDir = os.path.join(myDir, r"check")
                    myDir = myDir.replace('\\', '/')
                    if not os.path.isdir(myDir):
                        os.makedirs(myDir)
                    WriteFile = myDir + "/check.%04d.png"

                    self.nodeWrite['file'].setValue(WriteFile)

    def reformatText(self,model):
        
        if model==1:
            doSetUps.mergeSelectCamUI(1)
            self.selectedNode = nuke.selectedNodes('ContactSheet')[0]
            _source = nuke.selectedNodes('Read')

        elif model==2:
            self.selectedNode = nuke.selectedNodes('ContactSheet')[0]
            _source = nuke.selectedNodes('Read')

        if self.selectedNode:
            p=nuke.Panel('reformatTextUI')
            p.addSingleLineInput('scale:','0.5')
            p.addButton('Cancel')
            p.addButton('OK')
            p.setWidth(10)

            self.panleResult=p.show()
            if self.panleResult:
                option = p.value('scale:')
                if option:
                    self.createNode(option, 2)
                    myfileName = _source[0]['file'].value()
                   
                    myFiledirName = os.path.dirname(myfileName)
                    getSequences = pyseq.getSequences(myFiledirName)[0]
                    getStartFrame = getSequences[0]._get_filename().split(".")[1]
                    getLastFrame = getSequences[-1]._get_filename().split(".")[1]

                    myFileN=myfileName.split("/")
                    dirName="/".join(myFileN[0:-2])
                    myDir=dirName+"/check"
                    if not os.path.isdir(myDir):
                        os.makedirs(myDir)

                    WriteFile=myDir+"/check.%04d.png"
                    self.nodeWrite['file'].setValue(WriteFile)

                    nuke.scriptSaveAs(dirName+"/check_%s_(%s-%s).nk"%(myFileN[-3],getStartFrame,getLastFrame))
                    return 1
            else:
                return ""


#OCT_ReformatTexts().reformatText()

#OCT_ReformatTexts().checkSequece()
