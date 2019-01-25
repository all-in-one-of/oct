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

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_cacheDialog(object):
    def setupUi(self, cacheDialog):
        cacheDialog.setObjectName(_fromUtf8("cacheDialog"))
        cacheDialog.resize(659, 392)
        font = QtGui.QFont()
        font.setPointSize(11)
        cacheDialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(cacheDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(cacheDialog)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(1205)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.titileLabel = QtGui.QLabel(cacheDialog)
        font1 = QtGui.QFont()
        font1.setPointSize(16)
        self.titileLabel.setFont(font1)
        self.titileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titileLabel.setObjectName(_fromUtf8("titileLabel"))
        self.gridLayout.addWidget(self.titileLabel, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(cacheDialog)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.pathLineEdit = QtGui.QLineEdit(cacheDialog)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.horizontalLayout_2.addWidget(self.pathLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkPushButton = QtGui.QPushButton(cacheDialog)
        self.checkPushButton.setFont(font)
        self.checkPushButton.setStyleSheet("background-color: rgb(97, 21, 93)")
        self.checkPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.checkPushButton.setObjectName(_fromUtf8("checkPushButton"))
        self.horizontalLayout_3.addWidget(self.checkPushButton)
        self.ChangeSelectedPushButton = QtGui.QPushButton(cacheDialog)
        self.ChangeSelectedPushButton.setFont(font)
        self.ChangeSelectedPushButton.setStyleSheet("background-color: rgb(67, 98, 21)")
        self.ChangeSelectedPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ChangeSelectedPushButton.setObjectName(_fromUtf8("ChangeSelectedPushButton"))
        self.horizontalLayout_3.addWidget(self.ChangeSelectedPushButton)
        self.SelectAllPushButton = QtGui.QPushButton(cacheDialog)
        self.SelectAllPushButton.setFont(font)
        self.SelectAllPushButton.setStyleSheet("background-color: rgb(97, 21, 93)")
        self.SelectAllPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.SelectAllPushButton.setObjectName(_fromUtf8("SelectAllPushButton"))
        self.horizontalLayout_3.addWidget(self.SelectAllPushButton)
        self.ChangePushButton = QtGui.QPushButton(cacheDialog)
        self.ChangePushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.ChangePushButton.setFont(font)
        self.ChangePushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ChangePushButton.setObjectName(_fromUtf8("ChangePushButton"))
        self.horizontalLayout_3.addWidget(self.ChangePushButton)
        self.copySelectPushButton = QtGui.QPushButton(cacheDialog)
        self.copySelectPushButton.setFont(font)
        self.copySelectPushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.copySelectPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.copySelectPushButton.setObjectName(_fromUtf8("copySelectPushButton"))
        self.horizontalLayout_3.addWidget(self.copySelectPushButton)
        self.copyAllPushButton = QtGui.QPushButton(cacheDialog)
        self.copyAllPushButton.setFont(font)
        self.copyAllPushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.copyAllPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.copyAllPushButton.setObjectName(_fromUtf8("copyAllPushButton"))
        self.horizontalLayout_3.addWidget(self.copyAllPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.reportTitleLabel = QtGui.QLabel(cacheDialog)
        self.reportTitleLabel.setFont(font)
        self.reportTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.reportTitleLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reportTitleLabel.setObjectName(_fromUtf8("reportTitleLabel"))
        self.horizontalLayout_1.addWidget(self.reportTitleLabel)
        self.reportLabel = QtGui.QLabel(cacheDialog)
        self.reportLabel.setFont(font)
        self.reportLabel.setObjectName(_fromUtf8("reportLabel"))
        self.horizontalLayout_1.addWidget(self.reportLabel)
        self.gridLayout.addLayout(self.horizontalLayout_1, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(cacheDialog)
        QtCore.QMetaObject.connectSlotsByName(cacheDialog)

    def retranslateUi(self, cacheDialog):
        cacheDialog.setWindowTitle(QtGui.QApplication.translate("cacheDialog", "CacheFileManage_zwz", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("cacheDialog", "CacheName", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("cacheDialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.titileLabel.setText(QtGui.QApplication.translate("cacheDialog", "CacheFile_Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("cacheDialog", "DataPath:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkPushButton.setText(QtGui.QApplication.translate("cacheDialog", "Check CacheFiles", None, QtGui.QApplication.UnicodeUTF8))
        self.ChangeSelectedPushButton.setText(QtGui.QApplication.translate("cacheDialog", "Change Selected DataPath", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectAllPushButton.setText(QtGui.QApplication.translate("cacheDialog", "Select All CacheFiles", None, QtGui.QApplication.UnicodeUTF8))
        self.ChangePushButton.setText(QtGui.QApplication.translate("cacheDialog", "Change All DataPath", None, QtGui.QApplication.UnicodeUTF8))
        self.copySelectPushButton.setText(QtGui.QApplication.translate("cacheDialog", "Copy Selected Data", None, QtGui.QApplication.UnicodeUTF8))
        self.copyAllPushButton.setText(QtGui.QApplication.translate("cacheDialog", "Copy All Data", None, QtGui.QApplication.UnicodeUTF8))
        self.reportTitleLabel.setText(QtGui.QApplication.translate("cacheDialog", "Check Report:", None, QtGui.QApplication.UnicodeUTF8))
        self.reportLabel.setText(QtGui.QApplication.translate("cacheDialog", "Please press the \"Check CacheFile\" button", None, QtGui.QApplication.UnicodeUTF8))
        self.pathLineEdit.setText(QtGui.QApplication.translate("cacheDialog", "       Green: D:\work\Test\data\\test(Detail)\t\t\tBlue: D:\work\Test\data\(Sketchy)", None, QtGui.QApplication.UnicodeUTF8))
# class JobThread(QtCore.QThread):
#     def __init__(self, parent=None):
#         super(JobThread, self).__init__(parent)

#     def run(self):


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


def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)


class CacheFile_Tools(QtGui.QDialog):
    def __init__(self, parent=getMayaWindow()):
        super(CacheFile_Tools, self).__init__(parent)
        self.ui = Ui_cacheDialog()
        self.ui.setupUi(self)
        self.worker = JobThread(self)
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
        treeWidget.setColumnWidth(0, 250)

    def ChangeSelected(self):
        self.changePath(1)

    def ChangeAll(self):
        self.changePath(2)

    def copySelected(self):
        self.copyData(3)

    def copyAll(self):
        self.copyData(4)

    def errorMessage(self, msg):
        QtGui.QMessageBox.warning(self, _fromUtf8(u"警告"), _fromUtf8('<div style="font: 12pt ;">%s</div>' % msg))

    def getDatapath(self):
        path = '%s' % self.ui.pathLineEdit.text()
        return path

    def ChangeAllPath(self):
        allCacheFile = mc.ls(type='cacheFile')
        return allCacheFile

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

    def changePath(self, type):
        if type == 1:
            cacheFiles = self.ChangeSelectedPath()
        elif type == 2:
            cacheFiles = self.ChangeAllPath()
        if cacheFiles:
            ext = 'xml'
            count = 0
            node = []
            lenCaches = len(cacheFiles)
            root = self.getDatapath()
            while(True):
                if not os.path.isdir(root):
                    self.errorMessage(u'无效路径，不存在相应文件夹，请重新输入！')
                    break
                if type == 1:
                    if root.find('data') < 0:
                        self.errorMessage(u'输入的详细目录不含有‘data’！<br>请重新输入路径')
                        break
                elif type == 2:
                    if root[-4::] == 'data':
                        dataTypeLen = len('data')
                    else:
                        self.errorMessage(u'目前只支持‘data’结尾的目录下更改全部缓存节点！<br>请重新输入路径')
                        break
                for each in cacheFiles:
                    cacheName = mc.getAttr('%s.cacheName' % each)
                    if type == 1:
                        frontCachePath = root+'\\'
                    elif type == 2:
                        cachePath = mc.getAttr('%s.cachePath' % each)
                        print cachePath
                        dataAddress = cachePath.find('data')
                        lastCachePath = cachePath[dataAddress+dataTypeLen+1::]
                        lastCachePath = lastCachePath.replace("/", "\\")
                        frontCachePath = os.path.join(root, lastCachePath)+'\\'
                    print frontCachePath
                    newFile = os.path.join(frontCachePath, cacheName) + '.%s' % ext
                    # print newFile
                    if os.path.isfile(newFile):
                        count += 1
                        mc.setAttr('%s.cachePath' % each, frontCachePath, type='string')
                    else:
                        node.append(each)
                if count == lenCaches:
                    if type == 1:
                        self.errorMessage(u'所选的全部缓存节点已替换完成!')
                    elif type == 2:
                        self.errorMessage(u'全部缓存节点已替换完成!')
                elif count < lenCaches and count > 0:
                    self.errorMessage(u'有某些缓存节点在新的路径找不到,<br>详细请看脚本编辑器!')
                    om.MGlobal.displayInfo(node)
                    om.MGlobal.displayWarning(u'\n以下的节点缓存节点在新路径找不到:\n')
                    om.MGlobal.displayWarning(u'\n一共有 %d 个缓存节点,有 %s 个节点找不到相应文件' % (lenCaches, count))
                else:
                    om.MGlobal.displayWarning(node)
                    om.MGlobal.displayWarning(u'\n以下的节点缓存节点在新路径找不到:\n')
                    if type == 1:
                        self.errorMessage(u'所选缓存节点在指定路径中找不到相应的文件！<br>请检查指定路径下是否有相应的xml文件！')
                    elif type == 2:
                        self.errorMessage(u'所选的全部缓存节点都找不到相应文件！<br>请确保DataPath输入的data目录下的结构和源目标data目录下的结构一样！')
                break
        else:
            self.errorMessage(u'场景里没有cacheFile节点...')
        if type == 2:
            self.selectAllCache()
        return

    def createOneFile(self, firstPath, secondPath):
        finalPath = os.path.join(firstPath, secondPath)
        if os.path.isdir(finalPath):
            pass
        else:
            os.mkdir(finalPath)
        return finalPath

    def copyData(self, type):
        if type == 3:
            cacheNode = self.ChangeSelectedPath()
            sortCacheFile = self.soreFilePath(cacheNode)
        elif type == 4:
            cacheNode = self.ChangeAllPath()
            sortCacheFile = self.soreFilePath(cacheNode)
        lenCaches = len(sortCacheFile)
        #发送进程条信息
        print type
        if lenCaches:
            count = 0
            node = []
            root = self.getDatapath()
            while(True):
                if not os.path.isdir(root):
                    self.errorMessage(u'无效路径，不存在相应文件夹，请重新输入！')
                    break
                if root[-4::] == 'data':
                    dataTypeLen = len('data')
                else:
                    self.errorMessage(u'目前只支持‘data’结尾的目录下拷贝缓存！<br>请重新输入路径')
                    break
                self.progress_dialog = QtGui.QProgressDialog(u'Copy Data...Please wait', u'Cancel', 0, lenCaches, self)
                self.progress_dialog.setWindowTitle(u'Copying...')
                self.progress_dialog.setModal(True)
                self.progress_dialog.setRange(0, lenCaches)
                self.progress_dialog.setLabelText('Get Ready')
                self.progress_dialog.setValue(0)
                self.progress_dialog.show()
                for j, each in enumerate(sortCacheFile):
                    self.progress_dialog.setValue(j)
                    cachePath = mc.getAttr('%s.cachePath' % each[1])
                    sourceCacheFile = each[0]
                    #判断源文件是否存在
                    if os.path.isfile(sourceCacheFile):
                        dataAddress = cachePath.find('data')
                        lastCachePath = cachePath[dataAddress+dataTypeLen+1::]
                        lastCachePath = lastCachePath.replace("/", "\\")
                        # frontCachePath = root+lastCachePath
                        frontCachePath = ''
                        splitTexts = lastCachePath.split('\\')
                        #创建目录
                        for i, Text in enumerate(splitTexts):
                            if i == 0:
                                frontCachePath = root
                            frontCachePath = self.createOneFile(frontCachePath, Text)
                        #拷贝文件
                        listFile = os.listdir(cachePath)
                        numFile = len(listFile)
                        for q, myfile in enumerate(listFile):
                            #发送进程条信息
                            if not self.progress_dialog.wasCanceled():
                                self.progress_dialog.setLabelText('%s cacheFils %s\n%s File %s' % (lenCaches, j, numFile, q))
                            else:
                                self.errorMessage(u'您已经中断了缓存拷贝!')
                                self.progress_dialog.close()
                                return
                            sourceFile = os.path.join(cachePath, myfile)
                            targetFile = os.path.join(frontCachePath, myfile)
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
                        for p in range(len(each)):
                            if p > 0:
                                mc.setAttr('%s.cachePath' % each[p], frontCachePath, type='string')
                    else:
                        node.append(each)
                #发送进程条信息
                self.progress_dialog.setValue(lenCaches)
                if count == lenCaches:
                    if type == 3:
                        self.errorMessage(u'所选的全部缓存拷贝完成!')
                    elif type == 4:
                        self.errorMessage(u'全部缓存拷贝完成!')
                elif count < lenCaches and count > 0:
                    self.errorMessage(u'有某些缓存的原文件不存在,<br>详细请看脚本编辑器!')
                    om.MGlobal.displayInfo(node)
                    om.MGlobal.displayWarning(u'\n以下的节点缓存节点在新路径找不到:\n')
                    om.MGlobal.displayWarning(u'\n一共有 %d 个缓存节点,有 %s 个节点找不到相应文件' % (lenCaches, count))
                else:
                    om.MGlobal.displayWarning(node)
                    om.MGlobal.displayWarning(u'\n以下的节点缓存节点在新路径找不到:\n')
                    if type == 3:
                        self.errorMessage(u'所选全部缓存指定路径中找不到相应的文件！<br>请检查所选源缓存是否存在')
                    elif type == 4:
                        self.errorMessage(u'全部缓存都找不到相应文件！<br>请检查所有源缓存是否存在')
                break
        else:
            self.errorMessage(u'场景里没有cacheFile节点...')
        self.progress_dialog.close()
        self.selectAllCache()
        return

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

    def soreFilePath(self, cacheNode):
        ext = 'xml'
        allFilePaths = []
        sortFilePaths = []
        for each in cacheNode:
            cacheName = mc.getAttr('%s.cacheName' % each)
            cachePath = mc.getAttr('%s.cachePath' % each)
            if not cachePath:
                cachePath = 'scene\\'
                mc.setAttr('%s.cachePath' % each, cachePath, type='string')
            if not cacheName:
                cacheName = 'None'
                mc.setAttr('%s.cacheName' % each, cacheName, type='string')
            newFile = os.path.join(cachePath, cacheName) + '.%s' % ext
            allFilePaths.append(newFile)
        singlePaths = list(set(allFilePaths))
        if singlePaths:
            for i in range(len(singlePaths)):
                tmp = []
                tmp.append(singlePaths[i])
                for each in cacheNode:
                    cacheName = mc.getAttr('%s.cacheName' % each)
                    cachePath = mc.getAttr('%s.cachePath' % each)
                    newFile = os.path.join(cachePath, cacheName) + '.%s' % ext
                    if newFile == singlePaths[i]:
                        tmp.append(each)
                sortFilePaths.append(tmp)
        return sortFilePaths

    def checkPath(self):
        cacheNode = mc.ls(type='cacheFile')
        sortCacheFile = self.soreFilePath(cacheNode)
        treeWidget = self.ui.treeWidget
        treeWidget.clear()
        if sortCacheFile:
            j = 0
            errorCacheNum = 0
            NoFile = 'NoFileCache'
            errorfiles = []
            for i, ch in enumerate(sortCacheFile):
                if not os.path.isfile(ch[0]):
                    j += 1
                    root = QtGui.QTreeWidgetItem(treeWidget)
                    root.setText(0, '%s%s' % (NoFile, j))
                    root.setText(1, '%s' % ch[0])
                    for p, eh in enumerate(ch):
                        if p > 0:
                            errorCacheNum += 1
                            child = QtGui.QTreeWidgetItem(root)
                            child.setText(0, eh)
                            errorfiles.append(eh)
            if j:
                self.ui.reportLabel.setText('There has %s types of errors caches, and has %s error caches' % (j, errorCacheNum))
                mc.select(errorfiles)
                if mc.objExists('sortErrorCacheFiles_sets'):
                    mc.sets(cl='sortErrorCacheFiles_sets')
                    mc.sets(add='sortErrorCacheFiles_sets')
                else:
                    mc.sets(n='sortErrorCacheFiles_sets')
                    self.ui.pathLineEdit.setText("Change selected cacheFiles`s example: D:\work\Test\data\Test")
            else:
                self.ui.reportLabel.setText('Good!  Good!  Good! All cacheFile`s path is Right!')
        else:
            self.ui.reportLabel.setText('The file hasn`t got cacheFile!')

    def selectAllCache(self):
        allCacheFile = mc.ls(type='cacheFile')
        sortCacheFile = self.soreFilePath(allCacheFile)
        treeWidget = self.ui.treeWidget
        treeWidget.clear()
        if sortCacheFile:
            errorCacheNum = 0
            j = 1
            NoFile = 'NO_FileCache'
            OkFile = 'OK_FileCache'
            errorfiles = []
            for i, ch in enumerate(sortCacheFile):
                root = QtGui.QTreeWidgetItem(treeWidget)
                if os.path.isfile(ch[0]):
                    root.setText(0, '%s%s' % (OkFile, j))
                    root.setText(1, '%s' % ch[0])
                else:
                    root.setText(0, '%s%s' % (NoFile, j))
                    root.setText(1, '%s' % ch[0])
                for p, eh in enumerate(ch):
                    if p > 0:
                        errorCacheNum += 1
                        child = QtGui.QTreeWidgetItem(root)
                        child.setText(0, eh)
                        errorfiles.append(eh)
                j += 1
        if allCacheFile:
            mc.select(allCacheFile)
            self.ui.reportLabel.setText('You have select %s cacheFiles' % len(allCacheFile))
            if mc.objExists('AllCacheFiles_sets'):
                mc.sets(cl='AllCacheFiles_sets')
                mc.sets(add='AllCacheFiles_sets')
            else:
                mc.sets(n='AllCacheFiles_sets')
                self.ui.pathLineEdit.setText("Change all cacheFiles`s example: D:\work\Test\data")
        else:
            if mc.objExists('AllCacheFiles_sets'):
                mc.delete('AllcaCheFiles_sets')
            self.ui.reportLabel.setText('The file hasn`t got cacheFile!')
            self.ui.pathLineEdit.setText('')


if __name__ == "__main__":
    CacheFile_Ui = CacheFile_Tools()
    CacheFile_Ui.show()
