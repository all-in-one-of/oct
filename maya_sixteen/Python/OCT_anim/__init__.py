#!/usr/bin/env python
# coding: utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import threading
import maya.cmds as mc
import maya.mel as mel
import sys

import OCT_ChangeXxbOldCameras_zwz
import OCT_FYXBModifyCameras_zwz
import OCT_CreateGeometryCache_zwz
import OCT_exp_loc_zxy
import OCT_MotionCapture
import OCT_fix_animation_LXJ


from CacheFile_Tools_zwz import CacheFile_Tools

def kljz_dst():
    import DisplacementToScale
    DisplacementToScale.displacementToScale()

def Bake_Frame():
    import BakeFrame
    BakeFrame.bake_Frame()

def resetHeadsUpCurrentFrame():
    if not mc.headsUpDisplay('HUDCurrentFrame', ex = True):
        mel.eval('headsUpDisplay -section 9 -block 6 -blockSize "small" -label (uiRes("m_initHUD.kHUDCurrentFrameLabel")) -labelWidth 135 -dataWidth 75 -labelFontSize "small" -dataFontSize "small" -allowOverlap true -preset "currentFrame" -vis (`optionVar -q currentFrameVisibility`) HUDCurrentFrame;')

def studionLibrarys():
	sys.path.append(r'\\octvision.com\cg\Tech\maya_sixteen\Python\OCT_anim')
	import studiolibrary
	studiolibrary.main() 

def ChangeReference():
    import OCT_ChangeRefereceFile
    i = OCT_ChangeRefereceFile.ChangeReference()
    i.changeRef_UI()

def exportAnimData():
    import OCT_ExportAnimData
    i = OCT_ExportAnimData.ExportAnimData()
    i.ListAnimDataObj_UI()

def importAnimData():
    import OCT_ImportAnimData
    i = OCT_ImportAnimData.ImportAnimData()
    i.ListAnimImportObj_UI()


def miarmyGroup():
    from OCT_MiarmyGroup_YH import OCT_MiarmyGroup
    if mc.window("MiarmyGroupUI", exists=True):
        mc.deleteUI("MiarmyGroupUI", window=True)
    dialog = OCT_MiarmyGroup()
    t = threading.Thread(None, dialog.show())
    t.start()
    
def miaryAnimCopy():
    import OCT_MiaryCopyAnim_YH
    i = OCT_MiaryCopyAnim_YH.OCT_MiaryCopyAnim()
    i.miaryCopyAnim()

def run_CacheFile_Tools_zwz():
    if mc.window("cacheDialog", exists=True):
        mc.deleteUI("cacheDialog", window=True)
    dialog = CacheFile_Tools()
    t = threading.Thread(None, dialog.show())
    t.start()

def FaceTools():
    import OCT_FaceImportExport_YH
    i = OCT_FaceImportExport_YH.importExportTool()
    i.importExport()


def copyReference():
    from OCT_CopyReference_YH import CopyReferenceTool
    if mc.window("CopyReferenceDialog", exists=True):
        mc.deleteUI("CopyReferenceDialog", window=True)
    dialog = CopyReferenceTool()
    t = threading.Thread(None, dialog.show())
    t.start()
	# import OCT_CopyReference_YH
	# i=OCT_CopyReference_YH.copyReferenceTool()
	# i.copyReferenceUI()

def createAnimCurve():
    import OCT_CreateAnimCrvere
    i=OCT_CreateAnimCrvere.createCvere()
    i.createCvereUI()

def OCT_delMaterialAndFace():
    allMeshs = mc.ls(long=True,type="mesh",noIntermediate=True)

    createLambertShader = mc.shadingNode("lambert",asShader=True)
    createLambertShaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = "%sSG"%createLambertShader)
    mc.connectAttr("%s.outColor"%createLambertShader, "%s.surfaceShader"%createLambertShaderSG, f=True)
    
    mc.sets(allMeshs, forceElement = createLambertShaderSG,e=True)
    mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')

def OCT_deleteKeyFrames():
    import OCT_deleteKeyFrame
    i=OCT_deleteKeyFrame.deletekeyFrame()
    i.deleteKey()

def OCT_abcSglEdition():
    import OCT_Pipeline.ABC_Pipeline.ABC_SingleEdition as abcs
    reload(abcs)
    if (mc.window('abcS_win', exists=True, q=True)):
        mc.deleteUI('abcS_win')
    inWin = abcs.ABC_SingleWin()
    inWin.show()
    inWin.raise_()

#!/usr/bin/env python
# coding=utf-8
import maya.cmds as mc
import maya.mel as mm
def OCT_BakeCamera():
    allSelCamera = mc.ls(selection=True)
    find = False
    if not allSelCamera:
        mc.confirmDialog(title='Confirm', message=u'请选择摄像机')
        return
    for obj in allSelCamera:
        buf = mc.listRelatives(obj, fullPath = True, children = True)
        if buf:
            if mc.nodeType(buf[0]) == "camera" or mc.nodeType(buf[0]) == "stereoRigCamera":
                find = True
            else:
                find = False
                break
        else:
            find = False
            break

    if not find:
        mc.confirmDialog(title='Confirm', message=u'请选择摄像机')
        return

    timeLine = mc.playbackOptions(q=True,min=True)
    timeLine1 = mc.playbackOptions(q=True,max=True)

    for baked in allSelCamera:
        mc.select(d= True)
        mc.select(baked, r = True)
        #复制相机
        CopyCamera = mc.duplicate(rr = True)
        #改名
        selCamreaName = baked + baked
        mc.rename(baked,selCamreaName)
        mc.rename(CopyCamera[0], baked)
        mc.parent(baked, w = True)

        attrs = mc.listAttr(baked, keyable = True, locked = True)
        if attrs:
            for attr in attrs:
                mc.setAttr("%s.%s"%(baked,attr), l = False)

        buf = mc.listRelatives(baked, fullPath = True, children = True)
        attrShapes = mc.listAttr(buf[0], keyable = True, locked = True)
        if attrShapes:
            for at in attrShapes:
                mc.setAttr("%s.%s"%(baked,at), l = False)


        mc.parentConstraint(selCamreaName,baked,w= 1)
        mc.bakeResults(baked, simulation = True, t=(timeLine,timeLine1), sampleBy= True, disableImplicitControl = True,preserveOutsideKeys = True, sparseAnimCurveBake = False,removeBakedAttributeFromLayer=False, bakeOnOverrideLayer = False,minimizeRotation = True,controlPoints= False,shape = True)
        
        oldShapes = mc.listRelatives(selCamreaName, fullPath = True, children = True)

        attrs = ["horizontalFilmOffset", "verticalFilmOffset", "filmFitOffset", "focalLength"]
        
        focal = mc.listConnections("%s.focalLength" %buf[0],s= True,plugs= True)
        if focal:
            mc.disconnectAttr(focal[0], "%s.focalLength" % buf[0])
            
        for i in range(int(timeLine), int(timeLine1)+1):
            mc.currentTime(i)
            for attr in attrs:
                num = mc.getAttr("%s.%s"%(oldShapes[0], attr))
                mc.setKeyframe(buf[0], v = num, at = attr, t = i)
                
        # nameShapes = mc.listRelatives(baked,c= True)  
        # for i in range(int(timeLine), int(timeLine1)+1):
        #     mc.setKeyframe(nameShapes,at = "filmFitOffset",t = i)
        #     mc.setKeyframe(nameShapes,at = "horizontalFilmOffset",t = i)
        #     mc.setKeyframe(nameShapes,at = "verticalFilmOffset",t = i)
        # setKeyframe -v $translate[0] -at scaleX -t $keyframe[0] $child;

#OCT_BakeCamera()