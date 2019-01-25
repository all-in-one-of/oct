# *-* coding=utf-8
__author__ = 'yangh'
from PyQt4 import QtGui, QtCore
import maya.OpenMayaUI as apiUI
import sip
import os
import  maya.cmds as mc
import sys

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

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

#读取选择的物体名，填写到self.sourceList中
#把self.sourceList列表中的动画数据写入到xml中
class WriteDataToXml_YH(QtGui.QDialog):
    def __init__(self, parent=getMayaWindow()):
        super(WriteDataToXml_YH, self).__init__(parent)

        self.fileName = mc.file(q = True, sn = True)
        #{物体对象:[曲线tx,[曲线ty]]}
        self.allAnimCurveClass = {}
        #所选没有动画数据的的物体
        self.allInitLocation = []
        #{曲线:[连接属性]}
        self.myAnimCurveType = {}
        #曲线帧数{曲线:帧数,[tx2的值]]}
        self.myAnimCurveFrame = {}

        #maya选择的物体
        self.listItems = []
        #allXmlObjDict{xml对象名:xml对象}
        self.allXmlObjDict = {}
        self.setObjectName(_fromUtf8("Ui_WriteDataToXml"))
        self.setWindowTitle(_fromUtf8("Ui_WriteDataToXml"))
        #设置窗口的大小，窗口字体的大小
        self.resize(300, 700)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setFont(font)

        self.mainLayout = QtGui.QVBoxLayout(self)

        self.sourceLabel = QtGui.QLabel(self)
        self.sourceLabel.setFont(font)
        self.sourceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceLabel.setText("Source")
        self.mainLayout .addWidget(self.sourceLabel)

        self.soureList = QtGui.QListWidget(self)
        self.soureList.setObjectName(_fromUtf8("soureList"))
        self.soureList.setFont(font)
        self.mainLayout.addWidget(self.soureList)

        self.gridLayout1 = QtGui.QGridLayout()
        self.selectObj = QtGui.QPushButton(self)
        self.selectObj.setMinimumSize(QtCore.QSize(0, 40))
        self.selectObj.setText(_fromUtf8(u"Add Selected"))
        self.selectObj.setFont(font)
        self.gridLayout1.addWidget(self.selectObj, 0, 1, 1, 1)

        self.applyButton = QtGui.QPushButton(self)
        self.applyButton.setMinimumSize(QtCore.QSize(0, 40))
        self.applyButton.setText(_fromUtf8(u"Apply"))
        self.applyButton.setFont(font)
        self.gridLayout1.addWidget(self.applyButton, 0, 2, 1, 1)
        self.mainLayout.addLayout(self.gridLayout1)
        self.setUpGui()

    #设置按钮
    def setUpGui(self):
        selectObj = self.selectObj
        applyButton = self.applyButton
        selectObj.clicked.connect(self.addSelectedObj)
        applyButton.clicked.connect(self.applyButtonClicked)

    def addSelectedObj(self):
        self.soureList.clear()
        allSelectedMayaObj = mc.ls(sl = True, dagObjects = True, transforms=True, ni = True, rq = True)
        for obj in allSelectedMayaObj:
            soureListItem = QtGui.QListWidgetItem(obj, self.soureList)

    #读取self.sourceList物体名，根据物体名读取动画数据
    def applyButtonClicked(self):
        numSource = self.soureList.count()
        for i in range(int(numSource)):
            obj = str(self.soureList.item(i).text())
            connections = mc.listConnections(obj, s = True, d = False)
            if connections:
                flag = False
                for conn in connections:
                    if mc.objectType(conn) == "animCurveTU" or mc.objectType(conn) == "animCurveTL" or mc.objectType(conn) == "animCurveTA":
                        if not obj in self.allAnimCurveClass.keys():
                            self.allAnimCurveClass.update({obj : [conn]})
                        else:
                            self.allAnimCurveClass[obj].append(conn)
                        flag = True
                if not flag:
                    self.allInitLocation.append(obj)
            else:
                self.allInitLocation.append(obj)

        for objs in self.allAnimCurveClass.keys():
            for anim in self.allAnimCurveClass[objs]:
                objAttr = mc.listConnections("%s.output"%anim, p = True)
                if objAttr:
                    #曲线的属性类型
                    attr = objAttr[0].split(".")[-1]
                    self.myAnimCurveType.update({anim : attr})

                #曲线的关键帧的位置
                numFrame = mc.keyframe(anim, q = True, tc = True)
                for num in numFrame:
                    Values = mc.keyframe(anim, t = (num, num), q = True, eval = True)[0]
                    if not anim in self.myAnimCurveFrame.keys():
                        self.myAnimCurveFrame.update({anim : [num]})
                        self.myAnimCurveFrame[anim].append(Values)
                    else:
                        self.myAnimCurveFrame[anim].append(num)
                        self.myAnimCurveFrame[anim].append(Values)

        xmlName = os.path.splitext(self.fileName)[0]+".xml"
        animCurves = self.WriteAnimData()
        animCurves.write(xmlName,"utf-8",True)
        self.allAnimCurveClass.clear()
        self.allInitLocation = []
        self.myAnimCurveFrame.clear()
        self.myAnimCurveType.clear()

    #写入数据到xml文本
    def WriteAnimData(self):
        #记录对象数据
        objName = "obj"
        animCurves = ElementTree()
        purOrder =Element("preset")
        animCurves._setroot(purOrder)
        for key in self.allAnimCurveClass.keys():
            lists = Element(objName, {'name' : key})
            parents = mc.listRelatives(key, p=True)
            if parents:
                lists.set("parent",parents[0])
            else:
                lists.set("parent", "")
            childName = mc.listRelatives(key, c=True, shapes=True)
            if childName:
                objType = mc.objectType(childName[0])
                lists.set("type", objType)
            else:
                objType = "transform"
                lists.set("type", objType)
            item = SubElement(lists, "fromChanel")
            translateX = mc.getAttr("%s.translateX"%key)
            translateY = mc.getAttr("%s.translateY"%key)
            translateZ = mc.getAttr("%s.translateZ"%key)
            item1 = SubElement(item, "translate")
            values = str(translateX) + " " + str(translateY) + " " + str(translateZ)
            item1.text = values

            rotateX = mc.getAttr("%s.rotateX"%key)
            rotateY = mc.getAttr("%s.rotateY"%key)
            rotateZ = mc.getAttr("%s.rotateZ"%key)
            item2 = SubElement(item, "rotate")
            values = str(rotateX) + " " + str(rotateY) + " " + str(rotateZ)
            item2.text = values

            scaleX = mc.getAttr('%s.scaleX'%key)
            scaleY = mc.getAttr('%s.scaleY'%key)
            scaleZ = mc.getAttr('%s.scaleZ'%key)
            item3 = SubElement(item, "scale")
            values = str(scaleX) + " " + str(scaleY) + " " + str(scaleZ)
            item3.text = values
            item = SubElement(lists, "animCurve")

            for k, keyframeInfo in enumerate(self.allAnimCurveClass[key]):
                #曲线keyframeInfo下级目录的数据
                numKey = len(self.myAnimCurveFrame[keyframeInfo])/2
                keyframeInfos = SubElement(item, 'keyInfo')
                keyframeInfos.set('name', keyframeInfo)
                types = self.myAnimCurveType[keyframeInfo]
                keyframeInfos.set('type', str(types))
                keyframeInfos.set('numKey', str(numKey))

                #曲线帧数信息
                for f in range(numKey):
                    frame = str(self.myAnimCurveFrame[keyframeInfo][f*2])
                    values = str(self.myAnimCurveFrame[keyframeInfo][f*2+1])
                    keyframes = SubElement(keyframeInfos, 'keyframe')
                    keyframes.set('frame', frame)
                    keyframes.text = values
            purOrder.append(lists)

        for initObj in self.allInitLocation:
            lists = Element(objName, {'name' : initObj})
            parents = mc.listRelatives(initObj,p=True)
            if parents:
                lists.set("parent",parents[0])
            else:
                lists.set("parent", "")
            childName = mc.listRelatives(initObj, c=True, shapes=True)
            if childName:
                objType = mc.objectType(childName[0])
                lists.set("type", objType)
            else:
                objType = "transform"
                lists.set("type", objType)

            item = SubElement(lists, "fromChanel")

            translateX = mc.getAttr("%s.translateX"%initObj)
            translateY = mc.getAttr("%s.translateY"%initObj)
            translateZ = mc.getAttr("%s.translateZ"%initObj)
            item1 = SubElement(item, "translate")
            values = str(translateX) + " " + str(translateY) + " " + str(translateZ)
            item1.text = values

            rotateX = mc.getAttr("%s.rotateX"%initObj)
            rotateY = mc.getAttr("%s.rotateY"%initObj)
            rotateZ = mc.getAttr("%s.rotateZ"%initObj)
            item2 = SubElement(item, "rotate")
            values = str(rotateX) + " " + str(rotateY) + " " + str(rotateZ)
            item2.text = values

            scaleX = mc.getAttr('%s.scaleX'%initObj)
            scaleY = mc.getAttr('%s.scaleY'%initObj)
            scaleZ = mc.getAttr('%s.scaleZ'%initObj)
            item3 = SubElement(item, "scale")
            values = str(scaleX) + " " + str(scaleY) + " " + str(scaleZ)
            item3.text = values

            purOrder.append(lists)
        self.indent(purOrder)
        return animCurves

    def indent(self, elem, level = 0):
        i ="\n"+level*"    "
        # print elem;
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "    "
            for e in elem:
                #print e
                self.indent(e,level+1)
            if not e.tail or not e.tail.strip():
                e.tail =i
        if level and (not elem.tail or not elem.tail.strip()):
            # print elem.tail
            elem.tail =i
        return elem

if __name__ == "__main__":
    if mc.window("Ui_WriteDataToXml", exists=True):
        mc.deleteUI("Ui_WriteDataToXml")
    ReadXmlDataToMaya_Ui = WriteDataToXml_YH()
    ReadXmlDataToMaya_Ui.show()