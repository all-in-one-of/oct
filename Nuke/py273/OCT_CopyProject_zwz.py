# -*- coding: utf-8 -*-
import os
import getpass
import threading
import shutil
import nuke
import nukescripts
import pyseq

PROJECT_PATH = r'\\octvision.com\cg\Themes'
USERNAME = getpass.getuser()


class CopyJobThreading(threading.Thread):
    sourcePath = ''
    destPath = ''
    __stop = False

    def __init__(self, sourcePath='', destPath=''):
        super(CopyJobThreading, self).__init__()
        self.sourcePath = sourcePath
        self.destPath = destPath

    def run(self):
        if self.sourcePath and self.destPath:
            try:
                shutil.copy2(self.sourcePath, self.destPath)
            except:
                print '%s  \xe6\x8b\xb7\xe8\xb4\x9d\xe5\x87\xba\xe9\x94\x99' % self.sourcePath

    def stop(self):
        self.__stop = True


class myCheckFile(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'CheckFile', 'checkfile')
        self.textKnob = nuke.Multiline_Eval_String_Knob('Paths:')
        self.refereshButton = nuke.PyScript_Knob('refresh')
        self.addKnob(self.textKnob)
        self.addKnob(self.refereshButton)
        #按钮模式
        self.buttonModeType = 1
        #文件名分割出来的数组
        self.myFileSBName = []
        #输入的路径
        self.objectPath = ''
        self.myReads = []
        #所有的素材路径信息,数据类型{节点:地址}
        self.myReadsNameDict = {}
        #所有素材的开始时间，数据类型{节点:时间}
        self.myReadsStartDict = {}
        #所有素材的结束时间,数据类型{节点:时间}
        self.myReadsLastDict = {}
        #所有正确素材的后段路径,数据类型{节点:地址}
        self.myFileLastNameDict = {}
        #经过赛选的拷贝数据,数据类型{原始地址:[开始帧数，结束帧数，存放地址]}
        self.allCopyData = {}
        #经过赛选的设置数据:{节点名称:新地址}
        self.allSetData = {}
        self.worker1 = CopyJobThreading(self)
        self.worker1.setDaemon(False)
        self.worker2 = CopyJobThreading(self)
        self.worker2.setDaemon(False)
        #进度条
        self.myProgressWin = ''
        #输入地址
        self.panelReslut = ''

        #选择拷贝的帧数
        self.selectFrame=1

    def CopyDataJob(self, myCopyData):
        sourcePath = myCopyData[0]
        myDestFile = myCopyData[1]
        for i, mySourceFile in enumerate(sourcePath):
            if self.myProgressWin.isCancelled() is True:
                return False
            if i == 0:
                self.worker1.sourcePath = mySourceFile
                self.worker1.destPath = myDestFile
                try:
                    self.worker1.start()
                except:
                    self.worker1.run()
            elif i == 1:
                self.worker2.sourcePath = mySourceFile
                self.worker2.destPath = myDestFile
                try:
                    self.worker2.start()
                except:
                    self.worker2.run()
            else:
                while True:
                    if self.worker1.isAlive() is False:
                        self.worker1.sourcePath = mySourceFile
                        self.worker1.destPath = myDestFile
                        self.worker1.run()
                        break
                    elif self.worker2.isAlive() is False:
                        self.worker2.sourcePath = mySourceFile
                        self.worker2.destPath = myDestFile
                        self.worker2.run()
                        break
        while True:
            if self.worker1.isAlive() is False and self.worker2.isAlive() is False:
                break
        return True

    def myCheckProjectName(self):
        myFileFName = nuke.root().name()
        if myFileFName:
            myFileBName = os.path.basename(myFileFName)
            myFileBName = os.path.splitext(myFileBName)[0]
            self.myFileSBName = myFileBName.split('_')
            while '' in self.myFileSBName:
                self.myFileSBName.remove('')
            if len(self.myFileSBName) >= 3:
                serFilePath = os.path.join(PROJECT_PATH, self.myFileSBName[0], r'Project\scenes\animation', self.myFileSBName[1], self.myFileSBName[2])
                if os.path.isdir(serFilePath):
                    return True
        nuke.message('-----------------------\xe6\x96\x87\xe4\xbb\xb6\xe5\x91\xbd\xe5\x90\x8d\xe4\xb8\x8d\xe6\xa0\x87\xe5\x87\x86-----------------------\n\xe5\x9c\xa8\\\\octvision.com\\cg\\Themes\xe6\x89\xbe\xe4\xb8\x8d\xe5\x88\xb0\xe4\xb8\x8e\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d\xe7\x9b\xb8\xe5\xba\x94\xe7\x9a\x84\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9\xef\xbc\x81')
        return False

    def myGetCopypath(self):
        self.panelReslut = ''
        p = nuke.Panel('New Copy Path Tools')
        p.setWidth(200)
        p.addSingleLineInput('New Copy', '')
        p.addButton('Cancel')
        p.addButton('Apply')
        p.setWidth(350)
        self.panelReslut = p.show()
        if self.panelReslut:
            newCopyPath = p.value('New Copy')
            if newCopyPath and os.path.isdir(newCopyPath):
                if os.access(newCopyPath, os.W_OK):
                    self.objectPath = os.path.join(newCopyPath, self.myFileSBName[0], self.myFileSBName[1], self.myFileSBName[2])
                    return True
                else:
                    nuke.message('\xe4\xbd\xa0\xe4\xb8\x8d\xe5\x85\xb7\xe6\x9c\x89\xe8\xaf\xa5\xe8\xb7\xaf\xe5\xbe\x84\xe7\x9a\x84\xe5\x86\x99\xe5\x85\xa5\xe6\x9d\x83\xe9\x99\x90\xef\xbc\x81')
            else:
                nuke.message('\xe8\xbe\x93\xe5\x85\xa5\xe7\x9a\x84\xe7\x9b\xae\xe5\xbd\x95\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8\xef\xbc\x81')
        return False

    #拷贝文件路径的界面
    def mySeparateFrame(self):
        self.panelReslut = ''
        self.selectFrame=1
        p = nuke.Panel('New Copy Path Tools')
        p.addBooleanCheckBox ("0",True)
        p.addBooleanCheckBox ("1",False)
        p.addBooleanCheckBox ("2",False)
        p.setWidth(200)
        p.addSingleLineInput('New Copy', '')
        p.addButton('Cancel')
        p.addButton('Apply')
        p.setWidth(350)
        self.panelReslut = p.show()
        if p.value('0'):
            if p.value('1') or p.value('2'):
                nuke.message("\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe9\xa1\xb9\xef\xbc\x81")
                return False
            else:
                self.selectFrame=1

        elif p.value('1'):
            if p.value('2'):
                nuke.message("\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe9\xa1\xb9\xef\xbc\x81")
                return
            else:
                self.selectFrame=2

        elif p.value('2'):
            self.selectFrame=3

        if self.panelReslut:
            newCopyPath = p.value('New Copy')
            if newCopyPath and os.path.isdir(newCopyPath):
                if os.access(newCopyPath, os.W_OK):
                    self.objectPath = os.path.join(newCopyPath, self.myFileSBName[0], self.myFileSBName[1], self.myFileSBName[2])
                    return True
                else:
                    nuke.message('\xe4\xbd\xa0\xe4\xb8\x8d\xe5\x85\xb7\xe6\x9c\x89\xe8\xaf\xa5\xe8\xb7\xaf\xe5\xbe\x84\xe7\x9a\x84\xe5\x86\x99\xe5\x85\xa5\xe6\x9d\x83\xe9\x99\x90\xef\xbc\x81')
            else:
                nuke.message('\xe8\xbe\x93\xe5\x85\xa5\xe7\x9a\x84\xe7\x9b\xae\xe5\xbd\x95\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8\xef\xbc\x81')
        return False

    def delMyBackdrops(self):
        allMyBackdrops = nuke.allNodes('BackdropNode')
        for myBackdrop in allMyBackdrops:
            namebackdrop = myBackdrop.knob('name').value()
            if namebackdrop.find('Lack Frames') >= 0 or namebackdrop.find('Wrong Name') >= 0:
                nuke.delete(myBackdrop)

    def setSelecteNone(self):
        allmySelectedNodes = nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)

    def setMyReadsSelected(self, myReads):
        self.setSelecteNone()
        if myReads:
            for myRead in myReads:
                myRead.setSelected(True)

    def mySortNum(self, oriNum):
        sortNum = []
        tmpNum = [0,0]
        flag = False
        for i,num in enumerate(oriNum):
            if i<=len(oriNum)-2:
                if num != oriNum[i+1]-1:
                    if num != tmpNum[1]:
                        sortNum.append(num)
                    else:
                        sortNum.append(list(tmpNum))
                    flag = False
                else:
                    if not flag:
                        tmpNum[0] = num
                        tmpNum[1] = oriNum[i+1]
                        flag = True
                    else:
                        tmpNum[1] = oriNum[i+1]
            else:
                if num != oriNum[i-1]+1:
                    sortNum.append(num)
                    flag = False
                else:
                    tmpNum[1] = num
                    sortNum.append(tmpNum)
        return sortNum

    #检查缺帧
    def myCheckFrames(self):
        self.delMyBackdrops()
        self.myReadsNameDict.clear()
        self.myReadsStartDict.clear()
        self.myReadsLastDict.clear()
        j = 1
        addBackdropFlag = False
        noFileList = {}
        if self.myReads:
            for read in self.myReads:
                readFilePath = read['file'].value()
                if readFilePath:
                    fileType = os.path.splitext(readFilePath)[-1]
                    readFileStart = read['first'].value()
                    readFileLast = read['last'].value()
                    self.myReadsNameDict.update({read: readFilePath})
                    self.myReadsStartDict.update({read: readFileStart})
                    self.myReadsLastDict.update({read: readFileLast})
                    #查询位数
                    #numPlaces = len('%d' % readFileLast)
                    print readFilePath
                    self.setSelecteNone()
                    read.setSelected(True)
                    numPlaces=int(readFilePath.split("/")[-1].split(".")[-2].split("%0")[-1].split('d')[0])

                    if fileType != '.mov' and readFileStart != readFileLast:
                        k = []
                        pathSplit=readFilePath.split('/')
                        joinPath='/'.join(pathSplit[0:-1])
                        sequences=pyseq.getSequences(joinPath)
                        #k=sequences[0].missing()
                        for i in range(readFileStart, readFileLast+self.selectFrame,self.selectFrame):
                            
                            checkPath = readFilePath.replace(('.%'+'0%dd' % numPlaces), (('.%'+'0%dd' % numPlaces) % i))
                            print checkPath
                            if not os.path.isfile(checkPath):
                                print "aaa\n"
                                k.append(i)
                        if k:

                            sortNum = self.mySortNum(k)
                            numTT = ''
                            lenNum = len(sortNum)
                            for nn in sortNum:
                                if str(type(nn)).find('int')>=0:
                                    numTT +='%s,' % nn
                                else:
                                    numTT +='%s-%s,' % (nn[0], nn[1])
                            tmpText = readFilePath+'\n'+numTT[:-1]

                            if not tmpText in noFileList.values():
                                noFileList.update({read.name(): tmpText})
                            addBackdropFlag = True
                    else:
                        if not os.path.isfile(readFilePath):
                            if not readFilePath in noFileList.values():
                                noFileList.update({read.name(): readFilePath})
                            addBackdropFlag = True
                    if addBackdropFlag:
                            self.setSelecteNone()
                            read.setSelected(True)
                            myBackdrop = nukescripts.autoBackdrop()
                            myBackdrop.knob('tile_color').setValue(4278190335L)
                            myBackdrop.knob('name').setValue('Lack Frames %s' % j)
                            myBackdrop.knob('label').setValue('\xe7\xbc\xba\xe5\xb8\xa7')
                            addBackdropFlag = False
                            j = j+1
                    self.setSelecteNone()
        return noFileList

    def knobChanged(self, knob):
        if knob == self.refereshButton:
            readStr = ''
            if self.buttonModeType == 1:
                noFileList = self.myCheckFrames()
                if noFileList:
                    for eachFile in noFileList.keys():
                        readStr = eachFile + ':  ' + noFileList[eachFile] + '\n'
                self.textKnob.setValue(readStr)
            elif self.buttonModeType == 2:
                errorNameList = []
                errorNameList = self.myCheckFileName()
                if errorNameList:
                    readStr = "\n".join(errorNameList)
                    self.textKnob.setValue(readStr)

    def myCheckFileName(self):
        self.delMyBackdrops()
        errorNameList = []
        self.myFileLastNameDict.clear()
        self.myReadsNameDict.clear()
        if self.myReads:
            for read in self.myReads:
                readFilePath = read['file'].value()
                if readFilePath:
                    self.myReadsNameDict.update({read: readFilePath})
            if self.myReadsNameDict:
                j = 1
                for myReadD in self.myReadsNameDict:
                    myFileFullName = self.myReadsNameDict[myReadD]
                    pathSplit = myFileFullName.split('/')
                    if pathSplit:
                        findFlag = False
                        pathSplitR = list(pathSplit)
                        pathSplitR.reverse()
                        for i, myPath in enumerate(pathSplitR):
                            #print myPath
                            if i > 1:
                                myPathSplit = myPath.split('_')
                                numMyPathSplit = len(myPathSplit)
                                if numMyPathSplit > 2:
                                    serProjectPath = os.path.join(PROJECT_PATH, myPathSplit[0], r'Project\scenes\animation', myPathSplit[1], myPathSplit[2])
                                    if os.path.isdir(serProjectPath):
                                        findFlag = True
                                        break
                        if findFlag:
                            lastPath = '\\'.join(pathSplit[-i-1::])
                            self.myFileLastNameDict.update({myReadD: lastPath})
                            findFlag = False
                        else:
                            self.setSelecteNone()
                            myReadD.setSelected(True)
                            myBackdrop = nukescripts.autoBackdrop()
                            myBackdrop.knob('tile_color').setValue(4278255615L)
                            myBackdrop.knob('name').setValue('Wrong Name %s' % j)
                            myBackdrop.knob('label').setValue('\xe9\x94\x99\xe8\xaf\xaf')
                            errorNameList.append(myReadD.name()+": "+myFileFullName)
                            j += 1
        return errorNameList

    #分类处字典中相同和不同的数据
    def sortInDict(self, inDict):
        myDict = dict(inDict)
        #相同位置的字典，数据类型{地址: [节点群]}
        mySamePathReads = {}
        #相同位置的节点列表
        mySameReads = []
        #不同位置的节点列表
        myDiffReads = []
        for i in myDict.keys():
            k = 0
            n = []
            for j in myDict.keys():
                if myDict[i] and myDict[i] == myDict[j]:
                    n.append(j)
                    k += 1
            if k > 1:
                mySamePathReads.update({myDict[i]: n})
                for p in n:
                    myDict[p] = None
                    mySameReads.append(p)
                k = 0
        myDiffReads = list(set(self.myReads)-set(mySameReads))
        #返回的是字典和列表
        return [mySamePathReads, mySameReads, myDiffReads]

    def sortCopyData(self):
        self.allCopyData.clear()
        self.allSetData.clear()
        allFilePath = {}
        allFileLastPaths = {}
        #所有末端素材路径
        allFileLastPaths = dict(self.myFileLastNameDict)
        #所有素材路径
        allFilePath = dict(self.myReadsNameDict)
        #取出末端路径的素材节点，和相同素材
        tmp = self.sortInDict(allFileLastPaths)
        allSameLastPath = tmp[0]
        allDifferentLastReads = tmp[2]
        #取出相同路径的素材节点,先处理相同素材的
        tmp = self.sortInDict(allFilePath)
        allSameFullPath = tmp[0]
        allSameFullReads = tmp[1]
        #第一步处理路径完全相同的素材
        #第一步最终的拷贝路径数组，不允许出现一样，导致数据丢失
        allmySerCopyPath = []
        for sameFullPath in allSameFullPath.keys():
            startFV = 100000000
            lastFV = -100000000
            for i, myFullRead in enumerate(allSameFullPath[sameFullPath]):
                sameFlag = False
                #采集设置数据
                if i == 0:
                    tmpPath = self.myFileLastNameDict[myFullRead]
                    tmpFullSerpath = os.path.join(self.objectPath, tmpPath)
                    mySerCopyPath = os.path.dirname(tmpFullSerpath)
                    tmpLocalFullDirPath = os.path.dirname(sameFullPath)
                    #判断当路径一样时不加入拷贝和设置数据里
                    if mySerCopyPath == tmpLocalFullDirPath:
                        sameFlag = True
                        break
                    #当原路径和拷贝路径不一样时：需要排除后段一样的可能
                    if mySerCopyPath in allmySerCopyPath:
                        tmpPathSplit = tmpPath.split('\\')
                        while True:
                            k = 0
                            if len(tmpPathSplit) > 1:
                                tmpPathSplit[1] = '%s_s%s' % (tmpPathSplit[1], k)
                            else:
                                tmpPathSplit.insert(0, '%s_s%s' % (tmpPathSplit[0], k))
                            tmpPath = '\\'.join(tmpPathSplit)
                            tmpFullSerpath = os.path.join(self.objectPath, tmpPath)
                            mySerCopyPath = os.path.dirname(tmpFullSerpath)
                            if not mySerCopyPath in allmySerCopyPath:
                                break
                            k += 1
                startLV = self.myReadsStartDict[myFullRead]
                lastLV = self.myReadsLastDict[myFullRead]
                #判断完全相同的素材最小和最大的帧数
                if startLV < startFV:
                    startFV = startLV
                if lastLV > lastFV:
                    lastFV = lastLV
                self.allSetData.update({myFullRead: tmpFullSerpath})
                #采集拷贝数据
            if not sameFlag:
                self.allCopyData.update({sameFullPath: [startFV, lastFV, mySerCopyPath]})
                allmySerCopyPath.append(mySerCopyPath)
        #第二部：处理末端素材相同的素材，需要排除上一步处理完的数据
        for samLastPath in allSameLastPath.keys():
            mySameLastReads = []
            for myLastRead in allSameLastPath[samLastPath]:
                #如果素材节点是第一步的则忽略加入处理
                if not myLastRead in allSameFullReads:
                    mySameLastReads.append(myLastRead)
            if mySameLastReads:
                j = 1
                for samLastRead in mySameLastReads:
                    mySamePath = self.myFileLastNameDict[samLastRead]
                    mySPathSplit = mySamePath.split('\\')
                    if len(mySPathSplit) > 1:
                        mySPathSplit[1] = '%s_%s' % (mySPathSplit[1], j)
                    else:
                        mySPathSplit.insert(0, '%s_%s' % (mySPathSplit[0], j))
                    j += 1
                    tmpPath = '\\'.join(mySPathSplit)
                    tmpFullSerpath = os.path.join(self.objectPath, tmpPath)
                    mySerCopyPath = os.path.dirname(tmpFullSerpath)
                    tmpFullLocalPath = self.myReadsNameDict[samLastRead]
                    tmpFullLocalDirPath = os.path.dirname(tmpFullLocalPath)
                    if mySerCopyPath == tmpFullLocalDirPath:
                        continue
                    self.allSetData.update({samLastRead: tmpFullSerpath})
                    startLV = self.myReadsStartDict[samLastRead]
                    lastLV = self.myReadsLastDict[samLastRead]
                    self.allCopyData.update({tmpFullLocalPath: [startLV, lastLV, mySerCopyPath]})
        #第三步：处理素材路径完全不一样的
        for differentLastRead in allDifferentLastReads:
            #采集设置数据
            tmpPath = self.myFileLastNameDict[differentLastRead]
            tmpFullSerpath = os.path.join(self.objectPath, tmpPath)
            mySerCopyPath = os.path.dirname(tmpFullSerpath)
            tmpFullLocalPath = self.myReadsNameDict[differentLastRead]
            tmpFullLocalDirPath = os.path.dirname(tmpFullLocalPath)
            if mySerCopyPath == tmpFullLocalDirPath:
                continue
            self.allSetData.update({differentLastRead: tmpFullSerpath})
            #采集拷贝数据
            startLV = self.myReadsStartDict[differentLastRead]
            lastLV = self.myReadsLastDict[differentLastRead]
            self.allCopyData.update({self.myReadsNameDict[differentLastRead]: [startLV, lastLV, mySerCopyPath]})
            if not (self.allCopyData and self.allSetData):
                return False
        return True

    def copyAndSetJob(self):
        if self.allCopyData:
            self.myProgressWin = nuke.ProgressTask('My Copy Job', len(self.allCopyData))
            for i, myLocalPath in enumerate(self.allCopyData.keys()):
                tmpValue = self.allCopyData[myLocalPath]
                startFV = tmpValue[0]
                lastFV = tmpValue[1]
                #numPlaces = len('%d' % startFV)
                numPlaces=int(myLocalPath.split("/")[-1].split(".")[-2].split("%0")[-1].split('d')[0])
                mySerPath = tmpValue[2]
                fileRFlag = False
                if os.path.isdir(mySerPath):
                    fileRFlag = True
                else:
                    os.makedirs(mySerPath)
                    fileRFlag = False
                allCopyLocalpath = []
                if startFV == lastFV:
                    if os.path.isfile(myLocalPath):
                        tmpPath = myLocalPath
                    else:
                        tmpPath = myLocalPath.replace(('.%'+'0%dd' % numPlaces), (('.%'+'0%dd' % numPlaces) % startFV))
                    if fileRFlag:
                        myBasename = os.path.basename(tmpPath)
                        testPath = os.path.join(mySerPath, myBasename)
                        if os.path.isfile(testPath):
                            testMtime = os.path.getmtime(testPath)
                            tmpMtime = os.path.getmtime(tmpPath)
                            if int(testMtime) > int(tmpMtime):
                                break
                    allCopyLocalpath.append(tmpPath)
                    if allCopyLocalpath:
                        if not self.CopyDataJob([allCopyLocalpath, mySerPath]):
                            del self.myProgressWin
                            nuke.message('\xe6\x8b\xb7\xe8\xb4\x9d\xe8\xa2\xab\xe4\xb8\xad\xe6\x96\xad\xef\xbc\x81')
                else:
                    for frame in range(startFV, (lastFV+self.selectFrame),self.selectFrame):
                        tmpPath = myLocalPath.replace(('.%'+'0%dd' % numPlaces), (('.%'+'0%dd' % numPlaces) % frame))
                        if fileRFlag:
                            myBasename = os.path.basename(tmpPath)
                            testPath = os.path.join(mySerPath, myBasename)
                            if os.path.isfile(testPath):
                                testMtime = os.path.getmtime(testPath)
                                tmpMtime = os.path.getmtime(tmpPath)
                                if int(testMtime) > int(tmpMtime):
                                    continue
                        allCopyLocalpath.append(tmpPath)
                    if allCopyLocalpath:
                        if not self.CopyDataJob([allCopyLocalpath, mySerPath]):
                            del self.myProgressWin
                            nuke.message('\xe6\x8b\xb7\xe8\xb4\x9d\xe8\xa2\xab\xe4\xb8\xad\xe6\x96\xad\xef\xbc\x81')
                self.myProgressWin.setProgress(i+1)
            if self.allSetData:
                for myRead in self.allSetData.keys():
                    myRead['file'].setValue('%s' % self.allSetData[myRead].replace('\\', '/'))
            del self.myProgressWin
        return True

    def doShowFramesResult(self):
        self.buttonModeType = 1
        readStr = ''
        noFileList = {}
        noFileList = self.myCheckFrames() #检查帧数的完整性
        #缺帧的节点名，路径和帧数
        if noFileList:
            for eachFile in noFileList.keys():
                readStr = eachFile + ':  ' + noFileList[eachFile] + '\n'
            nukescripts.registerPanel('checkFrame', myCheckFile)
            self.textKnob.setValue(readStr)
            #self.show()
            return False
        return True

    def doShowFileNameResult(self):
        self.buttonModeType = 2
        errorNameList = []
        errorNameList = self.myCheckFileName() #检查文件名是否与服务器上相同
        if errorNameList:
            nukescripts.registerPanel('checkFileName', myCheckFile)
            readStr = "\n".join(errorNameList)
            self.textKnob.setValue(readStr)
            #self.show()
            return False
        return True

    def myJob(self, myModel):
        selectFlag = False
        if myModel < 3:
            self.myReads = nuke.selectedNodes('Read')
            if len(self.myReads) == 0:
                selectFlag = False
                self.myReads = nuke.allNodes('Read')
            else:
                selectFlag = True
        else:
            self.myReads = nuke.allNodes('Read')
        #打X的素材不在拷贝范围内
        if self.myReads:
            tmpList = []
            for eachRead in self.myReads:
                if not eachRead['disable'].value():
                    tmpList.append(eachRead)
            self.myReads = tmpList
        if len(self.myReads) == 0:
            nuke.message('\xe6\xb2\xa1\xe6\x9c\x89\xe5\x8f\xaf\xe6\x8b\xb7\xe8\xb4\x9d\xe7\x9a\x84\xe7\xb4\xa0\xe6\x9d\x90\xef\xbc\x81')
            return
        else:
            showFlag = False
            if myModel == 1:
                if self.doShowFramesResult():
                    self.setMyReadsSelected(self.myReads)
                    showFlag = True
                    if selectFlag:
                        nuke.message('\xe6\x89\x80\xe9\x80\x89  \xe7\xb4\xa0\xe6\x9d\x90\xe5\x9c\xa8\xe7\x9b\xb8\xe5\xba\x94\xe7\x9a\x84\xe5\xb8\xa7\xe6\x95\xb0\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe6\x98\xaf\xe5\xae\x8c\xe6\x95\xb4\xe7\x9a\x84\xef\xbc\x81')
                    else:
                        nuke.message('\xe6\x89\x80\xe6\x9c\x89\xe7\xb4\xa0\xe6\x9d\x90\xe5\x9c\xa8\xe7\x9b\xb8\xe5\xba\x94\xe7\x9a\x84\xe5\xb8\xa7\xe6\x95\xb0\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe6\x98\xaf\xe5\xae\x8c\xe6\x95\xb4\xe7\x9a\x84\xef\xbc\x81')
                if not showFlag:
                    self.setMyReadsSelected(self.myReads)
            elif myModel == 2:
                if self.doShowFileNameResult():
                    self.setMyReadsSelected(self.myReads)
                    showFlag = True
                    if selectFlag:
                        nuke.message('\xe6\x89\x80\xe9\x80\x89  \xe7\xb4\xa0\xe6\x9d\x90\xe7\x9a\x84\xe5\x91\xbd\xe5\x90\x8d\xe7\xac\xa6\xe5\x90\x88\xe8\xa7\x84\xe8\x8c\x83\xef\xbc\x81')
                    else:
                        nuke.message('\xe6\x89\x80\xe6\x9c\x89\xe7\xb4\xa0\xe6\x9d\x90\xe7\x9a\x84\xe5\x91\xbd\xe5\x90\x8d\xe7\xac\xa6\xe5\x90\x88\xe8\xa7\x84\xe8\x8c\x83\xef\xbc\x81')
                if not showFlag:
                    self.setMyReadsSelected(self.myReads)
            elif myModel == 3:
                if self.myCheckProjectName():   #检查nuke的项目名是否和文件夹的项目名相同
                    if self.myGetCopypath():  #获取新的路径(素材拷贝到新的路径下)
                        if self.doShowFramesResult():
                            if self.doShowFileNameResult():
                                if self.sortCopyData():
                                    self.copyAndSetJob()
                                    nuke.message('\xe6\x8b\xb7\xe8\xb4\x9d\xe5\x92\x8c\xe8\xae\xbe\xe7\xbd\xae\xe8\xb7\xaf\xe5\xbe\x84\xe5\xae\x8c\xe6\x88\x90\xef\xbc\x81')
                                else:
                                    nuke.message('\xe6\xb2\xa1\xe6\x9c\x89\xe6\x95\xb0\xe6\x8d\xae\xe9\x9c\x80\xe8\xa6\x81\xe6\x8b\xb7\xe8\xb4\x9d')
            elif myModel == 4:
                if self.myCheckProjectName():
                    if self.mySeparateFrame():
                        if self.doShowFramesResult():
                            if self.doShowFileNameResult():
                                if self.sortCopyData():
                                    self.copyAndSetJob()
                                    nuke.message('\xe6\x8b\xb7\xe8\xb4\x9d\xe5\x92\x8c\xe8\xae\xbe\xe7\xbd\xae\xe8\xb7\xaf\xe5\xbe\x84\xe5\xae\x8c\xe6\x88\x90\xef\xbc\x81')
                                else:
                                    nuke.message('\xe6\xb2\xa1\xe6\x9c\x89\xe6\x95\xb0\xe6\x8d\xae\xe9\x9c\x80\xe8\xa6\x81\xe6\x8b\xb7\xe8\xb4\x9d')




# myNewJob = myCheckFile()
# myNewJob.myJob(1)