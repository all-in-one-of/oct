# *-* coding: utf-8 *-*
import nuke
import os
import pyseq

class OCT_OutputMOV():
    def __init__(self):
        self.nodeWrites=""
        self.nodeContactSheet=""
        self.nodeReformat=""
        self.allSelectNode=""
        self.nukeName=""

    def OutputMOV(self):
        self.nodeWrites=nuke.selectedNodes('Write')
        self.nodeContactSheet=nuke.selectedNodes('ContactSheet')
        self.nodeReformat=nuke.selectedNodes('Reformat')
        self.allSelectNode=nuke.selectedNodes()
        #self.selectRead=nuke.selectedNodes('Read')

        if not self.nodeWrites:
            nuke.message('\xe6\xb2\xa1\xe6\x9c\x89\xe9\x80\x89\xe6\x8b\xa9write\xe8\x8a\x82\xe7\x82\xb9')
            return
        if not self.nodeContactSheet:
            nuke.message('\xe6\xb2\xa1\xe6\x9c\x89\xe9\x80\x89\xe6\x8b\xa9ContactSheet\xe8\x8a\x82\xe7\x82\xb9')
            return
        if not self.nodeReformat:
            nuke.message('\xe6\xb2\xa1\xe6\x9c\x89\xe9\x80\x89\xe6\x8b\xa9Reformat\xe8\x8a\x82\xe7\x82\xb9')
            return
        writeFile=self.nodeWrites[0]['file'].value()
        
        #输出的文件夹
        outPutDir=os.path.dirname(writeFile)
        all=pyseq.getSequences(outPutDir)
        if not all:
            nuke.message("write\xe8\x8a\x82\xe7\x82\xb9\xe6\xb2\xa1\xe6\x9c\x89\xe8\xbe\x93\xe5\x87\xba\xe7\xb4\xa0\xe6\x9d\x90")
            return
        dirNames=all[0].path()
        print dirNames
        dirName=pyseq.getSequences(dirNames)
        print dirName
        if dirName and dirName[0].length() == 1:
            createReadNode=nuke.nodes.Read()
            ReadPath=dirNames.replace("\\",'/')
            createReadNode['file'].setValue(ReadPath)
            createReadNode['origfirst'].setValue(1)
            createReadNode['origlast'].setValue(1)  
            createReadNode['first'].setValue(1)
            createReadNode['last'].setValue(1)  
            createReadNode['on_error'].setValue('cheeckerboard') 

            _w=self.nodeContactSheet[0]['width'].value()*self.nodeReformat[0]['scale'].value()
            _h=self.nodeContactSheet[0]['height'].value()*self.nodeReformat[0]['scale'].value()
            _width=int(_w)
            _height=int(_h)
            ReadOFormat = createReadNode['format'].value()
            Flag=True
            j=0
            if ReadOFormat.width()!=_width or ReadOFormat.height() != _height:
                allFormat = nuke.formats()
                for eachFormat in allFormat:
                    if eachFormat.width() == _width and eachFormat.height() == _height:
                        myFormat = eachFormat.name()
                        if myFormat != None:
                            createReadNode['format'].setValue(myFormat)
                            Flag = False
                            break
                if Flag:
                    #键的名字
                    mySize=""
                    while True:
                        mySize = ('my_Size%s' % j)
                        if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                            break
                        else:
                            j += 1
                    widthHeight = str(_width)+" "+str(_height)
                    square = widthHeight+" "+mySize
                    nuke.addFormat(square)
                    createReadNode['format'].setValue(mySize)

            createNodeWrite=nuke.nodes.Write()
            mydirName=writeFile.split("/")
            myFiledirName=os.path.dirname(writeFile)
            getSequences=pyseq.getSequences(myFiledirName)[0]
            getStartFrame=getSequences[0]._get_filename().split(".")[1]
            getLastFrame=getSequences[-1]._get_filename().split(".")[1]
            myWritePath='/'.join(mydirName[0:-2])+"/"+mydirName[-3]+"("+getStartFrame+"-"+getLastFrame+").mov"
            createNodeWrite['file'].setValue(myWritePath)
            createNodeWrite.setInput(0,createReadNode)
            
            createNodeWrite['file_type'].setValue('mov')
            createNodeWrite['meta_codec'].setValue('jpeg')
            createNodeWrite['mov64_quality_min'].setValue(10)
            createNodeWrite['mov64_quality_max'].setValue(10)

            self.nukeName='/'.join(mydirName[0:-2])+"/"+"mov_"+mydirName[-3]+"_("+getStartFrame+"-"+getLastFrame+").nk"
        else:
            createReadNode=nuke.nodes.Read()
            createReadNode['file'].setValue(writeFile)
            createReadNode['on_error'].setValue('cheeckerboard')
            _w=self.nodeContactSheet[0]['width'].value()*self.nodeReformat[0]['scale'].value()
            _h=self.nodeContactSheet[0]['height'].value()*self.nodeReformat[0]['scale'].value()
            _width=int(_w)
            _height=int(_h)
            ReadOFormat = createReadNode['format'].value()
            Flag=True
            j=0
            if ReadOFormat.width()!=_width or ReadOFormat.height() != _height:
                allFormat = nuke.formats()
                for eachFormat in allFormat:
                    if eachFormat.width() == _width and eachFormat.height() == _height:
                        myFormat = eachFormat.name()
                        if myFormat != None:
                            createReadNode['format'].setValue(myFormat)
                            Flag = False
                            break
                if Flag:
                    #键的名字
                    mySize=""
                    while True:
                        mySize = ('my_Size%s' % j)
                        if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                            break
                        else:
                            j += 1
                    widthHeight = str(_width)+" "+str(_height)
                    square = widthHeight+" "+mySize
                    nuke.addFormat(square)
                    createReadNode['format'].setValue(mySize)

            createNodeWrite=nuke.nodes.Write()

            mydirName=writeFile.split("/")

            myFiledirName=os.path.dirname(writeFile)
            getSequences=pyseq.getSequences(myFiledirName)[0]
            getStartFrame=getSequences[0]._get_filename().split(".")[1]
            getLastFrame=getSequences[-1]._get_filename().split(".")[1]
            print getStartFrame
            print getLastFrame

            createReadNode['origfirst'].setValue(int(getStartFrame))
            createReadNode['origlast'].setValue(int(getLastFrame))  
            createReadNode['first'].setValue(int(getStartFrame))
            createReadNode['last'].setValue(int(getLastFrame))

            myWritePath='/'.join(mydirName[0:-2])+"/"+mydirName[-3]+"("+getStartFrame+"-"+getLastFrame+").mov"
            createNodeWrite['file'].setValue(myWritePath)
            createNodeWrite.setInput(0,createReadNode)
            createNodeWrite['file_type'].setValue('mov')
            createNodeWrite['meta_codec'].setValue('jpeg')
            createNodeWrite['mov64_quality_min'].setValue(10)
            createNodeWrite['mov64_quality_max'].setValue(10)
            self.nukeName='/'.join(mydirName[0:-2])+"/"+"mov_"+mydirName[-3]+"_("+getStartFrame+"-"+getLastFrame+").nk"
            print self.nukeName
        for nodes in self.allSelectNode:
            nuke.delete(nodes)
            
        nuke.scriptSaveAs(self.nukeName)

    def createWriteOutMov(self):
        self.allSelectNode = nuke.selectedNodes()
        nodeRead = nuke.selectedNodes('Read')

        self.fileName = nuke.root().knob("name").value() 

        nodeWrite = nuke.nodes.Write()
        nodeWrite.setInput(0, self.allSelectNode[0])
        nodeWrite['channels'].setValue("rgb")
        nodeWrite['file_type'].setValue('mov')
        nodeWrite['meta_codec'].setValue('jpeg')
        nodeWrite['mov64_quality_min'].setValue(3)
        nodeWrite['mov64_quality_max'].setValue(3)

        Fps = nuke.root().knob('fps').value()
        p = nuke.Panel('input fps')
        p.setWidth(180)
        p.addSingleLineInput('input fps', Fps)  
        p.addButton('Cancel')
        p.addButton('OK')
        panleResult = p.show() 
        path = p.value('input fps') 
        if not path:
            nuke.message('\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\xb8\xa7\xe7\x8e\x87\xef\xbc\x81')
            return

        nodeWrite['mov64_fps'].setValue(float(path))
        movName= ''
        if self.fileName:
            newPath = os.path.splitext(self.fileName)[0]
            movName = '%s.mov'%newPath
            nodeWrite['file'].setValue(movName)
        else:
            if nodeRead:
                readFile = nodeRead[0]['file'].value()
               # name = os.path.basename(readFile).split('.')[0]
                newPath = os.path.dirname(readFile)
                movName = '%s.mov' % (newPath)
            else:
                p = nuke.Panel('input Write Path')
                p.setWidth(180)
                p.addSingleLineInput('input Write Path', '')  
                p.addButton('Cancel')
                p.addButton('OK')
                while True:
                    panleResult = p.show() 
                    path = p.value('input Write Path')
                    if path:
                        if not os.path.isdir(path):
                            path = p.value('input Write Path')
                        else:
                            break
                    else:
                        return
               
                movName = '%s/mov.mov'%path 
                movName = movName.replace('\\', '/')

        if movName:
            nuke.message('write\xe8\xbe\x93\xe5\x87\xba\xe8\xb7\xaf\xe5\xbe\x84%s'%movName)
            nodeWrite['file'].setValue(movName)
#OCT_OutputMOV().OutputMOV()

# OCT_OutputMOV().createWriteOutMov()

