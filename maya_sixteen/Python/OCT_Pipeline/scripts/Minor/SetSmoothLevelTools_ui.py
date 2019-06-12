# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetSmoothLevelTools.ui'
#
# Created: Thu Jun  6 16:46:19 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import os,sys,re
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
from PyQt4 import QtCore, QtGui
import sip
import maya.OpenMayaUI as mui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_smth_widget(object):
    def setupUi(self, smth_widget):
        smth_widget.setObjectName(_fromUtf8("smth_widget"))
        smth_widget.resize(506, 140)
        self.gridLayout = QtGui.QGridLayout(smth_widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(smth_widget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lab = QtGui.QLabel(self.frame)
        self.lab.setObjectName(_fromUtf8("lab"))
        self.horizontalLayout.addWidget(self.lab)
        self.lv_line = QtGui.QLineEdit(self.frame)
        self.lv_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lv_line.setObjectName(_fromUtf8("lv_line"))
        self.lv_line.setText(str(0))
        self.horizontalLayout.addWidget(self.lv_line)
        self.smth_sld = QtGui.QSlider(self.frame)
        self.smth_sld.setMinimum(0)
        self.smth_sld.setMaximum(3)
        self.smth_sld.setValue(0)
        self.smth_sld.setOrientation(QtCore.Qt.Horizontal)
        self.smth_sld.setObjectName(_fromUtf8("smth_sld"))
        self.horizontalLayout.addWidget(self.smth_sld)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addbt = QtGui.QPushButton(self.frame)
        self.addbt.setObjectName(_fromUtf8("addbt"))
        self.horizontalLayout_2.addWidget(self.addbt)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.delbt = QtGui.QPushButton(self.frame)
        self.delbt.setObjectName(_fromUtf8("delbt"))
        self.horizontalLayout_2.addWidget(self.delbt)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.smth_sld.valueChanged.connect(self.sl_val_changed)
        self.lv_line.returnPressed.connect(self.ln_val_entered)
        self.addbt.clicked.connect(self.objsAddAttr)
        self.delbt.clicked.connect(self.objsDelAttr)

        self.retranslateUi(smth_widget)
        QtCore.QMetaObject.connectSlotsByName(smth_widget)

    def retranslateUi(self, smth_widget):
        smth_widget.setWindowTitle(_translate("smth_widget", "Smooth Level Attribute Tools", None))
        self.lab.setText(_translate("smth_widget", "Smooth Level", None))
        self.addbt.setText(_translate("smth_widget", "Add/Set Attribute", None))
        self.delbt.setText(_translate("smth_widget", "Delete Attribute", None))


    def sl_val_changed(self):
        sm_level = self.smth_sld.value()
        self.lv_line.setText(str(sm_level))

    def ln_val_entered(self):
        sm_level = int(self.lv_line.text())
        self.smth_sld.setValue(sm_level)

    def objsAddAttr(self):
        attr_v = int(self.lv_line.text())
        for ea in self.collect_mesh_trns():
            self.addOrSet(ea,'setSmooth','long',attr_v,False,*[0,3])
            om.MGlobal.displayInfo("ADD ATTRIBUTE  setSmooth to node:  {}".format(ea.nodeName()))
    def objsDelAttr(self):
        for ea in self.collect_mesh_trns():
            if ea.hasAttr('setSmooth'):
                ea.deleteAttr('setSmooth')
                om.MGlobal.displayInfo("DEL ATTRIBUTE setSmooth from node:  {}".format(ea.nodeName()))
    def collect_mesh_trns(self):# get seleceted node contains meshes node's transform node list
        MeshesTrns = []
        SEL = pm.selected()
        for e in SEL:
            sel_shp = e.getShape()
            if sel_shp and sel_shp.type() != 'mesh': continue
            for n in e.listRelatives(ad=True, ni=True, type='mesh'):
                if n.getParent() not in MeshesTrns:
                    MeshesTrns.append(n.getParent())
        return MeshesTrns

    def addOrSet(self,objNode, attrName, attrType, attrV, kable=False, *minmax):#add attribute
        at = None
        if objNode.hasAttr(attrName):
            at = objNode.attr(attrName)
            if at.type() != attrType:
                objNode.deleteAttr(attrName)
                at = None
            else:
                at.set(attrV)
        if at == None:
            pm.addAttr(objNode, ln=attrName, at=attrType, dv=attrV)
            at = objNode.attr(attrName)
            at.setKeyable(kable)
        if minmax:
            at.setMin(minmax[0])
            at.setMax(minmax[1])


class QW_smth_widget(QtGui.QWidget):
    def __init__(self,*args,**kwargs):
        super(QW_smth_widget,self).__init__(*args,**kwargs)
        self.ui = Ui_smth_widget()
        self.ui.setupUi(self)
class SetSmoothLevelTools_ui(QtGui.QMainWindow):
    instance = None # 标记窗口是否已经被创建
    def __init__(self,parent=None):
        self.deleteInstance()
        self.__class__.instance = self
        super(SetSmoothLevelTools_ui,self).__init__(parent)
        self.setObjectName('SetSmoothLevelWin')
        self.cntWidget = QW_smth_widget()
        self.setCentralWidget(self.cntWidget)

        self.setWindowTitle('Smooth Level Tools')
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)

    def deleteInstance(self):
        if self.__class__.instance is not None:
            try:
                self.__class__.instance.deleteLater()
            except Exception as e:
                pass

    def showIt(self):
        self.show()


def main_my():
    # global appName
    # try:
    #     appName.ui.deleteLater()
    # except:
    #     pass
    MayaMainWin = sip.wrapinstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
    appName = SetSmoothLevelTools_ui(MayaMainWin)
    appName.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = SetSmoothLevelTools_ui()
    ex.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    main()