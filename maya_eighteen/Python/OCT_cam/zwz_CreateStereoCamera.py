#!/usr/bin/env python
# coding=utf-8
import maya.cmds as mc
import maya.mel as mm


#锁上位移，旋转，缩放属性
def LockObjectTRS(Object, BoolV):
    mc.setAttr('%s.tx' % Object, l=BoolV)
    mc.setAttr('%s.ty' % Object, l=BoolV)
    mc.setAttr('%s.tz' % Object, l=BoolV)
    mc.setAttr('%s.rx' % Object, l=BoolV)
    mc.setAttr('%s.ry' % Object, l=BoolV)
    mc.setAttr('%s.rz' % Object, l=BoolV)
    mc.setAttr('%s.sx' % Object, l=BoolV)
    mc.setAttr('%s.sy' % Object, l=BoolV)
    mc.setAttr('%s.sz' % Object, l=BoolV)


#隐藏位移，旋转，缩放属性
def HideObjectAttr(Object, BoolV):
    mc.setAttr('%s.tx' % Object, k=BoolV)
    mc.setAttr('%s.ty' % Object, k=BoolV)
    mc.setAttr('%s.tz' % Object, k=BoolV)
    mc.setAttr('%s.rx' % Object, k=BoolV)
    mc.setAttr('%s.ry' % Object, k=BoolV)
    mc.setAttr('%s.rz' % Object, k=BoolV)
    mc.setAttr('%s.sx' % Object, k=BoolV)
    mc.setAttr('%s.sy' % Object, k=BoolV)
    mc.setAttr('%s.sz' % Object, k=BoolV)


#创建摄像机
def CreatMyCamera_zwz(nameV, rotV):
    myCamera = mc.camera(n=nameV, rot=rotV, fcp=1000000, hfa=1, vfa=1, fl=21.997, ff='fill')
    LockObjectTRS(myCamera[0], True)
    mc.setAttr('%s.hfa' % myCamera[1], l=True)
    mc.setAttr('%s.vfa' % myCamera[1], l=True)
    mc.setAttr('%s.fl' % myCamera[1], l=True)
    mc.setAttr('%s.lsr' % myCamera[1], l=True)
    mc.setAttr('%s.fs' % myCamera[1], l=True)
    mc.setAttr('%s.fd' % myCamera[1], l=True)
    mc.setAttr('%s.sa' % myCamera[1], l=True)
    mc.setAttr('%s.coi' % myCamera[1], l=True)
    tmp = mc.rename(myCamera[0], nameV)
    tmpShape = mc.listRelatives(tmp, s=True)
    myCamera = [tmp, tmpShape]
    return myCamera


def zwz_CreateStereoCamera_menu():
   #def zwz_CreateStereoCamera_menu():
    #左眼摄像机
    LMCamera = CreatMyCamera_zwz('L_M', [0, 0, 0])
    LLCamera = CreatMyCamera_zwz('L_L', [0, 60, 0])
    LRCamera = CreatMyCamera_zwz('L_R', [0, -60, 0])
    #右眼摄像机
    RMCamera = CreatMyCamera_zwz('R_M', [0, 0, 0])
    RLCamera = CreatMyCamera_zwz('R_L', [0, 60, 0])
    RRCamera = CreatMyCamera_zwz('R_R', [0, -60, 0])
    #立体摄像机
    mm.eval('loadPlugin -qt "stereoCamera";')
    from maya.app.stereo import stereoCameraRig
    myStereo = stereoCameraRig.createStereoCameraRig(rigName='StereoCamera')
    CenterShape = mc.listRelatives(myStereo[0], s=True, pa=True)
    mc.setAttr("%s.horizontalFilmAperture" % CenterShape[0], 1)
    mc.setAttr("%s.verticalFilmAperture" % CenterShape[0], 1)
    mc.setAttr("%s.focalLength" % CenterShape[0], 21.997)
    mc.setAttr("%s.interaxialSeparation" % CenterShape[0], 0.068)
    mc.setAttr("%s.farClipPlane" % CenterShape[0], 1000000)
    mc.setAttr("%s.stereo" % CenterShape[0], 1)
    mc.setAttr("%s.zeroParallax" % CenterShape[0], 5)
    mc.setAttr("%s.translate" % myStereo[1], l=False)
    mc.setAttr("%s.rotate" % myStereo[1], l=False)
    mc.setAttr("%s.translate" % myStereo[2], l=False)
    mc.setAttr("%s.rotate" % myStereo[2], l=False)
    mc.disconnectAttr('%s.stereoLeftOffset' % myStereo[0], '%s.translateX' % myStereo[1])
    mc.disconnectAttr('%s.stereoLeftAngle' % myStereo[0], '%s.rotateY' % myStereo[1])
    mc.disconnectAttr('%s.stereoRightOffset' % myStereo[0], '%s.translateX' % myStereo[2])
    mc.disconnectAttr('%s.stereoRightAngle' % myStereo[0], '%s.rotateY' % myStereo[2])
    mc.pointConstraint(LMCamera[0], myStereo[1], w=1)
    mc.orientConstraint(LMCamera[0], myStereo[1], w=1)
    mc.pointConstraint(RMCamera[0], myStereo[2], w=1)
    mc.orientConstraint(RMCamera[0], myStereo[2], w=1)
    LockObjectTRS(myStereo[0], True)
    LGroup = mc.group(LMCamera[0], LLCamera[0], LRCamera[0], n='L_Cameras')
    LGroup = mc.ls(LGroup, l=True)[0]
    mc.xform(LGroup, t=[-0.034, 0, 0])
    LockObjectTRS(LGroup, True)
    RGroup = mc.group(RMCamera[0], RLCamera[0], RRCamera[0], n='R_Cameras', absolute=True)
    RGroup = mc.ls(RGroup, l=True)[0]
    mc.xform(RGroup, t=[0.034, 0, 0])
    LockObjectTRS(RGroup, True)
    myGroup = mc.group(LGroup, RGroup, myStereo[0], n='Cam_Rig')
    mc.setAttr('%s.visibility' % myGroup, 0)
    #测试摄像机
    TMCamera = CreatMyCamera_zwz('Test_M_T', [0, 0, 0])
    LockObjectTRS(TMCamera[0], False)
    mc.pointConstraint(TMCamera[0], myGroup, w=1)
    mc.orientConstraint(TMCamera[0], myGroup, w=1)
    mc.scaleConstraint(TMCamera[0], myGroup, w=1)
    LockObjectTRS(myGroup, True)
    TLCamera = CreatMyCamera_zwz('Test_L', [0, 60, 0])
    mc.setAttr('%s.template' % TLCamera[1][0], 1)
    TRCamera = CreatMyCamera_zwz('Test_R', [0, -60, 0])
    mc.setAttr('%s.template' % TRCamera[1][0], 1)
    mc.parent(TLCamera[0], TMCamera[0])
    mc.parent(TRCamera[0], TMCamera[0])
    TMCamera[1] = mc.rename(TMCamera[1], 'Test_M')
    myLocator = mc.spaceLocator(n='Constrain_for_animation', p=(0, 0, 0))
    mc.xform(myLocator, s=[10, 10, 10])
    mc.pointConstraint(TMCamera[0], myLocator, w=1)
    mc.orientConstraint(TMCamera[0], myLocator, w=1)
    testGroup = mc.group(TMCamera, myLocator, n='Test_Cam_Rig')
    LockObjectTRS(testGroup, False)
    HideObjectAttr(testGroup, False)
    LockObjectTRS(myLocator[0], True)
