#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import sys
import maya.cmds as mc
import maya.mel as mm
import maya.utils
import maya.OpenMaya as om
import random

import OCT_XXBDeleteUnUseCameras_zwz
import OCT_FKSDYDelBot_zwz
import OCT_SQTGGCModifyEyes_zwz
import OCT_DelUnuseUvSets_zxy
import spPaint3dGui
import spPaint3dContext
import OCT_AssignRandShader_zwz
import repairTex_YJL
import SnapToPlane

def ReductionFace():
    import ReductionFaceForHoudini
    dialog = ReductionFaceForHoudini.ReductionFaceForHoudini()
    dialog.showWindow()

def SeparateAndCombine():
    # 先框选需要分离的所有模型
    # 运行命令
    # 结束后如果有错误的物体超过1个
    selectObj = mc.ls(sl = True, l = True)
    SeparateErrorObj = []
    if not selectObj:
        mc.error('please select model!')
    for obj in selectObj:
        objSplit = obj.split('|')
        objName = objSplit[-1]
        objParent = ('|').join(objSplit[:-1])
        try:
            objSeparate = mc.polySeparate(obj, ch = 1)
            newObj = mc.polyUnite(objSeparate, name = objName, ch = 1, mergeUVSets = 1)
            mm.eval('DeleteHistory;')
            if objParent:
                mc.parent(newObj[0], objParent)
        except:
            SeparateErrorObj.append(obj)

    mc.select(SeparateErrorObj)


def removeDuplicateMat():
    import RemoveDuplicateMat
    dialog = RemoveDuplicateMat.CleanMatertialTool()
    dialog.showWindow()


def rPaint3d():
    mm.eval('ScriptPaintToolOptions;')
    mm.eval('artUserPaintCtx -e -tsc "geometryPaints" `currentCtx`;')
    mm.eval('artUserPaintCtx -e -tsc "geometryPaints" `currentCtx`;')

# def repairTex_YJL():
#     import repairTex_YJL
#     repairTex_YJL.repWin()

def selectedCreateGroup():
    allSelectObjs = mc.ls(sl = True, dag = True, shapes = True, ni = True)
    for obj in allSelectObjs:
        tranf = mc.listRelatives(obj, p = True)[0]
        groupName = mc.group(empty = True, name = '%s_group'%tranf)
        mc.parent(tranf, groupName, relative=True)

#Yeti笔刷
def YetiPaintTool():
    import OCT_YetiPaintTool
    i = OCT_YetiPaintTool.paint3dContext()

#arnold显示box，解决代理卡的问题
def ArnoldBox():
    allAiStandIn = mc.ls(type = "aiStandIn")
    for obj in allAiStandIn:
        mc.setAttr("%s.mode"%obj, 0)
        mc.setAttr("%s.standInDrawOverride"%obj,2)


def randomUVSet_YH():
    import OCT_RandomUVSet_YH
    i=OCT_RandomUVSet_YH.setUV()
    i.setUVUI()

def runWhiteBoxTool():
    import WhiteBoxTool
    WhiteBoxTool.makeWin()

def runSpPaint3d():
    spPaint3dwin = spPaint3dGui.spPaint3dWin()

def TextureMaterialTool():
    import OCT_TextureMaterials
    i=OCT_TextureMaterials.OCT_TextureMaterial()
    i.FindArnoldOpacity()

def selectUVEdge():
    import OCT_selectUVEdges
    i=OCT_selectUVEdges.selectUVEdges()
    i.LsUVMap()
    
def displacementShader():
    import OCT_DisplacementShader
    i=OCT_DisplacementShader.DisplacementShaderAndShading()
    i.DisplacementShaderAndShadingUI()

def placeOnMesh():
    import OCT_vfx
    import OCT_util
    _ls = mc.ls(sl=True)
    _count = len(_ls)
    _obj = mc.ls(sl=True,head=_count-1)
    _placeObj = mc.ls(sl=True,tail=1)
    _origNormal = om.MVector(0,1,0)

    i = 0
    while i<len(_obj):
        _foundPoint = OCT_vfx.uvToPos(_placeObj[0],random.uniform(0,1),random.uniform(0,1))
        if not _foundPoint == None:
            mc.setAttr((_obj[i] + '.translate'),0,0,0)
            mc.setAttr((_obj[i] + '.rotate'),0,0,0)
            mc.setAttr((_obj[i] + '.scale'),1,1,1)
            transFn = om.MFnTransform(OCT_util.nameToNode(_obj[i]))
            _translate = om.MVector(_foundPoint[0][0],_foundPoint[0][1],_foundPoint[0][2])
            transFn.setTranslation(_translate,om.MSpace.kObject)
            _normal = om.MVector(_foundPoint[1][0],_foundPoint[1][1],_foundPoint[1][2])
            _quatAlignY = om.MQuaternion()
            _quatAlignY.setToYAxis(random.uniform(0, 2))
            _quatAlignN = om.MQuaternion(om.MVector(0,1,0),_normal)
            _quat = _quatAlignY * _quatAlignN
            transFn.rotateBy(_quat,om.MSpace.kObject)
            _scaleIndex = random.uniform(0.5,1.5)
            scale_util = om.MScriptUtil()
            scale_util.createFromDouble(_scaleIndex,_scaleIndex,_scaleIndex)
            scale_ptr = scale_util.asDoublePtr()
            transFn.setScale(scale_ptr)
            i = i + 1
        
def dupToCurveFlow():
    allSel = mc.ls(sl=True)
    count = len(allSel)
    if count < 2:
        om.MGlobal.displayError('Please select some will follow Curve Objects and Curve...')
        return
    
    curveSel = mc.ls(sl=True,tail=1)
    if mc.nodeType(curveSel[0]) == 'transform':
        curveShape = mc.listRelatives(curveSel,shapes=True)
        if mc.nodeType(curveShape[0]) == 'nurbsCurve':
            shape = curveShape[0]
    elif mc.nodeType(curveSel[0]) == 'nurbsCurve':
        shape = curveSel[0]
    else:
        om.MGlobal.displayError('Please select lastest Curve...')
        return

    _min = mc.getAttr(shape + '.minValue')
    _max = mc.getAttr(shape + '.maxValue')
    
    objSel = allSel[:count-1]
    for eachObj in objSel:
        if mc.attributeQuery('translate',node=eachObj,ex=True) == False:
            om.MGlobal.displayWarning('%s Object have not "Transform" attribute,ingore it...' % eachObj)
            objSel.remove(eachObj)
        elif mc.attributeQuery('rotate',node=eachObj,ex=True) == False:
            om.MGlobal.displayWarning('%s Object have not "Rotate" attribute,ingore it...' % eachObj)
            objSel.remove(eachObj)
    
    _length = _max - _min
    segment = _length / (len(objSel)-1)
    
    if not mc.pluginInfo('dupToCurveFlowPlugin.py',q=True,l=True):
        mc.loadPlugin(r'\\octvision.com\cg\TD\Maya\2012\Plugins\dupToCurveFlowPlugin.py')
    
    icNode = mc.createNode('ic_dupToCurveFlow')
    mc.connectAttr(shape + '.local',icNode + '.inCurve',f=True)
    for i in range(0,len(objSel)):
        mc.getAttr(icNode + '.outTranslate[%i]' % i)
        mc.getAttr(icNode + '.outRotate[%i]' % i)
        if not mc.attributeQuery('param',node=objSel[i],ex=True):
            mc.addAttr(objSel[i],ln='param',at='double')
            mc.setAttr(objSel[i] + '.param',e=True,keyable=True)
            
        mc.connectAttr(objSel[i] + '.param',icNode + '.inParam[%i]'%i,f=True)
        mc.connectAttr(icNode + '.outTranslate[%i].outTranslateX'%i,objSel[i] + '.translateX',f=True)
        mc.connectAttr(icNode + '.outTranslate[%i].outTranslateY'%i,objSel[i] + '.translateY',f=True)
        mc.connectAttr(icNode + '.outTranslate[%i].outTranslateZ'%i,objSel[i] + '.translateZ',f=True)
        mc.connectAttr(icNode + '.outRotate[%i].outRotateX'%i,objSel[i] + '.rotateX',f=True)
        mc.connectAttr(icNode + '.outRotate[%i].outRotateY'%i,objSel[i] + '.rotateY',f=True)
        mc.connectAttr(icNode + '.outRotate[%i].outRotateZ'%i,objSel[i] + '.rotateZ',f=True)
        mc.setAttr(objSel[i] + '.param',segment*i)
        
def paintGeo():
    loc = mm.eval('getenv "MAYA_LOCATION";')
    cmdStr = 'source "%s/scripts/others/geometryPaint.mel";' % loc
    mm.eval(cmdStr)
    cmdStr = 'string $obj[] = `ls -sl -head 1`;string $paintObj[] = `ls -sl -tail 1`;select -cl;select $paintObj[0];ScriptPaintToolOptions;artUserPaintToolScript 3;\
    toolPropertyWindow1 ("");artUserPaintCtx -e -tsc "geoPaint" `currentCtx`;geometryPaintAlignToSrfCB(true);'
    mm.eval(cmdStr)
    
#    cmdStr = 'string $geoName = "";evalDeferred "textFieldGrp -e -text $obj[0] $geoName";'
#    mm.eval(cmdStr)
    cmdStr = 'pause -sec 1;string $geoName = "geometryName";evalDeferred "textFieldGrp -e -text $obj[0] $geoName";evalDeferred "refresh";'
    mm.eval(cmdStr)


##SMOOTH工具：
##模式：所有，所选（radioButtonGrp)
##1.删除所有SMOOTH节点
##2.删除选择的模型的SMOOTH节点
##3.添加Smooth
##4.Divisions设为0和1
####################################################################
def smooth():
    if mc.window("smoothUI",exists=1):
        mc.deleteUI("smoothUI",window=1)


    mc.window("smoothUI",title="Smooth Tools",maximizeButton=0,resizeToFitChildren=1,sizeable=0,topLeftCorner=[3,3],wh=[205,170])
    mc.columnLayout(rowSpacing=4,cw=190,columnAttach=['both',5])
    mc.radioButtonGrp('mode',numberOfRadioButtons=2,l=u'模式:',labelArray2=[u'所有',u'所选'],columnAttach3=['both','both','both'],columnWidth3=[50,50,50],select=2,cc='OCT_mod.checkSel()')
    mc.button('delNode',l=u'删除Smooth节点',c='OCT_mod.delSmoothNode()')
    mc.button('makeSmooth',l=u'Smooth模型',c='OCT_mod.smoothPoly()')
    mc.rowLayout(numberOfColumns=2)
    mc.button('zero',l='Divisions >> 0',c='OCT_mod.setDivision(0)')
    mc.button('one',l='Divisions >> 1',c='OCT_mod.setDivision(1)')
    mc.setParent('..')
    mc.frameLayout('frameLyt',l='Message',lv=False,borderStyle='in')
    mc.columnLayout(rowSpacing=4,cw=190)
    mc.text('msg1',l=u'请选择Polygon物体',font='plainLabelFont')
    mc.text('msg2',l='',font='plainLabelFont')
    mc.setParent('..')
    mc.setParent('..')
    #mc.textField('msg',en=False,text='lable')

    mc.showWindow('smoothUI')

    mc.scriptJob(e=['SelectionChanged','OCT_mod.checkSel()'],protected=True,p='frameLyt')

def getMode():
    modeState = mc.radioButtonGrp('mode',q=True,select=True)
    return modeState

def checkSel():
    if getMode() == 2:
        _sel = mc.ls(sl=True,dag=True,o=True)
        sel = mc.ls(_sel,type='transform')

        if len(sel) == 0:
            mc.text('msg1',e=True,l=u'请选择Polygon物体')
            mc.text('msg2',e=True,l='')
            #om.MGlobal.displayWarning(u'请选择Polygon物体')
            return

        obj = []
        del obj[:]
        shape = []
        del shape[:]
        _relatShape = []
        del _relatShape[:]

        for eachSel in sel:
            if mc.nodeType(eachSel) == 'transform':
                _relatShape = mc.listRelatives(eachSel,shapes=True)
            elif mc.nodeType(eachSel) == 'mesh':
                _relatShape = [eachSel]
            else:
                _relatShape = None

            if _relatShape == None:
                obj.append(eachSel)
            elif not mc.nodeType(_relatShape[0]) == 'mesh':
                obj.append(eachSel) 
            else:
                shape.append(_relatShape[0])

        _msg1 = u'一共选择了' + str(len(sel)) + u'物体'
        _msg2 = u'有' + str(len(obj)) + u'个物体不是Polygon,忽略操作'
        mc.text('msg1',e=True,l=_msg1)
        mc.text('msg2',e=True,l=_msg2)
        return shape
    else:
        mc.text('msg1',e=True,l='')
        mc.text('msg2',e=True,l='')
        return None

def delSmoothNode():
    obj = checkSel()
    allNode = []
    del allNode[:]

    if obj == None:
        allNode = mc.ls(type='polySmoothFace')
    else:
        for eachShape in obj:
            try:
                smoothNode = mc.listConnections(eachShape + '.inMesh',d=True)
            except RuntimeError:
                om.MGlobal.displayWarning(u'%s节点没有inMesh属性,跳过操作...\n' % eachShape)
            else:
                if mc.nodeType(smoothNode[0]) == 'polySmoothFace':
                    allNode.append(smoothNode[0])

    if len(allNode) > 0:
        mc.delete(allNode)

    _msg1 = u'一共删除了' + str(len(allNode)) + u'个Poly Smooth节点'
    _msg2 = u''
    mc.text('msg1',e=True,l=_msg1)
    mc.text('msg2',e=True,l=_msg2)

def smoothPoly():
#   obj = checkSel()
    if getMode() == 2:
        obj = mc.ls(sl=True,dag=True,o=True,type='mesh')
    else:
        obj = mc.ls(type='mesh')

    allNode = []
    del allNode[:]

    #allNode = obj

    for eachObj in obj:
        try:
            smoothNode = mc.listConnections(eachObj + '.inMesh',d=True)
        except:
            om.MGlobal.displayWarning(u'%s节点没有inMesh属性,跳过操作...\n' % eachObj)
        else:
            #print smoothNode
            if smoothNode == None:
                allNode.append(eachObj)
            else:
                if not mc.nodeType(smoothNode[0]) == 'polySmoothFace':
                    allNode.append(eachObj)
                else:
                    sys.stdout.write(u'%s节点已经有Poly Smooth节点,跳过操作...\n' % eachObj)

        del smoothNode

    if len(allNode) == 0:
        return

    _count = 0
    #mc.waitCursor(state=True)
    for eachNode in allNode:
        try:
            mc.polySmooth(eachNode,c=1,dv=1,kb=True)
        except:
            om.MGlobal.displayWarning(u'%s节点Smooth过程中出现错误,请检查该模型...\n' % eachNode)
        else:
            _count += 1
    #mc.waitCursor(state=False)

    _msg1 = u'一共添加了' + str(_count) + u'个Poly Smooth节点'
    _msg2 = u''
    mc.text('msg1',e=True,l=_msg1)
    mc.text('msg2',e=True,l=_msg2)

def setDivision(_level):
    obj = checkSel()
    allNode = []
    del allNode[:]

    if obj == None:
        obj = mc.ls(type='mesh')

    mc.waitCursor(state=True)
    for eachObj in obj:
        try:
            smoothNode = mc.listConnections(eachObj + '.inMesh',d=True)
        except RuntimeError:
            om.MGlobal.displayWarning(u'%s节点没有inMesh属性,跳过操作...\n' % eachObj)
        else:
            if not smoothNode == None:
                if mc.nodeType(smoothNode[0]) == 'polySmoothFace':
                    mc.setAttr(smoothNode[0] + '.divisions',_level)

        del smoothNode

    mc.waitCursor(state=False)
##########################################################