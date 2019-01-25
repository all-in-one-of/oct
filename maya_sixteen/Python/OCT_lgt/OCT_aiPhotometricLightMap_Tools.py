#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui,QtCore
import maya.OpenMayaUI as apiUI
import maya.cmds as mc
import maya.OpenMaya as OpenMaya
import sys
import sip
import os
import shutil

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s : s

class UI_aiPhotometricLight(object):
    def setupUi(self, LightPathDialog):
        LightPathDialog.setObjectName(_fromUtf8("LightPathDialog"))
        LightPathDialog.resize(659, 392)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.verticalLayout = QtGui.QVBoxLayout(LightPathDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(LightPathDialog)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(1205)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.titileLabel = QtGui.QLabel(LightPathDialog)
        font1 = QtGui.QFont()
        font1.setPointSize(16)
        self.titileLabel.setFont(font1)
        self.titileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titileLabel.setObjectName(_fromUtf8("titileLabel"))
        self.gridLayout.addWidget(self.titileLabel, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(LightPathDialog)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.pathLineEdit = QtGui.QLineEdit(LightPathDialog)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.horizontalLayout_2.addWidget(self.pathLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkPushButton = QtGui.QPushButton(LightPathDialog)
        self.checkPushButton.setFont(font)
        self.checkPushButton.setStyleSheet("background-color: rgb(97, 21, 93)")
        self.checkPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.checkPushButton.setObjectName(_fromUtf8("checkPushButton"))
        self.horizontalLayout_3.addWidget(self.checkPushButton)
        self.ChangeSelectedPushButton = QtGui.QPushButton(LightPathDialog)
        self.ChangeSelectedPushButton.setFont(font)
        self.ChangeSelectedPushButton.setStyleSheet("background-color: rgb(67, 98, 21)")
        self.ChangeSelectedPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ChangeSelectedPushButton.setObjectName(_fromUtf8("ChangeSelectedPushButton"))
        self.horizontalLayout_3.addWidget(self.ChangeSelectedPushButton)
        self.SelectAllPushButton = QtGui.QPushButton(LightPathDialog)
        self.SelectAllPushButton.setFont(font)
        self.SelectAllPushButton.setStyleSheet("background-color: rgb(97, 21, 93)")
        self.SelectAllPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.SelectAllPushButton.setObjectName(_fromUtf8("SelectAllPushButton"))
        self.horizontalLayout_3.addWidget(self.SelectAllPushButton)
        # self.ChangePushButton = QtGui.QPushButton(LightPathDialog)
        # self.ChangePushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        # self.ChangePushButton.setFont(font)
        # self.ChangePushButton.setMinimumSize(QtCore.QSize(0, 40))
        # self.ChangePushButton.setObjectName(_fromUtf8("ChangePushButton"))
        # self.horizontalLayout_3.addWidget(self.ChangePushButton)
        self.copySelectPushButton = QtGui.QPushButton(LightPathDialog)
        self.copySelectPushButton.setFont(font)
        self.copySelectPushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        self.copySelectPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.copySelectPushButton.setObjectName(_fromUtf8("copySelectPushButton"))
        self.horizontalLayout_3.addWidget(self.copySelectPushButton)
        # self.copyAllPushButton = QtGui.QPushButton(LightPathDialog)
        # self.copyAllPushButton.setFont(font)
        # self.copyAllPushButton.setStyleSheet("background-color: rgb(21, 32, 97)")
        # self.copyAllPushButton.setMinimumSize(QtCore.QSize(0, 40))
        # self.copyAllPushButton.setObjectName(_fromUtf8("copyAllPushButton"))
        # self.horizontalLayout_3.addWidget(self.copyAllPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.reportTitleLabel = QtGui.QLabel(LightPathDialog)
        self.reportTitleLabel.setFont(font)
        self.reportTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.reportTitleLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reportTitleLabel.setObjectName(_fromUtf8("reportTitleLabel"))
        self.horizontalLayout_1.addWidget(self.reportTitleLabel)
        self.reportLabel = QtGui.QLabel(LightPathDialog)
        self.reportLabel.setFont(font)
        self.reportLabel.setObjectName(_fromUtf8("reportLabel"))
        self.horizontalLayout_1.addWidget(self.reportLabel)
        self.gridLayout.addLayout(self.horizontalLayout_1, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(LightPathDialog)
        QtCore.QMetaObject.connectSlotsByName(LightPathDialog)

    def retranslateUi(self, LightPathDialog):
        LightPathDialog.setWindowTitle(QtGui.QApplication.translate("LightPathDialog", "aiPhotometricLightManage", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("LightPathDialog", "LightName", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("LightPathDialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.titileLabel.setText(QtGui.QApplication.translate("LightPathDialog", "aiPhotomeLightFile_Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LightPathDialog", "DataPath:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkPushButton.setText(QtGui.QApplication.translate("LightPathDialog", "Check aiPhotomeLightFiles", None, QtGui.QApplication.UnicodeUTF8))
        self.ChangeSelectedPushButton.setText(QtGui.QApplication.translate("LightPathDialog", "Change Selected DataPath", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectAllPushButton.setText(QtGui.QApplication.translate("LightPathDialog", "Select All aiPhotomeLightFiles", None, QtGui.QApplication.UnicodeUTF8))
       # self.ChangePushButton.setText(QtGui.QApplication.translate("LightPathDialog", "Change All DataPath", None, QtGui.QApplication.UnicodeUTF8))
        self.copySelectPushButton.setText(QtGui.QApplication.translate("LightPathDialog", "Copy Selected Data", None, QtGui.QApplication.UnicodeUTF8))
        #self.copyAllPushButton.setText(QtGui.QApplication.translate("LightPathDialog", "Copy All Data", None, QtGui.QApplication.UnicodeUTF8))
        self.reportTitleLabel.setText(QtGui.QApplication.translate("LightPathDialog", "Check Report:", None, QtGui.QApplication.UnicodeUTF8))
        self.reportLabel.setText(QtGui.QApplication.translate("LightPathDialog", "Please press the \"Check Light path\" button", None, QtGui.QApplication.UnicodeUTF8))
        self.pathLineEdit.setText(QtGui.QApplication.translate("LightPathDialog", "", None, QtGui.QApplication.UnicodeUTF8))


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


class aiPhotomeLightFile_Tools(QtGui.QDialog):
    def __init__(self, parent=getMayaWindow()):
        super(aiPhotomeLightFile_Tools, self).__init__(parent)
        self.ui = UI_aiPhotometricLight()
        self.ui.setupUi(self)
        self.worker = JobThread(self)
        self.setUpGui()

    def setUpGui(self):
        #取的控件
        treeWidget = self.ui.treeWidget
        #ChangePushButton = self.ui.ChangePushButton
        checkPushButton = self.ui.checkPushButton
        ChangeSelectedPushButton = self.ui.ChangeSelectedPushButton
        SelectAllPushButton = self.ui.SelectAllPushButton
        copySelectPushButton = self.ui.copySelectPushButton
        #copyAllPushButton = self.ui.copyAllPushButton
        #按钮的链接
        #ChangePushButton.clicked.connect(self.ChangeAll)
        ChangeSelectedPushButton.clicked.connect(self.ChangeSelected)
        checkPushButton.clicked.connect(self.checkPath)
        SelectAllPushButton.clicked.connect(self.selectAllLight)
        copySelectPushButton.clicked.connect(self.copySelected)
        #copyAllPushButton.clicked.connect(self.copyAll)
        treeWidget.itemClicked.connect(self.itemClick)
        #表格控制
        treeWidget.setColumnWidth(0, 250)

    def errorMessage(self, msg):
        QtGui.QMessageBox.warning(self, _fromUtf8(u"警告"), _fromUtf8('<div style="font: 12pt ;">%s</div>' % msg))

    def getDatapath(self):
        path = '%s' % self.ui.pathLineEdit.text()
        return path 

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

    def ChangeSelected(self):
        LightFiles = self.ChangeSelectedPath()
        if LightFiles:
            count = 0
            node = []
            lenLight = len(LightFiles)
            root = self.getDatapath()
            while(True):
                if not os.path.isdir(root):
                    self.errorMessage(u'无效路径，不存在相应文件夹，请重新输入！')
                    break
                for each in LightFiles:
                    LightFile = mc.getAttr("%s.ai_filename" %each) 
                    LightFileName = os.path.basename(LightFile)
                    newFile = os.path.join(root,LightFileName)
                    if os.path.isfile(newFile):
                        count += 1
                        mc.setAttr("%s.ai_filename" %each, newFile, type = "string")
                    else:
                        node.append(each)
                if count == lenLight:
                    self.errorMessage(u'所选的全部灯光节点已替换完成!')
                elif count<lenLight and count>0:
                    self.errorMessage(u'有某些灯光节点在新的路径找不到,<br>详细请看脚本编辑器!')
                    om.MGlobal.displayInfo(node)
                    om.MGlobal.displayWarning(u'\n以下的节点缓存节点在新路径找不到:\n')
                    om.MGlobal.displayWarning(u'\n一共有 %d 个缓存节点,有 %s 个节点找不到相应文件' % (lenLight, count))
                else:
                    om.MGlobal.displayWarning(node)
                    om.MGlobal.displayWarning(u'\n以下的节点缓存节点在新路径找不到:\n')
                    self.errorMessage(u'所选灯光节点在指定路径中找不到相应的文件！<br>请检查指定路径下贴图！')
                break
        else:
            self.errorMessage(u'场景里没有aiPhotometricLight节点...') 
        return

    def copySelected(self):
        LightFiles = self.ChangeSelectedPath()
        lenFile = len(LightFiles)
        if lenFile:
            count = 0
            node = []
            root = self.getDatapath()
            while(True):
                if not os.path.isdir(root):
                    self.errorMessage(u'无效路径，不存在相应文件夹，请重新输入！')
                    break
                self.progress_dialog = QtGui.QProgressDialog(u'Copy Data...Please wait', u'Cancel', 0, lenFile, self)
                self.progress_dialog.setWindowTitle(u'Copying...')
                self.progress_dialog.setModal(True)
                self.progress_dialog.setRange(0, lenFile)
                self.progress_dialog.setLabelText('Get Ready')
                self.progress_dialog.setValue(0)
                self.progress_dialog.show()
                for j, each in enumerate(LightFiles):
                    self.progress_dialog.setValue(j)
                    LightPath = mc.getAttr('%s.ai_filename' % each)
                    #判断源文件是否存在
                    if os.path.isfile(LightPath): 
                        if not self.progress_dialog.wasCanceled():
                            self.progress_dialog.setLabelText('%s aiPhotometricLight %s' % (lenFile, j))
                        else:
                            self.errorMessage(u'您已经中断了缓存拷贝!')
                            self.progress_dialog.close()
                            return

                        LightFileName = os.path.basename(LightPath)
                        sourceFile = LightPath
                        targetFile = os.path.join(root, LightFileName)
                        if not os.path.isfile(targetFile):
                            print targetFile 
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

                        mc.setAttr('%s.ai_filename' % each, targetFile, type='string')
                    else:
                        node.append(each)
                self.progress_dialog.setValue(lenFile)
                if count == lenFile:
                    self.errorMessage(u'所选的全部灯光贴图拷贝完成!')
                elif count < lenFile and count > 0:
                    self.errorMessage(u'有某些节点贴图的原文件不存在,<br>详细请看脚本编辑器!')
                    om.MGlobal.displayInfo(node)
                    om.MGlobal.displayWarning(u'\n以下的节点灯光节点在新路径找不到:\n')
                    om.MGlobal.displayWarning(u'\n一共有 %d 个灯光节点,有 %s 个节点找不到相应文件' % (lenFile, count))
                else:
                    om.MGlobal.displayWarning(node)
                    om.MGlobal.displayWarning(u'\n以下的节点灯光节点在新路径找不到:\n')
                    self.errorMessage(u'所选全部灯光指定路径中找不到相应的文件！<br>请检查所选源灯光贴图是否存在')
                break

        else:
            self.errorMessage(u'场景里没有aiPhotometricLight节点...')

    def ChangeSelectedPath(self):
        mySelectedItems = []
        treeWidget = self.ui.treeWidget
        selecteditems = treeWidget.selectedItems()
        for item in selecteditems:
            childNum = item.childCount()
            if childNum:
                for i in range(childNum):
                    mySelectedItems.append("%s" % item.child(i).text(0))
            else:
                mySelectedItems.append("%s" % item.text(0))
        return mySelectedItems


    def checkPath(self):
        allLightFile = mc.ls(type = "aiPhotometricLight")
        treeWidget = self.ui.treeWidget
        treeWidget.clear()
        NoFile = "NO_FileLight"
        j = 0
        NoNodeLight = {}

        for each in allLightFile:
            LightFile = mc.getAttr("%s.ai_filename" %each)
            LightPath = os.path.dirname(LightFile)
            if not os.path.isfile(LightFile):
                if not LightPath in NoNodeLight.keys():
                    NoNodeLight.update({LightPath : [each]})
                else:
                    NoNodeLight[LightPath].append(each)

        for key in NoNodeLight.keys():
            root = QtGui.QTreeWidgetItem(treeWidget)
            root.setText(0, '%s%s' % (NoFile, j))
            root.setText(1, '%s' % key)
            for NOLight in NoNodeLight[key]:
                child = QtGui.QTreeWidgetItem(root)
                child.setText(0, NOLight)
            j+=1

    def selectAllLight(self):
        allLightFile = mc.ls(type = "aiPhotometricLight")
        treeWidget = self.ui.treeWidget
        treeWidget.clear()
        errorLightNum = 0
        j = 1
        NoFile = "NO_FileLight"
        OkFile = "OK_FileLight"
        NoNodeLight = {}
        OkNodeLight = {}

        for each in allLightFile:
            LightFile = mc.getAttr("%s.ai_filename" %each)
            LightPath = os.path.dirname(LightFile)
            if os.path.isfile(LightFile):
                if not LightPath in OkNodeLight.keys():
                    OkNodeLight.update({LightPath : [each]})
                else:
                    OkNodeLight[LightPath].append(each)
            else:
                if not LightPath in NoNodeLight.keys():
                    NoNodeLight.update({LightPath : [each]})
                else:
                    NoNodeLight[LightPath].append(each)

        for key in OkNodeLight.keys():
            root = QtGui.QTreeWidgetItem(treeWidget)
            root.setText(0, '%s%s' % (OkFile, j))
            root.setText(1, '%s' % key)
            for OkLight in OkNodeLight[key]:
                child = QtGui.QTreeWidgetItem(root)
                child.setText(0, OkLight)
            j+=1

        for key in NoNodeLight.keys():
            root = QtGui.QTreeWidgetItem(treeWidget)
            root.setText(0, '%s%s' % (NoFile, j))
            root.setText(1, '%s' % key)
            for NOLight in NoNodeLight[key]:
                child = QtGui.QTreeWidgetItem(root)
                child.setText(0, NOLight)
            j+=1

        if allLightFile:
            mc.select(allLightFile)
            self.ui.reportLabel.setText('You have select %s aiPhotometricLight' % len(allLightFile))
        else:
            self.ui.reportLabel.setText('The file hasn`t got aiPhotometricLight!')

if __name__ == "__main__":
    UI_aiPhotometricLight = aiPhotomeLightFile_Tools()
    UI_aiPhotometricLight.show()
