# -*- coding: utf-8 -*-
import pyseq
import nuke
import os
class MyFrame():
    def __init__(self):
        #判断是否找帧数的范围
        self.checkFlag=False
        #判断是否找素材的大小
        self.formatFlag=False
        #用字典的更新素材大小
        self.myOrangeDict={}
        #暂存界面
        self.panelReslut = ''
        #所有节点
        self.myReads=''
    def myOrigFrame(self):
        j=1
        self.myReads = nuke.selectedNodes('Read')
        if len(self.myReads) == 0:
            self.myReads= nuke.allNodes('Read')
        #打X的素材不在范围内
        if self.myReads:
            tmpList=[]
            for eachRead in self.myReads:
                if not eachRead['disable'].value():
                    tmpList.append(eachRead)
            self.myReads=tmpList
        if len(self.myReads)==0:
            nuke.message('No Reads!')
            return  
        self.myFormatCheck_UI()          
        if self.formatFlag:
            try:
                if nuke.root().firstFrame()==nuke.frame():
                    nuke.activeViewer().frameControl(+1)
                elif nuke.root().lastFrame()==nuke.frame():
                    nuke.activeViewer().frameControl(-1)
                else:
                    nuke.activeViewer().frameControl(+1)
            except:
                nuke.message('\xe8\xaf\xb7\xe5\x88\x9b\xe5\xbb\xba\xe4\xb8\x80\xe4\xb8\xaaviewer\xe8\xa7\x86\xe7\xaa\x97\xef\xbc\x81')
                return
        if self.myReads:
            for read in self.myReads:
                Flag=True
                readFilePath = read['file'].value()
                if readFilePath:
                    if self.formatFlag:
                        formatW=read.width()
                        formatH=read.height()
                        ReadOFormat = read['format'].value()
                        if ReadOFormat.width() != formatW or ReadOFormat.height() != formatH:
                            if self.myOrangeDict:
                                for orange in self.myOrangeDict.keys():
                                    sizeW=self.myOrangeDict[orange].split(" ")[0]
                                    sizeH=self.myOrangeDict[orange].split(" ")[1]
                                    if sizeW==formatW and sizeH==formatH:
                                        read['format'].setValue(orange)
                                        Flag=False
                                        break
                            if Flag:
                                allFormat=nuke.formats()
                                for eachFormat in allFormat:
                                    if eachFormat.width()==formatW and eachFormat.height()==formatH:
                                        myFormat=eachFormat.name()
                                        if myFormat != None:
                                            read['format'].setValue(myFormat)
                                            Flag=False
                                            break
                                if Flag:
                                    while True:
                                        mySize=('my_Size%s' % j)
                                        if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                            break
                                        else:
                                            j+=1  
                                    widthHeight=str(formatW)+" "+str(formatH)
                                    self.myOrangeDict.update({mySize:widthHeight})
                                    square =widthHeight+" "+mySize
                                    nuke.addFormat(square)
                                    read['format'].setValue(mySize)
                                                 
                    if self.checkFlag:
                        readDir=os.path.split(readFilePath)[0]
                        frameOrange=pyseq.getSequences(readDir)
                        for frames in frameOrange:
                            myPath = frames.path()
                            if os.path.isdir(myPath):
                                continue 
                            else:
                                if frames.tail():
                                    firstFrameName = frames[0]._get_filename()  
                                    lastFrameName = frames[-1]._get_filename()
                                    readFileStart=firstFrameName.split(".")[-2] 
                                    readFileLast=lastFrameName.split(".")[-2]
                                    read['origfirst'].setValue(int(readFileStart))  
                                    read['origlast'].setValue(int(readFileLast))  
                                    read['first'].setValue(int(readFileStart))
                                    read['last'].setValue(int(readFileLast))
            else:
                if self.formatFlag or self.checkFlag:
                    nuke.message('OK')

    def myFormatCheck_UI(self):
        self.panelReslut = ''
        p=nuke.Panel('New Frame Range And Format Szie Tools')
        #p.setWidth(200)
        p.addBooleanCheckBox('Size',False)
        p.addBooleanCheckBox('Frame',False)
        self.panelReslut=p.show()
        if self.panelReslut:
            self.formatFlag=p.value('Size')
            #print self.formatFlag
            self.checkFlag=p.value('Frame')
           # print self.checkFlag

# a= MyFrame()
# a.myOrigFrame()
