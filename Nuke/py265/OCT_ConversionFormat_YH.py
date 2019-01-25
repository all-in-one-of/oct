# -*- coding: utf-8 -*-
import pyseq
import nuke
import os
import nukescripts
class conversionFormats(object):
    """docstring for conversionFormat"""
    def __init__(self):
        self.panelResult = ''
        self.newPaths=""
        self.oldPaths=""
        self.list=1
        self.myOrangeDict={}
        #节点个数
        self.number=0
        self.k=1

    #UI界面
    def conversionFormatUI(self):
        i=1
        p = nuke.Panel('conversionFormat')
        p.setWidth(250)
        p.addSingleLineInput('Old Path:','') 
        p.addSingleLineInput('New Path:', '')
        p.addSingleLineInput('options:', '')  
        p.addButton('Cancel')
        p.addButton('OK')
        self.panleResult = p.show() 
        option=p.value('options:')
        options=""
        if option:
            options=int(option)
        oldPath=p.value('Old Path:')
        newPath=p.value('New Path:')
        nuke.selectAll()
        nukescripts.node_delete(popupOnError=True)
        if oldPath and newPath:
            self.newPaths=newPath.replace('\\', '/')
            self.oldPaths=oldPath.replace('\\', '/')
            self.importImage(oldPath,options,i)
            
    def importImage(self,oldPath,options,i):
        j=i
        myOldPath=oldPath
        all=pyseq.getSequences(myOldPath)
        #第几个文件夹中导出Read节点
        if options!=0:
            for dirName in all:
                myOldPath=dirName.path()
                if os.path.isdir(myOldPath) and (options-1)>self.list:
                    self.list=int(self.list+1)
                    self.importImage(myOldPath,options,j)

                elif (not os.path.isdir(myOldPath)) and (options-1)==self.list:
                    Flag=True
                    Flags=True
                    myDir=myOldPath.split("\\")
                    myDirs = '/'.join(myDir[0:-1])
                    if dirName.length()==1:
                        the_head=dirName.head()
                        if the_head=="Thumbs.db":
                            continue
                        #单帧
                        else:
                            if the_head.find('.exr') >= 0 or the_head.find('.jpg') >= 0 or the_head.find('.tif') >= 0 or the_head.find('.iff') >= 0 or the_head.find('.tga') >= 0 or the_head.find('.png') >= 0:
                                if self.number>0 and self.number%60==0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)
                                    else:
                                        fileName=int(self.number/60)
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)

                                self.number=self.number+1  

                                firstFrameName=dirName[0]._get_filename()
                                #创建节点
                                nodeRead = nuke.nodes.Read()
                                nodeRead['postage_stamp'].setValue(False)
                                #素材路径
                                setData = os.path.join(myDirs, firstFrameName)
                                nodeRead['file'].setValue('%s' % setData.replace('\\', '/'))
                                nodeRead['origfirst'].setValue(1)
                                nodeRead['origlast'].setValue(1)  
                                nodeRead['first'].setValue(1)
                                nodeRead['last'].setValue(1)  

                                nodeRead['on_error'].setValue('checkerboard')   
                                formatW=nodeRead.width()
                                formatH=nodeRead.height()
                                ReadOFormat = nodeRead['format'].value()
                                if ReadOFormat.width() != formatW or ReadOFormat.height() != formatH:
                                    allFormat = nuke.formats()
                                    if self.myOrangeDict:
                                        for myOrange in self.myOrangeDict.keys():
                                            SazeW = self.myOrangeDict[myOrange].split(" ")[0]
                                            SazeH = self.myOrangeDict[myOrange].split(" ")[1]
                                            if SazeW == formatW and SazeH == formatH: 
                                                nodeRead['format'].setValue(myOrange) 
                                                Flag = False   
                                                break 

                                    if Flag:
                                        for eachFormat in allFormat:
                                            if eachFormat.width() == formatW and eachFormat.height() == formatH:
                                                myFormat=eachFormat.name()
                                                if myFormat != None:
                                                    nodeRead['format'].setValue(myFormat)
                                                    Flag = False
                                                    break
                                        if Flag:
                                            while True:
                                                mySize=('my_Size%s'%j)
                                                if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                    break
                                                else:
                                                    j+=1
                                            widthHeight=str(formatW)+" "+str(formatH)
                                            self.myOrangeDict.update({mySize:widthHeight})
                                            square = widthHeight+" "+mySize
                                            nuke.addFormat(square)
                                            nodeRead['format'].setValue(mySize)

                                            nodeReformat=nuke.nodes.Reformat()

                                nodeWrite=nuke.nodes.Write()
                                nodeReformat.setInput(0,nodeRead)
                                nodeWrite.setInput(0,nodeReformat)

                                if the_tail == '.exr':
                                    nodeWrite['file_type'].setValue("exr")
                                    nodeWrite['datatype'].setValue(0)
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['compression'].setValue(2)
                                else:
                                    filetype=the_tail.split(".")
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['file_type'].setValue(filetype)

                                WriteFile=setData.replace(self.oldPaths,self.newPaths)
                                nodeWrite['file'].setValue(WriteFile)
                                myNewPath=os.path.dirname(WriteFile)
                                if not os.path.isdir(myNewPath):
                                    os.makedirs(myNewPath)


                                ReformatFormat = nodeReformat['format'].value()
                                if ReformatFormat.width() != 500 or ReformatFormat.height() != 500:
                                    allFormat = nuke.formats()
                                    for eachFormat in allFormat:
                                        if eachFormat.width() == 500 and eachFormat.height() == 500:
                                            myFormat=eachFormat.name()
                                            if myFormat != None:
                                                nodeReformat['format'].setValue(myFormat)
                                                Flag = False
                                                break
                                    if Flag:
                                        while True:
                                            mySize=('my_Size%s'%j)
                                            if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                break
                                            else:
                                                j+=1
                                        widthHeight=str(formatW)+" "+str(formatH)
                                        square = widthHeight+" "+mySize
                                        nuke.addFormat(square)
                                        nodeReformat['format'].setValue(mySize)
                                if self.number>0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                    fileName=int(self.number/60)+1
                                    nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)


                    #序列帧
                    else:
                        the_tail = dirName.tail()
                        if the_tail:
                            if the_tail == '.exr' or the_tail == '.jpg' or the_tail == '.tif' or the_tail == '.iff' or the_tail == '.tiff' or the_tail == '.tga' or the_tail == '.png':
                                if self.number>0 and self.number%60==0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)
                                    else:
                                        fileName=int(self.number/60)
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)

                                self.number=self.number+1  

                                firstFrameName = dirName[0]._get_filename()  
                                lastFrameName=dirName[-1]._get_filename()
                                #the_firstframes=int(firstFrameName.split(".")[-2])
                                #the_lastframes = int(lastFrameName.split(".")[-2])

                                if len(firstFrameName.split("."))==2:
                                    the_firstframes = int(firstFrameName.split(".")[-2].replace(myDir[-2],"")) 
                                    the_lastframes = int(lastFrameName.split(".")[-2].replace(myDir[-2],""))
                                else:
                                    #获取第一帧的文件名
                                    the_firstframes = int(firstFrameName.split(".")[-2]) 
                                    the_lastframes = int(lastFrameName.split(".")[-2])

                                nodeRead = nuke.nodes.Read()
                                nodeRead['postage_stamp'].setValue(False)

                                setData = os.path.join(myDirs, firstFrameName)
                                nodeRead['file'].setValue('%s' % setData.replace('\\', '/'))
                                formatW = nodeRead.width()
                                formatH = nodeRead.height()
                                widthHeight = str(formatW)+" "+str(formatH)
                                ReadOFormat = nodeRead['format'].value()

                                
                                if ReadOFormat.width() != formatW or ReadOFormat.height() != formatH:
                                    if self.myOrangeDict:
                                        for myOrange in self.myOrangeDict.keys(): 
                                            SazeW = self.myOrangeDict[myOrange].split(" ")[0]
                                            SazeH = self.myOrangeDict[myOrange].split(" ")[1]
                                            if SazeW == formatW and SazeH == formatH:
                                                nodeRead['format'].setValue(myOrange)
                                                Flag = False 
                                                break
                                    if Flag:
                                        allFormat=nuke.formats()
                                        for eachFormat in allFormat:
                                            if eachFormat.width()==formatW and eachFormat.height()==formatH:
                                                myFormat=eachFormat.name()
                                                
                                                if myFormat!=None:
                                                    nodeRead['format'].setValue(myFormat)
                                                    Flag=False
                                                    break
                                        if Flag:
                                            while True:
                                                mySize=('my_Size%s'%j)
                                                if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                    break
                                                else:
                                                    j+=1
                                            widthHeight=str(formatW)+" "+str(formatH)
                                            self.myOrangeDict.update({mySize:widthHeight})
                                            square=widthHeight+" "+mySize
                                            nuke.addFormat(square)
                                            nodeRead['format'].setValue(mySize)

                                #查找位数
                                if len(firstFrameName.split("."))==2:
                                    num=firstFrameName.split(".")[-2].replace(myDir[-2],"")
                                    numPlaces=len("%s"%num)
                                    the_image=dirName.tail()
                                    
                                    #number=lastFrameName.split(".")
                                    #name=".".join(number[0:-2])

                                    setData=myDirs+"/"+myDir[-2]+"%"+"0%dd"%numPlaces+the_image
                                else:
                                    num=firstFrameName.split(".")[-2]
                                    numPlaces=len("%s"%num)
                                    the_image=dirName.tail()
                                    number=lastFrameName.split(".")
                                    name=".".join(number[0:-2])

                                    setData=myDirs+"/"+name+".%"+"0%dd"%numPlaces+the_image


                                nodeRead['file'].setValue(setData)
                                nodeRead['origfirst'].setValue(the_firstframes)
                                nodeRead['origlast'].setValue(the_lastframes)
                                nodeRead['first'].setValue(the_firstframes)
                                nodeRead['last'].setValue(the_lastframes)
                                nodeRead['on_error'].setValue('checkerboard')

                                nodeReformat=nuke.nodes.Reformat()
                                nodeWrite=nuke.nodes.Write()
                                nodeReformat.setInput(0,nodeRead)
                                nodeWrite.setInput(0,nodeReformat)

                                if the_tail == '.exr':
                                    nodeWrite['file_type'].setValue("exr")
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['compression'].setValue(2)
                                    nodeWrite['datatype'].setValue(0)
                                else:
                                    filetype=the_tail.split(".")
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['file_type'].setValue(filetype)

                                WriteFile=setData.replace(self.oldPaths,self.newPaths)
                                nodeWrite['file'].setValue(WriteFile)
                                myNewPath=os.path.dirname(WriteFile)
                                if not os.path.isdir(myNewPath):
                                    os.makedirs(myNewPath)

                                ReformatFormat = nodeReformat['format'].value()
                                if ReformatFormat.width() != 500 or ReformatFormat.height() != 500:
                                    allFormat = nuke.formats()
                                    for eachFormat in allFormat:
                                        if eachFormat.width() == 500 and eachFormat.height() == 500:
                                            myFormat=eachFormat.name()
                                            if myFormat != None:
                                                nodeReformat['format'].setValue(myFormat)
                                                Flag = False
                                                break
                                    if Flag:
                                        while True:
                                            mySize=('my_Size%s'%j)
                                            if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                break
                                            else:
                                                j+=1
                                        widthHeight=str(formatW)+" "+str(formatH)
                                        square = widthHeight+" "+mySize
                                        nuke.addFormat(square)
                                        nodeReformat['format'].setValue(mySize)

                                if self.number>0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                    fileName=int(self.number/60)+1
                                    nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)

                               

                            else:
                                myDirs='/'.join(myDir[0:-1])
                                mySequenceDir=myDir[-1].split('-')
                                print mySequenceDir
                                num_1=mySequenceDir[0].split("_")
                                num_2=mySequenceDir[1].split("_")
                                for i in range(int(num_2[0])):
                                    g=str(i+1)
                                    myOldPath=myDirs+"/"+num_1[0]+"_"+g+"_"+num_2[-1]
                                    if i!=0:
                                        self.list=self.list+1
                                    self.importImage(myOldPath,options,j)

            else:
                #print myOldPath
                self.list=1
               
                            
        #导入所有
        elif options==0:
            for dirName in all:
                myOldPath = dirName.path()
                
                if os.path.isdir(myOldPath):
                    self.importImage(myOldPath,options,j)
                else:
                    
                    Flag=True
                    Flags=True
                    myDir= myOldPath.split('\\')
                    myDirs="/".join(myDir[0:-1])

                    if dirName.length()==1:
                        the_head = dirName.head()
                        if the_head=="Thumbs.db":
                            continue
                        #单帧
                        else:
                            if the_head.find('.exr') >= 0 or the_head.find('.jpg') >= 0 or the_head.find('.tif') >= 0 or the_head.find('.iff') >= 0 or the_head.find('.tga') >= 0 or the_head.find('.png') >= 0:
                                if self.number>0 and self.number%60==0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)
                                    else:
                                        fileName=int(self.number/60)
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)

                                self.number=self.number+1  

                                firstFrameName = dirName[0]._get_filename()
                                #创建Read节点
                                nodeRead=nuke.nodes.Read()
                                nodeRead['postage_stamp'].setValue(False)
                                #素材路径
                                setData=os.path.join(myDirs,firstFrameName)
                                nodeRead['file'].setValue('%s' %setData.replace("\\","/"))

                                nodeRead['origfirst'].setValue(1)
                                nodeRead['origlast'].setValue(1)
                                nodeRead['first'].setValue(1)
                                nodeRead['last'].setValue(1)

                                nodeRead["on_error"].setValue('checkerboard')
                                formatW=nodeRead.width()
                                formatH=nodeRead.height()
                                ReadOFormat=nodeRead['format'].value()
                                if ReadOFormat.width()!=formatW or ReadOFormat.height()!=formatH:
                                    allFormat=nuke.format()
                                    if self.myOrangeDict:
                                        for myOrange in self.myOrangeDict.keys():
                                            SazeW=self.myOrangeDict['myOrange'].split(" ")[0]
                                            SazeH=self.myOrangeDict['myOrange'].split(" ")[1]
                                            if SazeW==formatW or SazeH==formatH:
                                                nodeRead['format'].setValue(myOrange)
                                                Flag=False
                                                break
                                    if Flag:
                                        for eachFormat in allFormat:
                                            if eachFormat.width==formatW and eachFormat.height==formatH:
                                                myFormat=eachFormat.name()
                                                if  myFormat!=None:
                                                    nodeRead['format'].setValue(myFormat)
                                                    Flag=False
                                                    break
                                        if Flag:
                                            #键的名字
                                            while True:
                                                mySize = ('my_Size%s' % j)
                                                if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                    break
                                                else:
                                                    j+=1
                                            widthHeight=str(formatW)+" "+str(formatH)
                                            self.myOrangeDict.update({mySize:widthHeight})
                                            square=widthHeight+" "+mySize
                                            nuke.addFormat(square)
                                            nodeRead['format'].setValue(mySize)

                                nodeReformat=nuke.nodes.Reformat()
                                nodeReformat.setInput(0,nodeRead)
                                nodeWrite=nuke.nodes.Write()
                                nodeWrite.setInput(0,nodeReformat)


                                if the_tail == '.exr':
                                    nodeWrite['file_type'].setValue("exr")
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['compression'].setValue(2)
                                    nodeWrite['datatype'].setValue(0)
                                else:
                                    filetype=the_tail.split(".")
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['file_type'].setValue(filetype)

                                WriteFile=setData.replace(self.oldPaths,self.newPaths)
                                nodeWrite['file'].setValue(WriteFile)

                                myNewPath=os.path.dirname(WriteFile)
                                if not os.path.isdir(myNewPath):
                                    os.makedirs(myNewPath)

                                ReformatFormat = nodeReformat['format'].value()
                                if ReformatFormat.width() != 500 or ReformatFormat.height() != 500:
                                    allFormat = nuke.formats()
                                    for eachFormat in allFormat:
                                        if eachFormat.width() == 500 and eachFormat.height() == 500:
                                            myFormat=eachFormat.name()
                                            if myFormat != None:
                                                nodeReformat['format'].setValue(myFormat)
                                                Flags = False
                                                break
                                    if Flags:
                                        while True:
                                            mySize=('my_Size%s'%j)
                                            if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                break
                                            else:
                                                j+=1
                                        widthHeight=str(formatW)+" "+str(formatH)
                                        square = widthHeight+" "+mySize
                                        nuke.addFormat(square)
                                        nodeReformat['format'].setValue(mySize)

                                if self.number>0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                    fileName=int(self.number/60)+1
                                    nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)


                    #序列帧
                    else:
                        the_tail=dirName.tail()
                        if the_tail:
                            if the_tail == '.exr' or the_tail == '.jpg' or the_tail == '.tif' or the_tail == '.iff' or the_tail == '.tiff' or the_tail == '.tga' or the_tail == '.png':
                                
                                if self.number>0 and self.number%60==0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)
                                    else:
                                        fileName=int(self.number/60)
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)
                                        nuke.selectAll()
                                        nukescripts.node_delete(popupOnError=True)

                                self.number=self.number+1  

                                firstFrameName=dirName[0]._get_filename()
                                lastFrameName=dirName[-1]._get_filename()
                                
                                if len(firstFrameName.split("."))==2:
                                    the_firstframes = int(firstFrameName.split(".")[-2].replace(myDir[-2],"")) 
                                    the_lastframes = int(lastFrameName.split(".")[-2].replace(myDir[-2],""))
                                else:
                                    #获取第一帧的文件名
                                    the_firstframes = int(firstFrameName.split(".")[-2]) 
                                    the_lastframes = int(lastFrameName.split(".")[-2])

                                nodeRead=nuke.nodes.Read()
                                nodeRead['postage_stamp'].setValue(False)

                                setData=os.path.join(myDirs,firstFrameName)
                                nodeRead['file'].setValue("%s" %setData.replace("\\",'/'))

                                #节点的大小
                                formatW=nodeRead.width()
                                formatH=nodeRead.height()

                                widthHeight=str(formatW)+" "+str(formatH)
                                ReadOFormat = nodeRead['format'].value()

                                
                                if ReadOFormat.width()!=formatW or ReadOFormat.height()!=formatH:
                                    if self.myOrangeDict:
                                        for myOrange in self.myOrangeDict.keys():
                                            SazeW=self.myOrangeDict[myOrange].split(" ")[0]
                                            SazeH=self.myOrangeDict[myOrange].split(" ")[1]
                                            if SazeW==formatW and SazeH==formatH:
                                                nodeRead['format'].setValue(myOrange)
                                                Flag=False
                                                break
                                    if Flag:
                                        allFormat=nuke.formats()
                                        for eachFormat in allFormat:
                                            if eachFormat.width()==formatW and eachFormat.height()==formatH:
                                                myFormat=eachFormat.name()
                                                if myFormat!=None:
                                                    nodeRead['format'].setValue(myFormat)
                                                    Flag=False
                                                    break
                                        if Flag:
                                            while True:
                                                mySize=('my_Size%s' % j)
                                                if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                    break
                                                else:
                                                    j+=1
                                            widthHeight=str(formatW)+" " +str(formatH)
                                            self.myOrangeDict.update({mySize:widthHeight})
                                            square=widthHeight+" "+mySize
                                            nuke.addFormat(square)
                                            nodeRead['format'].setValue(mySize)

                                #查找位数
                                if len(firstFrameName.split("."))==2:
                                    num=firstFrameName.split(".")[-2].replace(myDir[-2],"")
                                    numPlaces=len("%s"%num)
                                    the_image=dirName.tail()
                                    
                                    #number=lastFrameName.split(".")
                                    #name=".".join(number[0:-2])

                                    setData=myDirs+"/"+myDir[-2]+"%"+"0%dd"%numPlaces+the_image
                                else:
                                    num=firstFrameName.split(".")[-2]
                                    numPlaces=len("%s"%num)
                                    the_image=dirName.tail()
                                    number=lastFrameName.split(".")
                                    name=".".join(number[0:-2])

                                    setData=myDirs+"/"+name+".%"+"0%dd"%numPlaces+the_image

                                nodeRead['file'].setValue(setData)
                                nodeRead['origfirst'].setValue(the_firstframes)
                                nodeRead['origlast'].setValue(the_lastframes)
                                nodeRead['first'].setValue(the_firstframes)
                                nodeRead['last'].setValue(the_lastframes)
                                nodeRead['on_error'].setValue('checkerboard')
                                nodeReformat=nuke.nodes.Reformat()
                                nodeWrite=nuke.nodes.Write()
                                nodeReformat.setInput(0,nodeRead)
                                nodeWrite.setInput(0,nodeReformat)
                                
                                if the_tail == '.exr':
                                    nodeWrite['file_type'].setValue("exr")
                                    nodeWrite['datatype'].setValue(0)
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['compression'].setValue(2)
                                else:
                                    filetype=the_tail.split(".")
                                    nodeWrite['channels'].setValue("all")
                                    nodeWrite['file_type'].setValue(filetype)

                                WriteFile=setData.replace(self.oldPaths,self.newPaths)
                                nodeWrite['file'].setValue(WriteFile)
                                myNewPath=os.path.dirname(WriteFile)
                                if not os.path.isdir(myNewPath):
                                    os.makedirs(myNewPath)

                                ReformatFormat = nodeReformat['format'].value()
                                if ReformatFormat.width() != 500 or ReformatFormat.height() != 500:
                                    allFormat = nuke.formats()
                                    for eachFormat in allFormat:
                                        if eachFormat.width() == 500 and eachFormat.height() == 500:
                                            myFormat=eachFormat.name()
                                            if myFormat != None:
                                                nodeReformat['format'].setValue(myFormat)
                                                Flags = False
                                                break
                                    if Flags:
                                        while True:
                                            mySize=('my_Size%s'%j)
                                            if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                break
                                            else:
                                                j+=1
                                        widthHeight=str(500)+" "+str(500)
                                        square = widthHeight+" "+mySize
                                        nuke.addFormat(square)
                                        nodeReformat['format'].setValue(mySize)
                                if self.number>0:
                                    if not os.path.isdir("D:/nukeFile"):
                                        os.makedirs("D:/nukeFile")
                                        nuke.scriptSave("D:/nukeFile/v%d.nk"%1)
                                    fileName=int(self.number/60)+1
                                    nuke.scriptSave("D:/nukeFile/v%d.nk"%fileName)

                            else:
                                myDirs='/'.join(myDir[0:-1])
                                mySequenceDir=myDir[-1].split('-')
                                
                                num_1=mySequenceDir[0].split("_")
                                num_2=mySequenceDir[1].split("_")
                                for i in range(int(num_2[0])):
                                    g=str(i+1)
                                    myOldPath=myDirs+"/"+num_1[0]+"_"+g+"_"+num_2[-1]
                                    self.importImage(myOldPath,options,j)
                        else:
                            for dirtList in dirName:
                                myOldPath=dirtList.path
                                if os.path.isdir(myOldPath):
                                    self.importImage(myOldPath,options,j)