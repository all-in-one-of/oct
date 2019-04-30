# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os

def OCT_RenderSet_zwz_UI():
    if mc.windowPref('RenderSet_zwz', exists=True):
        mc.windowPref('RenderSet_zwz', remove=True)
    if mc.window('RenderSet_zwz', exists=True):
        mc.deleteUI('RenderSet_zwz', window=True)
    allCameras = mc.listCameras(p=True)
    myStartFrameV = mc.getAttr("defaultRenderGlobals.startFrame")
    myEndFrameV = mc.getAttr("defaultRenderGlobals.endFrame")
    myRenderwidth = mc.getAttr("defaultResolution.width")
    myRenderheight = mc.getAttr("defaultResolution.height")

    mc.window("RenderSet_zwz",title = u"OCT_RenderSet_zwz",menuBar = True,widthHeight =(350,340),resizeToFitChildren = True,sizeable = True)
    mc.formLayout('formLyt', numberOfDivisions=100)

    one = mc.columnLayout('First_Set',parent = 'formLyt')
    mc.rowLayout('projectRow',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [5,260,35],columnOffset3 =[2,2,2],adjustableColumn3 = True,parent = 'First_Set')
    mc.text(label=u'工程地址：',w = 68,parent = 'projectRow')
    mc.textField('ProjectAddress',text = '',width = 250,alwaysInvokeEnterCommandOnReturn= True,parent = 'projectRow')
    mc.button(label =u'设置',width = 35,command = 'OCT_generel.OCT_RenderSet_zwz.SetProjectAddress_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"请输入工程层名",parent = 'projectRow')

    mc.rowLayout('oneRow',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [5,260,35],columnOffset3 =[2,2,2],adjustableColumn3 = True,parent = 'First_Set')
    mc.text(label=u'一般渲染名：',w = 68,parent = 'oneRow')
    mc.textField('RederAddress',text = '<Scene>/<RenderLayer>/<Camera>/<RenderPass>/<Camera>.<RenderPass>',width = 250,alwaysInvokeEnterCommandOnReturn= True,parent = 'oneRow')
    mc.button(label =u'设置',width = 35,command = 'OCT_generel.OCT_RenderSet_zwz.SetRenderAddress_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"请输入渲染层名",parent = 'oneRow')

    mc.rowLayout('twoRow',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [5,260,35],columnOffset3 =[2,2,2],adjustableColumn3 = True,parent = 'First_Set')
    mc.text(label=u'Vray渲染名：',w = 68,parent = 'twoRow')
    mc.textField('VrayRederAddress',text = '<Scene>/<Layer>/<Camera>/<Camera>',width = 250,alwaysInvokeEnterCommandOnReturn= True,parent = 'twoRow')
    mc.button(label =u'设置',width = 35,command = 'OCT_generel.OCT_RenderSet_zwz.SetVrayRenderAddress_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"请输入渲染层名",parent = 'twoRow')

    mc.rowLayout('threeRow',numberOfColumns = 2,columnAttach2 = ['left','left'],columnWidth2 = [260,35],columnOffset2 =[2,1],columnAlign=[1,'left'],cw2 = [334,35],parent = 'First_Set')
    mc.radioButtonGrp('FormatSet',label=u'渲染格式设置:',labelArray2=['Software/Mental Ray (iff)', 'Arnold (Tiff)'], numberOfRadioButtons=2,columnAlign=[1,'left'],columnAlign2=['left','left'],cw3 = [85,160,90],sl = 1,parent = 'threeRow')
    mc.button(label =u'设置',width = 35,command = 'OCT_generel.OCT_RenderSet_zwz.SetRenderFormat_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"请输入需要选择物体的名字",parent = 'threeRow')

    mc.rowLayout('fourRow',numberOfColumns = 5,columnAttach5 = ['left','left','left','left','left'],columnWidth5 = [5,68,70,88,80],columnOffset5 =[2,2,10,15,24],adjustableColumn5 = True,parent = 'First_Set')
    mc.text(label=u'开始帧：',w = 68,parent = 'fourRow')
    mc.textField('startFrame',text = myStartFrameV,width = 60,alwaysInvokeEnterCommandOnReturn= True,parent = 'fourRow')
    mc.text(label=u'结束帧：',w = 68,parent = 'fourRow')
    mc.textField('endFrame',text = myEndFrameV,width = 60,alwaysInvokeEnterCommandOnReturn= True,parent = 'fourRow')
    mc.button(label =u'设置',width = 35,command = 'OCT_generel.OCT_RenderSet_zwz.SetRenderStarFram_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"请输入帧数范围",parent = 'fourRow')

    mc.rowLayout('fiveRow',numberOfColumns = 5,columnAttach5 = ['left','left','left','left','left'],columnWidth5 = [5,68,70,88,80],columnOffset5 =[2,2,10,15,24],adjustableColumn5 = True,parent = 'First_Set')
    mc.text(label=u'宽：',w = 68,parent = 'fiveRow')
    mc.textField('RenderWidth',text = myRenderwidth ,width = 60,alwaysInvokeEnterCommandOnReturn= True,parent = 'fiveRow')
    mc.text(label=u'高：',w = 68,parent = 'fiveRow')
    mc.textField('RenderHeight',text = myRenderheight,width = 60,alwaysInvokeEnterCommandOnReturn= True,parent = 'fiveRow')
    mc.button(label =u'设置',width = 35,command = 'OCT_generel.OCT_RenderSet_zwz.SetRenderWH_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"请输入渲染尺寸",parent = 'fiveRow')

    two =mc.frameLayout('Cameras_Set',label = u'设置渲染摄像机(面板可拉伸)',labelAlign = 'top',borderStyle = 'etchedOut',w=300,h=100,parent = 'formLyt')
    mc.textScrollList('selectCameras',append = allCameras,allowMultiSelection=True,h = 100,parent = 'Cameras_Set')

    three = mc.columnLayout('Second_Set',parent = 'formLyt')
    mc.rowLayout('CamerasButton',numberOfColumns = 2,columnWidth2 =(190,190),columnAlign2=('center', 'center'),height =30,parent = 'Second_Set')
    mc.button( 'loadCameras',label=u'设置摄像机',width =170,command = 'OCT_generel.OCT_RenderSet_zwz.SetAllmyCameras_zwz()',backgroundColor = (0.9,0.5,0),parent = 'CamerasButton')
    mc.button( 'clearCameras',label=u'清除所有摄像机',width =170,command = 'OCT_generel.OCT_RenderSet_zwz.CleanAllCameras_zwz()',backgroundColor = (0.9,0.3,0.3),parent = 'CamerasButton')
    mc.button( 'SetAll',label=u'设置以上所有选项',width =362,h=25,command = 'OCT_generel.OCT_RenderSet_zwz.SetAllmyRenderSetting_zwz()',backgroundColor = (0.2,0.8,0.3),parent = 'Second_Set')

    four =mc.frameLayout('clipPlane_Set', label = u'设置所有摄像机距离值', labelAlign = 'top', w=362, bv=0, cll=True, cl=True, parent = 'formLyt')
    mc.columnLayout(parent =four)
    mc.checkBox('cheackClip', label='Auto Render Clip Plane',w=135)
    mc.textFieldGrp('nearClip', label='Near Clip Plane', text = '0.100',cw2=[85, 100], cal=[1, 'left'])
    mc.textFieldGrp('farClip', label='Far Clip Plane', text = '10000000.000', cw2=[85, 100], cal=[1, 'left'])
    mc.button(label =u'设置所有摄像机距离值', width = 365, command = 'OCT_generel.OCT_RenderSet_zwz.setAllmyCmaerasClip_zwz()', backgroundColor = (0.9,0.5,0))

    mc.formLayout('formLyt', e=True,
                  attachForm=[(one, 'top', 5), (one, 'left', 5), (two, 'right', 5),(two, 'top', 155),  (two, 'left', 5), (three, 'left', 5), (four, 'left', 5), (four, 'bottom', 5)],
                  attachControl=[(two, 'bottom', 1, three) ,(three, 'bottom', 1, four)],
                  attachNone=[(three, 'top')],
                  attachPosition=[(one, 'left', 0, 0), (one, 'top', 0, 0)])
    mayaversions = mc.about(v=True)
    if mayaversions.find('2009') >= 0:
        mc.radioButtonGrp('FormatSet', e=True, enable2=False)
    mc.showWindow('RenderSet_zwz')


def SetProjectAddress_zwz():
    myProjectAddress = mc.textField('ProjectAddress', query=True, text=True)
    if myProjectAddress!="":
        myProjectAddress  = os.path.normpath(myProjectAddress )
        myProjectAddress  = myProjectAddress  .replace('\\', '/')
        mm.eval('setProject "%s"' % myProjectAddress)

def SetRenderAddress_zwz():
    mtAddress =mc.textField('RederAddress',query = True,text = True)
    mc.setAttr("defaultRenderGlobals.imageFilePrefix",mtAddress,type="string")

def SetVrayRenderAddress_zwz():
    mtAddress =mc.textField('VrayRederAddress',query = True,text = True)
    if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True) and mc.objExists('vraySettings'):
            mc.setAttr("vraySettings.fileNamePrefix", mtAddress, type="string")
            mc.setAttr("vraySettings.animBatchOnly", 1)

def SetRenderFormat_zwz():
    tmp = mc.radioButtonGrp('FormatSet', query = True, sl = True)
    if tmp == 1:
        mc.setAttr("defaultRenderGlobals.imageFormat",7)
    if tmp == 2:
        try:
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
        except:
            pass
    mc.setAttr("defaultRenderGlobals.animation", 1)
    mc.setAttr("defaultRenderGlobals.putFrameBeforeExt", 1)
    mc.setAttr("defaultRenderGlobals.periodInExt", 1)
    if (mc.getAttr("defaultRenderGlobals.outFormatControl")== 1):
        mc.setAttr("defaultRenderGlobals.outFormatControl", 0)
    mc.setAttr("defaultRenderGlobals.extensionPadding", 4)

def SetRenderStarFram_zwz():
    myStartFrameV = mc.textField('startFrame',query = True,text = True)
    myEndFrameV  = mc.textField('endFrame',query = True,text = True)
    mc.setAttr("defaultRenderGlobals.startFrame", myStartFrameV)
    mc.setAttr("defaultRenderGlobals.endFrame", myEndFrameV)
    
def SetRenderWH_zwz():
    myRenderwidth= mc.textField('RenderWidth',query = True,text = True)
    myRenderheight = mc.textField('RenderHeight',query = True,text = True)
    mc.setAttr("defaultResolution.width", float(myRenderwidth))
    mc.setAttr("defaultResolution.height", float(myRenderheight))
    
def CleanAllCameras_zwz():
    allCameras = mc.listCameras(p=True)
    for MyCamera in allCameras:
        MyCameraShape = mc.listRelatives(MyCamera,s=True,f=True)
        if MyCameraShape:
            mc.setAttr("%s.renderable"%MyCameraShape[0],0)
    cmd = 'updateMayaSoftwareCameraControl;'
    try:
        mm.eval(cmd)
    except:
        pass

def SetAllmyCameras_zwz():
    allMyCameras = mc.textScrollList('selectCameras',query = True,selectItem = True)
    if allMyCameras:
        CleanAllCameras_zwz()
        for MyCamera in allMyCameras:
            if MyCamera.find('persp')>=0:
                MyCameraShape = mc.listRelatives(MyCamera,s=True)
            else:
                MyCameraShape = mc.listRelatives(MyCamera,s=True,f=True)
            if MyCameraShape:
                mc.setAttr("%s.renderable"%MyCameraShape[0],1)
        cmd = 'updateMayaSoftwareCameraControl;'
        try:
            mm.eval(cmd)
        except:
            pass
    else:
        pass

def SetAllmyRenderSetting_zwz():
    SetRenderAddress_zwz()
    SetVrayRenderAddress_zwz()
    SetRenderFormat_zwz()
    SetRenderStarFram_zwz()
    SetRenderWH_zwz()
    SetAllmyCameras_zwz()
    SetProjectAddress_zwz()

def setAllmyCmaerasClip_zwz():
    checkAutoV = mc.checkBox('cheackClip',  q=True, v=True)
    AutoFV = ''
    if checkAutoV:
        AutoFV = 'true'
    else:
        AutoFV = 'false'
    nearClipText = mc.textFieldGrp('nearClip', query=True, text=True)
    farClipText = mc.textFieldGrp('farClip', query=True, text=True)
    AllCameras = mc.listCameras(p=True)
    if AllCameras:
            for mycamera in AllCameras:
                mm.eval('setAttr "%s.nearClipPlane" %s;' % (mycamera, nearClipText))
                mm.eval('setAttr "%s.farClipPlane" %s;' % (mycamera, farClipText))
                mm.eval('setAttr %s.bestFitClippingPlanes %s;' % (mycamera, AutoFV))
    mm.eval("autoUpdateAttrEd;")
        