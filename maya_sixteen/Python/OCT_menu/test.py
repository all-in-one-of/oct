# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import sys
import string
import os


def OCT_RenderLayers_Menum_zwz():
    if mc.windowPref('OCT_RenderLayers_zwz', exists=True):
        mc.windowPref('OCT_RenderLayers_zwz', remove=True)
    if mc.window('OCT_RenderLayers_zwz', exists=True):
        mc.deleteUI('OCT_RenderLayers_zwz', window=True)
    mc.window("OCT_RenderLayers_zwz", title="OCT_RenderLayers_zwz", menuBar=True, widthHeight=(330, 150), resizeToFitChildren=True, sizeable=True)
    mc.columnLayout('mainmenu', adjustableColumn=True)
    mc.frameLayout('oneFL', label='Layers', labelAlign='top', borderStyle='etchedOut')
    mc.rowColumnLayout('Xml_First_Com', numberOfColumns=7, columnWidth=[(1, 55), (2, 50), (3, 50), (4, 40), (5, 40), (6, 50), (7, 40)], h=33)
    mc.button(label='Mr_Occ', w=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignMrOcc_zwz()', backgroundColor=(0.9, 0.9, 0.9))
    mc.button(label='Depth', w=50, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWDepth_zwz()', backgroundColor=(0.9, 0.9, 0.9))
    mc.button(label='Diffuse', w=50, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignMRDiffuse_zwz()', backgroundColor=(0.613, 0.613, 0.613))
    # mc.button(label='Lgt', w=40, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignMRLgt_zwz()', backgroundColor=(0.613,0.613,0.613))
    mc.button(label='Amb', w=40, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWAmb_zwz()', backgroundColor=(0.780, 0.780, 0.780))
    # mc.button(label='Lgt2_NS/R', w=70, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignMRLgt2_zwz()', backgroundColor=(0.613,0.613,0.613))
    mc.button(label='RIM', width=40, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignRimSur_zwz()', backgroundColor=(0.613, 0.613, 0.613))
    mc.button(label='Ramp', width=40, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignProjectRamp()', backgroundColor=(0.9, 0.3, 0.3))
    mc.setParent('mainmenu')
    mc.frameLayout('secondFL', label=u'以下层都带置换，透明等 注：物体赋新RGBA材质后尽量不重复选择', labelAlign='top', borderStyle='etchedOut')
    mc.columnLayout('Xml_RGBA___Tran', adjustableColumn=True)
    mc.rowLayout('txRow', numberOfColumns=9, columnAttach6=['left', 'left', 'left', 'left', 'left', 'left'], columnWidth6=[55, 55, 55, 55, 55, 55], columnOffset6 =[2, 2, 2, 2, 2, 2], h=33)
    mc.button(label='R', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(0)', backgroundColor=(0.7, 0,  0))
    mc.button(label='G', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(1)', backgroundColor=(0, 0.7, 0))
    mc.button(label='B', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(2)', backgroundColor=(0, 0, 0.7))
    mc.button(label='Y', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(5)', backgroundColor=(0.7, 0.7, 0))
    mc.button(label='C', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(6)', backgroundColor=(0, 0.7, 0.7))
    mc.button(label='P', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(7)', backgroundColor=(0.7, 0, 0.7))
    mc.button(label='A', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_Tran_zwz(3)', backgroundColor=(0.8, 0.8, 0.8))
    mc.button(label='Lambert', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignLamLam_zwz()', backgroundColor=(0.6, 0.6, 0.6))
    mc.button(label='Matte', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWMatte_Tran_zwz(4)', backgroundColor=(0.3, 0.3, 0.3))
    mc.setParent('mainmenu')
    mc.frameLayout('thirdFL', label=u'不带透明的RGBA、遮罩Matte', labelAlign='top', borderStyle='etchedOut')
    mc.columnLayout('Xml_RGBA', adjustableColumn=True)
    mc.rowLayout('txRow', numberOfColumns=8, columnAttach5=['left', 'left', 'left', 'left', 'left'], columnWidth5=[55, 55, 55, 55, 55], columnOffset5=[2, 2, 2, 2, 2], h=33)
    mc.button(label='R', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(0)', backgroundColor=(0.7, 0, 0))
    mc.button(label='G', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(1)', backgroundColor=(0, 0.7, 0))
    mc.button(label='B', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(2)', backgroundColor=(0, 0, 0.7))
    mc.button(label='Y', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(5)', backgroundColor=(0.7, 0.7, 0))
    mc.button(label='C', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(6)', backgroundColor=(0, 0.7, 0.7))
    mc.button(label='P', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(7)', backgroundColor=(0.7, 0, 0.7))
    mc.button(label='A', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWRGBA_zwz(3)', backgroundColor=(0.8, 0.8, 0.8))
    mc.button(label='Matte', width=55, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignSWMatte_zwz(4)', backgroundColor=(0.3, 0.3, 0.3))

    mc.setParent('mainmenu')
    mc.frameLayout('fourthFL', label='Arnold Layers', labelAlign='top', borderStyle='etchedOut')
    mc.rowLayout('ArnoldRow', numberOfColumns=4, columnAttach4=['left', 'left', 'left', 'left'], columnWidth4=[30, 60, 35, 35], columnOffset4=[1, 1, 1, 1], h=33)
    sss_B = mc.button(label='SSS', w=50, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignArnold3SSd_zwz()', backgroundColor=(0.918, 0.774, 0.774))
    SSS_Matte_B = mc.button(label='SSS_Matte', w=60, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignArnold3SMatteSd_zwz()', backgroundColor=(0.341, 0.341, 0.341))
    OCC_B = mc.button(label='OCC', w=50, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignArnoldOCC_zwz()', backgroundColor=(0.780, 0.780, 0.780))

    mc.setParent('mainmenu')
    mc.frameLayout('FiveFL', label='VRay Layers', labelAlign='top', borderStyle='etchedOut')
    mc.rowLayout('VRayRow', numberOfColumns=4, columnAttach4=['left', 'left', 'left', 'left'], columnWidth4=[60, 60, 35, 35], columnOffset4=[1, 1, 1, 1], h=33)
    mc.button(label='ColorAG', w=60, h=30, command='OCT_render.OCT_RenderLayers_zwz.AssignVRayGamma_zwz()', backgroundColor=(0.5, 0.774, 0.774))
    mc.button(label='VrayToLambert', w=90, h=30, command='OCT_render.OCT_RenderLayers_zwz.allVRayMatToLambert()', backgroundColor=(0.5, 0.774, 0.3))


    mc.setParent('mainmenu')
    mc.rowColumnLayout( numberOfColumns=2, columnAlign=(1, 'right'), columnAttach=(2, 'both', 0), columnWidth=(2, 150) )
    mc.text(label='Diffuse')
    mc.separator(style='single')
    mc.setParent('mainmenu')
    mc.rowLayout('GammerRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[150, 50, 50], columnOffset3=[5, 2, 2])
    mc.text(label='Change GammaCorrect Value:')
    mc.textField('GCValue', text='0.454', width=70, alwaysInvokeEnterCommandOnReturn=True)
    mc.button(label='Change', width=60, command='OCT_render.OCT_RenderLayers_zwz.ChangeGammaCorrectValue_zwz(1)', backgroundColor=(0.9, 0.5, 0))
    mc.setParent('mainmenu')
    
    mc.rowColumnLayout( numberOfColumns=2, columnAlign=(1, 'right'), columnAttach=(2, 'both', 0), columnWidth=(2, 150) )
    mc.text(label='RIM')
    mc.separator(style='single')
    mc.setParent('mainmenu')
    mc.floatSliderGrp('RimRamp0', label='Ramp`s Value0', field=True, minValue=0, maxValue=1, fieldMinValue=0, fieldMaxValue=1, cc="OCT_render.OCT_RenderLayers_zwz.changeRimRamp('RimRamp0', 'color', 'colorEntryList[0].position')", pre=3, cw3=[75, 50, 130], value=0)
    mc.floatSliderGrp('RimRamp1', label='Ramp`s Value1', field=True, minValue=0, maxValue=1, fieldMinValue=0, fieldMaxValue=1, cc="OCT_render.OCT_RenderLayers_zwz.changeRimRamp('RimRamp1', 'color', 'colorEntryList[2].position')", pre=3, cw3=[75, 50, 130], value=1)
    mc.floatSliderGrp('RimBump', label='Bump`s Depth', field=True, minValue=0, maxValue=20, fieldMinValue=-100, fieldMaxValue=100, cc="OCT_render.OCT_RenderLayers_zwz.changeRimRamp('RimBump', 'normalCamera', 'bumpDepth')", pre=3, cw3=[72, 50, 130], value=1)
    mc.setParent('mainmenu')
    
    mc.rowColumnLayout( numberOfColumns=2, columnAlign=(1, 'right'), columnAttach=(2, 'both', 0), columnWidth=(2, 150) )
    mc.text(label='Vray')
    mc.separator(style='single')
    mc.setParent('mainmenu')
    mc.rowLayout('VRGammerRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[180, 50, 50], columnOffset3=[5, 2, 2])
    mc.text(label='Change VRayGammaCorrect Value:')
    mc.textField('GCVRayValue', text='2.2', width=70, alwaysInvokeEnterCommandOnReturn=True)
    mc.button(label='VrayChange', width=90, command='OCT_render.OCT_RenderLayers_zwz.ChangeGammaCorrectValue_zwz(2)', backgroundColor=(0.9, 0.5, 0))
    mc.setParent('mainmenu')
    mc.rowLayout('VrayDelGammaRow', numberOfColumns=4, columnAttach4=['left', 'left', 'left', 'left'], columnWidth4=[168, 53, 65, 1], columnOffset4=[5, 2, 2, 2])
    mc.text(label=u'删除Vray设置的所有gamma节点')
    mc.button(label='Del AlL', width=93, command='OCT_render.OCT_RenderLayers_zwz.DelAllMyGamma_zwz()', backgroundColor=(0.5, 0.5, 0.5))
    mc.rowLayout('OpaqueRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[150, 70, 70], columnOffset3=[5, 2, 2])
    mc.setParent('mainmenu')
    mc.rowLayout('VrayMeshtoBox', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[200, 70, 70], columnOffset3=[5, 2, 2])
    mc.text(label='Turn On\off VrayMesh Bounding Box:')
    mc.button(label='On', width=60, command='OCT_render.OCT_RenderLayers_zwz.setAllVrayMeshtoBox(True)', backgroundColor=(0.342, 1, 0.449))
    mc.button(label='Off', width=60, command='OCT_render.OCT_RenderLayers_zwz.setAllVrayMeshtoBox(False)', backgroundColor=(1.000, 0.101, 0.101))
    mc.setParent('mainmenu')
    mc.rowLayout('VrayOpenLight_r', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[265, 70, 70], columnOffset3=[5, 2, 2])
    mc.text(label=u'打开/关闭 所选 默认灯光或Vray灯光的默认灯光链接')
    mc.button(label='On', width=60, command='OCT_render.OCT_RenderLayers_zwz.LightCondefaultLight(True)', backgroundColor=(0.342, 1, 0.449))
    mc.button(label='Off', width=60, command='OCT_render.OCT_RenderLayers_zwz.LightCondefaultLight(False)', backgroundColor=(1.000, 0.101, 0.101))
    mc.setParent('mainmenu')
    
    mc.rowColumnLayout( numberOfColumns=2, columnAlign=(1, 'right'), columnAttach=(2, 'both', 0), columnWidth=(2, 150) )
    mc.text(label='Arnold')
    mc.separator(style='single')
    mc.setParent('mainmenu')
    mc.rowLayout('OpaqueRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[150, 70, 70], columnOffset3=[5, 2, 2])
    mc.text(label='Change Object`s Opaque:')
    mc.button(label='Open', width=60, command='OCT_render.OCT_RenderLayers_zwz.ChangeObjectOpaque_zwz(1)', backgroundColor=(0.342, 1, 0.449))
    mc.button(label='Close', width=60, command='OCT_render.OCT_RenderLayers_zwz.ChangeObjectOpaque_zwz(0)', backgroundColor=(1.000, 0.101, 0.101))
    mc.setParent('mainmenu')
    
    mc.rowColumnLayout( numberOfColumns=2, columnAlign=(1, 'right'), columnAttach=(2, 'both', 0), columnWidth=(2, 150) )
    mc.text(label='Other')
    mc.separator(style='single')
    mc.setParent('mainmenu')
    mc.rowLayout('MatteRow', numberOfColumns=4, columnAttach4=['left', 'left', 'left', 'left'], columnWidth4=[168, 53, 65, 1], columnOffset4=[5, 2, 2, 2])
    mc.text(label=u'改变所选材质球的OpacityMode:')
    mc.button(label='BlackHole', width=53, command='OCT_render.OCT_RenderLayers_zwz.OCT_ChangeShadeOpacityMode_zwz(0)', backgroundColor=(0.5, 0.5, 0.5))
    mc.button(label='OpacityGain', width=65, command='OCT_render.OCT_RenderLayers_zwz.OCT_ChangeShadeOpacityMode_zwz(2)', backgroundColor=(0.9, 0.9, 0.9))
    mc.button(label=u'选择所有材质球', width=80, command='OCT_render.OCT_RenderLayers_zwz.OCT_ChangeShadeOpacityMode_zwz(3)', backgroundColor=(0.2, 0.9, 0.2))
    mc.setParent('mainmenu')
    mc.rowLayout('ObjectBoundBoxRow', numberOfColumns=2, columnAttach2=['left', 'left'], columnWidth2=[190, 53], columnOffset2=[5, 2])
    mc.text(label=u'Iso bBox:')
    mc.button("ShowObjectR", label='Off', ann='off', width=100, command='OCT_render.OCT_RenderLayers_zwz.isoBbox()', backgroundColor=(0.3,0.3,0.3))
    mc.setParent('mainmenu')
    mc.rowLayout('ObjectTextureRow', numberOfColumns=2, columnAttach2=['left', 'left'], columnWidth2=[190, 53], columnOffset2=[5, 2])
    mc.text(label=u'Iso Texture:')
    mc.button("ShowObjectT", label='Do It', width=100, command='OCT_render.OCT_RenderLayers_zwz.isoTextured()', backgroundColor=(0.3,0.3,0.3))

    mayaversions = mc.about(v=True)
    if mayaversions.find('2009') >= 0:
        mc.button(sss_B, e=True, en=0)
        mc.button(SSS_Matte_B, e=True, en=0)
        mc.button(OCC_B, e=True, en=0)
    mc.showWindow('OCT_RenderLayers_zwz')



def CreateMyArnold3SSd_zwz():
    if not mc.objExists('my3sArnoldaiSkin'):
        my3sArnoldaiSkin = mc.shadingNode('aiSkinSss',asShader =True, n ='my3sArnoldaiSkin')
        mc.setAttr("%s.diffuseWeight"%my3sArnoldaiSkin,1)
        mc.setAttr("%s.shallowScatterColor"%my3sArnoldaiSkin,1,1,1,type='double3')
        mc.setAttr("%s.shallowScatterWeight"%my3sArnoldaiSkin,0)
        mc.setAttr("%s.shallowScatterRadius"%my3sArnoldaiSkin,0.15)
        mc.setAttr("%s.midScatterColor"%my3sArnoldaiSkin,0.588235,0.588235,0.588235,type='double3')
        mc.setAttr("%s.midScatterWeight"%my3sArnoldaiSkin,0)
        mc.setAttr("%s.deepScatterColor"%my3sArnoldaiSkin,1,1,1,type='double3')
        mc.setAttr("%s.deepScatterRadius"%my3sArnoldaiSkin,0.5)
        mc.setAttr("%s.primaryReflectionColor"%my3sArnoldaiSkin,1,1,1,type='double3')
        mc.setAttr("%s.primaryReflectionWeight"%my3sArnoldaiSkin,0.5)
        mc.setAttr("%s.secondaryReflectionColor"%my3sArnoldaiSkin,0.917647,0.968627,1,type='double3')
        mc.setAttr("%s.secondaryReflectionWeight"%my3sArnoldaiSkin,0.3)
        mc.setAttr("%s.globalSssRadiusMultiplier"%my3sArnoldaiSkin,1)
        my3sArnoldaiSkin_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = my3sArnoldaiSkin+'_SG')
        mc.connectAttr(my3sArnoldaiSkin + '.outColor',my3sArnoldaiSkin_SG + '.surfaceShader',force=True)
    if not mc.objExists('my3sStandMatte'):
        my3sStandMatte = mc.shadingNode('aiStandard',asShader =True, n ='my3sStandMatte')
        my3sStandMatte_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = my3sStandMatte+'_SG')
        mc.connectAttr('%s.outColor'%my3sStandMatte,'%s.surfaceShader'%my3sStandMatte_SG,force=True)
        mc.setAttr('%s.color'%my3sStandMatte,0, 0,0)
        my3sStandMatteC = mc.duplicate(my3sStandMatte,upstreamNodes=1)[0]
        my3sStandMatteC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = my3sStandMatteC +'_SG')
        mc.connectAttr(my3sStandMatteC + '.outColor',my3sStandMatteC_SG + '.surfaceShader',force=True)
        mc.setAttr('%s.aiEnableMatte'%my3sStandMatteC,1)
    MyArnold3SSd=['my3sArnoldaiSkin', 'my3sStandMatte', 'my3sStandMatte_SG', 'my3sStandMatte1', 'my3sStandMatte1_SG']
    return MyArnold3SSd

def CreateMyArnoldOCCSd_zwz():
    if not mc.objExists('myArnoldOcc'):
        myArnoldOcc = mc.shadingNode('aiAmbientOcclusion',asShader =True, n ='myArnoldOcc')
        myArnoldOcc_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myArnoldOcc+'_SG')
        mc.connectAttr(myArnoldOcc + '.outColor',myArnoldOcc_SG + '.surfaceShader',force=True)
        mc.setAttr("%s.samples"%myArnoldOcc,5)
        myArnoldOccC = mc.duplicate(myArnoldOcc,upstreamNodes=1)[0]
        myArnoldOccC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myArnoldOccC +'_SG')
        mc.connectAttr(myArnoldOccC + '.outColor',myArnoldOccC_SG + '.surfaceShader',force=True)
    myArnoldOCCSd=['myArnoldOcc', 'myArnoldOcc_SG', 'myArnoldOcc1', 'myArnoldOcc1_SG', 'myArnoldOcc_SG']
    return myArnoldOCCSd

def CreateMyGammaCorrect_zwz():
    if not mc.objExists('MyGammaCorrect'):
        MyGammaCorrect = mc.shadingNode('gammaCorrect',asUtility =True, n ='MyGammaCorrect')
        mc.editRenderLayerAdjustment ("%s.gamma"%MyGammaCorrect)
        mc.setAttr('%s.gammaX'%MyGammaCorrect, 0.454)
        mc.setAttr('%s.gammaY'%MyGammaCorrect, 0.454)
        mc.setAttr('%s.gammaZ'%MyGammaCorrect, 0.454)
    else:
        MyGammaCorrect='MyGammaCorrect'
    return MyGammaCorrect

def CreateMyVRayGammaCorrect_zwz():
    if not mc.objExists('MyVRayGammaCorrect'):
        MyVRGammaCorrect = mc.shadingNode('gammaCorrect',asUtility =True, n ='MyVRayGammaCorrect')
        mc.setAttr('%s.gammaX'%MyVRGammaCorrect, 0.454)
        mc.setAttr('%s.gammaY'%MyVRGammaCorrect, 0.454)
        mc.setAttr('%s.gammaZ'%MyVRGammaCorrect, 0.454)
    else:
        MyVRGammaCorrect='MyVRayGammaCorrect'
    return MyVRGammaCorrect

def CreatMyDepthSd_zwz():
    mc.select(cl = True)
    if not mc.objExists('my_depth_lam'):
        myLam = mc.shadingNode('lambert',asShader =True, n ='my_depth_lam')
        mySample = mc.shadingNode('samplerInfo',asUtility =True)
        myRange = mc.shadingNode('setRange',asUtility =True, n='my_depth_setRange')
        myMulti = mc.shadingNode('multiplyDivide',asUtility =True, n ='my_depth_multiplyDivide')
        myLam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myLam+'_SG')
        mc.connectAttr(myLam + '.outColor',myLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myRange + '.oldMaxX',50)
        mc.setAttr(myRange + '.maxX',1)
        mc.setAttr(myMulti + '.input2X',-1)
        mc.addAttr(mySample,ln="cameraNearClipPlane",attributeType='double')
        mc.addAttr(mySample,ln="cameraFarClipPlane",attributeType='double')
        mc.connectAttr(mySample + '.cameraNearClipPlane',myRange + '.oldMin.oldMinX',force = True)
        mc.connectAttr(mySample + '.pointCamera.pointCameraZ',myMulti + '.input1.input1X',force = True)
        mc.connectAttr(myMulti + '.output.outputX',myRange + '.value.valueX',force = True)
        mc.connectAttr(myRange + '.outValue.outValueX',myLam  + '.color.colorR',force = True)
        mc.connectAttr(myRange + '.outValue.outValueX',myLam  + '.color.colorG',force = True)
        mc.connectAttr(myRange + '.outValue.outValueX',myLam  + '.color.colorB',force = True)
    if not mc.objExists('my_depth_lam1'):
        tmp = mc.duplicate('my_depth_lam',upstreamNodes=1)
        myLam_d1 = tmp[0]
        myLam_SG1 = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myLam_d1+'SG')
        mc.connectAttr(myLam_d1 + '.outColor',myLam_SG1 + '.surfaceShader',force=True)
    if not mc.objExists('DepthV_Locator'):
        mydepLocator = mc.spaceLocator(name='DepthV_Locator')[0]
        mc.addAttr(mydepLocator,ln="Depth_V",attributeType='double',defaultValue = -1)
        mc.setAttr('%s.Depth_V'%mydepLocator,edit = True,keyable = True)
        mc.addAttr(mydepLocator,ln="Depth_Max_V",attributeType='double',defaultValue = 50)
        mc.setAttr('%s.Depth_Max_V'%mydepLocator,edit = True,keyable = True)
    myLam_out=['my_depth_lam', 'my_depth_lam_SG', 'my_depth_lam1', 'my_depth_lam1_SG', 'DepthV_Locator']
    return myLam_out

def CreatMyRGBASd_zwz():
    mc.select(cl = True)
    if not mc.objExists('my_RGBA_lamR'):
        myRLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamR')
        myRLam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myRLam+'_SG')
        mc.connectAttr(myRLam + '.outColor',myRLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myRLam + '.color',1,0, 0,type="double3")
        mc.setAttr(myRLam + '.ambientColor',1,0, 0,type="double3")
        mc.setAttr(myRLam + '.diffuse',1)
        mc.setAttr(myRLam + '.matteOpacityMode',1)
        mc.setAttr(myRLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamR1'):
        tmp = mc.duplicate('my_RGBA_lamR',upstreamNodes=1)
        myRLamC = tmp[0]
        myRLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myRLamC+'_SG')
        mc.connectAttr(myRLamC + '.outColor',myRLamC_SG + '.surfaceShader',force=True)
    if not mc.objExists('my_RGBA_lamG'):
        myGLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamG')
        myGLam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myGLam+'_SG')
        mc.connectAttr(myGLam + '.outColor',myGLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myGLam + '.color',0,1,0,type="double3")
        mc.setAttr(myGLam + '.ambientColor',0,1,0,type="double3")
        mc.setAttr(myGLam + '.diffuse',1)
        mc.setAttr(myGLam + '.matteOpacityMode',1)
        mc.setAttr(myGLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamG1'):
        tmp = mc.duplicate('my_RGBA_lamG',upstreamNodes=1)
        myGLamC = tmp[0]
        myGLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myGLamC+'_SG')
        mc.connectAttr(myGLamC + '.outColor',myGLamC_SG + '.surfaceShader',force=True)
    if not mc.objExists('my_RGBA_lamB'):
        myBLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamB')
        myBLam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myBLam+'_SG')
        mc.connectAttr(myBLam + '.outColor',myBLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myBLam + '.color',0, 0,1,type="double3")
        mc.setAttr(myBLam + '.ambientColor',0, 0,1,type="double3")
        mc.setAttr(myBLam + '.diffuse',1)
        mc.setAttr(myBLam + '.matteOpacityMode',1)
        mc.setAttr(myBLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamB1'):
        tmp = mc.duplicate('my_RGBA_lamB',upstreamNodes=1)
        myBLamC = tmp[0]
        myBLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myBLamC+'_SG')
        mc.connectAttr(myBLamC + '.outColor',myBLamC_SG + '.surfaceShader',force=True)

    if not mc.objExists('my_RGBA_lamY'):
        myYLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamY')
        myYLam_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=myYLam+'_SG')
        mc.connectAttr(myYLam + '.outColor',myYLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myYLam + '.color',1, 1, 0, type="double3")
        mc.setAttr(myYLam + '.ambientColor',1, 1, 0,type="double3")
        mc.setAttr(myYLam + '.diffuse',1)
        mc.setAttr(myYLam + '.matteOpacityMode',1)
        mc.setAttr(myYLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamY1'):
        tmp = mc.duplicate('my_RGBA_lamY',upstreamNodes=1)
        myYLamC = tmp[0]
        myYLamC_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=myYLamC+'_SG')
        mc.connectAttr(myYLamC + '.outColor',myYLamC_SG + '.surfaceShader', force=True)

    if not mc.objExists('my_RGBA_lamC'):
        myCLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamC')
        myCLam_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=myCLam+'_SG')
        mc.connectAttr(myCLam + '.outColor', myCLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myCLam + '.color',0, 1, 1, type="double3")
        mc.setAttr(myCLam + '.ambientColor', 0, 1, 1, type="double3")
        mc.setAttr(myCLam + '.diffuse',1)
        mc.setAttr(myCLam + '.matteOpacityMode',1)
        mc.setAttr(myCLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamC1'):
        tmp = mc.duplicate('my_RGBA_lamC',upstreamNodes=1)
        myCLamC = tmp[0]
        myCLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myCLamC+'_SG')
        mc.connectAttr(myCLamC + '.outColor', myCLamC_SG + '.surfaceShader',force=True)

    if not mc.objExists('my_RGBA_lamP'):
        myPLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamP')
        myPLam_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=myPLam+'_SG')
        mc.connectAttr(myPLam + '.outColor', myPLam_SG + '.surfaceShader',force=True)
        mc.setAttr(myPLam + '.color', 1, 0, 1, type="double3")
        mc.setAttr(myPLam + '.ambientColor', 1, 0, 1, type="double3")
        mc.setAttr(myPLam + '.diffuse',1)
        mc.setAttr(myPLam + '.matteOpacityMode',1)
        mc.setAttr(myPLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamP1'):
        tmp = mc.duplicate('my_RGBA_lamP',upstreamNodes=1)
        myPlamC = tmp[0]
        myPlamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myPlamC+'_SG')
        mc.connectAttr(myPlamC + '.outColor',myPlamC_SG + '.surfaceShader',force=True)

    if not mc.objExists('my_RGBA_lamA'):
        myALam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamA')
        myALam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myALam+'_SG')
        mc.connectAttr(myALam + '.outColor',myALam_SG + '.surfaceShader',force=True)
        mc.setAttr(myALam + '.color',0, 0,0,type="double3")
        mc.setAttr(myALam + '.ambientColor',0, 0,0,type="double3")
        mc.setAttr(myALam + '.diffuse',1)
    if not mc.objExists('my_RGBA_lamA1'):
        tmp = mc.duplicate('my_RGBA_lamA',upstreamNodes=1)
        myALamC = tmp[0]
        myALamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myALamC+'_SG')
        mc.connectAttr(myALamC + '.outColor',myALamC_SG + '.surfaceShader',force=True)
    if not mc.objExists('my_RGBA_lamM'):
        myMLam = mc.shadingNode('lambert',asShader =True, n ='my_RGBA_lamM')
        myMLam_SG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=myMLam+'_SG')
        mc.connectAttr(myMLam + '.outColor', myMLam_SG + '.surfaceShader', force=True)
        mc.setAttr(myMLam + '.color',0, 0,0,type="double3")
        mc.setAttr(myMLam + '.ambientColor',0, 0,0,type="double3")
        mc.setAttr(myMLam + '.diffuse',1)
        mc.setAttr(myMLam + '.matteOpacityMode',2)
        mc.setAttr(myMLam + '.matteOpacity',0)
    if not mc.objExists('my_RGBA_lamM1'):
        tmp = mc.duplicate('my_RGBA_lamM',upstreamNodes=1)
        myMLamC = tmp[0]
        myMLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myMLamC+'_SG')
        mc.connectAttr(myMLamC + '.outColor',myMLamC_SG + '.surfaceShader',force=True)
    myRGBALam_out=['my_RGBA_lamR', 'my_RGBA_lamR_SG', 'my_RGBA_lamR1', 'my_RGBA_lamR1_SG',\
                     'my_RGBA_lamG', 'my_RGBA_lamG_SG', 'my_RGBA_lamG1', 'my_RGBA_lamG1_SG',\
                     'my_RGBA_lamB', 'my_RGBA_lamB_SG', 'my_RGBA_lamB1', 'my_RGBA_lamB1_SG',\
                     'my_RGBA_lamA', 'my_RGBA_lamA_SG', 'my_RGBA_lamA1', 'my_RGBA_lamA1_SG',\
                     'my_RGBA_lamM', 'my_RGBA_lamM_SG', 'my_RGBA_lamM1', 'my_RGBA_lamM1_SG',\
                     'my_RGBA_lamY', 'my_RGBA_lamY_SG', 'my_RGBA_lamY1', 'my_RGBA_lamY1_SG',\
                     'my_RGBA_lamC', 'my_RGBA_lamC_SG', 'my_RGBA_lamC1', 'my_RGBA_lamC1_SG',\
                     'my_RGBA_lamP', 'my_RGBA_lamP_SG', 'my_RGBA_lamP1', 'my_RGBA_lamP1_SG']
    return myRGBALam_out

def CreateMyLamLamSd_zwz():
    if not mc.objExists('my_Lam_Lam'):
        myLamLam = mc.shadingNode('lambert',asShader =True, n ='my_Lam_Lam')
        myLamLam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myLamLam + '_SG')
        mc.connectAttr(myLamLam + '.outColor',myLamLam_SG + '.surfaceShader',force=True)
    if not mc.objExists('my_Lam_Lam1'):
        tmp = mc.duplicate('my_Lam_Lam',upstreamNodes=1)
        myLamLamC = tmp[0]
        myLamLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myLamLamC+'_SG')
        mc.connectAttr(myLamLamC+ '.outColor',myLamLamC_SG + '.surfaceShader',force=True)
    MyLamLamSd=['my_Lam_Lam', 'my_Lam_Lam_SG', 'my_Lam_Lam1', 'my_Lam_Lam1_SG']
    return MyLamLamSd

def CreateMyRampLamSd_zwz():
    if not mc.objExists('my_Ramp_Lam'):
        myLamLam = mc.shadingNode('lambert',asShader =True, n ='my_Ramp_Lam')
        myLamLam_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myLamLam + '_SG')
        mc.connectAttr(myLamLam + '.outColor',myLamLam_SG + '.surfaceShader',force=True)
    if not mc.objExists('my_Ramp_Lam1'):
        tmp = mc.duplicate('my_Ramp_Lam',upstreamNodes=1)
        myLamLamC = tmp[0]
        myLamLamC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myLamLamC+'_SG')
        mc.connectAttr(myLamLamC+ '.outColor',myLamLamC_SG + '.surfaceShader',force=True)
    MyLamLamSd=['my_Ramp_Lam', 'my_Ramp_Lam_SG', 'my_Ramp_Lam1', 'my_Ramp_Lam1_SG']
    return MyLamLamSd

def CreateMyProjectionRamp_zwz():
    if not mc.objExists('myProjection_asTexture'):
        myRamp = mm.eval('createRenderNodeCB -as2DTexture "" ramp "" ;')
        myRamp = mc.rename(myRamp, "myProjection_ramp")
        myProjection = mc.shadingNode('projection', asTexture=True,n='myProjection_asTexture')
        myplace3d = mc.shadingNode('place3dTexture', asUtility=True, n='myplace3dTexture')
        mc.connectAttr('%s.wim[0]' % myplace3d, '%s.pm' % myProjection)
        mc.connectAttr('%s.outColor' % myRamp, '%s.image' % myProjection)
    else:
       myProjection = 'myProjection_asTexture'
    return myProjection

def CreateMyRimSurSd_zwz():
    if not mc.objExists('my_rim_Sur'):
        myRimSur = mc.shadingNode('lambert',asShader =True, n ='my_rim_Sur')
        mc.setAttr("%s.ambientColor"%myRimSur,1,1,1,type='double3')
        mySample = mc.shadingNode('samplerInfo',asUtility =True)
        myRamp = mc.shadingNode('ramp',asTexture =True)
        myTex = mc.shadingNode('place2dTexture',asUtility =True)
        myRimSur_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myRimSur + '_SG')
        mc.connectAttr(myRimSur + '.outColor',myRimSur_SG + '.surfaceShader',force=True)
        mc.connectAttr('%s.outUV'%myTex ,'%s.uvCoord'%myRamp,force = True)
        mc.connectAttr('%s.outUvFilterSize'%myTex ,'%s.uvFilterSize'%myRamp,force = True)
        mc.connectAttr('%s.facingRatio'%mySample ,'%s.vCoord'%myRamp,force = True)
        mc.connectAttr('%s.facingRatio'%mySample ,'%s.uCoord'%myRamp,force = True)
        mc.connectAttr('%s.outColor'%myRamp ,'%s.color'%myRimSur,force = True)
        mc.removeMultiInstance('%s.colorEntryList[1]'%myRamp,b=True)
        mc.setAttr('%s.colorEntryList[2].position'%myRamp, 1)
        mc.setAttr('%s.colorEntryList[0].color'%myRamp,1,1,1,type='double3')
        mc.setAttr('%s.colorEntryList[2].color'%myRamp,0, 0,0,type='double3')
    if not mc.objExists('my_rim_Sur1'):
        tmp = mc.duplicate('my_rim_Sur',upstreamNodes=1)
        myRimSurC = tmp[0]
        myRimSurC_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myRimSurC+'_SG')
        mc.connectAttr(myRimSurC+ '.outColor',myRimSurC_SG + '.surfaceShader',force=True)
    MyRimSurSd=['my_rim_Sur', 'my_rim_Sur_SG', 'my_rim_Sur1', 'my_rim_Sur1_SG']
    return MyRimSurSd
#Occ材质的透明值与普通的相反，为不透明度
def creatDeafMrOccSD_zwz():
    if not mc.objExists('myMrOcc'):
        if mc.objExists('myMrOcc_SG'):
            mc.delete('myMrOcc_SG')
        myMrOcc = mc.shadingNode('surfaceShader',asShader =True, n ='myMrOcc')
        myMrOcc_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = myMrOcc+'_SG')
        myMrFg = mc.shadingNode('mib_fg_occlusion',asUtility =True, n ='myMrFg')
        myMrOp = mc.shadingNode('mib_opacity',asUtility =True, n ='myMrOp')
        rampNode = mc.shadingNode('ramp',asTexture =True, n='myMrramp')
        mc.connectAttr(myMrOcc + '.outColor',myMrOcc_SG + '.surfaceShader',force=True)
        mc.connectAttr('%s.outValue' % myMrOp, '%s.miMaterialShader' % myMrOcc_SG, f=True)
        mc.setAttr('%s.opacity'%myMrOp, 1, 1, 1,type="double3")
        mc.connectAttr('%s.outValue'%myMrFg,'%s.outColor'%myMrOcc,f=True)
        mc.connectAttr('%s.outValue' % myMrFg, '%s.input' % myMrOp, f=True)
        mc.connectAttr('%s.outValueA' % myMrFg, '%s.inputA' % myMrOp, f=True)
        mc.connectAttr('%s.outColor' % rampNode, '%s.opacity' % myMrOp, f=True)
        mc.connectAttr('%s.outAlpha' % rampNode, '%s.opacityA' % myMrOp, f=True)
        mc.setAttr('%s.colorEntryList[0].color'%rampNode,1,1,1,type="double3")
        mc.removeMultiInstance('%s.colorEntryList[2]'%rampNode)
        mc.removeMultiInstance('%s.colorEntryList[1]'%rampNode,b=True)
    AllMROccSd=['myMrOcc', 'myMrOcc_SG', 'myMrFg', 'myMrOp', 'myMrramp']
    return AllMROccSd

def CopyDeadMrOccSd_zwz():
    myNewMrOccSd = mc.duplicate('myMrOcc_SG',upstreamNodes=True)
    mc.delete(myNewMrOccSd[3])
    mc.connectAttr('myMrFg.outValue', '%s.outColor'%myNewMrOccSd[2],f=True)
    mc.connectAttr('myMrFg.outValue', '%s.input' %myNewMrOccSd[4], f=True)
    mc.connectAttr('myMrFg.outValueA', '%s.inputA' %myNewMrOccSd[4], f=True)
    AllMROcc_CSd =[myNewMrOccSd[0],myNewMrOccSd[2],myNewMrOccSd[5]]
    return AllMROcc_CSd

def SortallSelShader_zwz():
    #赛选被选物体，把类型为‘mesh’或‘nur'或‘sub’的shapes归为一组
    allMyShapes =[]
    allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
    for Shape in allShapes:
        ShapeType = mc.nodeType(Shape)
        if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
            allMyShapes.append(Shape)
    del allShapes
    if len(allMyShapes)==0:
        mc.confirmDialog( title=u'温馨提示', message=u'选择的组或者物体不含有模型\n请重新选择！', button=['OK'], defaultButton='Yes', dismissString='No')
        #通过Shapes选择相应的SG
    allSgs=[]
    for MyShape in allMyShapes:
        allAssignSG1 = allAssignSG2 =[]
        try:
            allAssignSG1 = mc.listConnections(MyShape+'.instObjGroups.objectGroups', d=True, s=False)
        except:
            pass
        try:
            allAssignSG2 = mc.listConnections(MyShape+'.instObjGroups', d=True, s=False)
        except:
            pass
        if allAssignSG1:
            for each in allAssignSG1:
                if mc.nodeType(each)=='shadingEngine':
                    allSgs.append(each)
        if allAssignSG2:
            for each in allAssignSG2:
                if mc.nodeType(each)=='shadingEngine':
                    allSgs.append(each)
    allMySg = set(allSgs)
    del allSgs
    #通过Sg选择Shader
    vrShd_SG=[]
    defaultShd_SG=[]
    otherShd_SG=[]
    arnoldShd_SG=[]
    allSelShader=[]

    for MySg in allMySg:
        eachShader = ''
        try:
            eachShader = mc.listConnections(MySg+'.miShadowShader', s=True, d=False)[0]
        except:
            pass
        else:
            otherShd_SG.append(MySg)
            allSelShader.append(eachShader)
        if not eachShader:
            try:
                eachShader = mc.listConnections(MySg+'.surfaceShader', s=True, d=False)[0]
            except:
                continue
            else:
                if mc.nodeType(eachShader) == 'VRayMtl':
                    vrShd_SG.append(MySg)
                    allSelShader.append(eachShader)
                elif mc.nodeType(eachShader) == 'lambert' or mc.nodeType(eachShader) == 'blinn' \
                    or mc.nodeType(eachShader) == 'phong' or mc.nodeType(eachShader) == 'phongE' \
                    or mc.nodeType(eachShader) == 'surfaceShader' or mc.nodeType(eachShader) == 'anisotropic' \
                    or mc.nodeType(eachShader) == 'layeredShader' or mc.nodeType(eachShader) == 'oceanShader':
                    defaultShd_SG.append(MySg)
                    allSelShader.append(eachShader)
                elif mc.nodeType(eachShader) == 'aiHair' or mc.nodeType(eachShader) == 'aiAmbientOcclusion' \
                    or mc.nodeType(eachShader) == 'aiStandard':
                    arnoldShd_SG.append(MySg)
                    allSelShader.append(eachShader)
                else:
                    if mc.nodeType(eachShader) != 'displacementShader':
                        otherShd_SG.append(MySg)
                        allSelShader.append(eachShader)

    allFSG=[vrShd_SG,defaultShd_SG,arnoldShd_SG,otherShd_SG,allSelShader,allMyShapes]
    return allFSG

def assignMy3sSd_zwz(mySd,allObjects):
    for eachObject in allObjects:
        addmySd = mc.duplicate(mySd,upstreamNodes=1)[0]
        addmySd_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = addmySd+'_SG')
        mc.connectAttr(addmySd + '.outColor',addmySd_SG + '.surfaceShader',force=True)
        mc.select(eachObject)
        mc.hyperShade(assign=addmySd)
        mc.sets(e=True,forceElement = addmySd_SG)

def VraySdtoMySD_zwz(mySd, mySd_SG, vrShd_SG, myCSd, myCSd_SG, allMyShapes=[]):
    myInputShaderType = 0
    SdTransAttr = ''
    mayaversions = mc.about(v=True)

    if mySd.find('my3sStandMatte') >= 0 or mySd.find('myArnoldOcc') >= 0:
        myInputShaderType = 0
    if mySd.find('my_depth_lam') >= 0:
        myInputShaderType = 1
    if mySd.find('my_RGBA_lam') >= 0:
        myInputShaderType = 2
    if mySd.find('myMrOcc') >= 0:
        myInputShaderType = 3
    if mySd.find('my_rim_Sur') >= 0:
        myInputShaderType = 4
    elif mySd.find('my_Lam_Lam') >= 0 or mySd.find('my_Ramp_Lam') >= 0:
        myInputShaderType = 5

    #根据层名，定义透明节点的名字
    if myInputShaderType == 0:
        SdTransAttr = 'opacity'
    elif myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
        SdTransAttr = 'transparency'
    elif myInputShaderType == 3:
        SdTransAttr = 'colorEntryList[0].color'
    for each in vrShd_SG:
        if myInputShaderType != 2:
            if each.find('%s' % mySd) >= 0:
                continue
        #选择所有被赋予该材质球的物体，若选择的物体数量为0时到下一个循环
        try:
            eachShader = mc.listConnections(each+'.surfaceShader', s=True, d=False)[0]
        except:
            continue
        mc.select(cl=True)
        mc.hyperShade(objects=eachShader)
        ObjectS = mc.ls(sl=True)
        if not len(ObjectS):
            continue

        #当为RGB层时，影响的只是被选择的物体
        MyRGBObjects = []
        tmp = ''
        if myInputShaderType == 2:
            for Object in ObjectS:
                if Object.find('.') >= 0:
                    tmp = mc.listRelatives(Object, p=True, pa=True)[0]
                    if tmp in allMyShapes:
                        MyRGBObjects.append(Object)
                else:
                    if Object in allMyShapes:
                        MyRGBObjects.append(Object)
            mc.select(cl=True)
            ObjectS = MyRGBObjects
            mc.select(ObjectS)

        #旗帜,SGC_V：置换链接; LaC_V ：层材质; TrC_V：透明链接; TrV_V：透明值; BuC_V：Bump链接
        SGC_V = 0
        TrC_V = 0
        TrV_V = 0
        BuC_V = 0
        LaC_V = 0
        #判断Sg是否有置换链接
        tmp = mc.listConnections('%s.displacementShader' % each, s=True, d=False, plugs=True)
        if tmp:
            SGDisplaceC = tmp[0]
            SGC_V = 1
        #判断是否是层材质，技术层材质的数量
        type = mc.nodeType(eachShader)
        if type == 'layeredShader':
            LaC_V = 1
            signLSd = signLSd + 1
        else:
            #定义透明链接类型：带R或不带R
            tranC_Type = 0
            tmp = ''
            if mayaversions.find('2009') >= 0:
                tmp = mc.listConnections('%s.opacityMap' % eachShader, s=True, d=False, plugs=True)
            else:
                tmp = mc.listConnections('%s.transparency' % eachShader, s=True, d=False, plugs=True)
            if tmp:
                tranC_Type = 1
                transPath = tmp[0]
                TrC_V = 1
            else:
                tmp = mc.listConnections('%s.opacityMapR' % eachShader, s=True, d=False, plugs=True)
                if tmp:
                    singVSd = singVSd + 1
                    tranC_Type = 2
                    transPath = tmp[0]
                    TrC_V = 1
                else:
                    #判断是否具有透明值
                    if mayaversions.find('2009') >= 0:
                        transValue = mc.getAttr('%s.opacityMap' % eachShader)
                    else:
                        transValue = mc.getAttr('%s.transparency' % eachShader)
                    if transValue[0][0] != 1 or transValue[0][1] != 1 or transValue[0][2] != 1:
                        TrV_V = 1
            #当不是OCC层时，判断是否带有bump链接
            if (myInputShaderType == 4 or myInputShaderType == 5) and type != 'surfaceShader':
                tmp = mc.listConnections('%s.bumpMap' % eachShader, s=True, d=False, plugs=True)
                if tmp:
                    bumpPath = tmp[0]
                    BuC_V = 1

        #当符合以下其中一个条件时，需要一个新的材质球，并连接上相应节点
        if SGC_V == 1 or TrC_V == 1 or TrV_V == 1 or BuC_V == 1 or LaC_V == 1:
            #复制材质球
            if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                tmp = mc.duplicate(mySd,upstreamNodes=1)
                addmySd = tmp[0]
                addmySd_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = addmySd+'_SG')
                mc.connectAttr(addmySd + '.outColor',addmySd_SG + '.surfaceShader',force=True)
            if myInputShaderType == 3:
                tmp = CopyDeadMrOccSd_zwz()
                addmySd_SG = tmp[0]
                addmySd = tmp[1]
                addmySd_Ramp = tmp[2]
                mc.setAttr("%s.invert"%addmySd_Ramp,1)
                #把复制出来的材质球赋予被选择的物体
            try:
                mc.hyperShade(assign = addmySd)
                mc.sets(e=True,forceElement = addmySd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)
            #链接处理：
            #不同层，透明值不一样
            tranc_Point=''
            if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                tranc_Point = addmySd
            elif myInputShaderType == 3:
                tranc_Point = addmySd_Ramp
            #当有透明链接或数值时，分清是什么渲染层
            if TrC_V == 1:
                opacityNode = transPath.split('.')[0]
                opcityType = mc.nodeType(opacityNode)
                #当透明节点是文件时
                if opcityType == 'file':
                    VmyInv = mc.getAttr('%s.invert'%opacityNode)
                    # if not (myInputShaderType == 2 or myInputShaderType == 5):
                    try:
                        mc.editRenderLayerAdjustment('%s.invert'%opacityNode)
                    except:
                        pass
                    if tranC_Type == 1:
                        mc.connectAttr(transPath,tranc_Point + '.%s'%SdTransAttr,force=True)
                    elif tranC_Type == 2:
                        mc.connectAttr(transPath,tranc_Point + '.%sR'%SdTransAttr,force=True)
                        mc.connectAttr(transPath,tranc_Point + '.%sG'%SdTransAttr,force=True)
                        mc.connectAttr(transPath,tranc_Point + '.%sB'%SdTransAttr,force=True)
                    if myInputShaderType == 0:
                        for Object in ObjectS:
                            ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                            mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                            mc.setAttr('%s.aiOpaque'%ObjectT,0)
                    if VmyInv:
                        mc.setAttr('%s.invert'%opacityNode,False)
                    else:
                        mc.setAttr('%s.invert'%opacityNode,True)
                    if myInputShaderType == 2 or myInputShaderType == 5:
                        if mc.getAttr('%s.alphaIsLuminance'%opacityNode):
                            try:
                                mc.editRenderLayerAdjustment('%s.alphaIsLuminance'%opacityNode)
                            except:
                                pass
                            mc.setAttr('%s.alphaIsLuminance'%opacityNode,0)
                #当透明节点是反向节点时
                elif opcityType == 'reverse':
                    temp = 0
                    revPath=mc.listConnections('%s.inputX' % opacityNode, s=True, d=False, plugs=True)
                    if revPath:
                        temp = 1
                    else:
                        temp = 2
                        revPath=mc.listConnections('%s.input' % opacityNode, s=True, d=False, plugs=True)
                    if revPath and temp == 1:
                        mc.connectAttr(revPath[0],addmySd + '.%sR'%SdTransAttr,force=True)
                        mc.connectAttr(revPath[0],addmySd + '.%sG'%SdTransAttr,force=True)
                        mc.connectAttr(revPath[0],addmySd + '.%sB'%SdTransAttr,force=True)
                    if revPath and temp == 2:
                        mc.connectAttr(revPath[0],addmySd + '.%s'%SdTransAttr,force=True)
                    if myInputShaderType == 0:
                        for Object in ObjectS:
                            ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                            mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                            mc.setAttr('%s.aiOpaque'%ObjectT,0)
                else:
                    reverseNode = mc.createNode('reverse')

                    if tranC_Type == 1:
                        mc.connectAttr(transPath,'%s.input' % reverseNode,f=True)
                    elif tranC_Type == 2:
                        mc.connectAttr(transPath,'%s.inputX' % reverseNode,force=True)
                        mc.connectAttr(transPath,'%s.inputY' % reverseNode,force=True)
                        mc.connectAttr(transPath,'%s.inputZ' % reverseNode,force=True)
                    mc.connectAttr('%s.output' % reverseNode,tranc_Point + '.%s'%SdTransAttr, f=True)

            else:
                #具有透明值
                if TrV_V == 1:
                    if not (myInputShaderType == 2 or myInputShaderType == 5):
                        mc.editRenderLayerAdjustment('%s.%s'%(tranc_Point,SdTransAttr))
                    if myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 3 or myInputShaderType == 4 or myInputShaderType == 5:
                        tmp = 'rgb_to_hsv(<<%s,%s,%s>>)' % (transValue[0][0], transValue[0][1], transValue[0][2])
                        oldSpeVHSV = mm.eval(tmp)
                        tmp = 'hsv_to_rgb(<<%f,%s,%f>>)' % (0, 0, 1-oldSpeVHSV[2])
                        newSpeVRGB = mm.eval(tmp)
                        mc.setAttr('%s.%s' % (tranc_Point, SdTransAttr), newSpeVRGB[0], newSpeVRGB[1], newSpeVRGB[2], type='double3')
                    # elif myInputShaderType == 3 or myInputShaderType == 0:
                    #     mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr),transValue[0][0],transValue[0][1],transValue[0][2],type='double3')
                    if myInputShaderType == 0:
                        for Object in ObjectS:
                            ObjectT = mc.listRelatives(Object, p=True, f=True)[0]
                            mc.editRenderLayerAdjustment('%s.aiOpaque' % ObjectT)
                            mc.setAttr('%s.aiOpaque' % ObjectT, 0)
            #当有凹凸连接时
            if BuC_V:
                mc.connectAttr(bumpPath, addmySd+'.normalCamera', force=True)
            #当有置换链接时
            if SGC_V == 1:
                mc.connectAttr(SGDisplaceC,'%s.displacementShader'%addmySd_SG,f=True)
                if myInputShaderType == 3 and TrV_V == 0:
                    mc.setAttr('%s.%s' % (tranc_Point, SdTransAttr), 0, 0, 0, type='double3')
        else:
            try:
                mc.hyperShade(assign = myCSd)
                mc.sets(e=True,forceElement = myCSd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)



def OtherSdMySD_zwz(mySd,myLam_SG,otherShd_SG,myCSd,myCSd_SG,allMyShapes=[]):
    myInputShaderType = 0
    SdTransAttr = ''

    if mySd.find('my3sStandMatte')>=0 or mySd.find('myArnoldOcc') >= 0:
        myInputShaderType = 0
    if mySd.find('my_depth_lam') >= 0:
        myInputShaderType = 1
    if mySd.find('my_RGBA_lam') >= 0:
        myInputShaderType = 2
    if mySd.find('myMrOcc') >= 0:
        myInputShaderType = 3
    if mySd.find('my_rim_Sur') >= 0:
        myInputShaderType = 4
    elif mySd.find('my_Lam_Lam') >= 0 or mySd.find('my_Ramp_Lam') >= 0:
        myInputShaderType = 5

        #根据层名，定义透明节点的名字
    if myInputShaderType == 0:
        SdTransAttr = 'opacity'
    elif myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
        SdTransAttr = 'transparency'
    elif myInputShaderType == 3:
        SdTransAttr = 'colorEntryList[0].color'

    for each in otherShd_SG:
        if myInputShaderType != 2:
            if each.find('%s'%mySd) >= 0:
                continue
            #选择所有被赋予该材质球的物体，若选择的物体数量为0时到下一个循环
        eachShader = ''
        tmp=[]
        tmp= mc.listConnections(each+'.surfaceShader', s=True, d=False)
        if tmp:
            eachShader = tmp[0]
            mc.select(cl = True)
            mc.hyperShade(objects=eachShader)
            ObjectS = mc.ls(sl=True)
            if not len(ObjectS):
                continue
            try:
                mc.hyperShade(assign = myCSd)
                mc.sets(e=True,forceElement = myCSd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)
        else:
        #处理MR材质球
            tmp = mc.listConnections(each+'.miShadowShader', s=True, d=False)
            if tmp:
                eachShader = tmp[0]
                mc.select(cl = True)
                mc.hyperShade(objects=eachShader)
                ObjectS = mc.ls(sl=True)
                if not len(ObjectS):
                    continue

                #当为RGB层时，影响的只是被选择的物体
                MyRGBObjects=[]
                tmp=''
                if myInputShaderType == 2:
                    for Object in ObjectS:
                        if Object.find('.') >= 0:
                            tmp = mc.listRelatives(Object, p=True, pa=True)[0]
                            if tmp in allMyShapes:
                                MyRGBObjects.append(Object)
                        else:
                            if Object in allMyShapes:
                                MyRGBObjects.append(Object)
                    mc.select(cl = True)
                    ObjectS = MyRGBObjects
                    mc.select(ObjectS)

                #旗帜,SGC_V：置换链接；TrC_V：透明链接；TrV_V：透明值；BuC_V：Bump链接
                SGC_V = 0
                TrC_V = 0
                TrV_V = 0
                BuC_V = 0

                #判断Sg是否有置换链接
                tmp = mc.listConnections('%s.displacementShader'%each,s=True, d=False,plugs=True)
                if tmp:
                    SGDisplaceC = tmp[0]
                    SGC_V = 1
                transAttr = 'transparency'
                #定义透明链接类型：带R或不带R
                tranC_Type = 0
                tmp=''
                try:
                    tmp = mc.listConnections('%s.%s' % (eachShader,transAttr), s=True, d=False,plugs=True)
                except:
                    pass
                else:
                    if tmp:
                        tranC_Type = 1
                        transPath=tmp[0]
                        TrC_V = 1
                if tranC_Type == 0:
                    #判断是否具有透明值
                    transValue = mc.getAttr('%s.%s' % (eachShader,transAttr))
                    if transValue != 0:
                        TrV_V = 1
                #当不是OCC层时，判断是否带有bump链接
                if myInputShaderType == 4 or myInputShaderType == 5:
                    try:
                        tmp = mc.listConnections('%s.standard_bump' % eachShader, s=True, d=False,plugs=True)
                    except:
                        pass
                    else:
                        if tmp:
                            bumpPath =tmp[0]
                            BuC_V = 1
                #当符合以下其中一个条件时，需要一个新的材质球，并连接上相应节点
                if SGC_V==1 or TrC_V==1 or TrV_V==1 or BuC_V==1:
                    #复制材质球
                    if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                        tmp = mc.duplicate(mySd,upstreamNodes=1)
                        addmySd = tmp[0]
                        addmySd_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = addmySd+'_SG')
                        mc.connectAttr(addmySd + '.outColor',addmySd_SG + '.surfaceShader',force=True)
                    if myInputShaderType == 3:
                        tmp = CopyDeadMrOccSd_zwz()
                        addmySd_SG = tmp[0]
                        addmySd = tmp[1]
                        addmySd_Ramp = tmp[2]
                        mc.setAttr("%s.invert"%addmySd_Ramp,1)
                        #把复制出来的材质球赋予被选择的物体
                    try:
                        mc.hyperShade(assign = addmySd)
                        mc.sets(e=True,forceElement = addmySd_SG)
                    except:
                        sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)
                    #链接处理：
                    #不同层，透明值不一样
                    tranc_Point=''
                    if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                        tranc_Point = addmySd
                    elif myInputShaderType == 3:
                        tranc_Point = addmySd_Ramp
                    #当有透明链接或数值时，分清是什么渲染层
                    if TrC_V == 1:
                        mc.connectAttr(transPath,tranc_Point + '.%sR'%SdTransAttr,force=True)
                        mc.connectAttr(transPath,tranc_Point + '.%sG'%SdTransAttr,force=True)
                        mc.connectAttr(transPath,tranc_Point + '.%sB'%SdTransAttr,force=True)
                        if myInputShaderType == 0:
                            for Object in ObjectS:
                                ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                                if not (myInputShaderType == 2 or myInputShaderType == 5):
                                    mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                                mc.setAttr('%s.aiOpaque'%ObjectT,0)
                        if myInputShaderType == 2 or myInputShaderType == 5:
                            TranNode = transPath.split('.')[0]
                            TranType = mc.nodeType(TranNode)
                            if TranType == 'file':
                                #mc.editRenderLayerAdjustment('%s.alphaIsLuminance'%TranNode)
                                if mc.getAttr('%s.alphaIsLuminance'%TranNode):
                                    mc.setAttr('%s.alphaIsLuminance'%TranNode,0)
                    else:
                        #具有透明值
                        if TrV_V == 1:
                            if not (myInputShaderType == 2 or myInputShaderType == 5):
                                mc.editRenderLayerAdjustment('%s.%s'%(tranc_Point,SdTransAttr))
                            if myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 3 or myInputShaderType == 4 or myInputShaderType == 5:
                                mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr),0, 0,transValue,type='double3')
                            # elif myInputShaderType == 3:
                            #     mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr),1-transValue[0][0],1-transValue[0][1],1-transValue[0][2],type='double3')
                            if myInputShaderType == 0:
                                for Object in ObjectS:
                                    ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                                    mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                                    mc.setAttr('%s.aiOpaque'%ObjectT,0)
                    #当有凹凸连接时
                    if BuC_V:
                        mc.connectAttr(bumpPath,addmySd + '.normalCamera',force=True)
                    #当有置换链接时
                    if SGC_V == 1:
                        mc.connectAttr(SGDisplaceC,'%s.displacementShader'%addmySd_SG,f=True)
                        if myInputShaderType == 3 and TrV_V == 0:
                            mc.setAttr('%s.%s' % (tranc_Point, SdTransAttr), 0, 0, 0, type='double3')
                #没有指定的链接或值时，给默认的相应材质球
                else:
                    try:
                        mc.hyperShade(assign=myCSd)
                        mc.sets(e=True, forceElement=myCSd_SG)
                    except:
                        sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)


def arnoldShdMySD_zwz(mySd,myLam_SG,arnoldShd_SG,myCSd,myCSd_SG,allMyShapes=[]):

    myInputShaderType = 0
    SdTransAttr = ''
    transAttr = 'opacity'

    if mySd.find('my3sStandMatte')>=0 or mySd.find('myArnoldOcc') >= 0:
        myInputShaderType = 0
    if mySd.find('my_depth_lam') >= 0:
        myInputShaderType = 1
    if mySd.find('my_RGBA_lam') >= 0:
        myInputShaderType = 2
    if mySd.find('myMrOcc') >= 0:
        myInputShaderType = 3
    if mySd.find('my_rim_Sur') >= 0:
        myInputShaderType = 4
    elif mySd.find('my_Lam_Lam') >= 0 or mySd.find('my_Ramp_Lam') >= 0:
        myInputShaderType = 5

    #根据层名，定义透明节点的名字
    if myInputShaderType == 0:
        SdTransAttr = 'opacity'
    elif myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
        SdTransAttr = 'transparency'
    elif myInputShaderType == 3:
        SdTransAttr = 'colorEntryList[0].color'
    for each in arnoldShd_SG:
        if myInputShaderType != 2:
            if each.find('%s'%mySd) >= 0:
                continue
        #选择所有被赋予该材质球的物体，若选择的物体数量为0时到下一个循环
        try:
            eachShader = mc.listConnections(each+'.surfaceShader', s=True, d=False)[0]
        except:
            continue
        mc.select(cl = True)
        mc.hyperShade(objects=eachShader)
        ObjectS = mc.ls(sl=True)
        if not len(ObjectS):
            continue

        #当为RGB层时，影响的只是被选择的物体
        MyRGBObjects=[]
        tmp=''
        if myInputShaderType == 2:
            for Object in ObjectS:
                if Object.find('.') >= 0:
                    tmp = mc.listRelatives(Object, p=True, pa=True)[0]
                    if tmp[0] in allMyShapes:
                        MyRGBObjects.append(Object)
                else:
                    if Object in allMyShapes:
                        MyRGBObjects.append(Object)
            mc.select(cl = True)
            ObjectS = MyRGBObjects
            mc.select(ObjectS)

        #旗帜,SGC_V：置换链接；TrC_V：透明链接；TrV_V：透明值；BuC_V：Bump链接
        SGC_V = 0
        TrC_V = 0
        TrV_V = 0
        BuC_V = 0

        #判断Sg是否有置换链接
        tmp = mc.listConnections('%s.displacementShader'%each,s=True, d=False,plugs=True)
        if tmp:
            SGDisplaceC = tmp[0]
            SGC_V = 1
        transAttr = 'opacity'
        #定义透明链接类型：带R或不带R
        tranC_Type = 0
        tmp=''
        tmp = mc.listConnections('%s.%s' % (eachShader,transAttr), s=True, d=False,plugs=True)
        if tmp:
            tranC_Type = 1
            transPath=tmp[0]
            TrC_V = 1
        else:
            tmp = mc.listConnections('%s.%sR' % (eachShader,transAttr), s=True, d=False,plugs=True)
            if tmp:
                singVSd = singVSd + 1
                tranC_Type = 2
                transPath=tmp[0]
                TrC_V = 1
            else:
                #判断是否具有透明值
                transValue = mc.getAttr('%s.%s' % (eachShader,transAttr))
                if transValue[0][0] != 1 or transValue[0][1] != 1 or transValue[0][2] != 1 :
                    TrV_V = 1
        #当不是OCC层时，判断是否带有bump链接
        if myInputShaderType == 4 or myInputShaderType == 5:
            tmp = mc.listConnections('%s.normalCamera' % eachShader, s=True, d=False,plugs=True)
            if tmp:
                bumpPath =tmp[0]
                BuC_V = 1

        #当符合以下其中一个条件时，需要一个新的材质球，并连接上相应节点
        if SGC_V==1 or LaC_V==1 or TrC_V==1 or TrV_V==1 or BuC_V==1:
            #复制材质球
            if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                tmp = mc.duplicate(mySd,upstreamNodes=1)
                addmySd = tmp[0]
                addmySd_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = addmySd+'_SG')
                mc.connectAttr(addmySd + '.outColor',addmySd_SG + '.surfaceShader',force=True)
            if myInputShaderType == 3:
                tmp = CopyDeadMrOccSd_zwz()
                addmySd_SG = tmp[0]
                addmySd = tmp[1]
                addmySd_Ramp = tmp[2]
                mc.setAttr("%s.invert"%addmySd_Ramp,1)
                #把复制出来的材质球赋予被选择的物体
            try:
                mc.hyperShade(assign = addmySd)
                mc.sets(e=True,forceElement = addmySd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)
            #链接处理：
            #不同层，透明值不一样
            tranc_Point=''
            if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                tranc_Point = addmySd
            elif myInputShaderType == 3:
                tranc_Point = addmySd_Ramp
            #当有透明链接或数值时，分清是什么渲染层
            if TrC_V == 1:
                if tranC_Type == 1:
                    mc.connectAttr(transPath,tranc_Point + '.%s'%SdTransAttr,force=True)
                elif tranC_Type == 2:
                    mc.connectAttr(transPath,tranc_Point + '.%sR'%SdTransAttr,force=True)
                    mc.connectAttr(transPath,tranc_Point + '.%sG'%SdTransAttr,force=True)
                    mc.connectAttr(transPath,tranc_Point + '.%sB'%SdTransAttr,force=True)
                if myInputShaderType == 0:
                    for Object in ObjectS:
                        ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                        mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                        mc.setAttr('%s.aiOpaque'%ObjectT,0)
                if myInputShaderType == 2 or myInputShaderType == 5:
                    TranNode = transPath.split('.')[0]
                    TranType = mc.nodeType(TranNode)
                    if TranType == 'file':
                        #mc.editRenderLayerAdjustment('%s.alphaIsLuminance'%TranNode)
                        if mc.getAttr('%s.alphaIsLuminance'%TranNode):
                            mc.setAttr('%s.alphaIsLuminance'%TranNode,0)
            else:
                #具有透明值
                if TrV_V == 1:
                    if not (myInputShaderType == 2 or myInputShaderType == 5):
                        mc.editRenderLayerAdjustment('%s.%s'%(tranc_Point,SdTransAttr))
                    if myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 3 or myInputShaderType == 4 or myInputShaderType == 5:
                        tmp='rgb_to_hsv(<<%s,%s,%s>>)'%(transValue[0][0],transValue[0][1],transValue[0][2])
                        oldSpeVHSV = mm.eval(tmp)
                        tmp='hsv_to_rgb(<<%f,%s,%f>>)'%(0, 0,oldSpeVHSV[2])
                        newSpeVRGB= mm.eval(tmp)
                        mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr), newSpeVRGB[0], newSpeVRGB[1], newSpeVRGB[2],type='double3')
                    # elif myInputShaderType == 3:
                    #     mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr),1-transValue[0][0],1-transValue[0][1],1-transValue[0][2],type='double3')
                    if myInputShaderType == 0:
                        for Object in ObjectS:
                            ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                            mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                            mc.setAttr('%s.aiOpaque'%ObjectT,0)
            #当有凹凸连接时
            if BuC_V:
                mc.connectAttr(bumpPath,addmySd + '.normalCamera',force=True)
            #当有置换链接时
            if SGC_V == 1:
                mc.connectAttr(SGDisplaceC,'%s.displacementShader'%addmySd_SG,f=True)
                if myInputShaderType == 3 and TrV_V == 0:
                    mc.setAttr('%s.%s' % (tranc_Point, SdTransAttr), 0, 0, 0, type='double3')
        #没有指定的链接或值时，给默认的相应材质球
        else:
            try:
                mc.hyperShade(assign = myCSd)
                mc.sets(e=True,forceElement = myCSd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)


def DeafSdtoMySD_zwz(mySd,mySd_SG,defaultShd_SG,myCSd,myCSd_SG,allMyShapes=[]):
    signLSd = 0
    singVSd = 0
    myInputShaderType = 0
    SdTransAttr = ''

    if mySd.find('my3sStandMatte')>=0 or mySd.find('myArnoldOcc') >= 0:
        myInputShaderType = 0
    elif mySd.find('my_depth_lam') >= 0:
        myInputShaderType = 1
    elif mySd.find('my_RGBA_lam') >= 0:
        myInputShaderType = 2
    elif mySd.find('myMrOcc') >= 0:
        myInputShaderType = 3
    elif mySd.find('my_rim_Sur') >= 0:
        myInputShaderType = 4
    elif mySd.find('my_Lam_Lam') >= 0 or mySd.find('my_Ramp_Lam') >= 0:
        myInputShaderType = 5

    #根据层名，定义透明节点的名字
    if myInputShaderType == 0:
        SdTransAttr = 'opacity'
    elif myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
        SdTransAttr = 'transparency'
    elif myInputShaderType == 3:
        SdTransAttr = 'colorEntryList[0].color'

    for each in defaultShd_SG:
        if myInputShaderType != 2:
            if each.find('%s'%mySd) >= 0:
                continue

        #选择所有被赋予该材质球的物体，若选择的物体数量为0时到下一个循环
        try:
            eachShader = mc.listConnections(each+'.surfaceShader', s=True, d=False)[0]
        except:
            continue
        mc.select(cl = True)
        mc.hyperShade(objects=eachShader)
        ObjectS = mc.ls(sl=True)
        if not len(ObjectS):
            continue

        #当为RGB层时，影响的只是被选择的物体
        MyRGBObjects=[]
        tmp=''
        if myInputShaderType == 2:
            for Object in ObjectS:
                if Object.find('.') >= 0:
                    tmp = mc.listRelatives(Object, p=True, pa=True)[0]
                    if tmp in allMyShapes:
                        MyRGBObjects.append(Object)
                else:
                    if Object in allMyShapes:
                        MyRGBObjects.append(Object)
            mc.select(cl=True)
            ObjectS = MyRGBObjects
            mc.select(ObjectS)

        #旗帜,SGC_V：置换链接；LaC_V ：层材质；TrC_V：透明链接；TrV_V：透明值；BuC_V：Bump链接
        SGC_V = 0
        LaC_V = 0
        TrC_V = 0
        TrV_V = 0
        BuC_V = 0

        #判断Sg是否有置换链接
        tmp = mc.listConnections('%s.displacementShader'%each,s=True, d=False,plugs=True)
        if tmp:
            SGDisplaceC = tmp[0]
            SGC_V = 1

        type = mc.nodeType(eachShader)
        #判断是否是层材质，技术层材质的数量
        if type == 'layeredShader':
            LaC_V = 1
            signLSd = signLSd + 1

        else:
            #判断是否带透明链接或者具有透明纸
            if type == 'surfaceShader':
                transAttr = 'outTransparency'
            else:
                transAttr = 'transparency'
            #定义透明链接类型：带R或不带R
            tranC_Type = 0
            tmp=''
            tmp = mc.listConnections('%s.%s' % (eachShader, transAttr), s=True, d=False, plugs=True)
            if tmp:
                tranC_Type = 1
                transPath=tmp[0]
                TrC_V = 1
            else:
                tmp = mc.listConnections('%s.%sR' % (eachShader, transAttr), s=True, d=False, plugs=True)
                if tmp:
                    singVSd = singVSd + 1
                    tranC_Type = 2
                    transPath=tmp[0]
                    TrC_V = 1
                else:
                    #判断是否具有透明值
                    transValue = mc.getAttr('%s.%s' % (eachShader, transAttr))
                    if transValue[0][0] != 0 or transValue[0][1] != 0 or transValue[0][2] != 0:
                        TrV_V = 1
                #当不是OCC层时，判断是否带有bump链接
            print myInputShaderType
            if (myInputShaderType == 4 or myInputShaderType == 5) and type != 'surfaceShader':
                tmp = mc.listConnections('%s.normalCamera' % eachShader, s=True, d=False, plugs=True)
                if tmp:
                    bumpPath=tmp[0]
                    BuC_V = 1
        #当符合以下其中一个条件时，需要一个新的材质球，并连接上相应节点
        if SGC_V==1 or LaC_V==1 or TrC_V==1 or TrV_V==1 or BuC_V==1:
            #复制材质球
            if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                tmp = mc.duplicate(mySd,upstreamNodes=1)
                addmySd = tmp[0]
                addmySd_SG = mc.sets(renderable=True, noSurfaceShader=True,empty=True, name = addmySd+'_SG')
                mc.connectAttr(addmySd + '.outColor',addmySd_SG + '.surfaceShader',force=True)
            if myInputShaderType == 3:
                tmp = CopyDeadMrOccSd_zwz()
                addmySd_SG = tmp[0]
                addmySd = tmp[1]
                addmySd_Ramp = tmp[2]
                mc.setAttr("%s.invert"%addmySd_Ramp, 1)
                #把复制出来的材质球赋予被选择的物体
            try:
                mc.hyperShade(assign = addmySd)
                mc.sets(e=True,forceElement = addmySd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)
                #链接处理：
            #不同层，透明值不一样
            tranc_Point=''
            if myInputShaderType == 0 or myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 4 or myInputShaderType == 5:
                tranc_Point = addmySd
            elif myInputShaderType == 3:
                tranc_Point = addmySd_Ramp
            #当是层材质时 不是Arnold渲染时,导出透明
            if LaC_V == 1:
                if myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 3 or myInputShaderType == 4 or myInputShaderType == 5:
                    mc.connectAttr('%s.outTransparency'%eachShader,tranc_Point + '.%s'%SdTransAttr,force=True)
            #不是层材质时：
            else:
                #当有透明链接或数值时，分清是什么渲染层
                if TrC_V == 1:
                    if tranC_Type == 1:
                        mc.connectAttr(transPath,tranc_Point + '.%s'%SdTransAttr,force=True)
                    elif tranC_Type == 2:
                        mc.connectAttr(transPath,tranc_Point + '.%sR'%SdTransAttr,force=True)
                        mc.connectAttr(transPath,tranc_Point + '.%sG'%SdTransAttr,force=True)
                        mc.connectAttr(transPath,tranc_Point + '.%sB'%SdTransAttr,force=True)
                    if myInputShaderType == 0:
                        for Object in ObjectS:
                            ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                            mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                            mc.setAttr('%s.aiOpaque'%ObjectT,0)
                    if myInputShaderType == 2 or myInputShaderType == 5:
                        TranNode = transPath.split('.')[0]
                        TranType = mc.nodeType(TranNode)
                        if TranType == 'file':
                            # mc.editRenderLayerAdjustment('%s.alphaIsLuminance'%TranNode)
                            if mc.getAttr('%s.alphaIsLuminance'%TranNode):
                                mc.setAttr('%s.alphaIsLuminance'%TranNode,0)
                else:
                    #具有透明值
                    if TrV_V == 1:
                        if not (myInputShaderType == 2 or myInputShaderType == 5):
                            mc.editRenderLayerAdjustment('%s.%s' % (tranc_Point, SdTransAttr))
                        if myInputShaderType == 1 or myInputShaderType == 2 or myInputShaderType == 3 or myInputShaderType == 4 or myInputShaderType == 5:
                            tmp='rgb_to_hsv(<<%s,%s,%s>>)'%(transValue[0][0],transValue[0][1],transValue[0][2])
                            oldSpeVHSV = mm.eval(tmp)
                            tmp='hsv_to_rgb(<<%f,%s,%f>>)'%(0, 0,oldSpeVHSV[2])
                            newSpeVRGB= mm.eval(tmp)
                            mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr), newSpeVRGB[0], newSpeVRGB[1], newSpeVRGB[2],type='double3')
                        # elif myInputShaderType == 3:
                        #     mc.setAttr('%s.%s' % (tranc_Point,SdTransAttr),1-transValue[0][0],1-transValue[0][1],1-transValue[0][2],type='double3')
                        if myInputShaderType == 0:
                            for Object in ObjectS:
                                ObjectT = mc.listRelatives(Object,p=True,f=True)[0]
                                mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectT)
                                mc.setAttr('%s.aiOpaque'%ObjectT,0)

            #当有置换链接时
            if SGC_V == 1:
                mc.connectAttr(SGDisplaceC,'%s.displacementShader'%addmySd_SG,f=True)
                if myInputShaderType == 3 and TrV_V == 0:
                    mc.setAttr('%s.%s' % (tranc_Point, SdTransAttr), 0, 0, 0, type='double3')
            #当有凹凸连接时
            if BuC_V:
                mc.connectAttr(bumpPath, addmySd + '.normalCamera', force=True)
        #没有指定的链接或值时，给默认的相应材质球
        else:
            try:
                mc.hyperShade(assign = myCSd)
                mc.sets(e=True,forceElement = myCSd_SG)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % ObjectS)




def AllSdtoMyDiffuseSDorLgt_zwz(allSelShader,InputNode):
    MakeDiffuseV = InputNode.find('GammaCorrect')
    MakeLgtV = InputNode.find('Lgt')
    MakeLgt2V = InputNode.find('Lgt2')
    for each in allSelShader:
        mc.select(cl = True)
        try:
            type = mc.nodeType(each)
        except:
            print 'NoneType object is unsubscriptable'
        else:
            if type == 'mia_material_x' or type == 'mia_material' or type == 'mia_material_x_passes':
                SdTransAttr = 'diffuse'
                SdSpeAttr = 'refl_color'
            elif type == 'VRayMtl':
                SdTransAttr = 'color'
                SdSpeAttr =  'reflectionColor'
            else:
                SdTransAttr = 'color'
                SdSpeAttr = 'specularColor'
                sdAmAttr = 'ambientColor'
            if type =='layeredShader':
                NextLSD =[]
                del NextLSD[:]
                for i in range(1,15):
                    try:
                        myLColorOutV = mc.listConnections('%s.inputs[%s].%s'%(each,i,SdTransAttr), s=True, d=False, plugs=True)[0]
                    except:
                        pass
                    try:
                        myLColorOutV = mc.listConnections('%s.inputs[%s].%sR'%(each,i,SdTransAttr), s=True, d=False, plugs=True)[0]
                    except:
                        pass
                    if myLColorOutV:
                        myLConnect = myLColorOutV.split('.')[0]
                        if NextLSD.count('%s' % myLConnect) <= 0:
                            NextLSD.append(myLConnect)
                    if len(NextLSD):
                        AllSdtoMyDiffuseSDorLgt_zwz(NextLSD, InputNode)
            elif type == 'VRayMeshMaterial':
                connectNodes = mc.listConnections(each, c=True, d=False, s=True, scn=True)
                if connectNodes:
                    NextVMSD = []
                    del NextVMSD[:]
                    for tmpCon in connectNodes:
                        if tmpCon.find('shaders') >= 0:
                            tmpVMNode = mc.listConnections(tmpCon)[0]
                            NextVMSD.append(tmpVMNode)
                    AllSdtoMyDiffuseSDorLgt_zwz(NextVMSD, InputNode)
            else:
                temp = tmp = tep = tap =  0
                myLColorOutV=''
                myLSpeOutV=''
                myLAmOutV=''
                try:
                    myLColorOutV = mc.listConnections('%s.%s'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    temp = 1
                try:
                    myLColorOutV = mc.listConnections('%s.%sR'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    temp = 2
                try:
                    myLSpeOutV = mc.listConnections('%s.%s'%(each,SdSpeAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    tep = 1
                try:
                    myLSpeOutV= mc.listConnections('%s.%sR'%(each,SdSpeAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    tep = 2
                try:
                    myLAmOutV = mc.listConnections('%s.%s'%(each,sdAmAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    tap = 1
                try:
                    myLAmOutV= mc.listConnections('%s.%sR'%(each,sdAmAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    tap = 2
                #判断是否为hdr贴图，如果是不处理
                fileType = ''
                conNode = ''
                try:
                    conNode = mc.listConnections('%s.%s' % (each, SdTransAttr))
                except:
                    pass
                if conNode:
                    if mc.nodeType(conNode) == 'file':
                        pathName = mc.getAttr('%s.fileTextureName' % conNode[0])
                        fileType = string.lower(os.path.splitext(pathName)[-1])
                if myLColorOutV and myLColorOutV.find('GammaCorrect') < 0 and MakeDiffuseV >= 0 and fileType.find('hdr') < 0:
                    tmp = mc.duplicate(InputNode,upstreamNodes=1)[0]
                    if temp == 1:
                        mc.disconnectAttr(myLColorOutV,'%s.%s'%(each,SdTransAttr))
                        mc.connectAttr(myLColorOutV,'%s.value'%tmp)
                        mc.connectAttr('%s.outValue'%tmp,'%s.%s'%(each,SdTransAttr))
                    if temp == 2:
                        myLColorOutVG = mc.listConnections('%s.%sG'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                        myLColorOutVB = mc.listConnections('%s.%sB'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                        mc.disconnectAttr(myLColorOutV,'%s.%sR'%(each,SdTransAttr))
                        mc.disconnectAttr(myLColorOutVG,'%s.%sG'%(each,SdTransAttr))
                        mc.disconnectAttr(myLColorOutVB,'%s.%sB'%(each,SdTransAttr))
                        mc.connectAttr(myLColorOutV,'%s.valueX'%tmp)
                        mc.connectAttr(myLColorOutVG,'%s.valueY'%tmp)
                        mc.connectAttr(myLColorOutVB,'%s.valueZ'%tmp)
                        mc.connectAttr('%s.outValueX'%tmp,'%s.%sR'%(each,SdTransAttr))
                        mc.connectAttr('%s.outValueY'%tmp,'%s.%sG'%(each,SdTransAttr))
                        mc.connectAttr('%s.outValueZ'%tmp,'%s.%sB'%(each,SdTransAttr))
                if (MakeLgtV>=0) or (MakeLgt2V>=0):
                    if myLColorOutV:
                        if temp == 1:
                            mc.disconnectAttr(myLColorOutV,'%s.%s'%(each,SdTransAttr))
                        if temp == 2:
                            myLColorOutVG = mc.listConnections('%s.%sG'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                            myLColorOutVB = mc.listConnections('%s.%sB'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                            mc.disconnectAttr(myLColorOutV,'%s.%sR'%(each,SdTransAttr))
                            mc.disconnectAttr(myLColorOutVG,'%s.%sG'%(each,SdTransAttr))
                            mc.disconnectAttr(myLColorOutVB,'%s.%sB'%(each,SdTransAttr))
                    else:
                        try:
                            oldColorVRGB = mc.getAttr('%s.%s'%(each,SdTransAttr))
                        except:
                            sys.stdout.write('%s Shader hasn`t got %s' %(each,SdTransAttr))
                        else:
                            tmp='rgb_to_hsv(<<%s,%s,%s>>)'%(oldColorVRGB[0][0],oldColorVRGB[0][1],oldColorVRGB[0][2])
                            oldColorVHSV = mm.eval(tmp)
                            tmp='hsv_to_rgb(<<%f,%s,%f>>)'%(0, 0,oldColorVHSV[2])
                            newColorVRGB= mm.eval(tmp)
                            mc.setAttr('%s.%s'%(each,SdTransAttr), newColorVRGB[0], newColorVRGB[1], newColorVRGB[2],type='double3')
                    if myLSpeOutV:
                        if tep == 1:
                            mc.disconnectAttr(myLSpeOutV,'%s.%s'%(each,SdSpeAttr))
                        if tep == 2:
                            myLSpeOutVG = mc.listConnections('%s.%sG'%(each,SdSpeAttr), s=True, d=False, plugs=True)[0]
                            myLSpeOutVB = mc.listConnections('%s.%sB'%(each,SdSpeAttr), s=True, d=False, plugs=True)[0]
                            mc.disconnectAttr(myLSpeOutV,'%s.%sR'%(each,SdSpeAttr))
                            mc.disconnectAttr(myLSpeOutVG,'%s.%sG'%(each,SdSpeAttr))
                            mc.disconnectAttr(myLSpeOutVB,'%s.%sB'%(each,SdSpeAttr))
                    else:
                        try:
                            oldSpeVRGB = mc.getAttr('%s.%s'%(each,SdSpeAttr))
                        except:
                            sys.stdout.write('%s Shader hasn`t got %s\n' %(each,SdSpeAttr))
                        else:
                            tmp='rgb_to_hsv(<<%s,%s,%s>>)'%(oldSpeVRGB[0][0],oldSpeVRGB[0][1],oldSpeVRGB[0][2])
                            oldSpeVHSV = mm.eval(tmp)
                            tmp='hsv_to_rgb(<<%f,%s,%f>>)'%(0, 0,oldSpeVHSV[2])
                            newSpeVRGB= mm.eval(tmp)
                            mc.setAttr('%s.%s'%(each,SdSpeAttr), newSpeVRGB[0], newSpeVRGB[1], newSpeVRGB[2],type='double3')
                    if MakeLgt2V>=0:
                        if myLAmOutV:
                            if tap == 1:
                                mc.disconnectAttr(myLAmOutV,'%s.%s'%(each,sdAmAttr))
                            if tap == 2:
                                myLAmOutVG = mc.listConnections('%s.%sG'%(each,sdAmAttr), s=True, d=False, plugs=True)[0]
                                myLAmOutVB = mc.listConnections('%s.%sB'%(each,sdAmAttr), s=True, d=False, plugs=True)[0]
                                mc.disconnectAttr(myLAmOutV,'%s.%sR'%(each,sdAmAttr))
                                mc.disconnectAttr(myLAmOutVG,'%s.%sG'%(each,sdAmAttr))
                                mc.disconnectAttr(myLAmOutVB,'%s.%sB'%(each,sdAmAttr))
                        try:
                            mc.setAttr('%s.ambientColor'%each,0.0, 0.0, 0.0,type='double3')
                        except:
                            pass
                        try:
                            mc.setAttr('%s.specularColor'%each,0.0, 0.0, 0.0,type='double3')
                        except:
                            pass
                        try:
                            mc.setAttr('%s.reflectivity'%each,0)
                        except:
                            pass
                        try:
                            mc.setAttr('%s.incandescence'%each,0.0, 0.0, 0.0,type='double3')
                        except:
                            pass

def AllSdtoDelAmb_zwz(allSelShader):
    for each in allSelShader:
        mc.select(cl = True)
        type = mc.nodeType(each)
        if type == 'lambert' or type == 'blinn' or type == 'phong' or type == 'phongE' or 'layeredShader':
            SdTransAttr = 'color'
            SdAmbAttr = 'ambientColor'
            if type =='layeredShader':
                NextLSD =[]
                del NextLSD[:]
                for i in range(1,15):
                    try:
                        myLColorOutV = mc.listConnections('%s.inputs[%s].%s'%(each,i,SdTransAttr), s=True, d=False, plugs=True)[0]
                    except:
                        pass
                    try:
                        myLColorOutV = mc.listConnections('%s.inputs[%s].%sR'%(each,i,SdTransAttr), s=True, d=False, plugs=True)[0]
                    except:
                        pass
                    if myLColorOutV:
                        myLConnect = myLColorOutV.split('.')[0]
                        if NextLSD.count('%s'%myLConnect)<=0:
                            NextLSD.append(myLConnect)
                    if len(NextLSD):
                        AllSdtoDelAmb_zwz(NextLSD)
            else:
                temp = 0
                myLAmbOutV =''
                try:
                    myLAmbOutV = mc.listConnections('%s.%s'%(each,SdAmbAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    temp = 1
                try:
                    myLAmbOutV= mc.listConnections('%s.%sR'%(each,SdAmbAttr), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    temp = 2
                if  myLAmbOutV:
                    if temp == 1:
                        mc.disconnectAttr(myLAmbOutV,'%s.%s'%(each,SdAmbAttr))
                    if temp == 2:
                        myLAmbOutVG = mc.listConnections('%s.%sG'%(each,SdAmbAttr), s=True, d=False, plugs=True)[0]
                        myLAmbOutVB = mc.listConnections('%s.%sB'%(each,SdAmbAttr), s=True, d=False, plugs=True)[0]
                        mc.disconnectAttr(myLAmbOutV,'%s.%sR'%(each,SdAmbAttr))
                        mc.disconnectAttr(myLAmbOutVG,'%s.%sG'%(each,SdAmbAttr))
                        mc.disconnectAttr(myLAmbOutVB,'%s.%sB'%(each,SdAmbAttr))
        else:
            continue
        if not mc.objExists('ambientlight_Amb'):
            mc.ambientLight(name='ambientlight_Amb')
        allLight = mc.ls(type='light')
        for myLight in allLight:
            buffer = mc.listRelatives(myLight,parent = True,path=True)
            try:
                mc.setAttr('%s.visibility'%buffer[0],0)
            except:
                sys.stdout.write('%s can`t hide'%myLight )
        mc.setAttr('ambientlight_Amb.visibility',1)

def AssignArnold3SSd_zwz():
    mayaversions = mc.about(v=True)
    if not mayaversions.find('2009') >= 0:
        if not mc.pluginInfo('mtoa.mll', query=True, loaded=True):
            mc.loadPlugin('mtoa.mll')
    allObjects = mc.ls(sl=True)
    tmp = 0
    for eachObject in allObjects:
        eachObjectShape = mc.listRelatives(eachObject,pa=True)[0]
        typeShape = mc.nodeType(eachObjectShape)
        if typeShape != 'mesh' and typeShape != 'nurbsSurface' and typeShape != 'subdiv':
            mc.confirmDialog( title=u'警告', message=u'请选择实体模型!\n不要选择组或者其他!', button=['OK'], defaultButton='Yes', dismissString='No')
            tmp =1
            break
    if len(allObjects) and not tmp:
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'SSS_Ar':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(allObjects, n='SSS_Ar', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold',type='string')
        else:
            mc.editRenderLayerMembers('SSS_Ar',allObjects)
            mc.editRenderLayerGlobals(currentRenderLayer = 'SSS_Ar')
        my3sArnoldaiSkin = CreateMyArnold3SSd_zwz()[0]
        assignMy3sSd_zwz(my3sArnoldaiSkin,allObjects)

def AssignArnold3SMatteSd_zwz():
    mayaversions = mc.about(v=True)
    if not mayaversions.find('2009') >= 0:
        if not mc.pluginInfo('mtoa.mll', query=True, loaded=True):
            mc.loadPlugin('mtoa.mll')
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'SSS_Ar':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='SSS_Ar', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold',type='string')
        else:
            mc.editRenderLayerMembers('SSS_Ar',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'SSS_Ar')
    allFShader = SortallSelShader_zwz()
    vrShd_SG =allFShader[0]
    defaultShd_SG =allFShader[1]
    arnoldShd_SG = allFShader[2]
    otherShd_SG =allFShader[3]
    MyArnoldSD = CreateMyArnold3SSd_zwz()
    my3sStandMatte = MyArnoldSD[1]
    my3sStandMatte_SG = MyArnoldSD[2]
    my3sStandMatteC = MyArnoldSD[3]
    my3sStandMatteC_SG = MyArnoldSD[4]
    DeafSdtoMySD_zwz(my3sStandMatte,my3sStandMatte_SG,defaultShd_SG,my3sStandMatteC,my3sStandMatteC_SG)
    VraySdtoMySD_zwz(my3sStandMatte,my3sStandMatte_SG,vrShd_SG,my3sStandMatteC,my3sStandMatteC_SG)
    OtherSdMySD_zwz(my3sStandMatte,my3sStandMatte_SG,otherShd_SG,my3sStandMatteC,my3sStandMatteC_SG)
    arnoldShdMySD_zwz(my3sStandMatte,my3sStandMatte_SG,arnoldShd_SG,my3sStandMatteC,my3sStandMatteC_SG)


def AssignArnoldOCC_zwz():
    mayaversions = mc.about(v=True)
    if not mayaversions.find('2009') >= 0:
        if not mc.pluginInfo('mtoa.mll', query=True, loaded=True):
            mc.loadPlugin('mtoa.mll')
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'OCC_Ar':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='OCC_Ar', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold',type='string')
        else:
            mc.editRenderLayerMembers('OCC_Ar',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'OCC_Ar' )
    allFShader = SortallSelShader_zwz()
    vrShd_SG =allFShader[0]
    defaultShd_SG =allFShader[1]
    arnoldShd_SG = allFShader[2]
    otherShd_SG =allFShader[3]
    myArnoldOCCSd = CreateMyArnoldOCCSd_zwz()
    myArnoldOcc = myArnoldOCCSd[0]
    myArnoldOcc_SG = myArnoldOCCSd[1]
    myArnoldOccC = myArnoldOCCSd[2]
    myArnoldOccC_SG = myArnoldOCCSd[3]
    if len(defaultShd_SG):
        DeafSdtoMySD_zwz(myArnoldOcc,myArnoldOcc_SG,defaultShd_SG,myArnoldOccC,myArnoldOccC_SG)
    if len(vrShd_SG):
        VraySdtoMySD_zwz(myArnoldOcc,myArnoldOcc_SG,vrShd_SG,myArnoldOccC,myArnoldOccC_SG)
    if len(otherShd_SG):
        OtherSdMySD_zwz(myArnoldOcc,myArnoldOcc_SG,otherShd_SG,myArnoldOccC,myArnoldOccC_SG)
    if len(arnoldShd_SG):
        arnoldShdMySD_zwz(myArnoldOcc,myArnoldOcc_SG,arnoldShd_SG,myArnoldOccC,myArnoldOccC_SG)

def nameToNode_zwz( name ):
    selectionList = om.MSelectionList()
    selectionList.add( name )
    node = om.MObject()
    selectionList.getDependNode( 0, node )
    return node


def AssignMRDiffuse_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'Diffuse_MR':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='Diffuse_MR', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            allSelShader = SortallSelShader_zwz()[4]
            if not mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                mc.loadPlugin('Mayatomr.mll')
            if not mc.objExists('mentalrayGlobals'):
                mc.createNode('mentalrayGlobals', n='mentalrayGlobals')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay', type='string')
            mc.directionalLight(name='sunDirection')
            sunDirectionShape='sunDirectionShape'
            sunDirection = mc.listRelatives(sunDirectionShape, p=True)[0]
            mc.setAttr('%s.rotateX' % sunDirection, -75)
            mpsky = mc.shadingNode('mia_physicalsky', asUtility=True, n='mia_physicalsky1')
            mpsun = mc.shadingNode('mia_physicalsun', asUtility=True, n='mia_physicalsun1')
            mes = mc.shadingNode('mia_exposure_simple', n='mia_exposure_simple1', asUtility=True)
            attrFn = om.MFnMessageAttribute()
            at = attrFn.create('sunAndSkyShader', 'sass')
            obj = nameToNode_zwz('mentalrayGlobals')
            mg = om.MDGModifier()
            mg.addAttribute(obj, at)
            mg.doIt()
            at = attrFn.create('miSkyExposure', 'msEx')
            obj = nameToNode_zwz('mia_physicalsky1')
            mg = om.MDGModifier()
            mg.addAttribute(obj, at)
            mg.doIt()
            mc.connectAttr('%s.message' % mpsun, '%s.miLightShader' % sunDirectionShape, force=True)
            mc.connectAttr('%s.message' % mpsun, '%s.miPhotonEmitter' % sunDirectionShape, force=True)
            mc.connectAttr('%s.on' % mpsky, '%s.on' % mpsun, force=True)
            mc.connectAttr('%s.multiplier' % mpsky, '%s.multiplier' % mpsun, force=True)
            mc.connectAttr('%s.rgb_unit_conversion' % mpsky, '%s.rgb_unit_conversion' % mpsun, force=True)
            mc.connectAttr('%s.haze' % mpsky, '%s.haze' % mpsun, force=True)
            mc.connectAttr('%s.redblueshift' % mpsky, '%s.redblueshift' % mpsun, force=True)
            mc.connectAttr('%s.saturation' % mpsky, '%s.saturation' % mpsun, force=True)
            mc.connectAttr('%s.horizon_height' % mpsky, '%s.horizon_height' % mpsun, force=True)
            mc.connectAttr('%s.y_is_up' % mpsky, '%s.y_is_up' % mpsun, force=True)
            mc.connectAttr('%s.message' % sunDirection, '%s.sun' % mpsky, force=True)
            mc.connectAttr('%s.message' % mes, '%s.miSkyExposure' % mpsky, force=True)
            mc.connectAttr('%s.message' % mes, 'perspShape.mentalRayControls.miLensShader', force=True)
            mc.connectAttr('%s.message' % mpsky, 'perspShape.mentalRayControls.miEnvironmentShader', force=True)
            mc.connectAttr('%s.message' % mpsky, 'mentalrayGlobals.sunAndSkyShader', force=True)
            mc.setAttr('%s.gain' % mes, 0.2)
            mc.setAttr('%s.knee' % mes, 0.75)
            mc.setAttr('%s.compression' % mes, 3)
            mc.setAttr('%s.compression' % mes, 3)
            mc.setAttr('%s.y_is_up' % mpsky, 1)
            mc.setAttr('%s.use_background' % mpsky, 1)
            mc.createNode('mentalrayOptions', n='miDefaultOptions')
            mc.setAttr("miDefaultOptions.finalGather", 1)
            mc.setAttr("miDefaultOptions.minSamples", 0)
            mc.setAttr("miDefaultOptions.maxSamples", 2)
            mc.editRenderLayerAdjustment("miDefaultOptions.maxReflectionRays")
            mc.setAttr("miDefaultOptions.maxReflectionRays", 0)
            mc.setAttr("miDefaultOptions.maxRefractionRays", 3)
            mc.setAttr("miDefaultOptions.maxRayDepth", 6)
            mc.setAttr("miDefaultOptions.filter", 2)
            mc.setAttr("miDefaultOptions.filterWidth", 1)
            mc.setAttr("miDefaultOptions.filterHeight", 1)
        else:
            mc.editRenderLayerMembers('Diffuse_MR', slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'Diffuse_MR')
            allSelShader = SortallSelShader_zwz()[4]
        MyGammaCorrect = CreateMyGammaCorrect_zwz()
        allLight = mc.ls(type='light')
        for myLight in allLight:
            buffer = mc.listRelatives(myLight, parent=True, path=True)
            try:
                mc.setAttr('%s.visibility' % buffer[0], 0)
            except:
                sys.stdout.write('%s can`t hide' % myLight)
        if mc.objExists('sunDirection'):
            mc.delete('sunDirection')
        AllSdtoMyDiffuseSDorLgt_zwz(allSelShader, MyGammaCorrect)


def AssignVRayGamma_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        #allSelShader = SortallSelShader_zwz()[4]
        allSelShader = mc.ls(mat=True)
        try:
            allSelShader.remove('lambert1')
            allSelShader.remove('particleCloud1')
        except:
            pass
        MyVRGammaCorrect = CreateMyVRayGammaCorrect_zwz()
        #AllSdtoMyDiffuseSDorLgt_zwz(allSelShader, MyVRGammaCorrect)

def VrayAndHairShaderTo(allSelShader,  MyVRGammaCorrect):
        for each in allSelShader:
            mc.select(cl=True)
            try:
                type = mc.nodeType(each)
            except:
                print "None Type object is unsubscriptable"
            else:
                if type == 'layeredShader':
                    AllLayerShaderCon = mc.listAttr("%s.inputs" % each)
                    if AllLayerShaderCon:
                        NextLSD = []
                        AllLyaerShaderNode = []
                        for eachLayerCon in AllLayerShaderCon:
                            if eachLayerCon.find('.') < 0:
                                AllLyaerShaderNode.append(eachLayerCon)
                        for eachLayerNode in AllLyaerShaderNode:
                            try:
                                myLColorOutV = mc.listConnections('%s.%s.color'%(each, eachLayerNode), s=True, d=False, plugs=True)[0]
                            except:
                                pass
                            try:
                                myLColorOutV = mc.listConnections('%s.inputs[%s].colorR'%(each, eachLayerNode), s=True, d=False, plugs=True)[0]
                            except:
                                pass
                            if myLColorOutV:
                                myLConnect = myLColorOutV.split('.')[0]
                                if NextLSD.count('%s' % myLConnect) <= 0:
                                    NextLSD.append(myLConnect)
                            if len(NextLSD):
                                VrayAndHairShaderTo(NextLSD, MyVRGammaCorrect)
                    elif type == 'VRayMeshMaterial':
                        connectNodes = mc.listConnections(each, c=True, d=False, s=True, scn=True)
                        if connectNodes:
                            NextVMSD = []
                            for tmpCon in connectNodes:
                                if tmpCon.find('shaders') >= 0:
                                    tmpVMNode = mc.listConnections(tmpCon)[0]
                                    NextVMSD.append(tmpVMNode)
                            VrayAndHairShaderTo(NextVMSD, MyVRGammaCorrect)
                    elif type == "VRayMtl":
                        SdTransAttr = 'color'
                        SdSpeAttr = 'reflectionColor'
                        temp = tmp = tep = tap =  0
                        myLColorOutV=''
                        myLSpeOutV=''
                        myLAmOutV=''
                        try:
                            myLColorOutV = mc.listConnections('%s.%s'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                        except:
                            pass
                        else:
                            temp = 1
                        try:
                            myLColorOutV = mc.listConnections('%s.%sR'%(each,SdTransAttr), s=True, d=False, plugs=True)[0]
                        except:
                            pass
                        else:
                            temp = 2
                        try:
                            myLSpeOutV = mc.listConnections('%s.%s'%(each,SdSpeAttr), s=True, d=False, plugs=True)[0]
                        except:
                            pass
                        else:
                            tep = 1
                        try:
                            myLSpeOutV= mc.listConnections('%s.%sR'%(each,SdSpeAttr), s=True, d=False, plugs=True)[0]

def DelAllMyGamma_zwz():
    allVrayGammaCorrects = mc.ls('*MyVRayGammaCorrect*', type='gammaCorrect')
    for myGamma in allVrayGammaCorrects:
        if myGamma != 'MyVRayGammaCorrect':
            temp = 1
            connectOutNode=''
            tmpConNode = mc.listConnections('%s.outValue' % myGamma, s=False, d=True, plugs=True)
            if tmpConNode:
                connectOutNode = tmpConNode[0]
                temp = 1
            else:
                connectOutNode = mc.listConnections('%s.outValueX' % myGamma, s=False, d=True, plugs=True)[0]
                temp = 2
            if temp == 1:
                connectInNode = mc.listConnections('%s.value' % myGamma, s=True, d=False, plugs=True)[0]
                mc.disconnectAttr('%s.outValue' % myGamma, connectOutNode)
                mc.disconnectAttr(connectInNode, '%s.value' % myGamma)
                mc.connectAttr(connectInNode, connectOutNode)
            else:
                connectOutYNode = mc.listConnections('%s.outValueY' % myGamma, s=False, d=True, plugs=True)[0]
                connectOutZNode = mc.listConnections('%s.outValueZ' % myGamma, s=False, d=True, plugs=True)[0]
                connectInXNode = mc.listConnections('%s.valueX' % myGamma, s=True, d=False, plugs=True)[0]
                connectInYNode = mc.listConnections('%s.valueY' % myGamma, s=True, d=False, plugs=True)[0]
                connectInZNode = mc.listConnections('%s.valueZ' % myGamma, s=True, d=False, plugs=True)[0]
                mc.disconnectAttr('%s.outValueX' % myGamma, connectOutNode)
                mc.disconnectAttr('%s.outValueY' % myGamma, connectOutYNode)
                mc.disconnectAttr('%s.outValueZ' % myGamma, connectOutZNode)
                mc.disconnectAttr(connectInXNode, '%s.valueX' % myGamma)
                mc.disconnectAttr(connectInYNode, '%s.valueY' % myGamma)
                mc.disconnectAttr(connectInZNode, '%s.valueZ' % myGamma)
                mc.connectAttr(connectInXNode, connectOutNode)
                mc.connectAttr(connectInYNode, connectOutNode)
                mc.connectAttr(connectInZNode, connectOutNode)
    mc.delete(allVrayGammaCorrects)


def AssignMRLgt_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'Lgt_MR':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='Lgt_MR', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            if not  mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                mc.loadPlugin('Mayatomr.mll')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay',type='string')
            allSelShader = SortallSelShader_zwz()[4]
            if not mc.objExists('miDefaultOptions'):
                mc.createNode('mentalrayOptions', n='miDefaultOptions')
                mc.setAttr("miDefaultOptions.minSamples",0)
                mc.setAttr("miDefaultOptions.maxSamples",2)
                mc.setAttr("miDefaultOptions.maxReflectionRays",3)
                mc.setAttr("miDefaultOptions.maxRefractionRays",3)
                mc.setAttr("miDefaultOptions.maxRayDepth",6)
                mc.setAttr("miDefaultOptions.maxShadowRayDepth",6)
                mc.setAttr("miDefaultOptions.filter",2)
                mc.setAttr("miDefaultOptions.filterWidth",1)
                mc.setAttr("miDefaultOptions.filterHeight",1)
        else:
            mc.editRenderLayerMembers('Lgt_MR',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'Lgt_MR' )
            allSelShader = SortallSelShader_zwz()[4]
        AllSdtoMyDiffuseSDorLgt_zwz(allSelShader,'Lgt')

def AssignMRLgt2_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'Lgt_MR':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='Lgt_MR', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            if not  mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                mc.loadPlugin('Mayatomr.mll')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay',type='string')
            allSelShader = SortallSelShader_zwz()[4]
            if not mc.objExists('miDefaultOptions'):
                mc.createNode('mentalrayOptions', n='miDefaultOptions')
                mc.setAttr("miDefaultOptions.minSamples",0)
                mc.setAttr("miDefaultOptions.maxSamples",2)
                mc.setAttr("miDefaultOptions.maxReflectionRays",3)
                mc.setAttr("miDefaultOptions.maxRefractionRays",3)
                mc.setAttr("miDefaultOptions.maxRayDepth",6)
                mc.setAttr("miDefaultOptions.maxShadowRayDepth",6)
                mc.setAttr("miDefaultOptions.filter",2)
                mc.setAttr("miDefaultOptions.filterWidth",1)
                mc.setAttr("miDefaultOptions.filterHeight",1)
        else:
            mc.editRenderLayerMembers('Lgt_MR',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'Lgt_MR' )
            allSelShader = SortallSelShader_zwz()[4]
        AllSdtoMyDiffuseSDorLgt_zwz(allSelShader,'Lgt2')

def AssignSWDepth_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'Depth_SW':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='Depth_SW', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware',type='string')
            allFShader = SortallSelShader_zwz()
            myLam_out = CreatMyDepthSd_zwz()
            mc.ambientLight(ambientShade = 0, name='ambientlight_Depth')
            amLightShape='ambientlight_DepthShape'
            amLight =  mc.listRelatives(amLightShape,parent = True,path=True)
        else:
            mc.editRenderLayerMembers('Depth_SW',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'Depth_SW' )
            allFShader = SortallSelShader_zwz()
            myLam_out = CreatMyDepthSd_zwz()
        myLam = myLam_out[0]
        myLam_SG = myLam_out[1]
        myCLam = myLam_out[2]
        myCLam_SG = myLam_out[3]
        mydepLocator = myLam_out[4]
        vrShd_SG =allFShader[0]
        defaultShd_SG =allFShader[1]
        arnoldShd_SG = allFShader[2]
        otherShd_SG =allFShader[3]
        if len(defaultShd_SG):
            DeafSdtoMySD_zwz(myLam,myLam_SG,defaultShd_SG,myCLam,myCLam_SG)
        if len(vrShd_SG):
            VraySdtoMySD_zwz(myLam,myLam_SG,vrShd_SG,myCLam,myCLam_SG)
        if len(arnoldShd_SG):
            arnoldShdMySD_zwz(myLam,myLam_SG,arnoldShd_SG,myCLam,myCLam_SG)
        if len(otherShd_SG):
            OtherSdMySD_zwz(myLam,myLam_SG,otherShd_SG,myCLam,myCLam_SG)
        allLight = mc.ls(type='light')
        for myLight in allLight:
            buffer = mc.listRelatives(myLight,parent = True,path=True)
            try:
                mc.setAttr('%s.visibility'%buffer[0],0)
            except:
                sys.stdout.write('%s can`t hide'%myLight )
        mc.setAttr('ambientlight_Depth.visibility',1)
        allMyMDs = mc.ls(type='multiplyDivide')
        for allMyMD in allMyMDs:
            if allMyMD.find('my_depth_multiplyDivide') >= 0:
                if str(allMyMD)=='my_depth_multiplyDivide':
                    continue
                try:
                    mc.connectAttr('%s.Depth_V'%mydepLocator,'%s.input2X'%allMyMD,force = True)
                except:
                    sys.stdout.write('%s.Depth_V is already connected to %s.input2X'%(mydepLocator,allMyMD))
        allMyMDSet = mc.ls(type='setRange')
        for MyMDSet in allMyMDSet:
            if MyMDSet.find('my_depth_setRange') >= 0:
                if str(MyMDSet)=='my_depth_multiplyDivide':
                    continue
                try:
                    mc.connectAttr('%s.Depth_Max_V'%mydepLocator,'%s.oldMaxX'%MyMDSet,force = True)
                except:
                    sys.stdout.write('%s.Depth_Max_V is already connected to %s.input2X'%(mydepLocator,MyMDSet))
        mc.select(cl = True)
        mc.select('DepthV_Locator')

def AssignSWAmb_zwz():
    allSelShader = mc.ls(materials = True)
    AllSdtoDelAmb_zwz(allSelShader)

def AssignSWRGBA_Tran_zwz(i):
    slObject = mc.ls(sl=True)
    myRGBALam = myRGBACLam = myRGBACLam_SG =''
    if len(slObject):
        # allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        # layerLive = 0
        # for Layer in allLayer:
        #     if Layer == 'RGBA_SW':
        #         layerLive = 1
        # if not layerLive:
        #     my_Depth=mc.createRenderLayer(slObject, n='RGBA_SW', mc=True, num=1, nr=True)
        #     mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
        #     mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware',type='string')
        #     allFShader = SortallSelShader_zwz()
        #     myRGBALam_out = CreatMyRGBASd_zwz()
        # else:
        #     mc.editRenderLayerMembers('RGBA_SW',slObject)
        #     mc.editRenderLayerGlobals(currentRenderLayer = 'RGBA_SW' )
        #     allFShader = SortallSelShader_zwz()
        #     myRGBALam_out = CreatMyRGBASd_zwz()
        allFShader = SortallSelShader_zwz()
        myRGBALam_out = CreatMyRGBASd_zwz()
        myRGBALam = myRGBALam_out[0+i*4]
        myRGBALam_SG = myRGBALam_out[1+i*4]
        myRGBACLam = myRGBALam_out[2+i*4]
        myRGBACLam_SG = myRGBALam_out[3+i*4]
        vrShd_SG =allFShader[0]
        defaultShd_SG =allFShader[1]
        arnoldShd_SG = allFShader[2]
        otherShd_SG =allFShader[3]
        allMyShapes = allFShader[5]
        if len(defaultShd_SG ):
            DeafSdtoMySD_zwz(myRGBALam,myRGBALam_SG,defaultShd_SG ,myRGBACLam,myRGBACLam_SG,allMyShapes)
        if len(vrShd_SG):
            VraySdtoMySD_zwz(myRGBALam,myRGBALam_SG,vrShd_SG ,myRGBACLam,myRGBACLam_SG,allMyShapes)
        if len(arnoldShd_SG ):
            arnoldShdMySD_zwz(myRGBALam,myRGBALam_SG,arnoldShd_SG ,myRGBACLam,myRGBACLam_SG,allMyShapes)
        if len(otherShd_SG ):
            OtherSdMySD_zwz(myRGBALam,myRGBALam_SG,otherShd_SG ,myRGBACLam,myRGBACLam_SG,allMyShapes)
        # allLight = mc.ls(type='light')
        # for myLight in allLight:
        #     buffer = mc.listRelatives(myLight,parent = True,path=True)
        #     try:
        #         mc.setAttr('%s.visibility'%buffer[0],0)
        #     except:
        #         sys.stdout.write('%s can`t hide'%myLight )
        mc.select(cl = True)

def AssignSWMatte_Tran_zwz(i):
    slObject = mc.ls(sl=True)
    myRGBALam = myRGBACLam = myRGBACLam_SG =''
    if len(slObject):
        allFShader = SortallSelShader_zwz()
        myRGBALam_out = CreatMyRGBASd_zwz()
        myRGBALam = myRGBALam_out[0+i*4]
        myRGBALam_SG = myRGBALam_out[1+i*4]
        myRGBACLam = myRGBALam_out[2+i*4]
        myRGBACLam_SG = myRGBALam_out[3+i*4]
        vrShd_SG =allFShader[0]
        defaultShd_SG =allFShader[1]
        arnoldShd_SG = allFShader[2]
        otherShd_SG =allFShader[3]
        allMyShapes = allFShader[5]
        if len(defaultShd_SG):
            DeafSdtoMySD_zwz(myRGBALam,myRGBALam_SG,defaultShd_SG,myRGBACLam,myRGBACLam_SG,allMyShapes)
        if len(vrShd_SG):
            VraySdtoMySD_zwz(myRGBALam,myRGBALam_SG,vrShd_SG,myRGBACLam,myRGBACLam_SG,allMyShapes)
        if len(arnoldShd_SG):
            arnoldShdMySD_zwz(myRGBALam,myRGBALam_SG,arnoldShd_SG,myRGBACLam,myRGBACLam_SG,allMyShapes)
        if len(otherShd_SG):
            OtherSdMySD_zwz(myRGBALam,myRGBALam_SG,otherShd_SG,myRGBACLam,myRGBACLam_SG,allMyShapes)
        mc.select(cl = True)

def AssignSWRGBA_zwz(i):
    slObject = mc.ls(sl=True)
    if len(slObject):
        # allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        # layerLive = 0
        # for Layer in allLayer:
        #     if Layer == 'RGBA_SW':
        #         layerLive = 1
        # if not layerLive:
        #     mc.createRenderLayer(slObject, n='RGBA_SW', mc=True, num=1, nr=True)
        #     mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
        #     mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware',type='string')
        #     myRGBALam_out = CreatMyRGBASd_zwz()
        # else:
        #     mc.editRenderLayerMembers('RGBA_SW',slObject)
        #     mc.editRenderLayerGlobals(currentRenderLayer = 'RGBA_SW' )
        #     myRGBALam_out = CreatMyRGBASd_zwz()
        myRGBALam_out = CreatMyRGBASd_zwz()
        myRGBACLam = myRGBALam_out[2+i*4]
        myRGBACLam_SG = myRGBALam_out[3+i*4]
        mc.select(slObject)
        mc.hyperShade(assign = myRGBACLam)
        mc.sets(e=True,forceElement = myRGBACLam_SG)
        # allLight = mc.ls(type='light')
        # for myLight in allLight:
        #     buffer = mc.listRelatives(myLight,parent = True,path=True)
        #     try:
        #         mc.setAttr('%s.visibility'%buffer[0],0)
        #     except:
        #         sys.stdout.write('%s can`t hide'%myLight )
        mc.select(cl = True)

def AssignSWMatte_zwz(i):
    slObject = mc.ls(sl=True)
    if len(slObject):
        myRGBALam_out = CreatMyRGBASd_zwz()
        myRGBACLam = myRGBALam_out[2+i*4]
        myRGBACLam_SG = myRGBALam_out[3+i*4]
        mc.select(slObject)
        mc.hyperShade(assign = myRGBACLam)
        mc.sets(e=True,forceElement = myRGBACLam_SG)
        mc.select(cl = True)

def AssignRimSur_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'RIM_MR':
                layerLive = 1
        if not layerLive:
            allFShader = SortallSelShader_zwz()
            mc.createRenderLayer(slObject, n='RIM_MR', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            if not  mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                mc.loadPlugin('Mayatomr.mll')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay',type='string')
            if not mc.objExists('miDefaultOptions'):
                mc.createNode('mentalrayOptions', n='miDefaultOptions')
            mc.setAttr("miDefaultOptions.minSamples",0)
            mc.setAttr("miDefaultOptions.maxSamples",2)
            mc.setAttr("miDefaultOptions.maxReflectionRays",3)
            mc.setAttr("miDefaultOptions.maxRefractionRays",3)
            mc.setAttr("miDefaultOptions.maxRayDepth",6)
            mc.setAttr("miDefaultOptions.maxShadowRayDepth",6)
            mc.setAttr("miDefaultOptions.filter",2)
            mc.setAttr("miDefaultOptions.filterWidth",1)
            mc.setAttr("miDefaultOptions.filterHeight",1)
            MyRimSurSd_out = CreateMyRimSurSd_zwz()
        else:
            mc.editRenderLayerMembers('RIM_MR',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'RIM_MR' )
            allFShader = SortallSelShader_zwz()
            MyRimSurSd_out = CreateMyRimSurSd_zwz()
        MyRimSur= MyRimSurSd_out[0]
        MyRimSur_SG = MyRimSurSd_out[1]
        MyRimSurC= MyRimSurSd_out[2]
        MyRimSurC_SG = MyRimSurSd_out[3]
        vrShd_SG =allFShader[0]
        defaultShd_SG =allFShader[1]
        arnoldShd_SG = allFShader[2]
        otherShd_SG =allFShader[3]
        if len(defaultShd_SG):
            DeafSdtoMySD_zwz(MyRimSur,MyRimSur_SG,defaultShd_SG,MyRimSurC,MyRimSurC_SG)
        if len(vrShd_SG):
            VraySdtoMySD_zwz(MyRimSur,MyRimSur_SG,vrShd_SG,MyRimSurC,MyRimSurC_SG)
        if len(arnoldShd_SG):
            arnoldShdMySD_zwz(MyRimSur,MyRimSur_SG,arnoldShd_SG,MyRimSurC,MyRimSurC_SG)
        if len(otherShd_SG):
            OtherSdMySD_zwz(MyRimSur,MyRimSur_SG,otherShd_SG,MyRimSurC,MyRimSurC_SG)
        allLight = mc.ls(type='light')
        for myLight in allLight:
            buffer = mc.listRelatives(myLight,parent = True,path=True)
            try:
                mc.setAttr('%s.visibility'%buffer[0],0)
            except:
                sys.stdout.write('%s can`t hide'%myLight )
        mc.select(cl = True)

def AssignLamLam_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        # allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        # layerLive = 0
        # for Layer in allLayer:
        #     if Layer == 'Lam_Mr':
        #         layerLive = 1
        # if not layerLive:
        #     mc.createRenderLayer(slObject, n='Lam_Mr', mc=True, num=1, nr=True)
        #     mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
        #     if not  mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
        #         mc.loadPlugin('Mayatomr.mll')
        #     mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay',type='string')
        #     if not mc.objExists('miDefaultOptions'):
        #         mc.createNode('mentalrayOptions', n='miDefaultOptions')
        #     mc.setAttr("miDefaultOptions.minSamples",0)
        #     mc.setAttr("miDefaultOptions.maxSamples",2)
        #     mc.setAttr("miDefaultOptions.maxReflectionRays",3)
        #     mc.setAttr("miDefaultOptions.maxRefractionRays",3)
        #     mc.setAttr("miDefaultOptions.maxRayDepth",6)
        #     mc.setAttr("miDefaultOptions.maxShadowRayDepth",6)
        #     mc.setAttr("miDefaultOptions.filter",2)
        #     mc.setAttr("miDefaultOptions.filterWidth",1)
        #     mc.setAttr("miDefaultOptions.filterHeight",1)
        #     allFShader = SortallSelShader_zwz()
        #     MyLamLamSd_out = CreateMyLamLamSd_zwz()
        # else:
        #     mc.editRenderLayerMembers('Lam_Mr',slObject)
        #     mc.editRenderLayerGlobals(currentRenderLayer = 'Lam_Mr' )
        #     allFShader = SortallSelShader_zwz()
        #     MyLamLamSd_out = CreateMyLamLamSd_zwz()
        allFShader = SortallSelShader_zwz()
        MyLamLamSd_out = CreateMyLamLamSd_zwz()
        MyLamLam= MyLamLamSd_out[0]
        MyLamLam_SG = MyLamLamSd_out[1]
        MyLamLamC= MyLamLamSd_out[2]
        MyLamLamC_SG = MyLamLamSd_out[3]
        vrShd_SG =allFShader[0]
        defaultShd_SG =allFShader[1]
        arnoldShd_SG = allFShader[2]
        otherShd_SG =allFShader[3]
        if len(defaultShd_SG):
            DeafSdtoMySD_zwz(MyLamLam,MyLamLam_SG,defaultShd_SG,MyLamLamC,MyLamLamC_SG)
        if len(vrShd_SG):
            VraySdtoMySD_zwz(MyLamLam,MyLamLam_SG,vrShd_SG,MyLamLamC,MyLamLamC_SG)
        if len(arnoldShd_SG):
            arnoldShdMySD_zwz(MyLamLam,MyLamLam_SG,arnoldShd_SG,MyLamLamC,MyLamLamC_SG)
        if len(otherShd_SG):
            OtherSdMySD_zwz(MyLamLam,MyLamLam_SG,otherShd_SG,MyLamLamC,MyLamLamC_SG)
        # allLight = mc.ls(type='light')
        # for myLight in allLight:
        #     buffer = mc.listRelatives(myLight,parent = True,path=True)
        #     try:
        #         mc.setAttr('%s.visibility'%buffer[0],0)
        #     except:
        #         sys.stdout.write('%s can`t hide'%myLight )
        mc.select(cl = True)

def AssignProjectRamp():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allFShader = SortallSelShader_zwz()
        if allFShader:
            MyLamLamSd_out = CreateMyRampLamSd_zwz()
            MyLamLam= MyLamLamSd_out[0]
            MyLamLam_SG = MyLamLamSd_out[1]
            MyLamLamC= MyLamLamSd_out[2]
            MyLamLamC_SG = MyLamLamSd_out[3]
            vrShd_SG =allFShader[0]
            defaultShd_SG =allFShader[1]
            arnoldShd_SG = allFShader[2]
            otherShd_SG =allFShader[3]
            if len(defaultShd_SG):
                DeafSdtoMySD_zwz(MyLamLam,MyLamLam_SG,defaultShd_SG,MyLamLamC,MyLamLamC_SG)
            if len(vrShd_SG):
                VraySdtoMySD_zwz(MyLamLam,MyLamLam_SG,vrShd_SG,MyLamLamC,MyLamLamC_SG)
            if len(arnoldShd_SG):
                arnoldShdMySD_zwz(MyLamLam,MyLamLam_SG,arnoldShd_SG,MyLamLamC,MyLamLamC_SG)
            if len(otherShd_SG):
                OtherSdMySD_zwz(MyLamLam,MyLamLam_SG,otherShd_SG,MyLamLamC,MyLamLamC_SG)
            mc.select(cl = True)

            myProjection = CreateMyProjectionRamp_zwz()
            myLams = mc.ls('*my_Ramp_Lam*',type="lambert")
            if myLams:
                for each in myLams:
                    if each != "my_Ramp_Lam":
                        try:
                            mc.connectAttr('%s.outColor' % myProjection, '%s.color' % each,force=True)
                        except:
                            pass


def ChangeObjectOpaque_zwz(TranV):
    #赛选被选物体，把类型为‘mesh’或‘nur'或‘sub’的shapes归为一组
    allMyShapes =[]
    allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
    for Shape in allShapes:
        ShapeType = mc.nodeType(Shape)
        if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
            allMyShapes.append(Shape)
    del allShapes
    if allMyShapes:
        for ObjectShap in allMyShapes:
            try:
                temp = mc.getAttr('%s.aiOpaque'%ObjectShap)
            except:
                mc.warning(u"没有开启mtoa插件")
            else:
                currentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
                if TranV and not temp:
                    if currentLayer != 'defaultRenderLayer':
                        mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectShap)
                    try:
                        mc.setAttr('%s.aiOpaque'%ObjectShap,TranV)
                    except:
                        print 'This %s hasn`t aiOpaque'%ObjectShap
                if not TranV and temp:
                    if currentLayer != 'defaultRenderLayer':
                        mc.editRenderLayerAdjustment('%s.aiOpaque'%ObjectShap)
                    try:
                        mc.setAttr('%s.aiOpaque'%ObjectShap,TranV)
                    except:
                        print 'This %s hasn`t aiOpaque'%ObjectShap

def ChangeGammaCorrectValue_zwz(i):
    if i==1:
        GammaValue =mc.textField('GCValue', query = 1, text = 1)
        allUGammaCorrects= mc.ls('*MyGammaCorrect*', type='gammaCorrect')
    else:
        GammaValue =mc.textField('GCVRayValue', query = 1, text = 1)
        allUGammaCorrects= mc.ls('*MyVRayGammaCorrect*', type='gammaCorrect')
    for UGammaCorrect in allUGammaCorrects:
        mc.setAttr("%s.gammaX"%UGammaCorrect,float(GammaValue))
        mc.setAttr("%s.gammaY"%UGammaCorrect,float(GammaValue))
        mc.setAttr("%s.gammaZ"%UGammaCorrect,float(GammaValue))

def OCT_ChangeShadeOpacityMode_zwz(myMode):
    currentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
    allMyMaterials=''
    if currentLayer == 'defaultRenderLayer':
        mc.confirmDialog( title='warning', message=u'不允许在masterLayer操作', button='OK', defaultButton='OK' )
    else:
        if myMode == 3:
            allMyMaterials = mc.ls(materials = True)
            mc.select(allMyMaterials)
        else:
            allMyMaterials = mc.ls(sl = True,materials = True)
            if not allMyMaterials:
                mc.confirmDialog( title='warning', message=u'没有材质球被选择', button='OK', defaultButton='OK' )
            else:
                for MyMaterial in allMyMaterials:
                    if MyMaterial != 'particleCloud1':
                        try:
                            mc.editRenderLayerAdjustment('%s.matteOpacityMode'%MyMaterial)
                        except:
                            pass
                        else:
                            mc.setAttr("%s.matteOpacityMode"%MyMaterial,myMode)

def AssignMrOcc_zwz():
    slObject = mc.ls(sl=True)
    if len(slObject):
        allLayer = mc.listConnections("renderLayerManager.renderLayerId")
        layerLive = 0
        for Layer in allLayer:
            if Layer == 'Occ_Mr':
                layerLive = 1
        if not layerLive:
            mc.createRenderLayer(slObject, n='Occ_Mr', mc=True, num=1, nr=True)
            mc.editRenderLayerAdjustment("defaultRenderGlobals.currentRenderer")
            allFShader = SortallSelShader_zwz()
            if not  mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                mc.loadPlugin('Mayatomr.mll')
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mentalRay',type='string')
            if not mc.objExists('mentalrayGlobals'):
                mc.createNode('mentalrayGlobals', n='mentalrayGlobals')
            if not mc.objExists('miDefaultOptions'):
                mc.createNode('mentalrayOptions', n='miDefaultOptions')
            if not mc.objExists('mentalrayItemsList'):
                mc.createNode('mentalrayItemsList', n='mentalrayItemsList')
            try:
                cmd='connectAttr -f "miDefaultOptions.message" "mentalrayGlobals.options";\nconnectAttr -f "mentalrayGlobals.message" "mentalrayItemsList.globals";\nconnectAttr -f "miDefaultOptions.message" "mentalrayItemsList.options[0]";\n'
                mm.eval(cmd)
            except:
                pass

            mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
            mc.setAttr('miDefaultOptions.rayTracing',1)
            mc.editRenderLayerAdjustment('miDefaultOptions.minSamples')
            mc.setAttr('miDefaultOptions.minSamples', 0)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxSamples')
            mc.setAttr('miDefaultOptions.maxSamples',2)
            mc.editRenderLayerAdjustment('miDefaultOptions.filter')
            mc.setAttr('miDefaultOptions.filter',1)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
            mc.setAttr('miDefaultOptions.maxReflectionRays',10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
            mc.setAttr('miDefaultOptions.maxRefractionRays',10)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
            mc.setAttr('miDefaultOptions.maxRayDepth',20)
            mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
            mc.setAttr('miDefaultOptions.maxShadowRayDepth',2)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGather')
            mc.setAttr('miDefaultOptions.finalGather',True)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherTraceReflection')
            mc.setAttr('miDefaultOptions.finalGatherTraceReflection',4)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherTraceRefraction')
            mc.setAttr('miDefaultOptions.finalGatherTraceRefraction',4)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherTraceDepth')
            mc.setAttr('miDefaultOptions.finalGatherTraceDepth',8)
            mc.editRenderLayerAdjustment('miDefaultOptions.contrastR')
            mc.setAttr('miDefaultOptions.contrastR', 0.01)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherRays')
            mc.setAttr("miDefaultOptions.finalGatherRays", 150)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherPresampleDensity')
            mc.setAttr("miDefaultOptions.finalGatherPresampleDensity", 6)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherFalloffStop')
            mc.setAttr("miDefaultOptions.finalGatherFalloffStop",1)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherMode')
            mc.setAttr("miDefaultOptions.finalGatherMode",1)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherMaxRadius')
            mc.setAttr("miDefaultOptions.finalGatherMaxRadius",0.01)
            mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherMinRadius')
            mc.setAttr("miDefaultOptions.finalGatherMinRadius",0.001)
            
            MyLamLamSd_out = creatDeafMrOccSD_zwz()
        else:
            mc.editRenderLayerMembers('Occ_Mr',slObject)
            mc.editRenderLayerGlobals(currentRenderLayer = 'Occ_Mr' )
            allFShader = SortallSelShader_zwz()
            MyLamLamSd_out = creatDeafMrOccSD_zwz()
        myMrOcc= MyLamLamSd_out[0]
        myMrOcc_SG = MyLamLamSd_out[1]
        vrShd_SG =allFShader[0]
        defaultShd_SG =allFShader[1]
        arnoldShd_SG = allFShader[2]
        otherShd_SG =allFShader[3]
        if len(defaultShd_SG):
            DeafSdtoMySD_zwz(myMrOcc,myMrOcc_SG,defaultShd_SG,myMrOcc,myMrOcc_SG)
        if len(vrShd_SG):
            VraySdtoMySD_zwz(myMrOcc,myMrOcc_SG,vrShd_SG,myMrOcc,myMrOcc_SG)
        if len(arnoldShd_SG):
            arnoldShdMySD_zwz(myMrOcc,myMrOcc_SG,arnoldShd_SG,myMrOcc,myMrOcc_SG)
        if len(otherShd_SG):
            OtherSdMySD_zwz(myMrOcc,myMrOcc_SG,otherShd_SG,myMrOcc,myMrOcc_SG)
        allLight = mc.ls(type='light')
        for myLight in allLight:
            buffer = mc.listRelatives(myLight,parent = True,path=True)
            try:
                mc.setAttr('%s.visibility'%buffer[0],0)
            except:
                sys.stdout.write('%s can`t hide'%myLight )
        mc.select(cl = True)


def getMateriaInfo_zwz(shaderNode):
    try:
        myConnections = mc.listConnections('%s.message' % shaderNode)
    except:
        pass
    else:
        for item in myConnections:
            if mc.objectType(item) == 'materialInfo':
                return item
    return ''


def disconnectMaterialInfo_zwz(shaderNode):
    materialInfoNode = getMateriaInfo_zwz(shaderNode)
    if not materialInfoNode:
        return
    mc.disconnectAttr('%s.message' % shaderNode, '%s.material' % materialInfoNode)


def changeMaterial_zwz(shaderNode, replaceType):
    replaceNode = mc.createNode(replaceType)
    disconnectMaterialInfo_zwz(shaderNode)

    model = 0
    modeType = mc.nodeType(shaderNode)
    if modeType == 'VRayMtl' or modeType == 'VRayLightMtl':
        model = 1
        if modeType == 'VRayMtl':
            tranPoint = 'transparency'
            tranThreePoint = 'opacityMap'
        elif modeType == 'VRayLightMtl':
            tranPoint = 'opacity'
            tranThreePoint = 'opacity.opacity'
    elif modeType == 'VRayBumpMtl' or modeType == 'VRayBlendMtl' or modeType == 'VRayMtl2Sided' or modeType == 'VRayMtlWrapper':
        model = 2
    if model == 1:
        TrC_V = 0
        TrV_V = 0
        #透明链接; TrV_V：
        tmp = 0
        try:
            tmp = mc.listConnections('%s.%s' % (shaderNode, tranPoint), s=True, d=False, plugs=True)
        except:
            pass
        if tmp:
            tranC_Type = 1
            transPath = tmp[0]
            TrC_V = 1
        else:
            try:
                tmp = mc.listConnections('%s.%sR' % (shaderNode, tranThreePoint), s=True, d=False, plugs=True)
            except:
                pass
            if tmp:
                tranC_Type = 2
                transPath = tmp[0]
                TrC_V = 1
            else:
                #判断是否具有透明值
                try:
                    transValue = mc.getAttr('%s.%s' % (shaderNode, tranPoint))
                except:
                    pass
                else:
                    if transValue[0][0] != 1 or transValue[0][1] != 1 or transValue[0][2] != 1:
                        TrV_V = 1

        if TrC_V == 1 or TrV_V == 1:
            if TrC_V == 1:
                opacityNode = transPath.split('.')[0]
                opcityType = mc.nodeType(opacityNode)
                #当透明节点是文件时
                if opcityType == 'file':
                    VmyInv = mc.getAttr('%s.invert' % opacityNode)
                    if VmyInv:
                        mc.setAttr('%s.invert' % opacityNode, False)
                    else:
                        mc.setAttr('%s.invert' % opacityNode, True)
                    if mc.getAttr('%s.alphaIsLuminance' % opacityNode):
                        try:
                            mc.editRenderLayerAdjustment('%s.alphaIsLuminance' % opacityNode)
                        except:
                            pass
                        mc.setAttr('%s.alphaIsLuminance' % opacityNode, 0)
                else:
                    reverseNode = mc.createNode('reverse')

                    if tranC_Type == 1:
                        mc.connectAttr(transPath, '%s.input' % reverseNode, f=True)
                    elif tranC_Type == 2:
                        mc.connectAttr(transPath, '%s.inputX' % reverseNode, force=True)
                        mc.connectAttr(transPath, '%s.inputY' % reverseNode, force=True)
                        mc.connectAttr(transPath, '%s.inputZ' % reverseNode, force=True)
                    mc.connectAttr('%s.output' % reverseNode, '%s.%s' % (shaderNode, tranPoint), f=True)
            else:
                #具有透明值
                if TrV_V == 1:
                    tmp = 'rgb_to_hsv(<<%s,%s,%s>>)' % (transValue[0][0], transValue[0][1], transValue[0][2])
                    oldSpeVHSV = mm.eval(tmp)
                    tmp = 'hsv_to_rgb(<<%f,%s,%f>>)' % (0, 0, 1-oldSpeVHSV[2])
                    newSpeVRGB = mm.eval(tmp)
                    mc.setAttr('%s.transparency' % replaceNode, newSpeVRGB[0], newSpeVRGB[1], newSpeVRGB[2], type='double3')

        mm.eval('replaceNode %s %s;' % (shaderNode, replaceNode))
        mm.eval('showEditor %s;' % replaceNode)
        # mc.delete(shaderNode)
        return replaceNode
    elif model == 2:
        mc.hyperShade(o=shaderNode)
        ObjectS = mc.ls(sl=True)
        myMat = ''
        try:
            myMat = mc.listConnections('%s.base_material' % shaderNode)
        except:
            pass
        if not myMat:
            try:
                myMat = mc.listConnections('%s.baseMaterial' % shaderNode)
            except:
                pass
        if not myMat:
            try:
                myMat = mc.listConnections('%s.frontMaterial' % shaderNode)
            except:
                pass
        modeType = ''
        try:
            modeType = mc.nodeType(myMat[0])
        except:
            pass

        if modeType == '':
            mm.eval('replaceNode %s %s;' % (shaderNode, replaceNode))
            mm.eval('showEditor %s;' % replaceNode)
            # mc.delete(shaderNode)
        elif modeType == 'VRayMtl' or modeType == 'VRayLightMtl' or modeType == 'VRayBumpMtl' or modeType == 'VRayBlendMtl' or modeType == 'VRayMtl2Sided' or modeType == 'VRayMtlWrapper':
            renturnMal = changeMaterial_zwz(myMat[0], replaceType)
            mc.select(ObjectS)
            mc.hyperShade(assign=renturnMal)
        else:
            # mc.delete(shaderNode)
            mc.hyperShade(assign=myMat[0])
    elif model == 3:
        mm.eval('replaceNode %s %s;' % (shaderNode, replaceNode))
        mm.eval('showEditor %s;' % replaceNode)
        # mc.delete(shaderNode)
    return


def allVRayMatToLambert():
    replaceType = 'lambert'
    allRepalces = []
    allVRS = mc.ls(type='VRayMtl')
    allRepalces += allVRS
    allVRS = mc.ls(type='VRayLightMtl')
    allRepalces += allVRS
    allVRS = mc.ls(type='VRayBumpMtl')
    allRepalces += allVRS
    allVRS = mc.ls(type='VRayBlendMtl')
    allRepalces += allVRS
    allVRS = mc.ls(type='VRayMtl2Sided')
    allRepalces += allVRS
    allVRS = mc.ls(type='VRayMtlWrapper')
    allRepalces += allVRS
    allVRS = mc.ls(type='VRayMeshMaterial')
    allRepalces += allVRS
    allRepalces = list(set(allRepalces))
    for j in allRepalces:
        changeMaterial_zwz(j, replaceType)


def setAllVrayMeshtoBox(Value):
    allMyVrayMeshs = mc.ls(type='VRayMesh')
    for myVrayMesh in allMyVrayMeshs:
        mc.setAttr('%s.showBBoxOnly' % myVrayMesh, Value)


def changeRimRamp(Type, ConAttr, Attr):
    allRimShaders = mc.ls('my_rim*', type='lambert')
    if allRimShaders:
        Value = mc.floatSliderGrp(Type, q=True, v=True)
        for RimShader in allRimShaders:
            try:
                myRamp = mc.listConnections('%s.%s' % (RimShader, ConAttr))
            except:
                pass
            else:
                if myRamp:
                    mc.setAttr('%s.%s' % (myRamp[0], Attr), Value)

def LightCondefaultLight(conLightFlag):
    allMySelectShapes = mc.ls(sl=True, dag=True, ni=True, l=True)
    allMyLightShapes = []
    for LShape in allMySelectShapes:
        LShapeType = mc.nodeType(LShape)
        if LShapeType.find("Light") >= 0:
            allMyLightShapes.append(LShape)
    if allMyLightShapes:
        for eachVLight in allMyLightShapes:
            lightVTra = mc.listRelatives(eachVLight, p=True, f=True)[0]
            try:
                if conLightFlag:
                    mc.connectAttr("%s.instObjGroups" % lightVTra, "defaultLightSet.dagSetMembers", na=True)
                else:
                    mc.disconnectAttr("%s.instObjGroups" % lightVTra, "defaultLightSet.dagSetMembers", na=True)
            except:
                pass
    else:
        mc.warning(u"所选里面没有灯光！")

def isoBbox():

    queryStateBbox = mc.button("ShowObjectR", q=1, l=1 )


    if queryStateBbox == 'Off':

        selection = mc.ls(sl=1,transforms=True)

        if selection == []:
            mc.warning('Nothing selected')

        else:
            allGeo = set( mc.ls(geometry=True) )
            singleObj = set( mc.listRelatives(shapes=True) )
            finalSelection = allGeo-singleObj

            for obj in finalSelection:
                try:
                    mc.setAttr(obj + ".overrideEnabled" , 1)
                    mc.setAttr(obj + ".overrideLevelOfDetail" , 1)
                except:
                    pass

            mc.button("ShowObjectR", e=1, l="On", ebg=0, bgc=(0.4,0.04,0.03) )

    else:
        allGeo = set( mc.ls(geometry=True) )

        for obj in allGeo:
            try:
                mc.setAttr(obj + ".overrideLevelOfDetail" , 0)
                mc.setAttr(obj + ".overrideEnabled" , 0)
            except:
                pass

        mc.button("ShowObjectR", e=1, l="Off", ebg=0, bgc=(0.3,0.3,0.3))


def isoTextured(*args):

    if mc.window('exitWindow', ex=True):

        mc.warning("Already in isolate mode")

    else:

        noSelection = mc.ls(sl=True)

        if noSelection == []:
            mc.warning( "No Objects Selected" )

        else:



            allGeo = set( mc.ls(geometry=True) )
            singleObj = set( mc.listRelatives(shapes=True) )
            
            finalSelection = allGeo-singleObj

            if len(finalSelection) <= 0:
                mc.warning( "All objects Selected" )

            else:

                if len(finalSelection) > 0:

                    if mc.getPanel(withFocus=1) != 'modelPanel4':
                        mc.setFocus('modelPanel4')

                    viewportPan = mc.getPanel( withFocus=True )

                    mc.modelEditor( viewportPan, edit=True, displayAppearance='smoothShaded', dtx=True)


                    for obj in finalSelection:
                        try:
                            mc.setAttr(obj + ".overrideEnabled" , 1)
                            mc.setAttr(obj + ".overrideTexturing" , 0)
                        except:
                            pass

                    window = mc.window( "exitWindow", bgc=[0.5,0.1,0.08], tb=0,s=False )
                    mc.columnLayout( adjustableColumn=True )
                    mc.button( label='Exit Isolate Mode', w=200,h=35, command=UndoIsoTextured )

                    vpX = mc.formLayout(viewportPan,q=True,w=True)
                    vpX = vpX/2
                    
                    mc.showWindow( window )
                    mc.window( "exitWindow", edit=True, tlc=(100,vpX-60) )



def UndoIsoTextured(*args):

    AllGeo = mc.ls(geometry=True)

    if mc.getPanel(withFocus=1) != 'modelPanel4':
        mc.setFocus('modelPanel4')

    viewportPan = mc.getPanel( withFocus=True )
    mc.modelEditor( viewportPan, edit=True, displayAppearance='smoothShaded', dtx=False)
    
    for objs in AllGeo:
        try:
            mc.setAttr(objs + ".overrideEnabled" , 0)
            mc.setAttr(objs + ".overrideTexturing" , 1)
        except:
            pass

    mc.deleteUI("exitWindow")