#!/usr/bin/env python
# coding=utf-8

import maya.cmds as mc

class OCT_MasK_Tool():
    def __init__(self):
        self._windowSize = (380, 340)
        self._windowName = 'OCT_MasK_Tool_UI'
        #选择所有物体的SG节点
        self.allSG = []

        self.mySurfaceList = []

    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName, window=True)
        if mc.windowPref(self._windowName, q=True, exists=True):
            mc.windowPref(self._windowName, remove=True)

    def OCT_MasK_Tool_UI(self):
        self.listSurface()
        self.close()
        win = mc.window(self._windowName, t = u'遮罩工具', menuBar=True, widthHeight=self._windowSize, sizeable=False)
        mc.formLayout('formLyt', numberOfDivisions=100)
        one = mc.frameLayout('surface_Node', label=u'选择surfaceShader材质(1.把物体赋予已有材质,2.可按delete删除材质)', labelAlign='top', w=380, h=200, parent='formLyt')
        self.uiTextSurface = mc.textScrollList('selectSurface', append=self.mySurfaceList, allowMultiSelection=True, h=100, sc = lambda*arg:self.SelectTextList(), dkc = lambda*arg:self.deleteListCommand(), parent='surface_Node')
        two = mc.columnLayout('First_Set', parent='formLyt')
        mc.rowLayout('buttonRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[180, 250, 50], columnOffset3=[2, 6, 2], adjustableColumn3=True, parent='First_Set')
        mc.button('createSurface', l = u'创建新的surfaceShader', w = 170, c = lambda*arg:self.createNewSurface())
        mc.button('getSurface', l = u'赋予已有的surfaceShader', w = 170, c = lambda*arg:self.ObjConSurface())
        mc.formLayout('formLyt', e=True,
                      attachForm=[(one, 'top', 5), (one, 'left', 5), (two, 'right', 5), (two, 'top', 135), (two, 'left', 5), (two, 'bottom', 5)],
                      attachControl=[(one, 'bottom', 1, two)],
                      attachNone=[(two, 'top')],
                      attachPosition=[(one, 'left', 0, 0), (one, 'top', 0, 0)])
        mc.showWindow(win)

    #选择列表
    def SelectTextList(self):
        allSelectSurface = mc.textScrollList(self.uiTextSurface, q=True, si=True)
        mc.select(allSelectSurface)
        return allSelectSurface

    #选择按delete删除
    def deleteListCommand(self):
        allSelectedObj = self.SelectTextList()
        result = mc.confirmDialog( title=u'温馨提示', message=u'确定要删除所选的surfaceShader\n是：按Yes，否：按NO！', button=['Yes', 'NO'], defaultButton='Yes', dismissString='No')
        if result == 'Yes':
            mc.delete(allSelectedObj)
            self.listSurface()
            mc.textScrollList('selectSurface',e = True, ra = True)
            mc.textScrollList('selectSurface',e = True, append=self.mySurfaceList)

    #获取所选择的物体
    def SelectedObj(self):
        allSelectedObj = mc.ls(sl = True, dag = True, ni = True, s = True)
        self.allMyShapes = []
        for Shape in allSelectedObj:
            ShapeType = mc.nodeType(Shape)
            if ShapeType == 'mesh':
                self.allMyShapes.append(Shape)
        if len(self.allMyShapes)==0:
            mc.confirmDialog( title=u'温馨提示', message=u'选择的组或者物体不含有模型\n请重新选择！', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        self.allSG = []
        for each in self.allMyShapes:
            eachObjSG = mc.listConnections('%s.instObjGroups'%each, s= False, d = True)
            for SG in eachObjSG:
                if mc.objectType(SG) == 'shadingEngine' and SG not in self.allSG:
                    #判断是否连接surfaceMasks和物体的SG节点连了没有选择的物体
                    surfaceMasks = mc.listConnections('%s.aiCustomAOVs'%SG, s = True, d = False)
                    cons = mc.listConnections('%s.dagSetMembers'%SG,s = True,d = False, sh = True)
                    flags = True
                    for ms in cons:
                        if mc.nodeType(ms) == 'mesh' and (ms not in self.allMyShapes):
                            flags = False

                    if surfaceMasks == None and flags:
                        self.allSG.append(SG)
                        continue

                    #重新给物体和材质一个SG节点
                    flag = False 
                    if surfaceMasks: 
                        for mask in surfaceMasks:
                            if mc.objectType(mask) == 'surfaceShader' and 'surface_Mask' in mask:
                                flag = True
                    if flag or not flags:
                        newSGname = '%s_new'%SG
                        j = 0
                        while True:
                            if mc.objExists(newSGname):
                                j = j + 1
                                newSGname = '%s_new%s' % (SG, j)
                            else:
                                break
                        mc.duplicate(SG, rr = True, name = newSGname)

                        con = mc.listConnections('%s.surfaceShader'%SG,s = True,d = False, p = True)
                        mc.connectAttr(con[0], '%s.surfaceShader'%newSGname)
                        j = 0
                        while True:
                            try:
                                mc.disconnectAttr('%s.instObjGroups'%each, '%s.dagSetMembers[%s]'%(SG,j))
                                break
                            except:
                                j = j + 1
                        
                        mc.connectAttr('%s.instObjGroups'%each,'%s.dagSetMembers[0]'%newSGname,f = True)
                        self.allSG .append(newSGname)
                    else:
                        self.allSG .append(SG)

        return True

    #列出已有的surfaceShader
    def listSurface(self):
        self.mySurfaceList = []
        allSurfaces = mc.ls(type = 'surfaceShader')
        for sur in allSurfaces:
            if 'surface_Mask' in sur:
                self.mySurfaceList.append(sur)

    #创建新的Surface
    def createNewSurface(self):
        if not self.SelectedObj():
            return False

        result = self.createAiAOV()
        #创建surfaceShader节点
        surfaceName = mc.shadingNode('surfaceShader', asShader = True, n = 'surface_Mask')
        if self.allSG:
            for eachSG in self.allSG:
                mc.connectAttr('%s.aiOutColor'%surfaceName, '%s.aiCustomAOVs[%s].aovInput'%(eachSG, result ), f= True)
        
        self.listSurface()
        mc.textScrollList('selectSurface',e = True, ra = True)
        mc.textScrollList('selectSurface',e = True, append=self.mySurfaceList)

    #创建aiAOV通道
    def createAiAOV(self):
        i = 0
        #创建通道节点
        if mc.objExists('aiAOV_Mask') and mc.objectType('aiAOV_Mask') == 'aiAOV':
            Option = mc.listConnections('aiAOV_Mask.message',s = False, d = True, p = True)
            if Option:
                num = Option[0].split('[')[-1]
                i = num.split(']')[0]
            else:
                while True:
                    try:
                        mc.connectAttr("aiAOV_Mask.message", "defaultArnoldRenderOptions.aovList[%s]"%i)
                        break
                    except:
                        i = i + 1
            if not mc.listConnections("aiAOV_Mask.outputs[0].driver", s = True, d = False):
                mc.connectAttr("defaultArnoldDriver.message", "aiAOV_Mask.outputs[0].driver")

            if not mc.listConnections("aiAOV_Mask.outputs[0].filter", s = True, d = False):
                mc.connectAttr("defaultArnoldFilter.message", "aiAOV_Mask.outputs[0].filter")
        else:
            aiAOV_Name = mc.createNode('aiAOV', n = 'aiAOV_Mask')
            name = aiAOV_Name.split('_')
            mc.setAttr("%s.name"%aiAOV_Name, name[-1], type = "string")
            while True:
                try:
                    mc.connectAttr("%s.message"%aiAOV_Name, "defaultArnoldRenderOptions.aovList[%s]"%i)
                    break
                except:
                    i = i + 1
            mc.connectAttr("defaultArnoldDriver.message", "%s.outputs[0].driver"%aiAOV_Name)
            mc.connectAttr("defaultArnoldFilter.message", "%s.outputs[0].filter"%aiAOV_Name)

        return i 
        

    #把选择的物体赋予已有的surface
    def ObjConSurface(self):
        if not self.SelectedObj():
            return False
        allSelectSurface = mc.textScrollList(self.uiTextSurface, q=True, si=True)
        if len(allSelectSurface) != 1:
            mc.confirmDialog( title=u'温馨提示', message=u'请选择一个surfaceShader材质！', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        result = self.createAiAOV()
        if self.allSG:
            for eachSG in self.allSG:
                mc.connectAttr('%s.aiOutColor'%allSelectSurface[0], '%s.aiCustomAOVs[%s].aovInput'%(eachSG, result ), f= True)
             
#OCT_MasK_Tool().OCT_MasK_Tool_UI()
