# -*- coding: utf-8 -*-
__author__ = 'zhongwzh'
import maya.cmds as mc
import maya.mel as mm


def SetUnlockCameras_zwz(MyCamera, value):
    mc.setAttr('%s.tx' % MyCamera, lock=value)
    mc.setAttr('%s.ty' % MyCamera, lock=value)
    mc.setAttr('%s.tz' % MyCamera, lock=value)
    mc.setAttr('%s.rx' % MyCamera, lock=value)
    mc.setAttr('%s.ry' % MyCamera, lock=value)
    mc.setAttr('%s.rz' % MyCamera, lock=value)


def FYXBModifyCameras_zwz():
    mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
    for i in range(1, 20):
        try:
            tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
        except:
            pass
        else:
            if tmp:
                activePlane = 'modelPanel%d' % i
    myStartFrameV = mc.getAttr("defaultRenderGlobals.startFrame")
    myEndFrameV = mc.getAttr("defaultRenderGlobals.endFrame")
    myCurves = mc.ls(type="nurbsCurve")
    myYeyaShapes = []
    myYeyaTras = []
    tmp = ''
    for each in myCurves:
        if each.find("yeyaShape") >= 0:
            myYeyaShapes.append(each)
    if myYeyaShapes:
        for each in myYeyaShapes:
            try:
                tmp = mc.listRelatives(each, p=True)
            except:
                continue
            if tmp[0].find("yeya") >= 0:
                try:
                    temp = mc.listRelatives(tmp[0], p=True)
                except:
                    continue
                else:
                    if temp[0].find('Master') >= 0:
                        myYeyaTras.append(tmp[0])
    if len(myYeyaTras) == 1:
        MyObject = myYeyaTras[0]
        myYeyaFName = mc.ls(MyObject, ap=True, l=True)[0]
        myYeyaG = myYeyaFName.split('|')[1]
        mc.select(myYeyaG)
        mm.eval("SelectIsolate;")
        myCamG = mc.ls(myYeyaG, dag=True, tr=True)
        flag = 0
        rightSemG = ''
        for each in myCamG:
            if mc.nodeType(each) == 'transform':
                if each.find('semiRing_Cam_Grp') >= 0:
                    if each.find('|') < 0:
                        flag = flag + 1
                        rightSemG = each
        if flag == 1:
            mc.select(cl=True)
            mc.select(rightSemG)
            SetUnlockCameras_zwz(rightSemG, False)
            mc.bakeResults(rightSemG, t=(myStartFrameV, myEndFrameV), sm=True, at=['tx', 'ty', 'tz', 'rx', 'ry', 'rz'], sb=True, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, cp=False, s=True)
            SetUnlockCameras_zwz(rightSemG, True)
            mysemRingC = mc.listRelatives(rightSemG, c=True, f=True)
            for peach in mysemRingC:
                try:
                    tmp = mc.nodeType(peach)
                except:
                    pass
                else:
                    if tmp:
                        if tmp == 'pointConstraint' or tmp == 'orientConstraint':
                            mc.delete(peach)

            mc.select(cl=True)
            mc.select(MyObject)
            SetUnlockCameras_zwz(MyObject, False)
            mc.bakeResults(MyObject, t=(myStartFrameV, myEndFrameV), sm=True, at=['rx', 'ry', 'rz'], sb=True, dic=True, pok=True, sac=False, ral=False, bol=False, mr=True, cp=False, s=True)
            SetUnlockCameras_zwz(MyObject, True)
            mc.rename(myYeyaG, '%s_baked' % myYeyaG)
            mc.isolateSelect(activePlane, state=False)
            mc.confirmDialog(title=u'温馨提示：', message=u'摄像机backed成功！\n摄像机大组名字改为%s_baked' % myYeyaG, button=['OK'], defaultButton='Yes', dismissString='No')
        elif flag > 1:
            mc.confirmDialog(title=u'温馨提示：', message=u'创建失败！\n相应的“semiRing_Cam_Grp”个数太多！', button=['OK'], defaultButton='Yes', dismissString='No')
            return
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'创建失败！\n相应的“semiRing_Cam_Grp”找不到！\n请确认该场是否要Baked摄像机', button=['OK'], defaultButton='Yes', dismissString='No')
            return
    elif len(myYeyaTras) >= 2:
        mc.confirmDialog(title=u'温馨提示：', message=u'创建失败！\n文件中有多个摄像组！', button=['OK'], defaultButton='Yes', dismissString='No')
    else:
        mc.confirmDialog(title=u'温馨提示：', message=u'创建失败！\n文件中没有相应的摄像机组，请导入个正确的！', button=['OK'], defaultButton='Yes', dismissString='No')
