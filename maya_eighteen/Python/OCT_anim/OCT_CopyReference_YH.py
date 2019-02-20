#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import maya.OpenMayaUI as apiUI
import maya.cmds as mc
import maya.mel as mm
import os, re, shutil
import sys
import sip
import maya.OpenMaya as om

__author__ = 'yangh'

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#UI类
class CopyReferenceUI():
    def setUI(self, CopyReferenceDialog):
        CopyReferenceDialog.setObjectName(_fromUtf8("CopyReferenceDialog"))
        CopyReferenceDialog.resize(200, 100)
        font = QtGui.QFont()
        font.setPointSize(11)
        CopyReferenceDialog.setFont(font)
        CopyReferenceDialog.setWindowTitle(_fromUtf8(u"copy refence file"))

        self.verticalLayout = QtGui.QVBoxLayout(CopyReferenceDialog)

        self.copyReference = QtGui.QPushButton(CopyReferenceDialog)
        self.updateRefence = QtGui.QPushButton(CopyReferenceDialog)
        self.modifyPath = QtGui.QPushButton(CopyReferenceDialog)

        self.copyReference.setText(_fromUtf8(u"CopyReferenceToLocal"))
        self.updateRefence.setText(_fromUtf8(u"UpdateLocalReference"))
        self.modifyPath.setText(_fromUtf8(u"modifyPathReferenceToServer"))

        self.copyReference.setFont(font)
        self.updateRefence.setFont(font)
        self.modifyPath.setFont(font)

        self.verticalLayout.addWidget(self.copyReference)
        self.verticalLayout.addWidget(self.updateRefence)
        self.verticalLayout.addWidget(self.modifyPath)


class JobThread(QtCore.QThread):
    def __init__(self, parent = None):
        super(JobThread, self).__init__(parent)

    def __del__(self):
        self.wait()

    def ready(self, source, dest):
        self.mySource = source
        self.myDest = dest
        self.start()

    def run(self):
        try:
            shutil.copy2(self.mySource, self.myDest)
        except:
            print "sss"
            om.MGlobal.displayWarning("copy file Error")

#获取maya的窗口Api
def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

#执行方法：1、拷贝网上的参考文件放本机E盘参考
#          2、更新本地参考
#          3、转换到网络路径

class CopyReferenceTool(QtGui.QDialog):
    def __init__(self, parent = getMayaWindow()):
        super(CopyReferenceTool, self).__init__(parent)
        self.project_path = r'\\octvision.com\CG\Themes'
        self.project_pathz = r'Z:\Themes'

        #存放目标和原文件
        self.freeMV = ""

        self.ui = CopyReferenceUI()
        self.ui.setUI(self)
        self.setUpGui()

        self.worker1 = JobThread(self)
        self.worker2 = JobThread(self)

    def setUpGui(self):
        copyReference = self.ui.copyReference
        copyReference.clicked.connect(self.copyReference)
        updateRefence = self.ui.updateRefence
        updateRefence.clicked.connect(self.copyReference)
        modifyPath = self.ui.modifyPath
        modifyPath.clicked.connect(self.modifyReferencePath)

    def modifyReferencePath(self):
        allReferences = mc.file(q=True, reference =True)
        for reference in allReferences:
            refences = reference.split("{")[0]
            scrFilePathSplit = refences.split("/")
            scrFilePathJoin = "\\".join(scrFilePathSplit)

            destFilePath=scrFilePathJoin.replace("E:\\REF","Z:\\Themes")

            if os.path.isfile(destFilePath):
                referenceNode=mc.file(refences,q=True,referenceNode=True)
                mc.file(destFilePath, loadReference=referenceNode)
            else:
                print destFilePath
                mc.confirmDialog(message=destFilePath+u" file not exists!",button="OK")

    #更新参考
    def updateRefence(self):
        allReferences = mc.file(q=True, reference =True)
        fileFile = {}
        for refence in allReferences:
            if "E:/REF" in refence:
                refences = refence.split("{")[0]
                scrFilePathSplit = refences.split("/")
                scrFilePathJoin = "\\".join(scrFilePathSplit[:-1])

                #sourcePath存放目标路径，E\\REF
                sourcePath = scrFilePathJoin.replace('E:\\REF', self.project_path)
                sourceFile = sourcePath + "\\" + scrFilePathSplit[-1]

                if os.path.isfile(sourceFile) and os.path.isfile(refences):
                    tempMtime = os.path.getmtime(refences)
                    testMtime = os.path.getmtime(sourceFile)
                    tempSize = os.path.getsize(refences)
                    testSize = os.path.getsize(sourceFile)

                    if int(testMtime) > int(tempMtime) or tempSize != testSize:
                        fileFile.update({sourceFile:refences})
        if fileFile:
            self.CopyFileJob(fileFile)

    #参考物体拷贝到本机
    def copyReference(self):
        #检查C盘大小
        freeSV = mm.eval('strip(system("wmic LogicalDisk where Caption=\'E:\' get FreeSpace /value"))')
        self.freeMV = re.sub("\D", "", freeSV)

        if self.freeMV < 5400000000:
            mc.confirmDialog(message = "E: Disk space is too small ")
           #mc.confirmDialog(message=u"E:盘空间过小将影响性能，建议马上清理磁盘空间", button="OK")
            return

        allReferences = mc.file(q=True, reference =True)
        fileFile = {}
        setFile = {}
        for refence in allReferences:
            refences = refence.split("{")[0]
            scrFilePathSplit = refences.split("/")
            scrFilePathJoin = "\\".join(scrFilePathSplit[:-1])

            #destFilePath存放目标路径，E\\REF
            destFilePath = scrFilePathJoin.replace(self.project_path, 'E:\\REF')
            destFilePath = destFilePath.replace(self.project_pathz,'E:\\REF')

            if not os.path.isdir(destFilePath):
                os.makedirs(destFilePath)

            #目标文件
            destFile = destFilePath+"\\"+scrFilePathSplit[-1]
            refences = refences.replace("/", "\\")

            if os.path.isfile(refences) and not os.path.isfile(destFile) and "E:" not in refences:
                referenceNode = mc.file(refence, q = True, referenceNode = True)
                fileFile.update({refences:destFile})
                setFile.update({referenceNode:destFile})

            elif os.path.isfile(refences) and os.path.isfile(destFile) and "E:" not in refences:
                tempMtime = os.path.getmtime(destFile)
                testMtime = os.path.getmtime(refences)
                tempSize = os.path.getsize(destFile)
                testSize = os.path.getsize(refences)
                referenceNode = mc.file(refence, q = True, referenceNode = True)
                if int(testMtime) > int(tempMtime) or tempSize != testSize:
                    fileFile.update({refences:destFile})
                    setFile.update({referenceNode:destFile})
                else:
                    setFile.update({referenceNode:destFile})

        if fileFile:
            self.CopyFileJob(fileFile)

        if setFile:
            for keys in setFile.keys():
                print keys
                print setFile
                mc.file(setFile[keys], loadReference = keys)

    #线程拷贝文件
    def CopyFileJob(self, fileFile):
        i = 0
        for keys in fileFile.keys():
            source = keys
            dest = fileFile[keys]

            if i == 0:
                self.worker1.ready(source, dest)
            elif i == 1:
                self.worker2.ready(source, dest)
            else:
                while True:
                    if self.worker1.isFinished():
                        self.worker1.ready(source, dest)
                        break
                    elif self.worker2.isFinished():
                        self.worker2.ready(source, dest)
                        break
            i += 1
        while True:
            if self.worker1.wait() and self.worker2.wait():
                break


if __name__ == "__main__":
    CopyReferenceTools = CopyReferenceTool()
    CopyReferenceTools.show()
