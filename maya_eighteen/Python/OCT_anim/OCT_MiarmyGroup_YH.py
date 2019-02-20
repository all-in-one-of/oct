# *-* coding=utf-8
__author__ = 'yangh'
import maya.cmds as mc
from PyQt4 import QtGui, QtCore
import maya.OpenMayaUI as apiUI
import sip

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#获取maya的主窗口api
def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

class MiarmyGroupUI():
    def groupOutputUI(self, groupUI):
        groupUI.setObjectName(_fromUtf8("MiarmyGroupUI"))
        groupUI.setWindowTitle(_fromUtf8("MiarmyGroupUI"))

        #设置窗口的大小，窗口字体的大小
        groupUI.resize(350, 180)
        font = QtGui.QFont()
        font.setPointSize(14)
        groupUI.setFont(font)
        self.mainLayout = QtGui.QGridLayout(groupUI)

        self.outputLabel = QtGui.QLabel(groupUI)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setText(_fromUtf8("outputName"))

        self.outputLine = QtGui.QLineEdit(groupUI)
        self.outputLine.setFont(font)
        #self.outputLine.setAlignment(QtCore.Qt.AlignCenter)

        self.inputLabel = QtGui.QLabel(groupUI)
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLabel.setText(_fromUtf8('inputName'))

        self.inputLine = QtGui.QLineEdit(groupUI)
        self.inputLine.setFont(font)
        #self.inputLine.setAlignment(QtCore.Qt.AlignCenter)

        self.inApplyButton = QtGui.QPushButton(groupUI)
        self.inApplyButton.setFont(font)
        self.inApplyButton.setText(_fromUtf8('inApply'))

        self.outApplyButton = QtGui.QPushButton(groupUI)
        self.outApplyButton.setFont(font)
        self.outApplyButton.setText(_fromUtf8('outApply'))

        self.mainLayout.addWidget(self.inputLabel, 0, 1, 1, 1)
        self.mainLayout.addWidget(self.outputLabel, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.inputLine, 0, 2, 1, 1)
        self.mainLayout.addWidget(self.outputLine, 1, 2, 1, 1)
        self.mainLayout.addWidget(self.inApplyButton, 0, 3, 1, 1)
        self.mainLayout.addWidget(self.outApplyButton, 1, 3, 1, 1)

class OCT_MiarmyGroup(QtGui.QDialog):
    def __init__(self, parent = getMayaWindow() ):
        super(OCT_MiarmyGroup, self).__init__(parent)
        self.allJointGroup = []
        self.allMesh = []
        self.allGroupName = []
        self.ui = MiarmyGroupUI()
        self.ui.groupOutputUI(self)
        self.setUpGui()

    def errorMessage(self, msg):
        QtGui.QMessageBox.warning(self, _fromUtf8(u"警告"), _fromUtf8('<div style="font: 12pt ;">%s</div>' % msg))

    def setUpGui(self):
        self.ui.outApplyButton.clicked.connect(self.MiarmyOutputGroup)
        self.ui.inApplyButton.clicked.connect(self.MiarmyinputGroup)

    def MiarmyinputGroup(self):
        self.allGroupName = []
        nameIn = '%s'%self.ui.inputLine.text()
        i = 1
        self.allJointGroup = mc.ls(sl = True, type = 'joint')
        if len(self.allJointGroup) != 1 or mc.objectType(self.allJointGroup[0]) != 'joint':
            self.errorMessage(u'请选择一组骨骼和填写inputName的值！')
            return
        jointsGroups = mc.ls(sl = True, shapes = True, dag = True, type = 'joint')
        for jointG in jointsGroups:
            try:
                allSkinClusters = mc.listConnections('%s.lockInfluenceWeights'%jointG)
                for skin in allSkinClusters:
                    if mc.objectType(skin) == 'skinCluster':
                        meshs = mc.listConnections('%s.outputGeometry'%skin)[0]
                        if not meshs in self.allMesh:
                            self.allMesh.append(meshs)
            except:
                pass

        mc.select(d = True)
        while True:
            nameSkin = 'skin%s'%i
            if mc.objExists(nameSkin):
                i = i + 1
            else:
                break
        try:
            name = mc.group(self.allMesh, name = nameSkin)
        except:
            self.errorMessage(u'可能有重名物体!')
            return
        self.allMesh = []

        name1 = '%s%s'%(nameIn, i)
        try:
            name1 = mc.group(self.allJointGroup[0], name, name = name1)
        except:
            self.errorMessage(u'可能有重名物体!')
            return
        self.allGroupName.append(name1)
        mc.select(d = True)
        i = i + 1

        j = 0
        names = 'Miarmy_input'
        while True:
            if j == 0:
                names = 'Miarmy_input'
            else:
                names = 'Miarmy_input%s'%j
            if mc.objExists(names):
                j = j + 1
            else:
                break
        try:
            mc.group(self.allGroupName, name = names)
        except:
                self.errorMessage(u'可能有重名物体!')
                return
    def MiarmyOutputGroup(self):
        self.allGroupName = []
        nameOut = '%s'%self.ui.outputLine.text()
        i = 1
        self.allJointGroup = mc.ls(sl = True, type = 'joint')
        if not self.allJointGroup or not nameOut:
            self.errorMessage(u'请选择骨骼和填写outputName的值！')
            return
        for joints in self.allJointGroup:
            mc.select(d = True)
            mc.select(joints, r = True)
            jointsGroups = mc.ls(sl = True, shapes = True, dag = True, type = 'joint')
            for jointG in jointsGroups:
                try:
                    allSkinClusters = mc.listConnections('%s.lockInfluenceWeights'%jointG)
                    for skin in allSkinClusters:
                        if mc.objectType(skin) == 'skinCluster':
                            meshs = mc.listConnections('%s.outputGeometry'%skin)[0]
                            if not meshs in self.allMesh:
                                self.allMesh.append(meshs)
                except:
                    pass
            mc.select(d = True)
            while True:
                nameSkin = 'skin%s'%i
                if mc.objExists(nameSkin):
                    i = i + 1
                else:
                    break
            try:
                name = mc.group(self.allMesh, name = nameSkin)
            except:
                self.errorMessage(u'可能有重名物体!')
                return
            self.allMesh = []

            name1 = '%s%s'%(nameOut, i)
            try:
                name1 = mc.group(joints, name, name = name1)
            except:
                self.errorMessage(u'可能有重名物体!')
                return
            self.allGroupName.append(name1)
            mc.select(d = True)
            i = i + 1

        j = 0
        names = 'Miarmy_Output'
        while True:
            if j == 0:
                names = 'Miarmy_Output'
            else:
                names = 'Miarmy_Output%s'%j
            if mc.objExists(names):
                j = j + 1
            else:
                break
        try:
            mc.group(self.allGroupName, name = names)
        except:
                self.errorMessage(u'可能有重名物体!')
                return

if __name__ == "__main__":
    if mc.window("MiarmyGroupUI", exists=True):
        mc.deleteUI("MiarmyGroupUI")
    MiarmyOutputGroupUI = OCT_MiarmyGroup()
    MiarmyOutputGroupUI.show()