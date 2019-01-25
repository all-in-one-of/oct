#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from OCT_generel.ui_Checkin import Ui_MainWindow
import maya.OpenMayaUI as apiUI
import maya.cmds as mc
import sip
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)


class Checkin(QtGui.QMainWindow):
    fileName = mc.file(q=True, sn=True)
    shortName = mc.file(q=True, sn=True, shn=True)

    def __init__(self, parent=getMayaWindow()):
        super(Checkin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setUpUi()

    def errorMessage(self, msg):
        QtGui.QMessageBox.warning(self, _fromUtf8("警告"), _fromUtf8('<div style="font: 12pt ;">%s</div>' % msg))

    def setUpUi(self):
        #获取控件
        spinBox = self.ui.spinBox
        horizontalSlider = self.ui.horizontalSlider
        sourceLabel = self.ui.sourceLabel
        filenameLabel1 = self.ui.filenameLabel1
        filenameLabel2 = self.ui.filenameLabel2
        timeLabel = self.ui.timeLabel
        addImagePushButton = self.ui.addImagePushButton
        addVideoPushButton = self.ui.addVideoPushButton
        #控件链接
        horizontalSlider.valueChanged.connect(spinBox.setValue)
        spinBox.valueChanged.connect(horizontalSlider.setValue)
        addImagePushButton.clicked.connect(self.addImage)
        addVideoPushButton.clicked.connect(self.addVideo)
        #设置控件
        # print (self.errorNum)
        fileInfo = QtCore.QFileInfo(self.fileName)
        dataTime = fileInfo.created().toString('MM_dd HH:mm')
 
        sourceLabel.setText(u'%s' % self.fileName)
        filenameLabel1.setText(self.shortName)
        filenameLabel2.setText(self.shortName)
        timeLabel.setText(dataTime)

    def checkFile(self):
        if not self.fileName:
            self.errorMessage(u"此文件名为空!<br>请先保存文件！")
            return False
        else:
            return True

    def addImage(self):
        imagesName = mc.workspace(fre='images')
        imagePath = mc.workspace(en=imagesName)
        File = QtGui.QFileDialog.getOpenFileNames(parent=self, caption=_fromUtf8("请选择要上传的视频"), directory=imagePath, filter='', options=QtGui.QFileDialog.ReadOnly)
        FileInfo = QtCore.QFileInfo(File[0])
        imageFilePath = FileInfo.absoluteFilePath()
        if mc.file('%s' % imageFilePath, q=True, typ=True)[0].find('image') >= 0:
            filetext = os.path.splitext('%s' % imageFilePath)
            fileType = filetext[1][1::]
            fileName = filetext[0].split('/')[-1]
            if fileType.lower() != 'jpg' and fileType.lower() != 'png':
                imagesTmpPath = '%s/tmp' % (imagePath)
                if os.path.isdir(imagesTmpPath):
                    pass
                else:
                    os.mkdir(imagesTmpPath)
                fileTmpPath = '%s/%s.jpg' % (imagesTmpPath, fileName)
                file_obj = om.MObject()
                im = om.MImage()
                try:
                    im.readFromFile(imageFilePath)
                except:
                    del im
                im.writeToFile(fileTmpPath, 'jpg')
                imageFilePath = fileTmpPath
            thisPixmap = QtGui.QPixmap(imageFilePath)
            newmap = thisPixmap.scaledToHeight(500)
            self.ui.imagesViewLabel.setPixmap(newmap)
            return imageFilePath
        else:
            self.errorMessage(u"请选择图片！")

    def addVideo(self):
        imagesName = mc.workspace(fre='images')
        imagePath = mc.workspace(en=imagesName)
        File = QtGui.QFileDialog.getOpenFileNames(parent=self, caption=_fromUtf8("请选择要上传的视频"), directory=imagePath, filter='', options=QtGui.QFileDialog.ReadOnly)
        FileInfo = QtCore.QFileInfo(File[0])
        imageFilePath = FileInfo.absoluteFilePath()
        filetext = os.path.splitext('%s' % imageFilePath)
        fileType = filetext[1][1::]
        if fileType.lower() == 'mov' or fileType.lower() == 'avi':
            self.ui.videoPath.setText('<div style="color:#0F0">%s</div>' % imageFilePath)
        else:
            self.errorMessage(u'只支持mov或avi的视频格式')
        
if __name__ == "__main__":
    #app = QtGui.QApplication(sys.argv)
    checkinApp = Checkin()
    if checkinApp.checkFile():
        checkinApp.show()

    #app.exec_()