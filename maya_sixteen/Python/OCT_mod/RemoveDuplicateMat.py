#!/usr/bin/env python
# coding=utf-8
import maya.cmds as mc
import maya.mel as mm


class CheckMat(object):
    def __init__(self):
        self.initSG = ['initialParticleSE', 'initialShadingGroup']
        self.__isCheck = 0
        self.sameSGTypeDict = {}

        self.__duplicateMat = []
        self.__unUsedSG = []

    @property
    def isCheck(self):
        return self.__isCheck

    @isCheck.setter
    def isCheck(self, value):
        if value in [0, 1, True, False]:
            self.__isCheck = value
        else:
            raise ValueError('value error!')

    @property
    def sameList(self):
        return self.__duplicateMat

    @property
    def unUsedList(self):
        return self.__unUsedSG

    def checkMat(self):
        if not self.__isCheck:
            self.all_SG = mc.ls(type = 'shadingEngine')
            self.all_SG = list(set(self.all_SG) - set(self.initSG))
            self.sameSGTypeDict = {}
            self.__duplicateMat = []
            self.__unUsedSG = []
            self.check()

    def check(self):
        for oneSG in self.all_SG:
            mc.hyperShade(objects = oneSG)
            selectObj = mc.ls(sl = True)
            if selectObj:
                self.classification_SG(oneSG)
            else:
                if not oneSG in self.initSG:
                    self.__unUsedSG.append(oneSG)
        self.sameSGNetworking()
        self.__isCheck = 1

    def classification_SG(self, sgNode):
        shaders = mc.listConnections(sgNode, d = False, s = True)
        if shaders == None:
            return

        for oneShader in shaders:
            typeNode = mc.nodeType(oneShader)
            if mc.getClassification(typeNode, satisfies = 'shader/surface'):
                if typeNode in self.sameSGTypeDict:
                    self.sameSGTypeDict[typeNode].append(sgNode)
                else:
                    self.sameSGTypeDict[typeNode] = [sgNode]

    def sameSGNetworking(self):
        for sameTypeSGList in self.sameSGTypeDict.values():
            dupSGList = sameTypeSGList
            id = 0
            num = len(sameTypeSGList)
            while id < (num-1):
                tempSGList = []
                for SG_Id in xrange(id+1, num):
                    shaderCompare = mc.shadingNetworkCompare(dupSGList[id], dupSGList[SG_Id])
                    if mc.shadingNetworkCompare(shaderCompare, q = True, eq = True):
                        if not dupSGList[id] in tempSGList:
                            tempSGList.append(' ')
                            tempSGList.append(dupSGList[id])
                        tempSGList.append(dupSGList[SG_Id])

                    mc.shadingNetworkCompare(shaderCompare, delete = True)
                
                if tempSGList:
                    self.__duplicateMat += tempSGList
                    dupSGList = list(set(dupSGList)- set(tempSGList))
                    num = len(dupSGList)
                else:
                    id += 1


class CleanMatertialTool(object):
    def __init__(self):
        if mc.window('cleanMaterialTool_UI', exists=True):
            mc.deleteUI('cleanMaterialTool_UI', window=True)

        if mc.windowPref('cleanMaterialTool_UI', exists=True):
            mc.windowPref('cleanMaterialTool_UI', remove=True)

        self.checkMat = CheckMat()
        self.dupMatInfo = {}

    # ------------------
    # UI窗口
    # __________________

    def showWindow(self):
        mc.window('cleanMaterialTool_UI', t='Clean Material Tool', wh=[520, 272], mnb=True, mxb=True, rtf=True, menuBar=True)
        mc.formLayout('formLyt', numberOfDivisions=100)
        mc.textScrollList('sameSGList_Scroll', nr=10, ams=True, h=160, w=148, parent='formLyt', dcc=lambda *args:self.sameList_dcc())
        mc.textScrollList('unUsedSGList_Scroll', nr=10, ams=True, h=160, w=148, parent='formLyt', dcc=lambda *args:self.unList_dcc())
        
        mc.columnLayout('sameSG_CL', cal='center',h=160, rs=30, parent='formLyt')
        mc.button('cleanSel', w=48, l='Clean Sel', parent='sameSG_CL', c=lambda *args:self.dupMat_cleanSel())
        mc.button('cleanAll', w=48, l='Clean All', parent='sameSG_CL', c=lambda *args:self.dupMat_cleanAll())
        mc.button('refresh1', w=48, l='Refresh', parent='sameSG_CL', c=lambda *args:self.dupMat_refresh())
        
        mc.columnLayout('unUsedSG_CL', cal='center',h=160, rs=30, parent='formLyt')
        mc.button('delAll2', l='Del All', w=48, parent='unUsedSG_CL', c=lambda *args:self.unUsed_cleanAll())
        mc.button('refresh2', l='Refresh', w=48, parent='unUsedSG_CL', c=lambda *args:self.unUsed_refresh())

        mc.button('refreshAll_B', l='Refresh All', w=408, parent='formLyt', c=lambda *args:self.refreshAll())
        mc.button('close_B', l='Close', width=408, parent='formLyt', c=lambda *args:self.close())

        mc.formLayout('formLyt', e=True, 
                      attachNone=( ['sameSG_CL', 'left'], ['refreshAll_B', 'top'], ['close_B', 'top'], ['unUsedSG_CL', 'left'] ), \
                      attachForm=( ['sameSGList_Scroll', 'left', 5], ['sameSGList_Scroll', 'top', 5], ['sameSG_CL','top',30], ['unUsedSGList_Scroll', 'top', 5], ['unUsedSG_CL', 'top', 30], ['unUsedSG_CL', 'right', 5], ['refreshAll_B', 'left', 5], ['refreshAll_B', 'right', 5], ['close_B', 'left', 5], ['close_B', 'bottom', 5], ['close_B', 'right', 5] ), \
                      attachControl=( ['sameSGList_Scroll', 'bottom', 5, 'refreshAll_B'], ['sameSGList_Scroll', 'right', 5, 'sameSG_CL'], ['sameSG_CL', 'bottom', 5, 'refreshAll_B'], ['unUsedSGList_Scroll', 'bottom', 5, 'refreshAll_B'], ['unUsedSGList_Scroll', 'right', 5, 'unUsedSG_CL'], ['unUsedSG_CL', 'bottom', 5, 'refreshAll_B'], ['refreshAll_B', 'bottom', 5, 'close_B'] ), \
                      attachPosition=( ['sameSG_CL', 'right', 5, 50], ['unUsedSGList_Scroll', 'left', 0, 50] ) )

        mc.showWindow('cleanMaterialTool_UI')

    def sameList_dcc(self):
        sel = mc.textScrollList('sameSGList_Scroll', q=True, si=True)
        if len(sel) > 0 and sel[0] != ' ':
            mc.select(sel,r=True,ne=True)

    def unList_dcc(self):
        sel = mc.textScrollList('unUsedSGList_Scroll', q=True, si=True)
        if len(sel) > 0 and sel[0] != ' ':
            mc.select(sel,r=True,ne=True)

    def dupMat_cleanSel(self):
        selItemList = mc.textScrollList('sameSGList_Scroll', q = True, si = True)
        if selItemList and self.dupMatInfo:
            for selItem in selItemList:
                if selItem == ' ':
                    continue
                for k, v in self.dupMatInfo.iteritems():
                    if selItem in v:
                        v.remove(selItem)
                        if len(v) > 0:
                            connections = mc.listConnections('%s.dagSetMembers' %selItem, p = True, connections = True)
                            if not connections:
                                continue
                            for i in xrange(0,len(connections),2):
                                setDstPlug = connections[i]
                                srcPlug = connections[i+1]
                                mc.disconnectAttr(srcPlug, setDstPlug)
                                mc.connectAttr(srcPlug, '%s.dagSetMembers' %v[0], na = True)
                            self.removeItem('sameSGList_Scroll', selItem)
                        if len(v) == 1:
                            self.removeItem('sameSGList_Scroll', v[0])
                        self.dupMatInfo[k] = v

    def dupMat_cleanAll(self):
        if self.dupMatInfo:
            for id, SGNodeList in self.dupMatInfo.iteritems():
                num = len(SGNodeList)
                if num > 1:
                    SGNodeName = self.getSGNode_MaxObjNum(SGNodeList)
                    for SGNode in SGNodeList:
                        if SGNode != SGNodeName:
                            connections = mc.listConnections('%s.dagSetMembers' %SGNode, p = True, connections = True)
                            if not connections:
                                continue
                            for i in xrange(0,len(connections),2):
                                setDstPlug = connections[i]
                                srcPlug = connections[i+1]
                                mc.disconnectAttr(srcPlug, setDstPlug)
                                mc.connectAttr(srcPlug, '%s.dagSetMembers' %SGNodeName, na = True)
            self.removeAllItem('sameSGList_Scroll')
            self.dupMatInfo.clear()

    def dupMat_refresh(self, isCheck = 0):
        self.dupMatInfo = {}
        if not isCheck:
            self.checkMat.isCheck = 0
            self.checkMat.checkMat()
        self.refreshBaseFuntion('sameSGList_Scroll', self.checkMat.sameList)
        self.dupMatInfo = self.getDuplicateMatInfo()

    def unUsed_cleanAll(self):
        allItem = mc.textScrollList('unUsedSGList_Scroll', q = True, ai = True)
        if allItem:
            mm.eval('MLdeleteUnused')
            self.removeAllItem('unUsedSGList_Scroll')

    def unUsed_refresh(self, isCheck = 0):
        if not isCheck:
            self.checkMat.isCheck = 0
            self.checkMat.checkMat()
        self.refreshBaseFuntion('unUsedSGList_Scroll', self.checkMat.unUsedList)

    def refreshAll(self):
        self.checkMat.isCheck = 0
        self.checkMat.checkMat()
        self.dupMat_refresh(1)
        self.unUsed_refresh(1)

    def close(self):
        mc.deleteUI("cleanMaterialTool_UI",window=True)
        del self.checkMat

    # ------------------------
    # 功能性
    # ________________________
    
    def removeAllItem(self, textScrollListName):
        mc.textScrollList(textScrollListName, e = True, removeAll = True)

    def addItem(self, textScrollListName, itemName):
        mc.textScrollList(textScrollListName, e = True, append = itemName)

    def removeItem(self, textScrollListName, itemName):
        mc.textScrollList(textScrollListName, e = True, ri = itemName)

    def refreshBaseFuntion(self, scrollName, itemList):
        self.removeAllItem(scrollName)
        if itemList:
            for item in itemList:
                self.addItem(scrollName, item)

    def getDuplicateMatInfo(self):
        sameMatInfo = {}
        id = -1
        if self.checkMat.sameList:
            for item in self.checkMat.sameList:
                if item == ' ':
                    id += 1
                    sameMatInfo[id] = []
                    continue
                sameMatInfo[id].append(item)
        return sameMatInfo
    
    def getHaveMatNodes(self, SGNodeList):
        matNodes = []

        for SGNode in SGNodeList:
            if mc.attributeQuery('surfaceShader', node = SGNode, ex = True):
                matNode = mc.listConnections('%s.surfaceShader' %SGNode)
                if matNode:
                    matNodes.append(SGNode)
                else:
                    continue
            else:
                continue
        return matNodes

    def getSGNode_MaxObjNum(self, SGNodeList):
        numDict = {}
        obj_Num = 0
        matNodes = self.getHaveMatNodes(SGNodeList)

        if len(matNodes) == 1:
            return matNodes[0]
        elif len(matNodes) == 0:
            matNodes = SGNodeList

        for SGNode in matNodes:
            SG_Obj = mc.listConnections(SGNode, sh = True, t = 'mesh')
            if SG_Obj:
                obj_Num = max(obj_Num, len(SG_Obj))
                numDict[len(SG_Obj)] = SGNode
        if obj_Num != 0:
            return numDict[obj_Num]
        else:
            return SGNodeList[0]