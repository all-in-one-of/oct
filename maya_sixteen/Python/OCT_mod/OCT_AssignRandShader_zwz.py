# -*- coding: utf-8 -*-
__author__ = 'zhongwzh'
import maya.cmds as mc
import random

def OCT_AssignRandShader_UI_zwz():
    if mc.windowPref('OCT_AssignRandShader_UI_zwz', exists=True):
        mc.windowPref('OCT_AssignRandShader_UI_zwz', remove=True)
    if mc.window('OCT_AssignRandShader_UI_zwz', exists=True):
        mc.deleteUI('OCT_AssignRandShader_UI_zwz', window=True)
    mc.window("OCT_AssignRandShader_UI_zwz", title=u"OCT_AssignRandShader_zwz", menuBar=True,
              widthHeight=(168, 100), resizeToFitChildren=False, sizeable=True)
    mc.columnLayout('formLyt', adjustableColumn=True)
    mc.button('get_Objets', label=u'Objects(支持"组"选择)', w=200, h=30, aop=True,
              c='OCT_mod.OCT_AssignRandShader_zwz.getObjets()', backgroundColor=(0.3, 0.7, 0.3))
    mc.button('get_Shaders', label=u'Shaders(选择材质)', w=200, h=30, aop=True,
              c='OCT_mod.OCT_AssignRandShader_zwz.getShaders()', backgroundColor=(0.3, 0.7, 0.3))
    mc.button('assign_Shaders', label=u'Assign Shaders', w=200, h=35, aop=True,
              c='OCT_mod.OCT_AssignRandShader_zwz.assignShaders()', backgroundColor=(0.9, 0.3, 0.3))
    mc.setParent('..')
    mc.showWindow('OCT_AssignRandShader_UI_zwz')

myMats = []
def getShaders():
    global myMats
    myMats = []
    myMats = mc.ls(sl=True, mat=True)
    if not myMats:
        mc.confirmDialog(title=u'错误:', message=u'没有选择到任何材质球', button=['OK'], defaultButton='Yes', dismissString='No')

allMyShapes =[]
def getObjets():
    global allMyShapes
    allMyShapes = []
    allShapes = mc.ls(selection=True, dagObjects=True, shapes=True, rq=True)
    for Shape in allShapes:
        ShapeType = mc.nodeType(Shape)
        if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
            if not mc.getAttr("%s.intermediateObject" % Shape):
                allMyShapes.append(Shape)
    if not allMyShapes:
        mc.confirmDialog(title=u'错误:', message=u'没有选择到任何物体', button=['OK'], defaultButton='Yes', dismissString='No')

def assignShaders():
    if allMyShapes and myMats:
        for shape in allMyShapes:
            myMat = random.choice(myMats)
            mc.select(shape)
            mc.hyperShade(assign=myMat)
            mySGs = mc.listConnections('%s.outColor' % myMat)
            if mySGs:
                numSg = len(mySGs)
                if numSg > 1:
                    i = 0
                    for mySG in mySGs:
                        if mySG.find('%s' % myMat):
                            mc.sets(e=True, forceElement=mySG)
                            i = 1
                            break
                    if i == 0:
                        mc.sets(e=True, forceElement=mySGs[0])
                elif numSg == 1:
                    mc.sets(e=True, forceElement=mySGs[0])
    else:
        mc.confirmDialog(title=u'错误:', message=u'Objects组或Shaders组为空', button=['OK'], defaultButton='Yes', dismissString='No')

