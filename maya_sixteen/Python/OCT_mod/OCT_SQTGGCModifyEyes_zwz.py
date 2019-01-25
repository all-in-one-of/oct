# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os


#查找函数
def findMyHideEyes(eyeName, eyeGroup, allTrans):
    for each in allTrans:
        if each.find(eyeName) >= 0:
            if not each.find(eyeName+'_') >= 0:
                eachG = mc.listRelatives(each, p=True)[0]
                if eachG.find(eyeGroup) >= 0:
                    return each
                else:
                    mc.confirmDialog(message=u"找不到%s" % eyeName, button="OK")
                    return False


#创建材质函数
def CreateEyeLam(colorFile, IncFile, EyeLamName):
    errorV = 0
    if not mc.objExists(EyeLamName):
        myEyeLam = mc.shadingNode('lambert', asShader=True, n=EyeLamName)
        myEyeLam_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=myEyeLam+'_SG')
        mc.connectAttr('%s.outColor' % myEyeLam, '%s.surfaceShader' % myEyeLam_SG, force=True)
        myRamp = mm.eval('createRenderNodeCB -as2DTexture "" ramp "";')
        myColorFile = mm.eval('createRenderNodeCB -as2DTexture "" file "";')
        mc.setAttr("%s.fileTextureName" % myColorFile, IncFile, type="string")
        mc.setAttr("%s.colorGain" % myColorFile, 0.85949999094009399, 0.85949999094009399, 0.85949999094009399, type="double3")
        mc.connectAttr("%s.outColor" % myColorFile, "%s.incandescence" % myEyeLam, f=True)
        myIncFile = mm.eval('createRenderNodeCB -as2DTexture "" file "";')
        mc.setAttr("%s.fileTextureName" % myIncFile, colorFile, type="string")
        mc.connectAttr("%s.outColor" % myIncFile, "%s.color" % myEyeLam, f=True)
        mc.removeMultiInstance('%s.colorEntryList[2]' % myRamp, b=True)
        mc.setAttr('%s.colorEntryList[1].position' % myRamp, 0.7149999737739563)
        mc.setAttr('%s.colorEntryList[0].position' % myRamp, 0.46500000357627869)
        mc.setAttr('%s.colorEntryList[1].color' % myRamp, 0.0056199943646788597, 0.25346201658248901, 0.28099998831748962, type='double3')
        mc.setAttr('%s.colorEntryList[0].color' % myRamp, 1.0, 1.0, 1.0, type='double3')
        mc.setAttr('%s.interpolation' % myRamp, 6)
        mc.connectAttr("%s.outColor" % myRamp, "%s.colorGain" % myIncFile, f=True)
        myfilePath1 = mc.getAttr('%s.fileTextureName' % myColorFile)
        myfilePath2 = mc.getAttr('%s.fileTextureName' % myIncFile)
        if (not os.path.isfile(r'%s' % myfilePath1)) or (not os.path.isfile(r'%s' % myfilePath2)):
            errorV = 1
    retrunV = [EyeLamName, errorV]
    return retrunV


def SQTGGCModifyEyes_zwz():
    #隐藏不需要的高光片
    allTrans = mc.ls(transforms=True, sn=True)
    if allTrans:
        allMyEyes = []
        allMyEyes.append(findMyHideEyes('eyeBall_03_L', 'eye_L', allTrans))
        allMyEyes.append(findMyHideEyes('eyeBall_04_L', 'eye_L', allTrans))
        allMyEyes.append(findMyHideEyes('eyeBall_03_R', 'eye_R', allTrans))
        allMyEyes.append(findMyHideEyes('eyeBall_04_R', 'eye_R', allTrans))
        mc.select(allMyEyes)
        myLayerName = mc.createDisplayLayer(name='Hidden Eyes', num=1, nr=1)
        mc.setAttr("%s.visibility" % myLayerName, 0)
        #赋予新的材质
        retrunV_L = CreateEyeLam('sourceimages\DH\SQTGGC_TGNH_eye_color_02.jpg', 'sourceimages\DH\SQTGGC_TGNH_eye_in_02.jpg', 'myEyeLam_L')
        retrunV_R = CreateEyeLam('sourceimages\DH\SQTGGC_TGNH_eye_color_01.jpg', 'sourceimages\DH\SQTGGC_TGNH_eye_in_01.jpg', 'myEyeLam_R')
        myEyeLam_L = retrunV_L[0]
        myEyeLam_R = retrunV_R[0]
        myeyeBall_L = findMyHideEyes('eyeBall_01_L', 'eye_L', allTrans)
        myeyeBall_R = findMyHideEyes('eyeBall_01_R', 'eye_R', allTrans)
        mc.select(myeyeBall_L)
        mc.hyperShade(assign=myEyeLam_L)
        mc.select(myeyeBall_R)
        mc.hyperShade(assign=myEyeLam_R)
        mc.select(cl=True)
        #检查本工程目录是否有此素材
        if retrunV_L[1] or retrunV_R[1]:
            mc.confirmDialog(message=u"修改完毕！\n但在指定的目录找不到贴图，请手动指定！", button="OK")
        else:
            mc.confirmDialog(message=u"修改完毕！\n并且找到了贴图！！！！！", button="OK")
