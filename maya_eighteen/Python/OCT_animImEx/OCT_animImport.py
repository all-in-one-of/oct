# *-* coding=utf-8
__author__ = 'yangh'
import xml.etree.ElementTree as ET
from PyQt4 import QtGui, QtCore
import sys
# import os
import maya.cmds as mc
import maya.OpenMayaUI as apiUI
import sip
import os

reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#获取maya的主窗口api
def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

# """实现读取xml信息和maya物体的类
#  1.实例UI类创建窗口是读取xml中的存的obj名写入窗口source列表
#  2.选择maya物体，把maya中选择的物体名写入窗口target列表
#  3.在maya中写入动画数据
class ReadXmlDataToMaya_YH(QtGui.QDialog):
    def __init__(self, parent=getMayaWindow()):
        super(ReadXmlDataToMaya_YH, self).__init__(parent)
        #maya选择的物体
        self.listItems = []
        #allXmlObjDict{xml对象名:xml对象}
        self.allXmlObjDict = {}
        self.setObjectName(_fromUtf8("Ui_ReadXmlDataToMaya"))
        self.setWindowTitle(_fromUtf8("Ui_ReadXmlDataToMaya"))
        #设置窗口的大小，窗口字体的大小
        self.resize(500, 700)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setFont(font)

        self.mainLayout = QtGui.QGridLayout(self)

        self.sourceLabel = QtGui.QLabel(self)
        self.sourceLabel.setFont(font)
        self.sourceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceLabel.setText("Source")
        self.mainLayout .addWidget(self.sourceLabel, 0, 1, 1, 1)

        self.soureList = QtGui.QListWidget(self)
        self.soureList.setObjectName(_fromUtf8("soureList"))
        self.soureList.setFont(font)
        #self.soureList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.mainLayout.addWidget(self.soureList, 1, 1, 1, 1)

        self.targetLabel = QtGui.QLabel(self)
        self.targetLabel.setFont(font)
        self.targetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.targetLabel.setText("Target")
        self.mainLayout .addWidget(self.targetLabel, 0 ,2, 1, 1)

        self.targetList = QtGui.QListWidget(self)
        self.targetList.setObjectName(_fromUtf8("targetList"))
        self.targetList.setFont(font)
        self.targetList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.targetList.connect(self.targetList, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)
        #支持拖放功能
        self.targetList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.mainLayout.addWidget(self.targetList, 1, 2, 1, 1)

        self.selectObj = QtGui.QPushButton(self)
        self.selectObj.setMinimumSize(QtCore.QSize(0, 40))
        self.selectObj.setText(_fromUtf8(u"Add Selected Obj"))
        self.selectObj.setFont(font)
        self.mainLayout.addWidget(self.selectObj, 2, 1, 1, 1)

        self.applyButton = QtGui.QPushButton(self)
        self.applyButton.setMinimumSize(QtCore.QSize(0, 40))
        self.applyButton.setText(_fromUtf8(u"Apply"))
        self.applyButton.setFont(font)
        self.mainLayout.addWidget(self.applyButton, 2, 2, 1, 1)
        self.mayaFileName = mc.file(q = True, sn = True)
        if not self.mayaFileName:
            mc.confirmDialog(title=u'警告', message=u'请保存文件，并命名文件名', button=['OK'], defaultButton='Yes', dismissString='No')
            mc.error(u'请保存文件，并命名文件名')
                       
        self.mayaFileName = os.path.splitext(self.mayaFileName)[0]+".xml"
        if not os.path.isfile(self.mayaFileName):
            mc.confirmDialog(title=u'警告', message=u'%s不存在！'%self.mayaFileName, button=['OK'], defaultButton='Yes', dismissString='No')
            mc.error(u'请保存文件，并命名文件名')
        #self.mayaFileName = 'E:/work/TestXml/scenes/Textxml.xml'

        #读取xml信息并填写到soureList列表中
        self.allXmlObjDict = self.readXmlObj(self.mayaFileName)
        self.setUpGui()

    #设置UI按钮
    def setUpGui(self):
        selectObj = self.selectObj
        applyButton = self.applyButton

        selectObj.clicked.connect(self.addSelectedObj)
        applyButton.clicked.connect(self.applyButtonClicked)
        self.soureList.itemDoubleClicked.connect(self.itemSoureSelection)
        self.targetList.itemDoubleClicked.connect(self.rebuildListWidget)

    def itemSoureSelection (self):
        numSource = self.soureList.count()
        soureList = []
        for i in range(int(numSource)):
            sourceName = str(self.soureList.item(i).text())
            soureList.append(sourceName)
        self.soureList.clear()
        for sel in soureList:
            print sel
            soureListItem = QtGui.QListWidgetItem(sel, self.soureList)

    #开始读取xml值并赋予maya物体动画数据
    def applyButtonClicked(self):
        currentItemtarget = self.targetList.currentItem()
        currentItemsoure = self.soureList.currentItem()
        if currentItemtarget and currentItemsoure:
            targetName = str(currentItemtarget.text())
            sourceName = str(currentItemsoure.text())
            xmlObj = self.allXmlObjDict[sourceName]
            print sourceName
            print xmlObj[-1].tag
            self.readAnimData(xmlObj, targetName)
        else:
            numSource = self.soureList.count()
            numTarget = self.targetList.count()
            num = ""
            if numSource > numTarget:
                num = int(numTarget)
            else:
                num = int(numSource)
            for i in range(num):
                sourceName = str(self.soureList.item(i).text())
                targetName = str(self.targetList.item(i).text())
                xmlObj = self.allXmlObjDict[sourceName]
                print xmlObj
                self.readAnimData(xmlObj, targetName)

    #读取xml中的动画数据在maya中设置
    def readAnimData(self, xmlObj, targetName):
        animCurveName = ""
        fromChanelName = ""
        if xmlObj[0].tag == "animCurve" and xmlObj[-1].tag == "fromChanel":
            fromChanelName = xmlObj[-1]
            animCurveName = xmlObj[0]
        elif xmlObj[-1].tag == "animCurve" and xmlObj[0].tag == "fromChanel":
            fromChanelName = xmlObj[0]
            animCurveName = xmlObj[-1]
        else:
            fromChanelName = xmlObj[0]

        for objs in fromChanelName:
            values = objs.text.split(" ")
            mc.setAttr("%s.%s"%(targetName,objs.tag),float(values[0]),float(values[1]),float(values[2]))

        if animCurveName:
            for anim in animCurveName:
                animName = anim.attrib["name"]
                types = anim.attrib['type']
                NodeName = ("%s_%s"%(targetName, types))
                #创建曲线节点
                if "translate" in types:
                    if not mc.objExists(NodeName):
                        NodeName = mc.createNode("animCurveTL", name = NodeName)
                    try:
                        mc.connectAttr("%s.output"%NodeName, "%s.%s"%(targetName, types))
                    except:
                        print(u"%s.output连接%s.%s出错"%(NodeName, targetName, types))

                if "rotate" in types:
                    if not mc.objExists(NodeName):
                        NodeName = mc.createNode("animCurveTA", name = NodeName)
                    try:
                        mc.connectAttr("%s.output"%NodeName, "%s.%s"%(targetName, types))
                    except:
                        print(u"%s.output连接%s.%s出错"%(NodeName, targetName, types))

                if "scale" in types:
                    if not mc.objExists(NodeName):
                        NodeName = mc.createNode("animCurveTU", name = NodeName)
                    try:
                        mc.connectAttr("%s.output"%NodeName, "%s.%s"%(targetName, types))
                    except:
                        print(u"%s.output连接%s.%s出错"%(NodeName, targetName, types))
                else:
                    if not mc.objExists(NodeName):
                        NodeName = mc.createNode("animCurveTU", name = NodeName)
                    try:
                        mc.connectAttr("%s.output"%NodeName, "%s.%s"%(targetName, types))
                    except:
                        print(u"%s.output连接%s.%s出错"%(NodeName, targetName, types))

                for curves in anim:
                    frame = float(curves.attrib['frame'])
                    mc.setKeyframe(NodeName, t = frame, v = float(curves.text))

    #鼠标右键触发的菜单事件
    def listItemRightClicked(self, QPos):
        self.listMenu= QtGui.QMenu()
        menu_item = self.listMenu.addAction("Remove Item")
        menu_item1 = self.listMenu.addAction("Move Top")
        if len(self.listItems) == 0:
            menu_item.setDisabled(True)
            menu_item1.setDisabled(True)
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
        self.connect(menu_item1, QtCore.SIGNAL("triggered()"), self.menuItem1Clicked)

        parentPosition = self.targetList.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(parentPosition + QPos)

        self.listMenu.show()

    #鼠标右键触发的选择的控件移到顶部事件
    def menuItem1Clicked(self):
        if len(self.listItems)==0:
            print 'return from menuItem1Clicked'
            return
        currentItemName=str(self.targetList.currentItem().text())
        self.listItems.remove(currentItemName)
        self.listItems.insert(0, currentItemName)
        self.rebuildListWidget()

    #鼠标右键触发的移除控件事件
    def menuItemClicked(self):
        if len(self.listItems)==0:
            print 'return from menuItemClicked'
            return
        currentItemName = str(self.targetList.currentItem().text())
        #self.listItems.pop(currentItemName, None)
        self.listItems.remove(currentItemName)
        self.rebuildListWidget()

    #选择maya物体添加到界面上
    def addSelectedObj(self):
        allSelect = mc.ls(sl = True)
        self.listItems = allSelect
        self.rebuildListWidget()

    def rebuildListWidget(self):
        self.targetList.clear()
        for sel in self.listItems:
            targetListItem = QtGui.QListWidgetItem(sel, self.targetList)

    #根据传入的xml文件名，读取xml中的对象，写入soureList列表中，并返回字典allXmlObjectDict{xml对象：xml对象名}
    def readXmlObj(self, mayaFileName):
        allXmlObjectDict = {}
        tree = ET.parse(mayaFileName)
        root = tree.getroot()
        for child in root:
            obj = child.attrib['name']
            allXmlObjectDict.update({obj:child})
            soureListItem = QtGui.QListWidgetItem(self.soureList)
            soureListItem.setText(obj)
        return allXmlObjectDict


if __name__ == "__main__":
    if mc.window("Ui_ReadXmlDataToMaya", exists=True):
        mc.deleteUI("Ui_ReadXmlDataToMaya")
    ReadXmlDataToMaya_Ui = ReadXmlDataToMaya_YH()
    ReadXmlDataToMaya_Ui.show()

    # app = QtGui.QApplication(sys.argv)
    # ReadXmlDataToMaya_YH = ReadXmlDataToMaya_YH()
    # ReadXmlDataToMaya_YH.show()
    # ReadXmlDataToMaya_YH.resize(480,320)
    # sys.exit(app.exec_())