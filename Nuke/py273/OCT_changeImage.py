# -*- coding: utf-8 -*-
import nuke
import os
import shutil
import threading

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
                shutil.copyfile(self.sourcePath, self.destPath) 
                #shutil.copy2(self.sourcePath, self.destPath)
            except:
                print '%s  \xe6\x8b\xb7\xe8\xb4\x9d\xe5\x87\xba\xe9\x94\x99' % self.sourcePath

    def stop(self):
        self.__stop = True


class OCT_changeImage():    
    def __init__(self):
        #界面返回值
        self.panleResult=""
        #进度条
        self.myProgressWin=""
        self.worker1 = CopyJobThreading(self)
        self.worker1.setDaemon(False)
        self.worker2 = CopyJobThreading(self)
        #设置子进程是否随主线程一起结束，必须在start()之前调用。
        self.worker2.setDaemon(False)

    def CopyDataJob(self, myDict):
        print myDict
        i = 0
        self.myProgressWin = nuke.ProgressTask('My Copy Job', len(myDict))
        for key in myDict.keys():
            mySourceFile = myDict[key]
            myDestFile = key
            if self.myProgressWin.isCancelled() is True:
                return False
            if i == 0:
                print 0
                self.worker1.sourcePath = mySourceFile
                self.worker1.destPath = myDestFile
                try:
                    self.worker1.start()
                except:
                    self.worker1.run()
            elif i == 1:
                print 1
                self.worker2.sourcePath = mySourceFile
                self.worker2.destPath = myDestFile
                try:
                    self.worker2.start()
                except:
                    self.worker2.run()
            else:
                while True:
                    #检查线程是否运行
                    print mySourceFile
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
            i += 1
            self.myProgressWin.setProgress(i)
        while self.worker1.isAlive() is False and self.worker2.isAlive() is False:
            break
        return True


    def myFindPanel(self):
        p = nuke.Panel('Frame change')
        p.setWidth(250)
        p.addSingleLineInput('Old Path', '') 
        p.addSingleLineInput('New Path', '') 
        p.addSingleLineInput('24startFrame', '') 
        p.addSingleLineInput('24endFrame', '') 
        p.addSingleLineInput('48startFrame', '')
        p.addButton('Cancel')
        p.addButton('OK')
        self.panleResult = p.show() 
        oldpath = p.value('Old Path')
        newpath = p.value('New Path')
        startFrame = p.value('24startFrame')
        endFrame = p.value('24endFrame')
        startFrame1 = p.value('48startFrame')

        if self.panleResult:
            if not os.path.isdir(oldpath) or not os.path.isdir(newpath):
                nuke.message('\xe4\xbd\xa0\xe8\xbe\x93\xe5\x85\xa5\xe7\x9a\x84\xe8\xb7\xaf\xe5\xbe\x84\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8\xef\xbc\x81')
            oldpath,newpath=self.myChangeNetPath(oldpath,newpath)
            self.myChangeImage(oldpath, newpath, startFrame, endFrame, startFrame1)

    def myChangeNetPath(self,oldpath,newpath):
        if oldpath.find('z:') >= 0:
            oldpath = oldpath.replace('z:', r'\\octvision.com\cg')
        elif oldpath.find('Z:') >= 0:
            oldpath = oldpath.replace('Z:', r'\\octvision.com\cg')
        elif oldpath.find('M:') >= 0:
            oldpath = oldpath.replace('M:', r'\\file2.nas\share')
        elif oldpath.find('m:') >= 0:
            oldpath = oldpath.replace('m:', r'\\file2.nas\share')

        if newpath.find('z:') >= 0:
            newpath = newpath.replace('z:', r'\\octvision.com\cg')
        elif newpath.find('Z:') >= 0:
            newpath = newpath.replace('Z:', r'\\octvision.com\cg')
        elif newpath.find('M:') >= 0:
            newpath = newpath.replace('M:', r'\\file2.nas\share')
        elif newpath.find('m:') >= 0:
            newpath = newpath.replace('m:', r'\\file2.nas\share')

        return [oldpath,newpath]

    def myChangeImage(self, oldpath, newpath, startFrame, endFrame, startFrame1):
        #print oldpath
        all = os.listdir(oldpath)
        all=sorted(all)
        i=0
        copyData = {}
        allCopyLocalpath = []
        for fileName in all:
            if fileName != "Thumbs.db":
                file_path = os.path.join(oldpath, fileName)
                listSplit = fileName.split(".")
                #num1 = int(listSplit[1])+i*2
                #num2 = int(listSplit[1])+i*2-1
                if startFrame != "" and endFrame != "":
                    if int(listSplit[1]) >= int(startFrame) and int(listSplit[1]) <= int(endFrame):
                        allCopyLocalpath.append(file_path)

                elif startFrame == "" and endFrame == "":
                    allCopyLocalpath.append(file_path)

       # print allCopyLocalpath

        
        for myLocalPath in allCopyLocalpath:
            fileName  = myLocalPath.split("\\")[-1]
            listSplit = fileName.split(".")
            #print fileName
            num1 = int(startFrame1)+i
            num2 = int(startFrame1)+i+1
            numPlaces1='%04d'%num1
            numPlaces2='%04d'%num2
            newName1 = (listSplit[0] + '.' + str(numPlaces1) + '.' + listSplit[-1])
            newName2 = (listSplit[0] + '.' + str(numPlaces2) + '.' + listSplit[-1])
            newfilePath1 = os.path.join(newpath, newName1)
            newfilePath2 = os.path.join(newpath, newName2)

            copyData.update({newfilePath2:myLocalPath})
            copyData.update({newfilePath1:myLocalPath})
            
    
            i = i+2
       
        if not self.CopyDataJob(copyData):
            del self.myProgressWin
            nuke.message('\xe6\x8b\xb7\xe8\xb4\x9d\xe8\xa2\xab\xe4\xb8\xad\xe6\x96\xad\xef\xbc\x81')

        del self.myProgressWin
        return True

#OCT_changeImage().myFindPanel()