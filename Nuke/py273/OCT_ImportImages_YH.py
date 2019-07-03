# -*- coding: utf-8 -*-
import pyseq
import nuke
import os
import re
class  myFindFrame():
    def __init__(self):
        self.panelResult = ''
        self.myOrangeDict = {}
        self.myOneReads = []
        #{序列字典:[素材节点,是否是序列（True,False）]}
        self.mySeqClassDict = {}
        #{素材类型字典:[素材类型,[素材节点]]}
        self.myImagesTClassDict = {}        
        
    def myFindPanel(self):
        i = 1
        p = nuke.Panel('Find  Frame Range')
        p.setWidth(250)
        p.addSingleLineInput('Input Path', '')  
        p.addButton('Cancel')
        p.addButton('OK')
        self.panleResult = p.show() 
        path = p.value('Input Path') 
        self.myFindFrame(path, i)
        self.classIfy()  

    def myFindFrame(self, path, i):
        # self.myReads = []
        j = i
        myPath = path
        #print myPath
        all = pyseq.getSequences(myPath)
        #print all 
        for dirName in all:
            #print dirName
            myPath = dirName.path()
            #print myPath
            if os.path.isdir(myPath):
                #print myPath
                self.myFindFrame(myPath, j)
            else:
                Flag = True
                myDir = myPath.split('\\')
                myDirs = '/'.join(myDir[0:-1])
                #print myDirs
                imagesType = myDir[-2]
                if dirName.length() == 1:
                    the_head = dirName.head()
                    if the_head == 'Thumbs.db':
                        continue     
                    #单帧             
                    else:
                        if the_head.find('.exr') >= 0 or the_head.find('.jpg') >= 0 or the_head.find('.tif') >= 0 or the_head.find('.iff') >= 0 or the_head.find('.tga') >= 0 or the_head.find('.png') >= 0:
                            firstFrameName = dirName[0]._get_filename()
                            #创建Read节点
                            nodeRead = nuke.nodes.Read()
                            #素材路径
                            setData = os.path.join(myDirs, firstFrameName)
                            nodeRead['file'].setValue('%s' % setData.replace('\\', '/'))
                    
                            nodeRead['origfirst'].setValue(1)
                            nodeRead['origlast'].setValue(1)  
                            nodeRead['first'].setValue(1)
                            nodeRead['last'].setValue(1)  
                            
                            nodeRead['on_error'].setValue('cheeckerboard')               
                            formatW = nodeRead.width()
                            formatH = nodeRead.height()
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
                                            myFormat = eachFormat.name()
                                            if myFormat != None:
                                                nodeRead['format'].setValue(myFormat)
                                                Flag = False
                                                break
                                    if Flag:               
                                        #键的名字
                                        while True:
                                            mySize = ('my_Size%s' % j)
                                            if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                break
                                            else:
                                                j += 1
                                        widthHeight = str(formatW) + " " + str(formatH)
                                        self.myOrangeDict.update({mySize:widthHeight})
                                        square = widthHeight+" "+mySize
                                        nuke.addFormat(square)
                                        nodeRead['format'].setValue(mySize)
                                self.myOneReads.append(nodeRead)
                                self.mySeqClassDict.update({nodeRead: False})
                                if not imagesType in self.myImagesTClassDict.keys():
                                    self.myImagesTClassDict.update({imagesType: [nodeRead]})
                                else:
                                    self.myImagesTClassDict[imagesType].append(nodeRead)

                            #添加到类型字典中
                            # self.myClassDict.update({nodeRead:[myDir[-2], False]})
                #序列帧     
                else: 
                    the_tail = dirName.tail()
                    if the_tail:
                        if the_tail == '.exr' or the_tail == '.jpg' or the_tail == '.tif' or the_tail == '.iff' or the_tail == '.tiff' or the_tail == '.tga' or the_tail == '.png':
                            firstFrameName = dirName[0]._get_filename()  
                            lastFrameName = dirName[-1]._get_filename()
                            # print firstFrameName
                            # print lastFrameName
                            # #获取第一帧的文件名
                            # the_firstframes = int(firstFrameName.split(".")[-2]) 
                            # the_lastframes = int(lastFrameName.split(".")[-2])

                            the_firstframes = dirName.start()
                            #print the_firstframes
                            the_lastframes = dirName.end()
                            nodeRead = nuke.nodes.Read()
        
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
                                    allFormat = nuke.formats()
                                    for eachFormat in allFormat:
                                        if eachFormat.width() == formatW and eachFormat.height() == formatH:
                                            myFormat = eachFormat.name()
                                            if myFormat != None:
                                                nodeRead['format'].setValue(myFormat)
                                                Flag = False
                                                break
                                    if Flag:          
                                        while True:
                                            mySize = ('my_Size%s' % j)
                                            if mySize not in [eachFormat.name() for eachFormat in allFormat]:
                                                break
                                            else:
                                                j += 1  
                                        widthHeight = str(formatW) + " " + str(formatH)
                                        self.myOrangeDict.update({mySize:widthHeight})
                                        square = widthHeight+" "+mySize
                                        nuke.addFormat(square)
                                        nodeRead['format'].setValue(mySize)
        
                            #查找位数
                            numStr = firstFrameName.split(".")[-2]
                            num = re.findall("\d+$", numStr)[-1]
                            numPlaces = len('%s' % num)
                            the_image = dirName.tail()

                            number = firstFrameName.split(num)
                            name = number[0]
                            #name = '.'.join(number[0:-2])

                            num2Str = lastFrameName.split(".")[-2]
                            num2 = re.findall("\d+$", num2Str)[-1]
                            numPlaces2 = len('%s' % num2)

                            if numPlaces == numPlaces2:
                                #setData = myDirs+'/'+name+'.%'+'0%dd'%numPlaces+the_image
                                setData = myDirs + '/' + name + '%' + '0%dd' % numPlaces + the_image
                            else:
                                #setData = myDirs+'/'+name+'.#'+the_image
                                setData = myDirs + '/' + name + '#' + the_image
                       
                            nodeRead['file'].setValue(setData)
                            nodeRead['origfirst'].setValue(the_firstframes)
                            nodeRead['origlast'].setValue(the_lastframes)
                            nodeRead['first'].setValue(the_firstframes)
                            nodeRead['last'].setValue(the_lastframes)
                            nodeRead['on_error'].setValue('cheeckerboard')
                            #添加到类型字典中
                            self.mySeqClassDict.update({nodeRead: True})
                            if not imagesType in self.myImagesTClassDict.keys():
                                self.myImagesTClassDict.update({imagesType: [nodeRead]})
                            else:
                                self.myImagesTClassDict[imagesType].append(nodeRead)
                            # self.myClassDict.update({nodeRead:[myDir[-2], True]})

                        else:
                            myDirs = '/'.join(myDir[0:-1])
                            mySequenceDir=myDir[-1].split('-')
                            print myDirs 
                            num_1 = re.findall(r"\d+\.?\d*",mySequenceDir[0])
                            num_2 = re.findall(r"\d+\.?\d*",mySequenceDir[1])

                            # num_1=mySequenceDir[0].split('_')
                            # num_2=mySequenceDir[1].split('_')

                            for  i in range(int(num_2[0])):
                                g=str(i+1)
                                myPath=myDirs+'/'+ mySequenceDir[0].split(num_1[0])[0]+g+mySequenceDir[1].split(num_2[0])[-1]
                                # myPath=myDirs+'/'+ num_1[0]+'_'+g+'_'+num_2[-1]
                                self.myFindFrame(myPath, j)
                            
                    else:
                        for dirtList in dirName:
                            myPath = dirtList.path
                            if os.path.isdir(myPath):
                                self.myFindFrame(myPath, j)

   #归类           
    def classIfy(self):
        #单类型数组
        singlList = []
        if self.mySeqClassDict:
            y = 0
            for mykey in self.myImagesTClassDict.keys():
                if len(self.myImagesTClassDict[mykey]) > 1:
                    x = 0
                    i = 0
                    j = 0
                    for i, myRead in enumerate(self.myImagesTClassDict[mykey]):
                        if self.mySeqClassDict[myRead]:
                            myRead.setXYpos(x, y)
                            x += 80
                            j += 1
                    #存在单帧的时候
                    if i != j:
                        x += 80
                        for myRead in self.myImagesTClassDict[mykey]:
                            if not self.mySeqClassDict[myRead]:
                                x += 80
                                myRead.setXYpos(x, y)
                    y += 90
                else:
                    #记录单类的
                    singlList.append(mykey)
            #处理单类的
            x = 0
            y += 90
            i = 0
            j = 0
            for i, mykey in enumerate(singlList):
                myRead = self.myImagesTClassDict[mykey][0]
                if self.mySeqClassDict[myRead]:
                            myRead.setXYpos(x, y)
                            x += 80
                            j += 1
            if i != j:
                x += 80
                for i, mykey in enumerate(singlList):
                    myRead = self.myImagesTClassDict[mykey][0]
                    if not self.mySeqClassDict[myRead]:
                        x += 80
                        myRead.setXYpos(x, y)
            #选择单帧
            if self.myOneReads:
                allmySelectedNodes = nuke.selectedNodes()
                if allmySelectedNodes:
                    for mySelectedNode in allmySelectedNodes:
                        mySelectedNode.setSelected(False)
                for myRead in self.myOneReads:
                    myRead.setSelected(True)

