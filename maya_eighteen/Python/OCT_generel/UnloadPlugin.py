# -*- coding: utf-8 -*-

import maya.cmds as mc
import shiboken
import os
import json
import maya.OpenMayaUI as omUI
from PySide import QtCore, QtGui


def unknownNodeClear():
    allunknows=mc.ls(et="unknown")
    for unknows in allunknows:
        if mc.objExists(unknows):
            if mc.lockNode(unknows,q=True):
                mc.lockNode(unknows,l=False)
            mc.delete(unknows)

def getMayaWindow():
    ptr = omUI.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken.wrapInstance(long(ptr), QtGui.QWidget)


class UnloadPlugin(object):
    def __init__(self):
        self.__pluginName = None

    def __str__(self):
        return 'plugin name is %s !' %self.__pluginName
    
    def __repr__(self):
        return 'plugin name is %s !' %self.__pluginName

    def __call__(self):
        return self.__pluginName

    @property
    def pluginName(self):
        return self.__pluginName

    @pluginName.setter
    def pluginName(self, name):
        if isinstance(name, str):
            self.__pluginName = name
        else:
            raise ValueError('value error!')

    def isLoaded(self):
        return mc.pluginInfo(self.__pluginName,q=True, l=True)

    def deleteNodes(self):
        if self.__pluginName:
            mentalNodeList = mc.pluginInfo(self.__pluginName, q=True, dn=True)
            if not mentalNodeList:
                return 0
            for nodeName in mentalNodeList:
                nodes = mc.ls(et=nodeName)
                if not nodes:
                    continue
                for node in nodes:
                    try:
                        mc.delete(node)
                    except:
                        mc.warning('%s can\'t delete!' % node)

    def setAutoLoad(self, autoLoadVal=0):
        mc.pluginInfo(self.__pluginName, e=True, a=autoLoadVal)

    def unload_normal(self):
        if self.__pluginName:
            mc.unloadPlugin(self.__pluginName, f=True)
            try:
                self.setAutoLoad()
            except:
                pass
            
    def unload_force(self):
        if self.__pluginName:
            mc.flushUndo()
            mc.pluginInfo(self.__pluginName,e=True, rm=True)
            try:
                self.setAutoLoad()
            except:
                pass

    def unknown_remove(self):
        if self.__pluginName:
            mc.unknownPlugin(self.__pluginName, r=True)


class ListWidget_Filter(object):
    def __init__(self, jsonPath):
        with open(jsonPath, 'r') as jsonFile:
            try:
                jsonInfo = json.load(jsonFile)
            except:
                raise('json file read error!')
        self.__RenderPlugin_Name = jsonInfo['RenderPluginName']
        self.__NoUsePlugin_Name = jsonInfo['NoUsePluginName']
        self.__whiteList_Path = self.absPath(jsonInfo['WhitePath'])
        self.__whiteList_Name = jsonInfo['WhiteName']
        self.__blackList_Path = self.absPath(jsonInfo['RemovePath'])
        self.__blackList_Name = list(set(jsonInfo['RemoveName'] + self.__RenderPlugin_Name))
        
    def __str__(self):
        return 'plugin filter!You can use "getRulesList" to get list!'
    
    def __repr__(self):
        return 'plugin filter!You can use "getRulesList" to get list!'

    def absPath(self, valList):
        result = []
        for val in valList:
            path = os.path.abspath(val)
            result.append(path)
        return result

    #def add_path(self, path):
    #    path = os.path.abspath(path)
    #    if path in self.__blackList_Path:
    #        self.__blackList_Path.remove(path)
    #    #else:
    #    #    self.__whiteList_Path(path)

    #def add_name(self, name):
    #    if name in self.__blackList_Name:
    #        self.__blackList_Name.remove(name)
    #    else:
    #        self.__whiteList_Name.append(name)

    #def remove_path(self, path):
    #    path = os.path.abspath(path)
    #    self.__blackList_Path.append(path)

    #def remove_name(self, name):
    #    self.__blackList_Name.append(name)

    def getAddName(self):
        return self.__whiteList_Name

    def getRemoveName(self):
        return self.__blackList_Name

    def getRemovePath(self):
        return self.__blackList_Path

    # rule list
    def getRulesList(self, valList):
        rightList = []
        for val in valList:
            if val in self.__blackList_Name:
                continue
            else:
                if val in self.__whiteList_Name:
                    rightList.append(val)
                    continue
            path = mc.pluginInfo(val, q=True, p=True)
            path = os.path.abspath(os.path.dirname(path))
            if path in self.__blackList_Path:
                continue
            rightList.append(val)
        return rightList

    #type list
    def getRenderPlugin(self, pluginNameList):
        renderList = []
        for name in pluginNameList:
            if name in self.__RenderPlugin_Name:
                renderList.append(name)
        return renderList

    def getPathPlugin(self, path, pluginNameList):
        pathPluginList = []
        path = os.path.abspath(path)
        for name in pluginNameList:
            pluginPath = mc.pluginInfo(name, q=True, p=True)
            if os.path.abspath(os.path.dirname(pluginPath)) == path:
                pathPluginList.append(name)
        return pathPluginList

    def getNoUsePlugin(self):
        return self.__NoUsePlugin_Name


class UnloadPlugin_Window(QtGui.QDialog):
    def __init__(self, jsonPath, parent=None):
        super(UnloadPlugin_Window, self).__init__(parent)
        self.unloadPlugin = UnloadPlugin()

        self.pluginFilter = ListWidget_Filter(jsonPath)
        self.mayaPluginPath = os.path.abspath('%s/bin/plug-ins'%os.environ['MAYA_LOCATION'])
        self.noUsePluginName = self.pluginFilter.getNoUsePlugin()
        
        if mc.window('UnloadPlugin_Window', q=True, ex=True):
            mc.deleteUI('UnloadPlugin_Window')

        self.setupUi(parent)
        self.ui_details()

    def setupUi(self, widget):
        self.setParent(widget)
        self.resize(500, 400)

        mainVL = QtGui.QVBoxLayout()
        mainVL.setObjectName("mainVL")

        loadedPlugin_HL = QtGui.QHBoxLayout()
        loadedPlugin_HL.setObjectName("loadedPlugin_HL")

        loadedPlugin_VL = QtGui.QVBoxLayout()
        loadedPlugin_VL.setObjectName("loadedPlugin_VL")

        self.loadedPlugin_L = QtGui.QLabel()
        self.loadedPlugin_L.setAlignment(QtCore.Qt.AlignCenter)
        self.loadedPlugin_L.setObjectName("loadedPlugin_L")
        
        self.loadedPlugin_LW = QtGui.QListWidget()
        self.loadedPlugin_LW.setObjectName("loadedPlugin_LW")

        self.loadedPlugin_PB = QtGui.QPushButton()
        self.loadedPlugin_PB.setObjectName('loadedPlugin_PB')
        
        loadedPlugin_VL.addWidget(self.loadedPlugin_L)
        loadedPlugin_VL.addWidget(self.loadedPlugin_LW)
        loadedPlugin_VL.addWidget(self.loadedPlugin_PB)
        
        loadedPlugin_HL.addLayout(loadedPlugin_VL)
        
        unknownPlugin_VL = QtGui.QVBoxLayout()
        unknownPlugin_VL.setObjectName("unknownPlugin_VL")
        
        self.unknownPlugin_L = QtGui.QLabel()
        self.unknownPlugin_L.setAlignment(QtCore.Qt.AlignCenter)
        self.unknownPlugin_L.setObjectName("unknownPlugin_L")
        
        self.unknownPlugin_LW = QtGui.QListWidget()
        self.unknownPlugin_LW.setObjectName("unknownPlugin_LW")

        self.unknownPlugin_PB = QtGui.QPushButton()
        self.unknownPlugin_PB.setObjectName('unknownPlugin_PB')
        
        unknownPlugin_VL.addWidget(self.unknownPlugin_L)
        unknownPlugin_VL.addWidget(self.unknownPlugin_LW)
        unknownPlugin_VL.addWidget(self.unknownPlugin_PB)
        
        loadedPlugin_HL.addLayout(unknownPlugin_VL)

        renderPlugin_VL = QtGui.QVBoxLayout()
        renderPlugin_VL.setObjectName("renderPlugin_VL")
        
        self.renderPlugin_L = QtGui.QLabel()
        self.renderPlugin_L.setAlignment(QtCore.Qt.AlignCenter)
        self.renderPlugin_L.setObjectName("renderPlugin_L")
        
        self.renderPlugin_LW = QtGui.QListWidget()
        self.renderPlugin_LW.setObjectName("renderPlugin_LW")

        self.renderPlugin_PB = QtGui.QPushButton()
        self.renderPlugin_PB.setObjectName('renderPlugin_PB')
        
        renderPlugin_VL.addWidget(self.renderPlugin_L)
        renderPlugin_VL.addWidget(self.renderPlugin_LW)
        renderPlugin_VL.addWidget(self.renderPlugin_PB)
        
        loadedPlugin_HL.addLayout(renderPlugin_VL)

        mainVL.addLayout(loadedPlugin_HL)

        Button_HL = QtGui.QHBoxLayout()
        Button_HL.setObjectName("horizontalLayout")
        
        self.run_B = QtGui.QPushButton()
        self.run_B.setObjectName("run_B")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_B.sizePolicy().hasHeightForWidth())
        self.run_B.setSizePolicy(sizePolicy)
        self.run_B.setMinimumSize(QtCore.QSize(50, 30))
        self.run_B.setMaximumSize(QtCore.QSize(200, 16777215))
        
        Button_HL.addWidget(self.run_B)
        
        self.cancel_B = QtGui.QPushButton()
        self.cancel_B.setObjectName("cancel_B")

        sizePolicy.setHeightForWidth(self.cancel_B.sizePolicy().hasHeightForWidth())
        self.cancel_B.setSizePolicy(sizePolicy)
        self.cancel_B.setMinimumSize(QtCore.QSize(50, 30))
        self.cancel_B.setMaximumSize(QtCore.QSize(200, 16777215))
        
        Button_HL.addWidget(self.cancel_B)

        mainVL.addLayout(Button_HL)

        self.setLayout(mainVL)

    def ui_details(self):
        self.setObjectName("UnloadPlugin_Window")
        self.setWindowTitle(u'插件卸载器')
        self.loadedPlugin_L.setText(u"已加载插件")
        self.unknownPlugin_L.setText(u"未知插件")
        self.renderPlugin_L.setText(u'渲染插件')
        self.loadedPlugin_PB.setText(u'全选')
        self.unknownPlugin_PB.setText(u'')
        self.renderPlugin_PB.setText(u'全选')
        self.run_B.setText(u'卸载')
        self.cancel_B.setText(u'取消')

        allPluginList = mc.pluginInfo(q=True, ls=True)
        self.loadedPluginList = self.pluginFilter.getRulesList(allPluginList)
        self.renderPluginList = self.pluginFilter.getRenderPlugin(allPluginList)
        self.unknownPluginList = mc.unknownPlugin(q=True, l=True)
        #if not self.unknownPluginList:
        #    self.unknownPluginList = []

        self.loadedPlugin_LW.itemClicked.connect(self.itemClicked)
        self.unknownPlugin_LW.itemClicked.connect(self.itemClicked)
        self.renderPlugin_LW.itemClicked.connect(self.itemClicked)

        otherList = list(set(self.loadedPluginList)-set(self.noUsePluginName))
        self.loadedPlugin_PB.clicked.connect(lambda:self.selectAllItem(self.loadedPlugin_LW, self.loadedPlugin_PB, otherList))
        #self.unknownPlugin_PB.clicked.connect(lambda:self.selectAllItem(self.unknownPlugin_LW, self.unknownPlugin_PB, self.unknownPluginList))
        self.renderPlugin_PB.clicked.connect(lambda:self.selectAllItem(self.renderPlugin_LW, self.renderPlugin_PB, self.renderPluginList))

        self.run_B.clicked.connect(self.run_Button)
        self.cancel_B.clicked.connect(self.close)

        self.loadedPlugin_Item()
        self.unknownPlugin_Item()
        self.renderPlugin_Item()

    def loadedPlugin_Item(self):
        if self.loadedPluginList:
            mayaPluginList = self.pluginFilter.getPathPlugin(self.mayaPluginPath, self.loadedPluginList)
            self.addItem(self.loadedPlugin_LW, mayaPluginList, QtCore.Qt.Checked)
            otherList = list(set(self.loadedPluginList)-set(mayaPluginList))
            self.addItem(self.loadedPlugin_LW, otherList)

    def unknownPlugin_Item(self):
        if self.unknownPluginList:
            self.addItem(self.unknownPlugin_LW, self.unknownPluginList, QtCore.Qt.Checked)

    def renderPlugin_Item(self):
        if self.renderPlugin_Item:
            self.addItem(self.renderPlugin_LW, self.renderPluginList)

    def addItem(self, listWidgetName, pluginList, checkedstate = QtCore.Qt.Unchecked):
        for name in pluginList:
            item = QtGui.QListWidgetItem(name, listWidgetName)
            item.setCheckState(checkedstate)
            item.setText(name)

    def itemClicked(self, item):
        pluginName = str(item.text())
        if pluginName in self.noUsePluginName:
            item.setCheckState(QtCore.Qt.Checked)
        #elif pluginName in self.unknownPluginList:
        #    item.setCheckState(QtCore.Qt.Checked)
        else:
            if item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

    def selectAllItem(self, listWidetName, pushButton, pluginList):
        if pushButton.text() == u'全选':
            pushButton.setText(u'取消全选')
            checkState = QtCore.Qt.Checked
        else:
            pushButton.setText(u'全选')
            checkState = QtCore.Qt.Unchecked
        num = listWidetName.count()
        row=0
        while (row<num):
            item = listWidetName.item(row)
            pluginName = str(item.text())
            if pluginName in pluginList:
                item.setCheckState(checkState)
            row += 1

    def run_Button(self, *args):
        if self.allItemSelect(self.renderPlugin_LW):
            mes = u'渲染器全卸载完后，当前文件内的相关渲染器的材质灯光等节点会全部删除（参考文件除外），并无法恢复，请谨慎处理！！！'
            ret = self.messageBox_Window(mes,1)
            if ret == QtGui.QMessageBox.Cancel:
                return 0

        self.setCursor(QtCore.Qt.WaitCursor)
        self.errorPluginList = []
        unknownNodeClear()
        self.deleteItemChicked(self.loadedPlugin_LW, self.loadedPluginList, 'loaded')
        self.deleteItemChicked(self.unknownPlugin_LW, self.unknownPluginList, 'unknown')
        self.deleteItemChicked(self.renderPlugin_LW,self.renderPluginList, 'render')
        self.setCursor(QtCore.Qt.ArrowCursor)
        if self.errorPluginList:
            for listWidgetName, pluginName, row in self.errorPluginList:
                mes = u'%s 无法删除！是否要使用暴力模式 -。-！！！\r\n PS. 确定后操作不可逆，请保存好文件' %pluginName
                ret = self.messageBox_Window(mes)
                if ret==QtGui.QMessageBox.Ok:
                    self.setCursor(QtCore.Qt.WaitCursor)
                    self.unloadPlugin.pluginName = pluginName
                    listWidgetName.takeItem(row)
                    self.unloadPlugin.unload_force()
                    self.setCursor(QtCore.Qt.ArrowCursor)
                    print('%s plugin is deleted!' %pluginName)

    def messageBox_Window(self, mes, styleOn=0):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(u'警告')
        msgBox.setInformativeText(mes)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok| QtGui.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtGui.QMessageBox.Cancel)
        msgBox.setIcon(QtGui.QMessageBox.Critical)
        if styleOn:
            msgBox.setStyleSheet("font: 18pt \"新宋体\";\n"
                                 "color: rgb(255, 0, 4);")
        ret = msgBox.exec_()
        return ret

    def allItemSelect(self, listWidgetName):
        isAllSelect = 1
        num = listWidgetName.count()
        row = 0
        while (row<num):
            item = listWidgetName.item(row)
            if item.checkState() == QtCore.Qt.Unchecked:
                isAllSelect = 0
                break
            else:
                row += 1
        return isAllSelect

    def deleteItemChicked(self, listWidgetName, itemList, type = 'unknown'):
        num = listWidgetName.count()
        row = 0
        while (row<num):
            item = listWidgetName.item(row)
            if not item:
                break
            if item.checkState() == QtCore.Qt.Unchecked:
                row += 1
                continue
            pluginName = str(item.text())
            self.unloadPlugin.pluginName = pluginName
            if type=='unknown':
                try:
                    self.unloadPlugin.unknown_remove()
                except:
                    mc.warning("%s plugin can't delete!" %pluginName)
                    #self.unloadPlugin.unknown_remove()
                listWidgetName.takeItem(row)
                itemList.remove(pluginName)
                print('%s plugin is deleted!' %pluginName)
            else:
                self.unloadPlugin.deleteNodes()
                try:
                    self.unloadPlugin.unload_normal()
                    print('%s plugin is deleted!' %pluginName)
                    listWidgetName.takeItem(row)
                    itemList.remove(pluginName)
                    if type=='render':
                        mes = u'  请保存或checkIn后重开Maya，以免新开的maya文件崩溃！\n\tQAQ'
                        self.messageBox_Window(mes, 1)
                except:
                    self.errorPluginList.append((listWidgetName,pluginName,row))
                    row+=1


def main():
    jsonPath = r'\\octvision\cg\Tech\maya_sixteen\Python\OCT_generel\json\UnloadPlugin.json'
    aa = UnloadPlugin_Window(jsonPath, getMayaWindow())
    aa.show()


