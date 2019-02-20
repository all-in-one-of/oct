#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import maya.OpenMayaUI as apiUI
import maya.cmds as mc
import sip
import sys
import os
import shutil
import maya.OpenMaya as om

OCT_DRIVE = r'\\octvision.com\cg'
OCT_FilePath = r'\\file.com\share'
OCT_MDRIVE = r'\\file2.nas\share'

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog():
    def setupUi(self, Dialog, fileType):
        self.fileType = fileType
        Dialog.setObjectName(_fromUtf8("%sDialog"%fileType))
        Dialog.resize(659, 392)
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(1205)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.titileLabel = QtGui.QLabel(Dialog)
        font1 = QtGui.QFont()
        font1.setPointSize(16)
        self.titileLabel.setFont(font1)
        self.titileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titileLabel.setObjectName(_fromUtf8("titileLabel"))
        self.gridLayout.addWidget(self.titileLabel, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.pathLineEdit = QtGui.QLineEdit(Dialog)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.horizontalLayout_2.addWidget(self.pathLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkPushButton = QtGui.QPushButton(Dialog)
        self.checkPushButton.setFont(font)
        self.checkPushButton.setStyleSheet("background-color: rgb(97, 21, 93)")
        self.checkPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.checkPushButton.setObjectName(_fromUtf8("checkPushButton"))
        self.horizontalLayout_3.addWidget(self.checkPushButton)
        self.ChangeSelectedPushButton = QtGui.QPushButton(Dialog)
        self.ChangeSelectedPushButton.setFont(font)
        self.ChangeSelectedPushButton.setStyleSheet("background-color: rgb(67, 98, 21)")
        self.ChangeSelectedPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ChangeSelectedPushButton.setObjectName(_fromUtf8("ChangeSelectedPushButton"))
        self.horizontalLayout_3.addWidget(self.ChangeSelectedPushButton)
        self.SelectAllPushButton = QtGui.QPushButton(Dialog)
        self.SelectAllPushButton.setFont(font)
        self.SelectAllPushButton.setStyleSheet("background-color: rgb(97, 21, 93)")
        self.SelectAllPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.SelectAllPushButton.setObjectName(_fromUtf8("SelectAllPushButton"))
        self.horizontalLayout_3.addWidget(self.SelectAllPushButton)
        self.ChangePushButton = QtGui.QPushButton(Dialog)
        self.ChangePushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.ChangePushButton.setFont(font)
        self.ChangePushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ChangePushButton.setObjectName(_fromUtf8("ChangePushButton"))
        self.horizontalLayout_3.addWidget(self.ChangePushButton)
        self.copySelectPushButton = QtGui.QPushButton(Dialog)
        self.copySelectPushButton.setFont(font)
        self.copySelectPushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.copySelectPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.copySelectPushButton.setObjectName(_fromUtf8("copySelectPushButton"))
        self.horizontalLayout_3.addWidget(self.copySelectPushButton)
        self.copyAllPushButton = QtGui.QPushButton(Dialog)
        self.copyAllPushButton.setFont(font)
        self.copyAllPushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.copyAllPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.copyAllPushButton.setObjectName(_fromUtf8("copyAllPushButton"))
        self.horizontalLayout_3.addWidget(self.copyAllPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.reportTitleLabel = QtGui.QLabel(Dialog)
        self.reportTitleLabel.setFont(font)
        self.reportTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.reportTitleLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reportTitleLabel.setObjectName(_fromUtf8("reportTitleLabel"))
        self.horizontalLayout_1.addWidget(self.reportTitleLabel)
        self.reportLabel = QtGui.QLabel(Dialog)
        self.reportLabel.setFont(font)
        self.reportLabel.setObjectName(_fromUtf8("reportLabel"))
        self.horizontalLayout_1.addWidget(self.reportLabel)
        self.gridLayout.addLayout(self.horizontalLayout_1, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "%sFileManage"%self.fileType, None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "%sName"%self.fileType, None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Dialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.titileLabel.setText(QtGui.QApplication.translate("Dialog", "%sFile_Tools"%self.fileType, None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "DataPath:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkPushButton.setText(QtGui.QApplication.translate("Dialog", "Check %sFiles"%self.fileType, None, QtGui.QApplication.UnicodeUTF8))
        self.ChangeSelectedPushButton.setText(QtGui.QApplication.translate("Dialog", "Change Selected DataPath", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectAllPushButton.setText(QtGui.QApplication.translate("Dialog", "Select All Files", None, QtGui.QApplication.UnicodeUTF8))
        self.ChangePushButton.setText(QtGui.QApplication.translate("Dialog", "Change All DataPath", None, QtGui.QApplication.UnicodeUTF8))
        self.copySelectPushButton.setText(QtGui.QApplication.translate("Dialog", "Copy Selected Data", None, QtGui.QApplication.UnicodeUTF8))
        self.copyAllPushButton.setText(QtGui.QApplication.translate("Dialog", "Copy All Data", None, QtGui.QApplication.UnicodeUTF8))
        self.reportTitleLabel.setText(QtGui.QApplication.translate("Dialog", "Check Report:", None, QtGui.QApplication.UnicodeUTF8))
        self.reportLabel.setText(QtGui.QApplication.translate("Dialog", "Please press the \"Check %sFile\" button"%self.fileType, None, QtGui.QApplication.UnicodeUTF8))
        self.pathLineEdit.setText(QtGui.QApplication.translate("Dialog", "       Green: D:\work\Test\data\\test(Detail)\t\t\tBlue: D:\work\Test\data\(Sketchy)", None, QtGui.QApplication.UnicodeUTF8))


def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

class JobThread(QtCore.QThread):
    mySourceFile = None
    myDestFile = None

    def __init__(self, parent=None):
        super(JobThread, self).__init__(parent)

    def __del__(self):
        self.wait()

    def ready(self, source, dest):
        self.mySourceFile = source
        self.myDestFile = dest
        self.start()

    def run(self):
        try:
            shutil.copy2(self.mySourceFile, self.myDestFile)
        except:
            om.MGlobal.displayWarning(u'复制文件时出错')

class File_Tools(QtGui.QDialog):
    def __init__(self,fileType, nodeAttr, dirName, parent=getMayaWindow()):
        super(File_Tools, self).__init__(parent)

        #传过来的文件类型
        self.fileType = fileType
        #节点属性
        self.nodeAttr = nodeAttr

        #存放文件夹的命名
        self.dirName = dirName

        self.ui = Ui_Dialog()
        self.ui.setupUi(self, self.fileType)

        self.worker = JobThread(self)
       # self.worker = JobThread(self)
        self.setUpGui()

    def setUpGui(self):
        #取的控件
        treeWidget = self.ui.treeWidget
        ChangePushButton = self.ui.ChangePushButton
        checkPushButton = self.ui.checkPushButton
        ChangeSelectedPushButton = self.ui.ChangeSelectedPushButton
        SelectAllPushButton = self.ui.SelectAllPushButton
        copySelectPushButton = self.ui.copySelectPushButton
        copyAllPushButton = self.ui.copyAllPushButton
        
        #按钮的链接
        ChangePushButton.clicked.connect(self.ChangeAll)
        ChangeSelectedPushButton.clicked.connect(self.ChangeSelected)
        checkPushButton.clicked.connect(self.checkPath)
        SelectAllPushButton.clicked.connect(self.selectAllCache)
        copySelectPushButton.clicked.connect(self.copySelected)
        copyAllPushButton.clicked.connect(self.copyAll)
        treeWidget.itemClicked.connect(self.itemClick)

        #表格控制
        treeWidget.setColumnWidth(0, 180)

    #选择界面节点时选择场景中相应的节点
    def itemClick(self):
        mySelectedItems = []
        treeWidget = self.ui.treeWidget
        selecteditems = treeWidget.selectedItems()
        for item in selecteditems:
            childNum = item.childCount()
            if childNum:
                for i in range(childNum):
                    mySelectedItems.append('%s' % item.child(i).text(0))
            else:
                mySelectedItems.append('%s' % item.text(0))
        mc.select(mySelectedItems)

    #转换路径  
    def myChangeNetPath(self, TempPath):
        if TempPath.find('${OCTV_PROJECTS}') >= 0:
            TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
        elif TempPath.find('z:') >= 0:
            TempPath = TempPath.replace('z:', OCT_DRIVE)
        elif TempPath.find('Z:') >= 0:
            TempPath = TempPath.replace('Z:', OCT_DRIVE)
        elif TempPath.find('w:') >= 0:
            TempPath = TempPath.replace('w:', OCT_FilePath)
        elif TempPath.find('W:') >= 0:
            TempPath = TempPath.replace('W:', OCT_FilePath)
        elif TempPath.find('M:') >= 0:
            TempPath = TempPath.replace('M:', OCT_MDRIVE)
        elif TempPath.find('m:') >= 0:
            TempPath = TempPath.replace('m:', OCT_MDRIVE)
        return TempPath
    #获取输入的路径
    def getDatapath(self):
        path = '%s' % self.ui.pathLineEdit.text()
        return path

    def ChangeSelected(self):
        self.changePath(1)

    #转换所有路径self.fileType类型节点的路劲
    def ChangeAll(self):
        self.changePath(2)

    #转换所有路径self.fileType类型节点的路劲
    def ChangeAllPath(self):
        allFile = mc.ls(type = self.fileType)
        return allFile

    #拷贝选择节点数据
    def copySelected(self):
        self.copyData(1)

    #拷贝所有节点数据
    def copyAll(self):
        self.copyData(2)

    #转换被选择节点的路径
    def ChangeSelectedPath(self):
        mySelectedItems = []
        treeWidget = self.ui.treeWidget
        selecteditems = treeWidget.selectedItems()
        for item in selecteditems:
            childNum = item.childCount()
            if childNum:
                for i in range(childNum):
                    mySelectedItems.append('%s' % item.child(i).text(0))
            else:
                mySelectedItems.append('%s' % item.text(0))
        return mySelectedItems
    
    #创建文件夹
    def createOneFile(self, firstPath, secondPath):
        finalPath = os.path.join(firstPath, secondPath)
        if os.path.isdir(finalPath):
            pass
        else:
            os.mkdir(finalPath)
        return finalPath

    #拷贝数据
    def copyData(self, type):
        cacheNode = ''
        myCacheFileDirt = {}
        if type == 1:
            #获取选择的节点的节点和路径
            cacheNode = self.ChangeSelectedPath()
            myCacheFileDirt = self.soreFilePath(cacheNode)
        elif type == 2:
            #获取所有的节点的节点和路径
            cacheNode = self.ChangeAllPath()
            myCacheFileDirt = self.soreFilePath(cacheNode)

        lenCaches = len(myCacheFileDirt)
        if lenCaches:
            count = 0
            node = []
            #获取拷贝到的路径
            root = self.getDatapath()
            while(True):
                if not os.path.isdir(root):
                    self.errorMessage(u'无效路径，不存在相应文件夹，请重新输入！')
                    break

                dataTypeLen = len(self.dirName)
                if root[-dataTypeLen::] != self.dirName:
                    self.errorMessage(u'目前只支持‘%s’结尾的目录下更改全部缓存节点！<br>请重新输入路径'%self.dirName)
                    break

                self.progress_dialog = QtGui.QProgressDialog(u'Copy Data...Please wait', u'Cancel', 0, lenCaches, self)
                self.progress_dialog.setWindowTitle(u'Copying...')
                self.progress_dialog.setModal(True)
                self.progress_dialog.setRange(0, lenCaches)
                self.progress_dialog.setLabelText('Get Ready')
                self.progress_dialog.setValue(0)
                self.progress_dialog.show()
                j = 0
                for key in myCacheFileDirt.keys():
                    self.progress_dialog.setValue(j)
                    if os.path.isfile(key):
                        dataAddress = key.find(self.dirName)
                        lastCacheFile = key[dataAddress+dataTypeLen+1::]
                        lastCacheFile = lastCacheFile.replace("/", "\\")
                        lastCachePath = os.path.dirname(lastCacheFile)

                        frontCachePath = ''
                        splitTexts = lastCachePath.split('\\')
                        #创建目录
                        for i, Text in enumerate(splitTexts):
                            if i == 0:
                                frontCachePath = root
                            frontCachePath = self.createOneFile(frontCachePath, Text)

                        if not self.progress_dialog.wasCanceled():
                                self.progress_dialog.setLabelText('%s %s %s\n' % (lenCaches, self.fileType, j))
                        else:
                            self.errorMessage(u'您已经中断了缓存拷贝!')
                            self.progress_dialog.close()
                            return

                        myfile = os.path.basename(key) 
                        self.myChangeNetPath  
                        sourceFile = key.replace("/", "\\")
                        targetFile = os.path.join(frontCachePath, myfile)
                        sourceFile = self.myChangeNetPath(sourceFile)
                        targetFile = self.myChangeNetPath(targetFile)

                        if not os.path.isfile(targetFile):
                            self.worker.ready(sourceFile, targetFile)
                            while True:
                                if self.worker.wait():
                                    break
                                else:
                                    self.worker.msleep(100)
                        else:
                            if os.path.getmtime(sourceFile) != os.path.getmtime(targetFile):
                                self.worker.ready(sourceFile, targetFile)
                                while True:
                                    if self.worker.wait():
                                        break
                                    else:
                                        self.worker.msleep(100)
                        count += 1

                        #设置目录
                        for eachfile in myCacheFileDirt[key]:
                            mc.setAttr('%s.%s' % (eachfile, self.nodeAttr), targetFile, type='string')
                    else:
                        node.append(myCacheFileDirt.items()[j])
                    j = j +1

                #发送进程条信息
                self.progress_dialog.setValue(lenCaches)
                if count == lenCaches:
                    if type == 1:
                        self.errorMessage(u'所选的全部%s拷贝完成!'%(self.fileType))
                    elif type == 2:
                        self.errorMessage(u'全部%s拷贝完成!'%(self.fileType))
                elif count < lenCaches and count > 0:
                    self.errorMessage(u'有某些原文件不存在,<br>详细请看脚本编辑器!')
                    om.MGlobal.displayInfo(node)
                    om.MGlobal.displayWarning(u'\n以下的节点在新路径找不到:\n')
                    om.MGlobal.displayWarning(u'\n一共有 %d 个节点,有 %s 个节点找不到相应文件' % (lenCaches, count))
                else:
                    om.MGlobal.displayWarning(node)
                    om.MGlobal.displayWarning(u'\n以下的节点在新路径找不到:\n')
                    if type == 1:
                        self.errorMessage(u'所选全部节点指定路径中找不到相应的文件！<br>请检查所选原文件是否存在')
                    elif type == 2:
                        self.errorMessage(u'全部都找不到相应文件！<br>请检查所有源文件是否存在')
                break
        else:
            self.errorMessage(u'场景里没有%s节点...'%(self.fileType))
        self.progress_dialog.close()
        self.selectAllCache()
        return


    #转换路径
    def changePath(self, type):
        cacheFiles = ''
        count = 0
        node = []
        if type == 1:
            cacheFiles = self.ChangeSelectedPath()
        elif type == 2:
            cacheFiles = self.ChangeAllPath()

        if cacheFiles:
            #获取路径
            root = self.getDatapath()
            lenCaches = len(cacheFiles)
            while True:
                if not os.path.isdir(root):
                    self.errorMessage(u'无效路径，不存在相应文件夹，请重新输入！')
                    break
                dataTypeLen = ''
                if type == 2:
                    dataTypeLen = len(self.dirName)
                    if root[-dataTypeLen::] != self.dirName:
                        self.errorMessage(u'目前只支持‘%s’结尾的目录下更改全部缓存节点！<br>请重新输入路径'% self.dirName)
                        break

                for eachfile in cacheFiles:
                    cachePath = mc.getAttr('%s.%s' % (eachfile, self.nodeAttr))
                    newFile = ''
                    if type == 1:
                        lastCachePath = os.path.basename(cachePath)
                        newFile = os.path.join(root,lastCachePath)
                    if type == 2:
                        dataAddress = cachePath.find(self.dirName)
                        lastCachePath = cachePath[dataAddress+dataTypeLen+1::]
                        newFile = os.path.join(root,lastCachePath)

                    newFile = newFile.replace("/", "\\")

                    if os.path.isfile(newFile):
                        count += 1
                        mc.setAttr('%s.%s' % (eachfile, self.nodeAttr), newFile, type='string')
                    else:
                        node.append(eachfile)

                if count == lenCaches:
                    if type == 1:
                        self.errorMessage(u'所选的全部节点已替换完成!')
                    elif type == 2:
                        self.errorMessage(u'全部节点已替换完成!')
                elif count < lenCaches and count > 0:
                    self.errorMessage(u'有某些节点在新的路径找不到,<br>详细请看脚本编辑器!')
                    om.MGlobal.displayInfo(node)
                    om.MGlobal.displayWarning(u'\n以下的节点节点在新路径找不到:\n')
                    om.MGlobal.displayWarning(u'\n一共有 %d 个节点,有 %s 个节点找不到相应文件' % (lenCaches, count))
                else:
                    om.MGlobal.displayWarning(node)
                    om.MGlobal.displayWarning(u'\n以下的节点在新路径找不到:\n')
                    if type == 1:
                        self.errorMessage(u'所选节点在指定路径中找不到相应的文件！')
                    elif type == 2:
                        self.errorMessage(u'所选的全部节点都找不到相应文件！<br>请确保DataPath输入的%s目录下的结构和源目标%s目录下的结构一样！'%(self.dirName,self.dirName))
                break

        else:
            self.errorMessage(u'场景里没有%s节点...'%self.fileType)
        if type == 2:
            self.selectAllCache()

        return 

    #节点路径分类
    def soreFilePath(self, allCacheFile):
        myCacheFileDirt = {} #存放路径和节点{路径:[节点,...]}
        for eachfile in allCacheFile:
            cachePath = mc.getAttr('%s.%s' % (eachfile, self.nodeAttr))
            if not cachePath:
                cachePath = 'scene\\'
                mc.setAttr('%s.%s' % (each, self.nodeAttr), cachePath, type='string')

            cachePath = cachePath.replace("/", "\\")  

            if not cachePath in myCacheFileDirt.keys():
                myCacheFileDirt.update({cachePath:[eachfile]})
            else:
                myCacheFileDirt[cachePath].append(eachfile)

        return myCacheFileDirt

    #选择所有缓存
    def selectAllCache(self):
        allCacheFile = mc.ls(type = self.fileType)
        myCacheFileDirt = self.soreFilePath(allCacheFile)
        treeWidget = self.ui.treeWidget
        treeWidget.clear()
        if myCacheFileDirt:
            errorCacheNum = 0
            j = 1
            NoFile = 'NO_FileCache'
            OkFile = 'OK_FileCache'
            errorfiles = []
            for key in myCacheFileDirt.keys():
                root = QtGui.QTreeWidgetItem(treeWidget)
                if os.path.isfile(key):
                    root.setText(0, '%s%s' % (OkFile, j))
                    root.setText(1, '%s' % key)
                else:
                    root.setText(0, '%s%s' % (NoFile, j))
                    root.setText(1, '%s' % key)

                for eh in myCacheFileDirt[key]:
                    errorCacheNum += 1
                    child = QtGui.QTreeWidgetItem(root)
                    child.setText(0, eh)
                    errorfiles.append(eh)
                j += 1

        if allCacheFile:
            mc.select(allCacheFile)
            self.ui.reportLabel.setText('You have select %s Files' % len(allCacheFile))
            if mc.objExists('All%s_sets'%self.fileType):
                mc.sets(cl='All%s_sets'%self.fileType)
                mc.sets(add='All%s_sets'%self.fileType)
            else:
                mc.sets(n='All%s_sets'%self.fileType)
                self.ui.pathLineEdit.setText("Change all Files`s example: D:\work\Test\data")
        else:
            if mc.objExists('All%s_sets'%self.fileType):
                mc.delete('All%s_sets'%self.fileType)
            self.ui.reportLabel.setText('The file hasn`t got File!')
            self.ui.pathLineEdit.setText('')

        
    #提示消息             
    def errorMessage(self, msg):
        QtGui.QMessageBox.warning(self, _fromUtf8(u"警告"), _fromUtf8('<div style="font: 12pt ;">%s</div>' % msg))


    def checkPath(self):
        cacheNode = mc.ls(type = self.fileType)
        myCacheFileDirt = self.soreFilePath(cacheNode)
        treeWidget = self.ui.treeWidget
        treeWidget.clear()
        if myCacheFileDirt:
            j = 0
            errorCacheNum = 0
            NoFile = 'NoFileCache'
            errorfiles = []
            for key in myCacheFileDirt.keys():
                if not os.path.isfile(key):
                    j += 1
                    root = QtGui.QTreeWidgetItem(treeWidget)
                    root.setText(0, '%s%s' % (NoFile, j))
                    root.setText(1, '%s' % key)
                    for eh in myCacheFileDirt[key]:
                        errorCacheNum += 1
                        child = QtGui.QTreeWidgetItem(root)
                        child.setText(0, eh)
                        errorfiles.append(eh)
            if j:
                self.ui.reportLabel.setText('There has %s types of errors node path, and has %s error node path' % (j, errorCacheNum))
                mc.select(errorfiles)
                if mc.objExists('sortError%s_sets'%self.fileType):
                    mc.sets(cl='sortError%s_sets'%self.fileType)
                    mc.sets(add='sortError%s_sets'%self.fileType)
                else:
                    mc.sets(n='sortError%s_sets'%self.fileType)
                    self.ui.pathLineEdit.setText("Change selected %s`s example: D:\work\Test\data\Test"%self.fileType)
            else:
                self.ui.reportLabel.setText('Good!  Good!  Good! All %s `s path is Right!'%self.fileType)
        else:
            self.ui.reportLabel.setText('The file hasn`t got %s!'%self.fileType)

if __name__ == "__main__":

    # fileType = 'AlembicNode' #节点类型
    # nodeAttr = 'abc_File'    #节点属性
    # dirName = 'alembic'     #文件夹
    # fileType = 'aiStandIn' #节点类型
    # nodeAttr = 'dso'    #节点属性
    # dirName = 'sourceimages'     #文件夹

    fileType = 'VRayMesh' #节点类型
    nodeAttr = 'fileName'    #节点属性
    dirName = 'sourceimages'     #文件

    if mc.window("%sDialog"%fileType, exists=True):
        mc.deleteUI("%sDialog"%fileType, window=True)
    File_Ui = File_Tools(fileType, nodeAttr, dirName)
    File_Ui.show()