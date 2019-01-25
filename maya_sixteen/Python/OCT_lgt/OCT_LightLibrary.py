#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os
import sys
from mtoa.utils import createLocator

try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 


# 读取xml功能
class GetXMLData(object):
    # 读取xml文件
    def __init__(self, path):
        tree = ET.parse(path)
        self.root = tree.getroot()

    # 判断给定的tag名称是否有效
    def tagNameLegality(self, tagName):
        tag = '*/%s' % tagName
        dataList = self.root.findall(tag)
        if not dataList:
            return ''
        else:
            return dataList

    # 按列表模式返回tag名称下的text内容
    def getTagData(self, tagName):
        tagValue = []
        dataList = self.tagNameLegality(tagName)
        if not dataList:
            return ''
        for value in dataList:
            tagValue.append(value.text)
        return tagValue

    # 根据提供的Key tag名称和value tag名称组成dict，value名称时用list表示
    def getDataDict(self, keyTagName, valueTagName, *otherValueTagName):
        dataDict = {}
        valueDataList = []
        
        keyData = self.tagNameLegality(keyTagName)
        keyDataNumber = len(keyData)

        valueData = self.tagNameLegality(valueTagName)
        valueDataNumber = len(valueData)

        # 判断value数量是否与key数量相同，如果不同则无法组成dict
        if keyDataNumber != valueDataNumber:
            raise Exception('line 42:tag list number is wrong!')

        valueDataList = self.getTagData(valueTagName)
        if otherValueTagName:
            for tagName in otherValueTagName:
                otherValueData = self.tagNameLegality(tagName)
                if len(otherValueData) != keyDataNumber:
                    raise Exception('line 53:tag list number is wrong!')
                
                otherValueDataValue = self.getTagData(tagName)
                valueDataList = map(self.mergeList, valueDataList, otherValueDataValue)

        for x in xrange(keyDataNumber):
            self.dictAppend(dataDict, keyData[x].text, valueDataList[x])

        return dataDict

    def dictAppend(self, dic, key, lis):
        if key in dic:
            dic[key].append(lis)
        else:
            dic[key]=[lis]

    def mergeList(self, lis1, lis2):
        lis = []
        if isinstance(lis1, list):
            lis = lis1
        else:
            lis.append(lis1)
        if isinstance(lis2,list):
            lis = lis + lis2
        else:
            lis.append(lis2)
        return lis



class OCT_LightLibrary():
    def __init__(self, path):
        self.info = {}
        self._windowSize = (720, 700)
        self._windowName = 'lightLib_UI'
        if not mc.pluginInfo('mtoa.mll',q = True,l = True):
            mc.loadPlugin('mtoa.mll')
        getXMLData = GetXMLData(path)
        self.tempInfo = getXMLData.getDataDict('fileType', 'fileName', 'filePath', 'mapPathName')

        #中英文转换
        self.enToZHInfo = {'Walllamp':u'壁灯',
                            'Lampslot':u'灯槽',
                            'droplight':u'吊灯',
                            'spotlight':u'射灯',
                            'desklamp':u'台灯',
                            'downlight':u'筒灯'}
        for key in self.tempInfo:
            self.info[self.enToZHInfo[key]] = self.tempInfo[key]


    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName)

    def show(self):
        self.close()
        win = mc.window(self._windowName, wh = self._windowSize, t = u'灯光库', sizeable = False)

        layout = mc.formLayout()
        control = mc.treeView('control', parent = layout, abr = False )
        lightScroll = mc.scrollLayout('light', p=layout)
        mc.formLayout(layout, e=True, attachForm = [(control,'top', 2), (control,'left', 2), (control,'bottom', 2),
                    (lightScroll,'top', 2), (lightScroll,'right', 2), (lightScroll,'bottom', 2)],
                    attachPosition = [(control, 'left', 0, 0), (control, 'right', 0, 25), (lightScroll, 'left', 0, 25),
                    (lightScroll, 'right', 0, 99)])

        for key in self.info.keys():
            mc.treeView(control, e = True, addItem = (key, ''))
            # for typeName in assertText[key]:
            #     mc.treeView(control, e = True, addItem = (typeName, key))

        mc.treeView(control, e = True, selectCommand = self.setLightList)
        mc.showWindow(win)

    def setLightList(self, *args):
        if mc.rowColumnLayout('lightRow', q = True, ex = True):
            mc.deleteUI('lightRow')
        listRowColum = mc.rowColumnLayout('lightRow', numberOfColumns = 4, p = 'light')

        if self.info[args[0]]:
            for infoList in self.info[args[0]]:
                self.iconButton_UI(infoList[0], infoList[1], infoList[2])

    def iconButton_UI(self, fileName, filePath, iconPath):
        iconBName = '%s_iconB' %fileName
        popName = '%s_pop' %fileName
        icon_B = mc.nodeIconButton(iconBName, style = 'iconAndTextVertical', numberOfPopupMenus = True, ann = fileName, image1 = iconPath, label = fileName, h = 135, w = 135, p = 'lightRow')
        pop_M = mc.popupMenu(popName, parent = icon_B, b = 3 )
        mc.menuItem(l = u'新建灯光', parent = pop_M, c=lambda *arg:self.createArnoldLight(filePath))
        mc.menuItem(l = u'赋予选择灯光', parent = pop_M, c=lambda *arg:self.changeArnoldLight(filePath))

    ##################设置材质属性分类###################
    #def AttrCassIfication(self, types, dIconPath, num):
    def createArnoldLight(self, iesPath):
        aiPhoL = createLocator('aiPhotometricLight', asLight=1)
        attrName = '%s.ai_filename'% aiPhoL[0]
        mc.setAttr(attrName, iesPath, type = 'string')
        mc.confirmDialog( title=u'提醒', message=u'已创建灯光%s' %aiPhoL[1], button=['OK'], defaultButton='OK', icon='information')

    def changeArnoldLight(self, iesPath):
        selectObj = mc.ls(sl=True)
        if not selectObj:
            mc.confirmDialog( title=u'提醒', message=u'请选择Photometric灯光', button=['OK'], defaultButton='OK', icon='warning')
            return
        selectObj_s = mc.ls(sl=True, s=True)
        obj_s = mc.listRelatives(selectObj, s=True)
        if obj_s:
            allSelect = obj_s + selectObj_s
        elif selectObj_s:
            allSelect = selectObj_s
        else:
            mc.confirmDialog( title=u'提醒', message=u'请选择Photometric灯光', button=['OK'], defaultButton='OK', icon='warning')
            return

        for obj in allSelect:
            if mc.nodeType(obj) == 'aiPhotometricLight':
                attrName = '%s.ai_filename'% obj
                mc.setAttr(attrName, iesPath, type = 'string')
        mc.confirmDialog( title=u'提醒', message=u'灯光设置完成', button=['OK'], defaultButton='OK', icon='information')



path = r'\\octvision.com\CG\Tech\lightLib\ligthIESFile.xml'
lightLib = OCT_LightLibrary(path)
lightLib.show()
