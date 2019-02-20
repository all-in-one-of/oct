#!/usr/bin/env python
# coding=utf-8

import os
import sys
import random
import math
from collections import defaultdict

import maya.cmds as mc
import maya.mel as mm

class ReplaceOriginalObject_zwz():
    def __init__(self):
        #UI
        self._windowSize = (350, 340)
        self._windowName = 'OCT_ReplaceOriginalObjectUI_zwz'
        self.myHideGroup = []
        self.SelectRandObject = []

    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName, window=True)
        if mc.windowPref(self._windowName, q=True, exists=True):
            mc.windowPref(self._windowName, remove=True)

    def show(self):
        self.close()
        try:
            mm.eval(r'source "\\\\octvision.com\\cg\\td\\Maya\\2009\\Scripts\\Mel\\tazz_TransferShaders.mel"')
        except:
            sys.stderr.write(u'传输材质脚本不能加载！')
        #make the window
        win = mc.window(self._windowName, title=u"OCT_ReplaceOriginalObject_zwz(窗口可拉伸    注：1、物体不可随意Freeze 2、不要对相关组缩放)", menuBar=True, widthHeight=self._windowSize, resizeToFitChildren=True, sizeable=True)

        mc.formLayout('formLyt', numberOfDivisions=100)
        mc.columnLayout('Xml_Type', adjustableColumn=True)

        mc.rowLayout('modifyTransform', numberOfColumns=2, columnWidth2=(417, 60), columnAttach2=['left', 'right'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        mc.text(label=u' 把被选择物体的原点归零:')
        mc.button(label='Modify', width=60, command=self.ModifyTransformToZero_zwz, backgroundColor=(0.9, 0.5, 0), annotation=u'请输入需要选择物体的名字')

        mc.rowLayout('ranSelect_zwz', numberOfColumns=3, columnWidth3=(357, 60, 60), columnAttach3=['left', 'right', 'right'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0), (3, 'both', 0)], parent='Xml_Type')
        self.uiRandSelectper = mc.intSliderGrp(label=u'随机按百分率选择被选中的物体：', field=True, minValue=1, maxValue=100, value=50, cl3=('left', 'left', 'left'), cw3=(160, 40, 280))
        mc.button(label='Select', width=60, command=lambda*args: self.selectRandPer(1, args), backgroundColor=(0.9, 0.5, 0))
        mc.button(label='Other', width=60, command=lambda*args: self.selectRandPer(2, args), backgroundColor=(0.1, 0.7, 0.1))

        mc.rowLayout('SelectOne', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[130, 282, 80], columnOffset3=[2, 2, 2], parent='Xml_Type')
        mc.text(label=u'模糊选择模型工具  Name:')
        self.uiMoSelectText = mc.textField(text='name_aa_bb_cc', width=282, alwaysInvokeEnterCommandOnReturn=True)
        mc.button(label='Select', width=60, command=self.selectN_zwz, backgroundColor=(0.9, 0.5, 0), annotation=u'请输入需要选择物体的名字')

        mc.rowLayout('selectTwo', numberOfColumns=2, columnWidth2=(417, 60), columnAttach2=['left', 'right'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        self.uiMoSelectCheck = mc.checkBoxGrp(numberOfCheckBoxes=2, w=350, ct2=['left', 'left'], cw3=[185, 70, 50], label=u'根据面数和boundingBox大小选择poly:', labelArray2=[u'面数', u'相对表面积'], v1=True, v2=False, parent='selectTwo')
        mc.button(label='Select', width=60, command=self.selectFaceBox_zwz, backgroundColor=(0.9, 0.5, 0), annotation=u'请输入需要选择物体的名字')

        mc.rowLayout('selectThree', numberOfColumns=2, columnWidth2=(417, 60), columnAttach2=['left', 'right'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        self.uiSoSelectCheck = mc.checkBoxGrp(numberOfCheckBoxes=3, ct2=['left', 'left'], cw4=[185, 70, 70, 50], label=u'选择相同属性的物体:                           ', labelArray3=[u'位移', u'旋转', u'缩放'], v1=True, v2=False, v3=False, parent='selectThree')
        mc.button(label='Select', width=60, command=self.selectSameMesh_zwz, backgroundColor=(0.9, 0.5, 0), annotation=u'请输入需要选择物体的名字')

        mc.rowLayout('selectSO', numberOfColumns=2, columnWidth2=(417, 60), columnAttach2=['left', 'right'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        mc.text(label=u' 选择重复物体:')
        mc.button(label='Select', width=60, command=self.selectSameObject, backgroundColor=(0.9, 0.5, 0))

        mc.rowLayout('SelectQuick_O', numberOfColumns=4, columnWidth4=(95, 100, 150, 128), columnAttach4=['left', 'both', 'both', 'both'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        mc.text(label=u'快速选择相关物体:')
        mc.button(label=u'选择相应源物体', width=60, command=lambda*args: self.selectQuick(1, args), backgroundColor=(0.9, 0.9, 0))
        mc.button(label=u'选择相应所有子物体', width=60, command=lambda*args: self.selectQuick(2, args), backgroundColor=(0.9, 0.7, 0))
        mc.button(label=u'选择相应源和子物体', width=60, command=lambda*args: self.selectQuick(3, args), backgroundColor=(0.9, 0.5, 0))

        mc.rowLayout('SelectQuick_VR', numberOfColumns=3, columnWidth3=(125, 170, 180), columnAttach3=['left', 'both', 'both'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        mc.text(label=u'快速选择Vray相关物体:')
        mc.button(label=u'选择相同VrayMesh的所有物体', width=60, command=lambda*args: self.selectQuick(4, args), backgroundColor=(0.9, 0.9, 0))
        mc.button(label=u'选择所有VrayMesh的"代表"物体', width=60, command=lambda*args: self.selectQuick(5, args), backgroundColor=(0.9, 0.7, 0))

        mc.rowLayout('VrayMeshtoBox', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[250, 122, 100], columnOffset3=[5, 2, 2], parent='Xml_Type')
        mc.text(label=u'Vray 或 Arnold 的 Bounding Box 显示开关:')
        mc.button(label='On', width=100, command=lambda*args: self.setAllVrayMeshOrAiStandToBox(True, args), backgroundColor=(0.342, 1, 0.449))
        mc.button(label='Off', width=100, command=lambda*args: self.setAllVrayMeshOrAiStandToBox(False, args), backgroundColor=(1.000, 0.101, 0.101))

        mc.rowLayout('createLG_VFX', numberOfColumns=2, columnWidth2=(417, 60), columnAttach2=['left', 'right'], columnAlign=(2, 'left'), columnAttach=[(1, 'left', 0), (2, 'both', 0)], parent='Xml_Type')
        mc.text(label=u' 根据代理的空间信息创建locator组:')
        mc.button(label='Create', width=60, command=self.CreatProxyLoator_forVfx, backgroundColor=(0.9, 0.5, 0))

        self.uimodelRadio = mc.radioButtonGrp(label=u'模式:', labelArray2=[u'创建', u'修复(仅限粒子替代模式)'], numberOfRadioButtons=2, columnAlign=[1, 'left'], columnAlign2=['left', 'left'], cw3=[45, 75, 90], sl=1, bgc=(0.2, 0.8, 0.3), cc=self.modelOption, parent='Xml_Type')

        self.uireplaceFrameLayout = mc.frameLayout(label=u'被替代物体', labelAlign='top', borderStyle='etchedOut', en=True, parent='formLyt')
        self.uiReplaceOText = mc.textScrollList(allowMultiSelection=True, sc=lambda*args: self.selectTextList('uiReplaceOText', args))
        self.uiReplace_AB = mc.button(label=u'加载', c=lambda*args: self.addOrDelorCleanButton(11, 'uiReplaceOText', args), backgroundColor=(0.9, 0.5, 0))
        self.uiReplace_DB = mc.button(label=u'删除选择的列', c=lambda*args: self.addOrDelorCleanButton(12, 'uiReplaceOText', args), backgroundColor=(0.9, 0.3, 0.3))
        self.uiReplace_CB = mc.button(label=u'清空', c=lambda*args: self.addOrDelorCleanButton(13, 'uiReplaceOText', args), backgroundColor=(0.2, 0.8, 0.3))

        self.uiinstancerFrameLayout = mc.frameLayout(label=u'替代的源物体', labelAlign='top', borderStyle='etchedOut', w=100, h=100, parent='formLyt')
        self.uiinstancerOText = mc.textScrollList(allowMultiSelection=True, sc=lambda*args: self.selectTextList('uiinstancerOText', args))
        self.uiinstancer_AB = mc.button(label=u'加载', c=lambda*args: self.addOrDelorCleanButton(21, 'uiinstancerOText', args), backgroundColor=(0.9, 0.5, 0))
        self.uiinstancer_DB = mc.button(label=u'删除选择的列', c=lambda*args: self.addOrDelorCleanButton(22, 'uiinstancerOText', args), backgroundColor=(0.9, 0.3, 0.3))
        self.uiinstancer_CB = mc.button(label=u'清除', c=lambda*args: self.addOrDelorCleanButton(23, 'uiinstancerOText', args), backgroundColor=(0.2, 0.8, 0.3))

        self.uimyLocatorFrameLayout = mc.frameLayout(label=u'Locators', labelAlign='top', en=False, borderStyle='etchedOut', parent='formLyt')
        self.uimyLocatorText = mc.textScrollList(allowMultiSelection=True, sc=lambda*args: self.selectTextList('uimyLocatorText', args))
        self.uimyLocator_AB = mc.button(label=u'加载', c=lambda*args: self.addOrDelorCleanButton(31, 'uimyLocatorText', args), backgroundColor=(0.267, 0.267, 0.267))
        self.uimyLocator_DB = mc.button(label=u'删除选择的列', c=lambda*args: self.addOrDelorCleanButton(32, 'uimyLocatorText', args), backgroundColor=(0.267, 0.267, 0.267))
        self.uimyLocator_CB = mc.button(label=u'清除', c=lambda*args: self.addOrDelorCleanButton(33, 'uimyLocatorText', args), backgroundColor=(0.267, 0.267, 0.267))

        self.uimyPaticleFrameLayout = mc.frameLayout(label=u'Particles(单个)', labelAlign='top', borderStyle='etchedOut', en=False, parent='formLyt')
        self.uimyParticleText = mc.textScrollList(allowMultiSelection=True, sc=lambda*args: self.selectTextList('uimyParticleText', args))
        self.uimyParticles_AB = mc.button(label=u'加载', c=lambda*args: self.addOrDelorCleanButton(41, 'uimyParticleText', args), backgroundColor=(0.267, 0.267, 0.267))
        mc.button(label='', en=False)
        self.uimyParticles_CB = mc.button(label=u'清除', c=lambda*args: self.addOrDelorCleanButton(43, 'uimyParticleText', args), backgroundColor=(0.267, 0.267, 0.267))

        self.uiinstancer_GName = mc.textFieldGrp(label=u'替换物体的组名', text='myInstanceGroup', cw2=[85, 250], cal=[1, 'left'], parent='formLyt')

        four = mc.frameLayout(label=u'静态模式(无动画)______可做动态模式的测试:判断位移,旋转,缩放是否正确', labelAlign='top', borderStyle='etchedOut', parent='formLyt')
        mc.rowLayout(numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[80, 180, 35], columnOffset3=[2, 2, 2], parent=four)
        mc.text(label=u'关联复制:')
        self.uiNoAnModel_ICB = mc.button(label=u'创建', w=130, command=self.NoAnInstanceCopy, backgroundColor=(0.2, 0.8, 0.3))
        mc.rowLayout(numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[80, 180, 35], columnOffset3=[2, 2, 2], parent=four)
        mc.text(label=u'粒子替代:')
        self.uiNoAnModel_PMB = mc.button(label=u'创建', w=130, command=lambda*args: self.AnInstanceParticle(0, args), backgroundColor=(0.2, 0.8, 0.3))

        
        five = mc.frameLayout(label=u'动态模式(动画)', labelAlign='top', borderStyle='etchedOut', parent='formLyt')
        mc.rowLayout(numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[80, 180, 35], columnOffset3=[2, 2, 2], parent=five)
        mc.text(label=u'关联复制:')
        self.uiAnModel_ICB = mc.button(label=u'创建', w=130, command=self.AnInstancerCopy, backgroundColor=(0.2, 0.8, 0.3))
        mc.rowLayout(numberOfColumns=4, columnAttach4=['left', 'left', 'left', 'left'], columnWidth4=[80, 180, 180, 35], columnOffset4=[2, 2, 2, 2], parent=five)
        mc.text(label=u'粒子替代:')
        self.uiAnModel_PCB = mc.button(label=u'创建', w=130, command=lambda*args: self.AnInstanceParticle(1, args), backgroundColor=(0.2, 0.8, 0.3))
        self.uiAnModel_PMB = mc.button(label=u'修复', w=130, command=self.repairInstance, en=False, backgroundColor=(0.267, 0.267, 0.267))

        mc.formLayout('formLyt', e=True,
                      attachForm=[(self.uireplaceFrameLayout, 'left', 0), (four, 'left', 0), (five, 'left', 0), (self.uimyPaticleFrameLayout, 'right', 0), (four, 'right', 0), (five, 'right', 0), (self.uireplaceFrameLayout, 'top', 272), (self.uiinstancerFrameLayout, 'top', 272), (self.uimyLocatorFrameLayout, 'top', 272), (self.uimyPaticleFrameLayout, 'top', 272), (five, 'bottom', 5)],
                      attachControl=[(self.uireplaceFrameLayout, 'bottom', 1, self.uiinstancer_GName), (self.uiinstancerFrameLayout, 'bottom', 1, self.uiinstancer_GName), (self.uimyLocatorFrameLayout, 'bottom', 1, self.uiinstancer_GName), (self.uimyPaticleFrameLayout, 'bottom', 1, self.uiinstancer_GName), (self.uiinstancer_GName, 'bottom', 1, four), (four, 'bottom', 1, five)],
                      attachNone=[],
                      attachPosition=[(self.uireplaceFrameLayout, 'right', 0, 25), (self.uiinstancerFrameLayout, 'left', 0, 25), (self.uiinstancerFrameLayout, 'right', 0, 50), (self.uimyLocatorFrameLayout, 'left', 0, 50), (self.uimyLocatorFrameLayout, 'right', 0, 75), (self.uimyPaticleFrameLayout, 'left', 0, 75), (self.uimyPaticleFrameLayout, 'right', 0, 100)])
        mc.showWindow(win)

    #选择重复物体
    def selectSameObject(self, *args):
       #所有的nurbsSurface和subdiv的shape
        allMyShapes = []
        #polygons相同面数的mesh物体
        allMyMesh=[]
        #存放mesh物体的面的个数的字典
        numFace={}
        #存放polygons的Tr节点
        myMeshTrDict={}
        myMeshRoDict={}
        myMeshScDict={}
        myMeshBoxDict={}
        
        myTrDict={}
        myRoDict={}
        myScDict={}
        myBoxDict={}
        
        allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True)
        for shape in allShapes:
            shapeType=mc.nodeType(shape)
            if shapeType=='mesh':
                cmd1=mc.polyEvaluate(shape,face=True)
                if not cmd1 in numFace.keys():
                    numFace.update({cmd1:[shape]})
                else:
                    numFace[cmd1].append(shape)        
            elif shapeType=='nurbsSurface' or shapeType == 'subdiv':
                allMyShapes.append(shape)

        for key in numFace.keys():
            if len(numFace[key])>1:
                for i in numFace[key]:
                    allMyMesh.append(i)        
                    
        if len(allShapes)==0:
            mc.confirmDialog(title=u'温馨提示', message=u'选择的组或者物体不含有模型\n请重新选择！', button='OK', defaultButton='Yes', dismissString='No')
            return
        else:
            if allMyMesh:
                for myMesh in allMyMesh:
                    myMeshTr=mc.listRelatives(myMesh,p=True,f=True)[0]
                    myTrTx = mc.xform(myMeshTr, q=True, sp=True, ws=True)
                    myTrTxs = str(myTrTx)
                    if myTrTxs not in myMeshTrDict.keys():
                        myMeshTrDict.update({myTrTxs:[myTrTx,myMeshTr]})
                    else:
                        myMeshTrDict[myTrTxs].append(myMeshTr)
                    
                    myRcTx = mc.xform(myMeshTr, q=True, s=True)
                    myRcTxs = str(myRcTx)
                    if myRcTxs not in myMeshRoDict.keys():
                        myMeshRoDict.update({myRcTxs:[myRcTx,myMeshTr]})
                    else:
                        myMeshRoDict[myRcTxs].append(myMeshTr)
                        
                    myScTx = mc.xform(myMeshTr, q=True, ro=True, ws=True)
                    myScTxs = str(myScTx)
                    
                    if myScTxs not in myMeshScDict.keys():
                        myMeshScDict.update({myScTxs:[myScTx,myMeshTr]})
                    else:
                        myMeshScDict[myScTxs].append(myMeshTr)
            

            if allMyShapes:
                for eachTr in allMyShapes:
                    myTr=mc.listRelatives(eachTr,p=True,f=True)[0]
                    
                    myTrTx = mc.xform(myTr, q=True, sp=True, ws=True)
                    myTrTxs = str(myTrTx)
                    if myTrTxs not in myTrDict.keys():
                        myTrDict.update({myTrTxs:[myTrTx,myTr]})
                    else:
                        myTrDict[myTrTxs].append(myTr)
                        
                    myRcTx = mc.xform(myTr, q=True, r=True, s=True)
                    myRcTxs = str(myRcTx)

                    if myRcTxs not in myRoDict.keys():
                        myRoDict.update({myRcTxs:[myRcTx,myTr]})
                    else:
                        myRoDict[myRcTxs].append(myTr)
                        
                    myScTx = mc.xform(myTr, q=True, ro=True, ws=True)
                    myScTxs = str(myScTx)
                    if myScTxs not in myScDict.keys():
                        myScDict.update({myScTxs:[myScTx,myTr]})
                    else:
                        myScDict[myScTxs].append(myTr)
                        
        
        allSets=list(set(mc.ls(sets=True))-set(['defaultLightSet', 'defaultObjectSet', 'initialParticleSE', 'initialShadingGroup']))
        for mySet in allSets:
            if mySet=='OCT_PolySets' or mySet=='OCT_NurbSubdSets':
                #mc.select(mySet,r=True,ne=True)
                mc.delete(mySet)
                
        mc.select(d=True)        
        #重合的mesh物体    
        myMeshTr=[]
        #print myMeshTrDict
        #print myMeshRoDict
        #print myMeshScDict
        
        for key in myMeshTrDict.keys():
            if len(myMeshTrDict[key])>2:
                flag=False
                for i in myMeshTrDict[key]:
                    if flag:
                        myMeshTr.append(i)
                    else:
                        flag=True
                        continue
                #del myMeshTrDict[key]
            else:
                flag=False
                for i in myMeshTrDict.keys():
                    if  key!=i and (len(myMeshTrDict[i])==2):
                        #求物体属性的值精确到小数点后3位时的值是否相同
                        number=myMeshTrDict[key][0]
                        numbers=myMeshTrDict[i][0]
                        
                        temp=('%0.3f'%float(number[0]))
                        tx=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        txs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        ty=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        tys=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        tz=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        tzs=temp[:-1]
                        
                        #当物体属性精确到很小的值
                        if (tx==txs) and (ty==tys) and (tz==tzs):
                            flag=True
                            break
                            
                if flag:
                    myMeshTr.append(myMeshTrDict[key][1])
                    #del myMeshTrDict[key]
                            
        #print myMeshTr        
        myMeshRo=[]                
        for key in myMeshRoDict.keys():
            if len(myMeshRoDict[key])>2:
                flag=False
                for i in myMeshRoDict[key]:
                    if flag:
                        myMeshRo.append(i)
                    else:
                        flag=True
                        continue    

            else:
                flag=False
                for i in myMeshRoDict.keys():
                    if key!=i and (len(myMeshRoDict[i])==2):
                        #求物体属性的值精确到小数点后3位时的值是否相同
                        number=myMeshRoDict[key][0]
                        
                        numbers=myMeshRoDict[i][0]
                        
                        
                        temp=('%0.3f'%float(number[0]))
                        rx=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        rxs=temp[:-1]
                        
                        
                        temp=('%0.3f'%float(number[1]))
                        ry=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        rys=temp[:-1]
                        
                        
                        temp=('%0.3f'%float(number[2]))
                        rz=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        rzs=temp[:-1]
                        
                        if (tx==txs) and (ty==tys) and (tz==tzs):
                            flag=True
                            break
                if flag:
                    myMeshRo.append(myMeshRoDict[key][1])

        
        myMeshRc=[]    
        for key in myMeshScDict.keys():
            if len(myMeshScDict[key])>2:
                flag=False
                for i in myMeshScDict[key]:
                    if flag:
                        myMeshRc.append(i)
                    else:
                        flag=True
                        continue
            else:
                flag=False
                for i in myMeshScDict.keys():
                    if key!=i and (len(myMeshScDict[i])==2):
                        #求物体属性的值精确到小数点后6位时的值是否相同
                        number=myMeshScDict[key][0]
                        numbers=myMeshScDict[i][0]
                        
                        temp=('%0.3f'%float(number[0]))
                        sx=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        sxs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        sy=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        sys=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        sz=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        szs=temp[:-1]
                        if (tx==txs) and (ty==tys) and (tz==tzs):
                            flag=True
                            break
                if flag:
                    myMeshRc.append(myMeshScDict[key][1])
                
        
                         
        #记录poly重合的物体个数
        myMeshWs=[]
        setPoly=0
        for Mesh in myMeshTr:
            if Mesh in myMeshRo:
                if Mesh in myMeshRc:
                    myMeshWs.append(Mesh)
                    
                    
        #print myMeshWs        
        #相同的boundingBox
        for ws in myMeshWs:
            myWS = mc.xform(ws, q=True, ws=True, boundingBox=True)
            myWSs = str(myWS)
            if myWSs not in myMeshBoxDict.keys():
                myMeshBoxDict.update({myWSs:[myWS,ws]})
            else:
                myMeshBoxDict[myWSs].append(ws)
        #ploy  在相同位置物体集合中找形同值的boundingBox
        for keys in myMeshBoxDict.keys():
            num=len(myMeshBoxDict[keys])-1
            if num>1:
                setPoly+=num
                flag=False
                #print 'bbb'
                #print myMeshBoxDict[keys]
                for i in myMeshBoxDict[keys]:
                    if flag:
                        mc.select(i,add=True)
                    else:
                        flag=True
                        continue
            else:
                flag=False
                for i in myMeshBoxDict.keys():
                    if keys!=i and len(myMeshBoxDict[keys])==2:
                        #print 'aaa'
                        #print myMeshBoxDict[keys]
                        number=myMeshBoxDict[keys][0]
                        numbers=myMeshBoxDict[i][0]
                        
                        temp=('%0.3f'%float(number[0]))
                        xmin=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        xmins=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        ymin=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        ymins=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        zmin=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        zmins=temp[:-1]
                        
                        temp=('%0.3f'%float(number[3]))
                        xmax=temp[:-1]
                        temp=('%0.3f'%float(numbers[3]))
                        xmaxs=temp[:-1]
                    
                        temp=('%0.3f'%float(number[4]))
                        ymax=temp[:-1]
                        temp=('%0.3f'%float(numbers[4]))
                        ymaxs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[5]))
                        zmax=temp[:-1]
                        temp=('%0.3f'%float(numbers[5]))
                        zmaxs=temp[:-1]
                
                        
                        if (xmin==xmins) and (ymin==ymins) and (zmin==zmins) and (xmax==xmaxs) and (ymax==ymaxs) and (zmax==zmaxs):
                            flag=True
                            break
                if flag:
                    setPoly+=1
                    mc.select(myMeshBoxDict[keys][1],add=True)

                #print keys
                    
                
        #创建OCT_PolySets        
        if setPoly>0:
            mc.sets(n='OCT_PolySets')
            
        mc.select(d=True)        
        #重合的nurbsSurface和subdiv的物体
        myTr=[]
        for key in myTrDict.keys():
            if len(myTrDict[key])>2:
                flag=False
                for i in myTrDict[key]:
                    if flag:
                        myTr.append(i)
                    else:
                        flag=True
                        continue
            else:
                flag=False
                for i in myTrDict.keys():
                    if key!=i and len(myTrDict[key])==2:
                        
                        number=myTrDict[key][0]
                        numbers=myTrDict[i][0]
                        
                        temp=('%0.3f'%float(number[0]))
                        tx=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        txs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        ty=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        tys=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        tz=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        tzs=temp[:-1]
                        if (tx==txs) and (ty==tys) and (tz==tzs):
                            flag=True
                            break
                if flag:
                    myTr.append(myTrDict[key][1])
                            
        
        myRo=[]                
        for key in myRoDict.keys():
            if len(myRoDict[key])>2:
                flag=False
                for i in myRoDict[key]:
                    if flag:
                        myRo.append(i)
                    else:
                        flag=True
                        continue
            else:
                flag=False
                for i in myRoDict.keys():
                    if key!=i:
                        number=myRoDict[key][0]
                        numbers=myRoDict[i][0]
                        
                        temp=('%0.3f'%float(number[0]))
                        rx=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        rxs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        ry=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        rys=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        rz=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        rzs=temp[:-1]
                        if (tx==txs) and (ty==tys) and (tz==tzs):
                            flag=True
                            break

                if flag:
                    myRo.append(myRoDict[key][1])
        
        
        myRc=[]    
        for key in myScDict.keys():
            if len(myScDict[key])>1:
                flag=False
                for i in myScDict[key]:
                    if flag:
                        myRc.append(i)    
                    else:
                        flag=True
                        continue
            else:
                flag=False
                for i in myScDict.keys():
                    if key!=i:
                        number=myScDict[key][0]
                        numbers=myScDict[i][0]
                        
                        temp=('%0.3f'%float(number[0]))
                        sx=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        sxs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        sy=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        sys=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        sz=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        szs=temp[:-1]
                        if (tx==txs) and (ty==tys) and (tz==tzs):
                            flag=True
                            break
                if flag:
                    myRc.append(myScDict[key][1])
        
        
        
        #记录NurbSubd重合的物体
        setNurbSubdSet=0
        myWs=[]
        for Mesh in myTr:
            if Mesh in myRo:
                if Mesh in myRc:
                    #setNurbSubdSet+=1
                    #mc.select(Mesh,add=True) 
                    myWs.append(Mesh)
                    
        #相同NurbSubd物体的boundingBox
        for ws in myWs:
            myWS = mc.xform(ws, q=True, ws=True, boundingBox=True)
            myWSs=str(myWS)
            if myWSs not in myBoxDict.keys():
                myBoxDict.update({myWSs:[myWS,ws]})
            else:
                myBoxDict[myWSs].append(ws)
                
        #NurbSubd  在相同位置物体集合中找形同值的boundingBox
        for keys in myBoxDict.keys():
            num=len(myBoxDict[keys])-1
            if num>1:
                setNurbSubdSet+=num
                flag=False
                for i in myBoxDict[keys]:
                    if flag:
                        mc.select(i,add=True)
                    else:
                        flag=True
                        continue
            else:
                flag=False
                for i in myBoxDict.keys():
                    if keys!=i:
                        number=myBoxDict[keys][0]
                        numbers=myBoxDict[i][0]
                        
                        
                        temp=('%0.3f'%float(number[0]))
                        xmin=temp[:-1]
                        temp=('%0.3f'%float(numbers[0]))
                        xmins=temp[:-1]
                        
                        temp=('%0.3f'%float(number[1]))
                        ymin=temp[:-1]
                        temp=('%0.3f'%float(numbers[1]))
                        ymins=temp[:-1]
                        
                        temp=('%0.3f'%float(number[2]))
                        zmin=temp[:-1]
                        temp=('%0.3f'%float(numbers[2]))
                        zmins=temp[:-1]
                        
                        temp=('%0.3f'%float(number[3]))
                        xmax=temp[:-1]
                        temp=('%0.3f'%float(numbers[3]))
                        xmaxs=temp[:-1]
                    
                        temp=('%0.3f'%float(number[4]))
                        ymax=temp[:-1]
                        temp=('%0.3f'%float(numbers[4]))
                        ymaxs=temp[:-1]
                        
                        temp=('%0.3f'%float(number[5]))
                        zmax=temp[:-1]
                        temp=('%0.3f'%float(numbers[5]))
                        zmaxs=temp[:-1]
                        
                    
                        
                        if (xmin==xmins) and (ymin==ymins) and (zmin==zmins) and (xmax==xmaxs) and (ymax==ymaxs) and (zmax==zmaxs):
                            flag=True
                if flag:
                    setPoly+=1
                    mc.select(myBoxDict[keys][1],add=True)
                
        if setNurbSubdSet>0:
            mc.sets(n='OCT_NurbSubdSets')
            mc.select('OCT_NurbSubdSets',r=True)
        if setPoly>0:
            mc.select('OCT_PolySets',add=True)
        num=setPoly+setNurbSubdSet
        mc.confirmDialog(title=u'温馨提示', message=u'总共有'+str(num)+u'个重合物体', button='OK', defaultButton='Yes', dismissString='No')            


    #随机按百分比选择物体
    def selectRandPer(self, *args):
        mode = args[0]
        per = mc.intSliderGrp(self.__dict__['uiRandSelectper'], q=True, v=True)
        if per == 0:
            mc.warning(u'请输入大于0的值')
        else:
            if mode == 1:
                myNowSelect = mc.ls(sl=True, tr=True)
                self.SelectRandObject = myNowSelect
            if self.SelectRandObject:
                numA = len(self.SelectRandObject)
                num = int(numA*per/100)
                randSelect = random.sample(self.SelectRandObject, num)
                if  randSelect:
                    mc.select(randSelect)
                else:
                    mc.warning(u"这个比例太小！")
            else:
                mc.warning(u'请选择物体')


    #快捷选择相关物体
    def selectQuick(self, *args):
        mode = args[0]
        if mode < 5:
            myTrans = mc.ls(sl=True, l=True, tr=True)
            if myTrans:
                allMySelectShapes = []
                for eachTran in myTrans:
                    #获取形节点
                    myTanS = mc.listRelatives(eachTran, s=True)[0]
                    allMySelectShapes.append(myTanS)
                allMySelectShapes = list(set(allMySelectShapes))
                if mode <= 3:
                    NoInstanObjects = []
                    AllMyParents = []
                    myAllTran = []
                    for eachSShape in allMySelectShapes:
                        eachSShape = mc.ls(eachSShape, l=True)
                        myATrans = mc.listRelatives(eachSShape, f=True, ap=True)
                        numMyTrans = len(myATrans)
                        if numMyTrans > 1:
                            #记录父子节点
                            myAllTran += myATrans
                            #记录父节点
                            AllMyParents.append(mc.listRelatives(eachSShape, f=True, p=True)[0])
                        elif numMyTrans == 1:
                            #记录单独节点
                            NoInstanObjects.append(myATrans[0])
                    myAllTran = list(set(myAllTran))
                    AllMyParents = list(set(AllMyParents))
                    #选择所有父节点
                    if mode == 1:
                        if AllMyParents:
                            mc.select(AllMyParents)
                    elif mode == 2:
                        for eachParent in AllMyParents:
                            if eachParent in myAllTran:
                                myAllTran.remove(eachParent)
                        if myAllTran:
                            mc.select(myAllTran)
                    elif mode == 3:
                        if myAllTran:
                            mc.select(myAllTran)
                    if NoInstanObjects:
                        mc.warning(u"\n%s\n这些物体没有关联！" % NoInstanObjects)
                else:
                    if mode == 4:
                        #找出这些物体Vray的代理路径，并保存到一个列表中
                        myFilaNames = []
                        allMySelectShapes = mc.ls(allMySelectShapes, l=True)
                        for eachSShape in allMySelectShapes:
                            myAllHistorys = mc.listHistory(eachSShape)
                            for myHistory in myAllHistorys:
                                myHistoryType = mc.nodeType(myHistory)
                                if myHistoryType == 'VRayMesh':
                                    tmpName = mc.getAttr('%s.fileName' % myHistory)
                                    if tmpName:
                                        myFilaNames.append(tmpName)

                        if myFilaNames:
                            mySelectVrayMesh = []
                            allSameVrayTran = []
                            allMyVrayMeshs = mc.ls(type="VRayMesh")
                            if allMyVrayMeshs:
                                for eachMesh in allMyVrayMeshs:
                                    myeachName = mc.getAttr('%s.fileName' % eachMesh)
                                    if myeachName in myFilaNames:
                                            mySelectVrayMesh.append(eachMesh)
                                for eachMySVrayMesh in mySelectVrayMesh:
                                    eachmeshCons = mc.listConnections(eachMySVrayMesh, sh=True)
                                    if eachmeshCons:
                                        for eachCon in eachmeshCons:
                                            if mc.nodeType(eachCon) == "mesh":
                                                allSameVrayTran += mc.listRelatives(eachCon, f=True, ap=True)
                                                break
                                if allSameVrayTran:
                                    mc.select(allSameVrayTran)
                            else:
                                mc.warning(u"选择为空！")
            else:
                mc.warning(u"选择为空！")
        else:
            #当mode为5时，选择vrayMesh的单一父物体
            allMyVrayMeshs = mc.ls(type="VRayMesh", l=True)
            myFilaNames = []
            allOnlyVrayMeshs = []
            allOnlyParents = []
            if allMyVrayMeshs:
                for eachMesh in allMyVrayMeshs:
                    myeachName = mc.getAttr('%s.fileName' % eachMesh)
                    if not myeachName in myFilaNames:
                        myFilaNames.append(myeachName)
                        allOnlyVrayMeshs.append(eachMesh)
                if allOnlyVrayMeshs:
                    for eachOnlySVrayMesh in allOnlyVrayMeshs:
                        eachmeshCons = mc.listConnections(eachOnlySVrayMesh)
                        if eachmeshCons:
                            for eachCon in eachmeshCons:
                                if mc.nodeType(eachCon) == "transform":
                                    allOnlyParents.append(mc.ls(eachCon, l=True)[0])
                mc.select(allOnlyParents)
            else:
                mc.warning(u"没有Vray代理物体")




    #归类列表的序列
    def sortListSeq(self, myList):
        mySeqList = []
        mySeqList = defaultdict(list)
        for k, va in [(v, i) for i, v in enumerate(myList)]:
            mySeqList[k].append(va)
        return mySeqList.items()

    #判断物体最终是否隐藏
    def judgeAndeCollectHide(self, Tran):
        if mc.getAttr("%s.v" % Tran):
            myParTran = mc.listRelatives(Tran, f=True, p=True)
            if myParTran:
                if not myParTran[0] in self.myHideGroup:
                    if mc.getAttr('%s.v' % myParTran[0]) == 0:
                        self.myHideGroup.append(myParTran[0])
                        return True
                    else:
                        if self.judgeAndeCollectHide(myParTran[0]):
                            return True
        return False

    def CreatProxyLoator_forVfx(self, *args):
        allMyVrayMeshs = mc.ls(type="VRayMesh")
        #所有Vray代理的地址列表
        allMyFileNames = []
        if allMyVrayMeshs:
            for eachMesh in allMyVrayMeshs:
                myeachName = mc.getAttr('%s.fileName' % eachMesh)
                if os.path.isfile(myeachName):
                    allMyFileNames.append(myeachName)
                else:
                    mc.confirmDialog(title=u'温馨提示', message=u'代理物体指定的路径找不到相应文件！', button=['OK'], defaultButton='Yes', dismissString='No')
                    return False
            mySortFileNames = self.sortListSeq(allMyFileNames)
            for eachSort in mySortFileNames:
                allMyVrayTrans = []
                for eachIndex in eachSort[1]:
                    eachmeshCons = mc.listConnections(allMyVrayMeshs[eachIndex], sh=True)
                    if eachmeshCons:
                        allMyShapePTran = []
                        for eachCon in eachmeshCons:
                            if mc.nodeType(eachCon) == "mesh":
                                allMyTrans = mc.listRelatives(eachCon, f=True, ap=True)
                                if allMyTrans:
                                    for myTan in allMyTrans:
                                        if not self.judgeAndeCollectHide(myTan):
                                            allMyVrayTrans.append(myTan)
                if allMyVrayTrans:
                    allMyLocatrs = []
                    myBaseName = os.path.basename(eachSort[0])
                    myLocatorBName = os.path.splitext(myBaseName)[0]
                    for i, myReplace in enumerate(allMyVrayTrans):
                        tt = mc.xform(myReplace, q=True, ws=True, piv=True)
                        myListReplacesP = mc.listRelatives(myReplace, p=True, f=True, pa=True)
                        myLocator = mc.spaceLocator(n="%s_%s" % (myLocatorBName, i), p=(0, 0, 0))[0]
                        if myListReplacesP:
                            mc.xform(myLocator, t=(tt[0], tt[1], tt[2]))
                            myLocator = mc.parent(myLocator, myListReplacesP[0])[0]
                            rrL = mc.xform(myReplace, q=True, ro=True)
                            ssL = mc.xform(myReplace, q=True, r=True, s=True)
                            mc.xform(myLocator, ro=(rrL[0], rrL[1], rrL[2]))
                            mc.xform(myLocator, s=(ssL[0], ssL[1], ssL[2]))
                            myLocator = mc.parent(myLocator, w=True)[0]
                            rr = mc.xform(myLocator, q=True, ro=True)
                            ss = mc.xform(myLocator, q=True, r=True, s=True)
                        else:
                            rr = mc.xform(myReplace, q=True, ws=True, ro=True)
                            ss = mc.xform(myReplace, q=True, r=True, s=True)
                            mc.xform(myLocator, a=True, s=(ss[0], ss[1], ss[2]))
                            mc.xform(myLocator, a=True, ro=(rr[0], rr[1], rr[2]))
                        allMyLocatrs.append(myLocator)
                    mc.group(allMyLocatrs, n="%s_LG_VFX" % myLocatorBName)
        else:
            mc.warning(u"没有代理物体")

    def ModifyTransformToZero_zwz(self, *args):
        allMyShapes = []
        allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True)
        for Shape in allShapes:
            ShapeType = mc.nodeType(Shape)
            if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
                allMyShapes.append(Shape)
        del allShapes
        if len(allMyShapes) == 0:
            mc.confirmDialog(title=u'温馨提示', message=u'选择的组或者物体不含有模型\n请重新选择！', button=['OK'], defaultButton='Yes', dismissString='No')
            #通过Shapes选择相应的SG
        else:
            myTrGroup = []
            for eachTr in allMyShapes:
               myTr = mc.listRelatives(eachTr, p=True, f=True)[0]
               myTrGroup.append(myTr)
        numMySelect = len(myTrGroup)
        OriginalObjects = mc.ls(myTrGroup, dagObjects=True, ni=True, s=True, l=True)
        numOriginalObjects = len(OriginalObjects)
        if numMySelect != numOriginalObjects:
            mc.confirmDialog(title=u'温馨提示', message=u'选择的物体存在关联关系，请普通复制之后再操作！', button=['OK'], defaultButton='Yes', dismissString='No')
        else:
            for each in myTrGroup:
                myPosition = mc.xform(each, q=True, rp=True, ws=True)
                mc.move(0, 0, 0, each, rpr=True)
                mc.makeIdentity(each, apply=True, t=1, r=0, s=0, n=0)
                mc.xform(each, t=myPosition, ws=True)

    #根据面数模糊选择物体
    def selectFaceBox_zwz(self, *args):
        radioValue1 = mc.checkBoxGrp(self.__dict__['uiMoSelectCheck'], q=True, v1=True)
        radioValue2 = mc.checkBoxGrp(self.__dict__['uiMoSelectCheck'], q=True, v2=True)
        if radioValue1 is False and radioValue2 is False:
            mc.confirmDialog(title=u'警告', message=u'请勾选相应选项！', button='OK', defaultButton='OK')
            return
        allTransforms = []
        mySelectO = mc.ls(sl=True, ni=True, tr=True)
        numMySelect0 = len(mySelectO)
        if numMySelect0 > 1:
            mc.confirmDialog(title=u'警告', message=u'仅能选择一个物体！\n请重新选择！', button='OK', defaultButton='OK')
        elif numMySelect0 == 0:
            mc.confirmDialog(title=u'警告', message=u'请选择物体！', button='OK', defaultButton='OK')
        else:
            selectShape = mc.listRelatives(mySelectO, c=True, pa=True)[0]
            selectShapeType = mc.nodeType(selectShape)
            if selectShapeType != 'mesh':
                mc.confirmDialog(title=u'警告', message=u'没有选择正确的poly模型！\n请重新选择！', button='OK', defaultButton='OK')
            else:
                allTypeObjects = mc.ls(ni=True, tr=True)
                for TranF in allTypeObjects:
                    rTmpP = mc.listRelatives(TranF, p=True)
                    if rTmpP and rTmpP[0][-13:] == 'OriginalGroup':
                        continue
                    if mc.nodeType(TranF) == 'transform':
                        try:
                            Shape = mc.listRelatives(TranF, c=True, pa=True)[0]
                        except:
                            continue
                        else:
                            ShapeType = mc.nodeType(Shape)
                        if ShapeType == 'mesh':
                            allTransforms.append(TranF)
                if allTransforms:
                    faceNum = mc.polyEvaluate(mySelectO, f=True)
                    sArea = mc.polyEvaluate(mySelectO, a=True)
                    allFinObjects = []
                    for mesh in allTransforms:
                        if radioValue1 and radioValue2 is False:
                            if mc.polyEvaluate(mesh, f=True) == faceNum:
                                allFinObjects.append(mesh)
                        if radioValue1 is False and radioValue2:
                            if sArea == mc.polyEvaluate(mesh, a=True):
                                allFinObjects.append(mesh)
                        if radioValue1 and radioValue2:
                            if mc.polyEvaluate(mesh, f=True) == faceNum:
                                if sArea == mc.polyEvaluate(mesh, a=True):
                                    allFinObjects.append(mesh)
                mc.select(allFinObjects)

    def selectSameMesh_zwz(self, *args):
        TrFlag = mc.checkBoxGrp(self.__dict__['uiSoSelectCheck'], q=True, v1=True)
        RoFlag = mc.checkBoxGrp(self.__dict__['uiSoSelectCheck'], q=True, v2=True)
        ScFlag = mc.checkBoxGrp(self.__dict__['uiSoSelectCheck'], q=True, v3=True)
        allMyShapes = []
        allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True)
        for Shape in allShapes:
            ShapeType = mc.nodeType(Shape)
            if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
                allMyShapes.append(Shape)
        del allShapes
        if len(allMyShapes) == 0:
            mc.confirmDialog(title=u'温馨提示', message=u'选择的组或者物体不含有模型\n请重新选择！', button=['OK'], defaultButton='Yes', dismissString='No')
            #通过Shapes选择相应的SG
        else:
            myTrGroup = []
            for eachTr in allMyShapes:
               myTr = mc.listRelatives(eachTr, p=True, f=True)[0]
               myTrGroup.append(myTr)
        myFinalGroup = []
        myTrDict = {}
        myRoDict = {}
        myScDict = {}
        #赛选出独一的字典
        if TrFlag or RoFlag or ScFlag:
            for myTr in myTrGroup:
                if TrFlag:
                    myTrTx = str(mc.xform(myTr, q=True, sp=True, ws=True))
                    if myTrTx not in myTrDict.keys():
                            myTrDict.update({myTrTx: myTr})
                if RoFlag:
                    myRcTx = str(mc.xform(myTr, q=True, r=True, s=True))
                    if myRcTx not in myRoDict.keys():
                            myRoDict.update({myRcTx: myTr})
                if ScFlag:
                    myScTx = str(mc.xform(myTr, q=True, ro=True, ws=True))
                    if myScTx not in myScDict.keys():
                            myScDict.update({myScTx: myTr})
            #对比出不用的元素
            for myTr in myTrGroup:
                if TrFlag:
                    if myTr in myTrDict.values():
                        continue
                if RoFlag:
                    if myTr in myRoDict.values():
                        continue
                if ScFlag:
                    if myTr in myScDict.values():
                        continue
                myFinalGroup.append(myTr)
        numMesh = len(myFinalGroup)
        if myFinalGroup:
            mc.select(myFinalGroup)
        mc.confirmDialog(title=u'温馨提示', message=u'一共有 %s 个物体具有相同属性' % numMesh, button=['OK'], defaultButton='Yes', dismissString='No')

    #根据名字模糊选择物体
    def selectN_zwz(self, *args):
        allTransforms = []
        typeCmd = mc.textField(self.__dict__['uiMoSelectText'], q=True, text=True)
        allTranFS = mc.ls("*" + typeCmd + "*", tr=True, ni=True)
        if allTranFS:
            for TranF in allTranFS:
                rTmpP = mc.listRelatives(TranF, p=True)
                if rTmpP and rTmpP[0][-13:] == 'OriginalGroup':
                    continue
                if mc.nodeType(TranF) == 'transform':
                    Shape = mc.listRelatives(TranF, c=True, pa=True)[0]
                    ShapeType = mc.nodeType(Shape)
                    if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv' or ShapeType == 'aiStandIn':
                        allTransforms.append(TranF)
        if allTransforms:
            mc.select(cl=True)
            mc.select(allTransforms)
        mySelectN = len(allTransforms)
        if mySelectN:
            mc.confirmDialog(title='warning', message=u'已选择了%s个含有%s字符名字的物体' % (mySelectN, typeCmd), button='OK', defaultButton='OK')
        else:
            mc.confirmDialog(title='warning', message=u'0个物体的名字含有%s字符' % typeCmd, button='OK', defaultButton='OK')

    def modelOption(self, *args):
        modelOptionV = mc.radioButtonGrp(self.uimodelRadio, q=True, sl=True)
        #创建模式
        if modelOptionV == 1:
            mc.frameLayout(self.uireplaceFrameLayout, e=True, en=True)
            mc.frameLayout(self.uimyLocatorFrameLayout, e=True, en=False)
            mc.frameLayout(self.uimyPaticleFrameLayout, e=True, en=False)
            mc.button(self.uiReplace_AB, e=True, backgroundColor=(0.9, 0.5, 0))
            mc.button(self.uiReplace_DB, e=True, backgroundColor=(0.9, 0.3, 0.3))
            mc.button(self.uiReplace_CB, e=True, backgroundColor=(0.2, 0.8, 0.3))
            mc.button(self.uimyLocator_AB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uimyLocator_DB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uimyLocator_CB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uimyParticles_AB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uimyParticles_CB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uiNoAnModel_ICB, e=True, en=True, backgroundColor=(0.2, 0.8, 0.3))
            mc.button(self.uiAnModel_ICB, e=True, en=True, backgroundColor=(0.2, 0.8, 0.3))
            mc.button(self.uiAnModel_PCB, e=True, en=True, backgroundColor=(0.2, 0.8, 0.3))
            mc.button(self.uiAnModel_PMB, e=True, en=False, backgroundColor=(0.267, 0.267, 0.267))
        #修复模式
        elif modelOptionV == 2:
            mc.frameLayout(self.uireplaceFrameLayout, e=True, en=False)
            mc.frameLayout(self.uimyLocatorFrameLayout, e=True, en=True)
            mc.frameLayout(self.uimyPaticleFrameLayout, e=True, en=True)
            mc.button(self.uiReplace_AB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uiReplace_DB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uiReplace_CB, e=True, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uimyLocator_AB, e=True, backgroundColor=(0.9, 0.5, 0))
            mc.button(self.uimyLocator_DB, e=True, backgroundColor=(0.9, 0.3, 0.3))
            mc.button(self.uimyLocator_CB, e=True, backgroundColor=(0.2, 0.8, 0.3))
            mc.button(self.uimyParticles_AB, e=True, backgroundColor=(0.9, 0.5, 0))
            mc.button(self.uimyParticles_CB, e=True, backgroundColor=(0.2, 0.8, 0.3))
            mc.button(self.uiNoAnModel_ICB, e=True, en=False, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uiAnModel_ICB, e=True, en=False, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uiAnModel_PCB, e=True, en=False, backgroundColor=(0.267, 0.267, 0.267))
            mc.button(self.uiAnModel_PMB, e=True, en=True, backgroundColor=(0.2, 0.8, 0.3))

    def setAllVrayMeshOrAiStandToBox(self, Value, *args):
        try:
            allMyVrayMeshs = mc.ls(type='VRayMesh')
        except:
            pass
        else:
            if allMyVrayMeshs:
                for myVrayMesh in allMyVrayMeshs:
                    mc.setAttr('%s.showBBoxOnly' % myVrayMesh, Value)
        try:
            allMyAiStandIn = mc.ls(type='aiStandIn')
        except:
            pass
        else:
            if allMyAiStandIn:
                if Value:
                    aiStandType = 0
                else:
                    aiStandType = 4
                for myAiStandIn in allMyAiStandIn:
                    mc.setAttr('%s.mode' % myAiStandIn, aiStandType)


    #按钮操作
    def addOrDelorCleanButton(self, *args):
        #num=11(添加)、12(删除)、13(清除)  是被替代物体
        #num=21(添加)、22(删除)、23(清除)  是替代的源物体
        #num=31(添加)、32(删除)、33(清除)  是Locator的物体
        #num=41(添加)、42(删除)、43(清除)  是Particle的物体
        myTextList = args[1]
        #类型
        num = args[0]
        mod = num % 10
        #添加模式
        if mod == 1:
            addObjects = []
            myObjects = []
            tmp = ''
            myListObjects = mc.textScrollList(self.__dict__[myTextList], q=True, ai=True)
            if num == 11 or num == 21:
                allTranFS = mc.ls(sl=True, dag=True, tr=True, ni=True, l=True)
                if allTranFS:
                    for TranF in allTranFS:
                        if mc.nodeType(TranF) == 'transform':
                            Shape = mc.listRelatives(TranF, c=True, pa=True)[0]
                            ShapeType = mc.nodeType(Shape)
                            if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv' or ShapeType == 'aiStandIn' or ShapeType == 'locator':
                                myObjects.append(TranF)
            elif num == 31:
                myObjects = mc.ls(sl=True, dag=True, type='locator', l=True)
            elif num == 41:
                if not myListObjects:
                    myObjects = mc.ls(sl=True, dag=True, type='particle', l=True)
                    if len(myObjects) > 1:
                        myObjects = []
                        sys.stderr.write(u'只能加载1个粒子')
            if myObjects:
                if num == 21:
                    finalAObjects = []
                    numInstaneObjects = len(myObjects)
                    OriginalObjects = mc.ls(myObjects, dagObjects=True, ni=True, s=True, l=True)
                    numOriginalObjects = len(OriginalObjects)
                    if numInstaneObjects != numOriginalObjects:
                        for myOriginalO in OriginalObjects:
                            temp = mc.listRelatives(myOriginalO, p=True, f=True)[0]
                            finalAObjects.append(temp)
                        myObjects = finalAObjects
                        mc.confirmDialog(title=u'温馨提示：', message=u'您选择的物体中含有关联物体！\n已经塞选出非关联物体,并添加到列表中！', button=['OK'], defaultButton='Yes', dismissString='No')
                    else:
                        if numInstaneObjects == 1:
                            temp = mc.listRelatives(OriginalObjects[0], p=True, f=True)[0]
                            if myObjects[0] != temp:
                                finalAObjects.append(temp)
                                myObjects = finalAObjects
                                mc.confirmDialog(title=u'温馨提示：', message=u'您选择的物体中含有关联物体！\n已经塞选出非关联物体,并添加到列表中！', button=['OK'], defaultButton='Yes', dismissString='No')
                for each in myObjects:
                    if num == 11 or num == 21:
                        if myListObjects:
                            if not each in myListObjects:
                                addObjects.append(each)
                        else:
                            addObjects.append(each)
                    else:
                        tmp = mc.listRelatives(each, p=True, pa=True)
                        if tmp:
                            #列表存在内容的时候
                            if myListObjects:
                                if not tmp[0] in myListObjects:
                                    addObjects.append(tmp[0])
                            else:
                                addObjects.append(tmp[0])
                mc.textScrollList(self.__dict__[myTextList], e=True, a=addObjects)
        #删除列表模式
        elif mod == 2:
            mySelectedItems = mc.textScrollList(self.__dict__[myTextList], q=True, si=True)
            if mySelectedItems:
                mc.textScrollList(self.__dict__[myTextList], e=True, ri=mySelectedItems)
        #清空模式
        elif mod == 3:
            mc.textScrollList(self.__dict__[myTextList], e=True, ra=True)

    def selectTextList(self, *args):
        myTextList = args[0]
        myListObjects = mc.textScrollList(self.__dict__[myTextList], q=True, si=True)
        mc.select(myListObjects)

    def CopyMat(self, dest, source):
        mc.select(dest, source)
        try:
            mm.eval('TransferUVMatSelProc(1, 1)')
        except:
            pass

    def NoAnInstanceCopy(self, *args):
        myInstanceGName = mc.textFieldGrp(self.__dict__['uiinstancer_GName'], q=True, text=True)
        allSameOs = mc.ls('%s' % myInstanceGName, tr=True)
        numGC = ''
        if allSameOs:
            retrnnValue = mc.confirmDialog(title=u'温馨提示：', message=u'当前输入的组名已存在,是否生成到该该组中！\nYes：加入当前组中 \nNo: 请重新新命名！', button=["Yes", "No"], defaultButton='Yes', cancelButton='No', dismissString='No')
            if retrnnValue == 'No':
                return
            else:
                groupC = mc.listRelatives('myInstanceGroup', c=True)
                numGC = len(groupC)/2
        allmyInstanceObjects = []
        myListReplaces = mc.textScrollList(self.__dict__['uiReplaceOText'], q=True, ai=True)
        myListInstancers = mc.textScrollList(self.__dict__['uiinstancerOText'], q=True, ai=True)

        result = mc.confirmDialog(title=u'温馨提示：', message=u'创建关联复制物体是否存放一个组里面！\nYes：存放一个组 \nNo: 每40个存放一个组！', button=["Yes", "No"], defaultButton='Yes', cancelButton='No', dismissString='No')
          
        numMyListReplaceQs = int(math.ceil(len(myListReplaces)/40.0))
        numMyListInstancers = 0
        #复制并把物体脱离组
        newMyInstancers = []
        firstN = 1
        while(1):
            tmpB = False
            for myInstancer in myListInstancers:
                if result == "Yes" and (firstN > 1) and (numMyListInstancers >= 1):
                    tmpB = True
                    break
                #if (firstN > 1) and (numMyListInstancers >= numMyListReplaceQs):
                elif result == "No" and (firstN > 1) and (numMyListInstancers >= numMyListReplaceQs):
                    tmpB = True
                    break
                # else:
                #     return
                myInstancerSN = mc.ls(myInstancer)[0]
                #设置含有VRmesh时用特殊复制
                SFlag = True
                
                MeshSC = mc.listRelatives(myInstancerSN, c=True)
                if MeshSC:
                    MeshVC = ''
                    try:
                        MeshVC = mc.listConnections('%s.inMesh' % MeshSC[0], s=True)
                    except:
                        pass
                    if MeshVC:
                        if mc.nodeType(MeshVC[0]) == 'transformGeometry':
                            tmpO = mc.duplicate(myInstancer, n='%sO' % myInstancerSN, un=True, rr=True)[0]
                            SFlag = False
                if SFlag:
                    cacheFileFlag = False
                    myAllHistorys = mc.listHistory(myInstancer)
                    for myHistory in myAllHistorys:
                        myHistoryType = mc.nodeType(myHistory)
                        if myHistoryType == 'cacheFile':
                            cacheFileFlag = True
                            break
                        elif myHistoryType == 'VRayMesh':
                            cacheFileFlag = True
                    if cacheFileFlag:
                        tmpO = mc.duplicate(myInstancer, n='%sO' % myInstancerSN, un=True, rr=True)[0]
                    else:
                        tmpO = mc.duplicate(myInstancer, n='%sO' % myInstancerSN, rr=True)[0]
                self.CopyMat(myInstancer, tmpO)
                newMyInstancers.append(tmpO)
                numMyListInstancers = numMyListInstancers+1
            firstN = firstN+1
            if tmpB:
                break
        MyOriginalGN = mc.group(newMyInstancers, n='%s_OriginalGroup%s' % (myInstanceGName, numGC), w=True)
        if myListReplaces and myListInstancers:
            for myReplace in myListReplaces:
                if mc.getAttr('%s.v' % myReplace):
                    tt = mc.xform(myReplace, q=True, ws=True, piv=True)
                    myListReplacesP = mc.listRelatives(myReplace, p=True, pa=True)
                    if myListReplacesP:
                        myLocator = mc.spaceLocator(p=(0, 0, 0))[0]
                        mc.xform(myLocator, t=(tt[0], tt[1], tt[2]))
                        myLocator = mc.parent(myLocator, myListReplacesP[0])[0]
                        rrL = mc.xform(myReplace, q=True, ro=True)
                        ssL = mc.xform(myReplace, q=True, r=True, s=True)
                        mc.xform(myLocator, ro=(rrL[0], rrL[1], rrL[2]))
                        mc.xform(myLocator, s=(ssL[0], ssL[1], ssL[2]))
                        myLocator = mc.parent(myLocator, w=True)[0]
                        rr = mc.xform(myLocator, q=True, ro=True)
                        ss = mc.xform(myLocator, q=True, r=True, s=True)
                        try:
                            mc.delete(myLocator)
                        except:
                            pass
                    else:
                        rr = mc.xform(myReplace, q=True, ws=True, ro=True)
                        ss = mc.xform(myReplace, q=True, r=True, s=True)
                    if numMyListInstancers == 1:
                        randomObject = newMyInstancers[0]
                    else:
                        randomObject = random.choice(newMyInstancers)
                    randomObjectSN = mc.ls(randomObject)[0]
                    myInstanceObject = mc.instance(randomObject, n='%s_%s' % (myInstanceGName, randomObjectSN))[0]
                    mc.xform(myInstanceObject, a=True, s=(ss[0], ss[1], ss[2]))
                    mc.xform(myInstanceObject, a=True, t=(tt[0], tt[1], tt[2]))
                    mc.xform(myInstanceObject, a=True, ro=(rr[0], rr[1], rr[2]))
                    allmyInstanceObjects.append(myInstanceObject)
            myInstaceGN = mc.group(allmyInstanceObjects, n='%s_InstanceGroup%s' % (myInstanceGName, numGC), w=True)
            mc.setAttr('%s.v' % MyOriginalGN, False)
            if allSameOs:
                mc.parent(MyOriginalGN, myInstanceGName)
                mc.parent(myInstaceGN, myInstanceGName)
            else:
                mc.group([MyOriginalGN, myInstaceGN], n='%s' % myInstanceGName, w=True)



    def AnInstancerCopy(self, *args):
        myInstanceGName = mc.textFieldGrp(self.__dict__['uiinstancer_GName'], q=True, text=True)
        allSameOs = mc.ls('*%s' % myInstanceGName, tr=True)
        numGC = ''
        if allSameOs:
            retrnnValue = mc.confirmDialog(title=u'温馨提示：', message=u'当前输入的组名已存在,是否生成到该该组中！\nYes：加入当前组中 \nNo: 请重新新命名！', button=["Yes", "No"], defaultButton='Yes', cancelButton='No', dismissString='No')
            if retrnnValue == 'No':
                return
            else:
                groupC = mc.listRelatives('myInstanceGroup', c=True)
                numGC = len(groupC)/2
        allmyInstanceObjects = []
        allMyParentCs = []
        allMyScaleCs = []
        allMyExpressions = []
        allMyLocators = []
        myListReplaces = mc.textScrollList(self.__dict__['uiReplaceOText'], q=True, ai=True)
        myListInstancers = mc.textScrollList(self.__dict__['uiinstancerOText'], q=True, ai=True)
        if myListReplaces and myListInstancers:
            #复制原始物体
            numMyListReplaceQs = int(math.ceil(len(myListReplaces)/40.0))
            numMyListInstancers = 0
            newMyInstancers = []
            firstN = 1
            while(1):
                tmpB = False
                for myInstancer in myListInstancers:
                    if (firstN > 1) and (numMyListInstancers >= numMyListReplaceQs):
                        tmpB = True
                        break
                    myInstancerSN = mc.ls(myInstancer)[0]
                    tmpO = mc.duplicate(myInstancer, n='%sO' % myInstancerSN, un=True, rr=True)[0]
                    self.CopyMat(myInstancer, tmpO)
                    newMyInstancers.append(tmpO)
                    numMyListInstancers = numMyListInstancers+1
                firstN = firstN+1
                if tmpB:
                    break
            MyOriginalGN = mc.group(newMyInstancers, n='%s_OriginalGroup%s' % (myInstanceGName, numGC), w=True)
            #关联复制模块
            for myReplace in myListReplaces:
                tt = mc.xform(myReplace, q=True, ws=True, piv=True)
                myListReplacesP = mc.listRelatives(myReplace, p=True, pa=True)
                if myListReplacesP:
                    #创建中间物体locator，并传递信息，并约束
                    myLocator = mc.spaceLocator(p=(0, 0, 0))[0]
                    mc.xform(myLocator, t=(tt[0], tt[1], tt[2]))
                    myLocator = mc.parent(myLocator, myListReplacesP[0])[0]
                    rrL = mc.xform(myReplace, q=True, ro=True)
                    ssL = mc.xform(myReplace, q=True, r=True, s=True)
                    mc.xform(myLocator, ro=(rrL[0], rrL[1], rrL[2]))
                    mc.xform(myLocator, s=(ssL[0], ssL[1], ssL[2]))
                    myLocator = mc.parent(myLocator, w=True)[0]
                    allMyLocators.append(myLocator)
                    rr = mc.xform(myLocator, q=True, ro=True)
                    ss = mc.xform(myLocator, q=True, r=True, s=True)
                    mc.parentConstraint(myReplace, myLocator, mo=True, w=True)[0]
                    mc.scaleConstraint(myReplace, myLocator, offset=(1, 1, 1), weight=1)
                    InstanceParent = myLocator
                else:
                    rr = mc.xform(myReplace, q=True, ws=True, ro=True)
                    ss = mc.xform(myReplace, q=True, r=True, s=True)
                    InstanceParent = myReplace
                #关联复制物体，并获取信息，并把相应物体约束复制出来的物体
                if numMyListInstancers == 1:
                    randomObject = newMyInstancers[0]
                else:
                    randomObject = random.choice(newMyInstancers)
                randomObjectSN = mc.ls(randomObject)[0]
                myInstanceObject = mc.instance(randomObject, n='%s_%s' % (myInstanceGName, randomObjectSN))[0]
                mc.xform(myInstanceObject, a=True, s=(ss[0], ss[1], ss[2]))
                mc.xform(myInstanceObject, a=True, t=(tt[0], tt[1], tt[2]))
                mc.xform(myInstanceObject, a=True, ro=(rr[0], rr[1], rr[2]))
                myParentC = mc.parentConstraint(InstanceParent, myInstanceObject, mo=True, w=True)[0]
                allMyParentCs.append(myParentC)
                myScaleC = mc.scaleConstraint(InstanceParent, myInstanceObject, offset=(1, 1, 1), weight=1)[0]
                allMyScaleCs.append(myScaleC)
                myExpression = mc.expression(s='%s.v=%s.v' % (myInstanceObject, myReplace), o=myInstanceObject, ae=True, uc='all')
                allMyExpressions.append(myExpression)
                allmyInstanceObjects.append(myInstanceObject)
            #baked动画
            myStartFrameV = mc.playbackOptions(q=True, min=True)
            myEndFrameV = mc.playbackOptions(q=True, max=True)
            mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
            activePlane = ''
            i = 1
            while(i):
                try:
                    tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
                except:
                    pass
                else:
                    if tmp:
                        activePlane = 'modelPanel%d' % i
                        break
                i += 1
            mc.modelEditor(activePlane, e=True, polymeshes=False, nurbsSurfaces=False)
            mc.select(allmyInstanceObjects)
            mm.eval("SelectIsolate;")
            mc.bakeResults(allmyInstanceObjects, t=(myStartFrameV, myEndFrameV), sm=True, at=['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'], sb=True, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, cp=False, s=True)
            if allMyLocators:
                try:
                    mc.delete(allMyLocators)
                except:
                    pass
            #mc.delete(allMyScaleCs)
            myInstaceGN = mc.group(allmyInstanceObjects, n='%s_InstanceGroup%s' % (myInstanceGName, numGC), w=True)
            mc.setAttr('%s.v' % MyOriginalGN, False)
            if allSameOs:
                mc.parent(MyOriginalGN, myInstanceGName)
                mc.parent(myInstaceGN, myInstanceGName)
            else:
                mc.group([MyOriginalGN, myInstaceGN], n='%s' % myInstanceGName, w=True)
            mc.isolateSelect(activePlane, state=False)
            mc.modelEditor(activePlane, e=True, polymeshes=True, nurbsSurfaces=True)

    def AnInstanceParticle(self, *args):
        modeType = args[0]
        print modeType
        try:
            mm.eval(r'source "\\\\octvision.com\\cg\\td\\Maya\\2009\\Scripts\\Mel\\tazz_TransferShaders.mel"')
        except:
            sys.stderr.write(u'传输材质脚本不能加载！')
        myInstanceGName = mc.textFieldGrp(self.__dict__['uiinstancer_GName'], q=True, text=True)
        allSameOs = mc.ls('*%s' % myInstanceGName, tr=True)
        numGC = ''
        if allSameOs:
            retrnnValue = mc.confirmDialog(title=u'温馨提示：', message=u'当前输入的组名已存在,是否生成到该该组中！\nYes：加入当前组中 \nNo: 请重新新命名！', button=["Yes", "No"], defaultButton='Yes', cancelButton='No', dismissString='No')
            if retrnnValue == 'No':
                return
            else:
                groupC = mc.listRelatives('myInstanceGroup', c=True)
                numGC = len(groupC)/2
        allMyLocators = []
        allMyLocatorsDel = []
        allMyParentCs = []
        allMyScaleCs = []
        allMyExpressions = []
        newMyInstancers = []
        myListReplaces = mc.textScrollList(self.__dict__['uiReplaceOText'], q=True, ai=True)
        myListInstancers = mc.textScrollList(self.__dict__['uiinstancerOText'], q=True, ai=True)
        if myListReplaces and myListInstancers:
            for myInstancer in myListInstancers:
                myInstancerSN = mc.ls(myInstancer)[0]
                tmpO = mc.duplicate(myInstancer, n='%sO' % myInstancerSN, un=True, rr=True)[0]
                self.CopyMat(myInstancer, tmpO)
                newMyInstancers.append(tmpO)
            # newMyInstancers = mc.duplicate(myListInstancers, rr=True, un=True)
            MyOriginalGN = mc.group(newMyInstancers, n='%s_OriginalGroup%s' % (myInstanceGName, numGC), w=True)
            newMyInstancers = mc.ls(MyOriginalGN, dagObjects=True, tr=True, ni=True, l=True)[1::]
            for tmpMyInstancer in newMyInstancers:
                mc.xform(tmpMyInstancer, ro=(0, 0, 0))
                mc.xform(tmpMyInstancer, t=(0, 0, 0))
                mc.xform(tmpMyInstancer, s=(1, 1, 1))
            #复制locator
            for myReplace in myListReplaces:
                myLocator = mc.spaceLocator(p=(0, 0, 0))[0]
                myListReplacesP = mc.listRelatives(myReplace, p=True, pa=True)
                ttL = mc.xform(myReplace, q=True, ws=True, piv=True)
                mc.xform(myLocator, t=(ttL[0], ttL[1], ttL[2]))
                if myListReplacesP:
                    myLocator = mc.parent(myLocator, myListReplacesP[0])[0]
                    rrL = mc.xform(myReplace, q=True, ro=True)
                    ssL = mc.xform(myReplace, q=True, r=True, s=True)
                    mc.xform(myLocator, ro=(rrL[0], rrL[1], rrL[2]))
                    mc.xform(myLocator, s=(ssL[0], ssL[1], ssL[2]))
                    myLocatorD = mc.parent(myLocator, w=True)[0]
                    allMyLocatorsDel.append(myLocatorD)
                    myLocator = mc.duplicate(myLocatorD, n='%s_Locator1' % myInstanceGName, rr=True)[0]
                    mc.parentConstraint(myReplace, myLocatorD, mo=True, w=True)[0]
                    mc.scaleConstraint(myReplace, myLocatorD, offset=(1, 1, 1), weight=1)
                    InstanceParent = myLocatorD
                else:
                    rr = mc.xform(myReplace, q=True, ws=True, ro=True)
                    ss = mc.xform(myReplace, q=True, r=True, s=True)
                    mc.xform(myLocator, a=True, s=(ss[0], ss[1], ss[2]))
                    mc.xform(myLocator, a=True, ro=(rr[0], rr[1], rr[2]))
                    InstanceParent = myReplace
                allMyLocators.append(myLocator)
                myParentC = mc.parentConstraint(InstanceParent, myLocator, mo=True, w=True)[0]
                allMyParentCs.append(myParentC)
                myScaleC = mc.scaleConstraint(InstanceParent, myLocator, offset=(1, 1, 1), weight=1)[0]
                allMyScaleCs.append(myScaleC)
                myExpression = mc.expression(s='%s.v=%s.v' % (myLocator, myReplace), o=myLocator, ae=True, uc='all')
                allMyExpressions.append(myExpression)
            #baked动画
            myStartFrameV = mc.playbackOptions(q=True, min=True)
            myEndFrameV = mc.playbackOptions(q=True, max=True)
            mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
            activePlane = ''
            i = 1
            while(i):
                try:
                    tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
                except:
                    pass
                else:
                    if tmp:
                        activePlane = 'modelPanel%d' % i
                        break
                i += 1
            mc.modelEditor(activePlane, e=True, polymeshes=False, locators=False, nurbsSurfaces=False)
            mc.select(allMyLocators)
            mm.eval("SelectIsolate;")
            if modeType == 1:
                mc.bakeResults(allMyLocators, t=(myStartFrameV, myEndFrameV), sm=True, at=['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'], sb=True, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, cp=False, s=True)
            if allMyLocatorsDel:
                try:
                    mc.delete(allMyLocatorsDel)
                except:
                    pass
            try:
                mc.delete(allMyScaleCs)
                mc.delete(allMyParentCs)
            except:
                pass
            myLocatorGN = mc.group(allMyLocators, n='%s_LocatorGroup%s' % (myInstanceGName, numGC), w=True)
            myNewLocators = mc.ls(myLocatorGN, dag=True, tr=True)[1::]
            # myNewLocators = mc.ls(myNewLocators, et='transform')
            #创建粒子，附着粒子
            allMyNewMyLocators = mc.ls('%s_LocatorGroup' % myInstanceGName, dag=True, tr=True)[1::]
            numP = len(myNewLocators)
            myInstanceParticle = mc.particle(n='%s_InParticle%s' % (myInstanceGName, numGC), jbp=[0, 0, 0], nj=numP, jr=0, c=1)
            mc.setAttr('%s.startFrame' % myInstanceParticle[1], myStartFrameV)
            mc.addAttr(myInstanceParticle[1], ln="rotatePP", dt='vectorArray')
            mc.addAttr(myInstanceParticle[1], ln="rotatePP0", dt='vectorArray')
            mc.setAttr(myInstanceParticle[1] + '.rotatePP', e=True, keyable=True)
            mc.addAttr(myInstanceParticle[1], ln="scalePP", dt='vectorArray')
            mc.addAttr(myInstanceParticle[1], ln="scalePP0", dt='vectorArray')
            mc.setAttr(myInstanceParticle[1] + '.scalePP', e=True, keyable=True)
            mc.addAttr(myInstanceParticle[1], ln="visibilityPP", dt='doubleArray')
            mc.addAttr(myInstanceParticle[1], ln="visibilityPP0", dt='doubleArray')
            mc.setAttr(myInstanceParticle[1] + '.visibilityPP', e=True, keyable=True)
            mc.addAttr(myInstanceParticle[1], ln="index", dt='doubleArray')
            mc.addAttr(myInstanceParticle[1], ln="index0", dt='doubleArray')
            mc.setAttr(myInstanceParticle[1] + '.index', e=True, keyable=True)
            numMyListInstancers = len(newMyInstancers)
            myNewLocatorS = []
            for tmp in myNewLocators:
                myNewLocatorS.append(str(tmp))
            myexpress = '''
string $prefix[] = {%s};
int $id = %s.particleId;
float $tx = `getAttr ($prefix[$id] + ".tx")`;
float $ty = `getAttr ($prefix[$id] + ".ty")`;
float $tz = `getAttr ($prefix[$id] + ".tz")`;
float $rx = `getAttr ($prefix[$id] + ".rx")`;
float $ry = `getAttr ($prefix[$id] + ".ry")`;
float $rz = `getAttr ($prefix[$id] + ".rz")`;
float $sx = `getAttr ($prefix[$id] + ".sx")`;
float $sy = `getAttr ($prefix[$id] + ".sy")`;
float $sz = `getAttr ($prefix[$id] + ".sz")`;
float $v = `getAttr ($prefix[$id] + ".v")`;
if (%s.particleId == $id)
{
%s.position = <<$tx,$ty,$tz>>;
%s.rotatePP = <<$rx,$ry,$rz>>;
%s.scalePP = <<$sx,$sy,$sz>>;
%s.visibilityPP = $v;
%s.index = $id%%%s;
}
            ''' % (myNewLocatorS, myInstanceParticle[1], myInstanceParticle[1], myInstanceParticle[1], myInstanceParticle[1], myInstanceParticle[1], myInstanceParticle[1], myInstanceParticle[1], numMyListInstancers)
            myexpress = myexpress.replace("\'", "\"")
            myexpress = myexpress.replace("{[", "{")
            myexpress = myexpress.replace("]}", "}")
            mc.dynExpression(myInstanceParticle[1], s=myexpress, c=True)
            mc.dynExpression(myInstanceParticle[1], s=myexpress, rbd=True)
            myInstancerName = mc.particleInstancer(myInstanceParticle[1], a=True, obj=newMyInstancers, cs=1,  csu='Frames', lod='Geometry', ru='Degrees', ro='XYZ', p='worldPosition', age='age')
            mc.select(myInstanceParticle[1])
            try:
                mm.eval('AEbuildControls')
                mc.checkBoxGrp('AEdisplayAllTypes', e=True, v1=True)
                mm.eval('AEeditInstancerOptionMenus %s' % myInstanceParticle[1])
            except:
                pass
            mc.particleInstancer(myInstanceParticle[1], e=True, n=myInstancerName, r='rotatePP')
            mc.particleInstancer(myInstanceParticle[1], e=True, n=myInstancerName, sc='scalePP')
            mc.particleInstancer(myInstanceParticle[1], e=True, n=myInstancerName, vis='visibilityPP')
            try:
                mc.particleInstancer(myInstanceParticle[1], e=True, n=myInstancerName, objectIndex='index')
            except:
                pass
            if allSameOs:
                mc.parent(MyOriginalGN, myInstanceGName)
                mc.parent(myLocatorGN, myInstanceGName)
                mc.parent(myInstanceParticle[0], myInstanceGName)
                mc.parent(myInstancerName, myInstanceGName)
            else:
                mc.group([MyOriginalGN, myLocatorGN, myInstanceParticle[0], myInstancerName], n=myInstanceGName, w=True)
            mc.setAttr('%s.v' % myLocatorGN, False)
            mc.setAttr('%s.v' % myInstanceParticle[0], False)
            mc.setAttr('%s.v' % MyOriginalGN, False)
            mc.isolateSelect(activePlane, state=False)
            mc.modelEditor(activePlane, e=True, polymeshes=True, locators=True, nurbsSurfaces=True)

    def repairInstance(self, *args):
        myListInstancers = mc.textScrollList(self.__dict__['uiinstancerOText'], q=True, ai=True)
        myNewLocators = mc.textScrollList(self.__dict__['uimyLocatorText'], q=True, ai=True)
        myInstanceParticle = mc.textScrollList(self.__dict__['uimyParticleText'], q=True, ai=True)
        if myListInstancers and myNewLocators and myInstanceParticle:
            numMyListInstancers = len(myListInstancers)
            myNewLocatorS = []
            for tmp in myNewLocators:
                myNewLocatorS.append(str(tmp))
            myexpress = '''
string $prefix[] = {%s};
int $id = %s.particleId;
float $tx = `getAttr ($prefix[$id] + ".tx")`;
float $ty = `getAttr ($prefix[$id] + ".ty")`;
float $tz = `getAttr ($prefix[$id] + ".tz")`;
float $rx = `getAttr ($prefix[$id] + ".rx")`;
float $ry = `getAttr ($prefix[$id] + ".ry")`;
float $rz = `getAttr ($prefix[$id] + ".rz")`;
float $sx = `getAttr ($prefix[$id] + ".sx")`;
float $sy = `getAttr ($prefix[$id] + ".sy")`;
float $sz = `getAttr ($prefix[$id] + ".sz")`;
float $v = `getAttr ($prefix[$id] + ".v")`;
if (%s.particleId == $id)
{
%s.position = <<$tx,$ty,$tz>>;
%s.rotatePP = <<$rx,$ry,$rz>>;
%s.scalePP = <<$sx,$sy,$sz>>;
%s.visibilityPP = $v;
%s.index = $id%%%s;
}
            ''' % (myNewLocatorS, myInstanceParticle[0], myInstanceParticle[0], myInstanceParticle[0], myInstanceParticle[0], myInstanceParticle[0], myInstanceParticle[0], myInstanceParticle[0], numMyListInstancers)
            myexpress = myexpress.replace("\'", "\"")
            myexpress = myexpress.replace("{[", "{")
            myexpress = myexpress.replace("]}", "}")
            mc.dynExpression(myInstanceParticle[0], s=myexpress, c=True)
            mc.dynExpression(myInstanceParticle[0], s=myexpress, rbd=True)

# def show():
#     i = ReplaceOriginalObject_zwz()
#     i.show()

# show()



