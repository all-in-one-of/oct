# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import maya.utils as utils
import sys


def OCT_QuantituRender_UI_zwz():
    if mc.windowPref('OCT_QuantituRender_UI_zwz', exists=True):
        mc.windowPref('OCT_QuantituRender_UI_zwz', remove=True)
    if mc.window('OCT_QuantituRender_UI_zwz', exists=True):
        mc.deleteUI('OCT_QuantituRender_UI_zwz', window=True)
    mc.window("OCT_QuantituRender_UI_zwz",title = u"OCT_QuantituRender_zwz",menuBar = True,widthHeight =(350,340),resizeToFitChildren = True,sizeable = True)
    mc.formLayout('formLyt', numberOfDivisions=100)

    one = mc.columnLayout('First_Set',parent = 'formLyt')
    mc.rowLayout('oneRow',numberOfColumns = 2,columnAttach2 = ['left','left'],columnWidth2 = [5,300],columnOffset2 =[2,2],adjustableColumn2 = True,parent = 'First_Set')
    mc.text(label=u'详细文件名：',w = 68,parent = 'oneRow')
    mc.textField('myAddress',text = 'D:\work\Test\scenes\Test.mb',width = 300,alwaysInvokeEnterCommandOnReturn= True,parent = 'oneRow')
    mc.radioButtonGrp('Playoption',label=u'Playblast:',labelArray2=[u'1  (是)', u'2  (否)'], numberOfRadioButtons=2,columnAlign=[1,'left'],columnAlign2=['left','left'],cw3 = [85,130,90],sl = 1,parent = 'First_Set')
    mc.radioButtonGrp('showoption',label=u'物体是否显示:',labelArray2=[u'1  (不显示)', u'2  (文件默认)'], numberOfRadioButtons=2,columnAlign=[1,'left'],columnAlign2=['left','left'],cw3 = [85,130,90],sl = 1,parent = 'First_Set')
    mc.button(label =u'加  载',width = 320,command = 'OCT_render.OCT_QuantityRender_zwz.Addaddress_zwz()',backgroundColor = (0.9,0.5,0),annotation =u"确认名字和选项",parent = 'First_Set')

    two =mc.text('Cameras_Set',label = u'渲染文件清单(面板可拉伸)',parent = 'formLyt',fn =  "boldLabelFont",al='left',w=200)
    two_one = mc.textScrollList('allMyAddress',append = u'文件地址：',allowMultiSelection=True, sc="OCT_render.OCT_QuantityRender_zwz.lsRenderlist_zwz('allMyAddress')", h = 100,width = 100,parent = 'formLyt')
    two_two = mc.textScrollList('myplayoptions',append = 'Playblast:',allowMultiSelection=True,sc="OCT_render.OCT_QuantityRender_zwz.lsRenderlist_zwz('myplayoptions')",h = 100,width = 60,parent = 'formLyt')
    two_three = mc.textScrollList('myshowoptions',append = u'物体显示性:',allowMultiSelection=True,sc="OCT_render.OCT_QuantityRender_zwz.lsRenderlist_zwz('myshowoptions')",h = 100,width = 65,parent = 'formLyt')

    three = mc.columnLayout('Second_Set',parent = 'formLyt')
    mc.button( 'clearlist',label=u'删除选中的清单',width =320,command = 'OCT_render.OCT_QuantityRender_zwz.clearLslist_zwz()',backgroundColor =(0.9,0.3,0.3),parent = 'Second_Set')
    mc.button( 'doRender',label=u'开始渲染',width =320,command = 'OCT_render.OCT_QuantityRender_zwz.Do_QuantituRender_zwz()',backgroundColor = (0.3,0.7,0.3),parent = 'Second_Set')

    mc.formLayout('formLyt', e=True, \
                  attachForm=[(one, 'top', 5),(one, 'left', 5),(two, 'left', 5),(two, 'top', 90),(two_one, 'top', 110),(two_two, 'top', 110),(two_three, 'top', 110),(two_one, 'left', 5),(two_three, 'right', 5),(three, 'left', 5),(three, 'bottom', 5)], \
                  attachControl=[(two_one, 'bottom', 1, three),(two_two, 'bottom', 1, three),(two_three, 'bottom', 1, three),(two_one, 'right', 1, two_two),(two_two, 'right', 1, two_three)], \
                  attachNone=[(three, 'top')], \
                  attachPosition=[(one, 'left',0, 0),(one, 'top',0, 0),] \
        )
    mc.showWindow('OCT_QuantituRender_UI_zwz')

def Addaddress_zwz():
    textAddress = mc.textField('myAddress',q=True,text=True)
    optionPlay = mc.radioButtonGrp('Playoption',q=True,sl=True)
    optionShow = mc.radioButtonGrp('showoption',q=True,sl=True)
    mc.textScrollList('allMyAddress',e=True, append = textAddress)
    mc.textScrollList('myplayoptions',e=True, append = optionPlay)
    mc.textScrollList('myshowoptions',e=True, append = optionShow)

def lsRenderlist_zwz(lsList):
    tmp = mc.textScrollList(lsList,q=True, sii=True)
    mc.textScrollList('allMyAddress',e=True, deselectAll=True)
    mc.textScrollList('myplayoptions',e=True, deselectAll=True)
    mc.textScrollList('myshowoptions',e=True, deselectAll=True)
    mc.textScrollList('allMyAddress',e=True, sii=tmp)
    mc.textScrollList('myplayoptions',e=True, sii=tmp)
    mc.textScrollList('myshowoptions',e=True, sii=tmp)

def clearLslist_zwz():
    tmp = mc.textScrollList('allMyAddress',q=True, sii=True)
    j=0
    for i in tmp:
        if i>1:
            mc.textScrollList('allMyAddress',e=True, rii=i-j)
            mc.textScrollList('myplayoptions',e=True, rii=i-j)
            mc.textScrollList('myshowoptions',e=True, rii=i-j)
            j+=1
            print i
        else:
            pass

def Do_QuantituRender_zwz():
    tmp = mc.textScrollList('allMyAddress',q=True, numberOfItems=True)
    Renderback = None
    for i in range(1, tmp+1):
        Renderback = None
        if i>1:
            mc.textScrollList('allMyAddress',e=True, deselectAll=True)
            mc.textScrollList('myplayoptions',e=True, deselectAll=True)
            mc.textScrollList('myshowoptions',e=True, deselectAll=True)
            mc.textScrollList('allMyAddress',e=True, sii=i)
            mc.textScrollList('myplayoptions',e=True, sii=i)
            mc.textScrollList('myshowoptions',e=True, sii=i)
            inAddress = mc.textScrollList('allMyAddress',q=True, selectItem=True)[0]
            if not mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                mc.loadPlugin('Mayatomr.mll')
            mc.file(f=True,new=True)
            myaddress = inAddress
            myScenesAddress = '/'.join(inAddress.split('\\')[:-2])
            mm.eval('setProject "%s";'%myScenesAddress)
            cmd ='mc.file("%s",f=True,options="v=0",typ="mayaBinary",o=True)' % myaddress
            mc.evalDeferred(cmd)
            if mc.evalDeferred('OCT_render.OCT_QuantityRender_zwz.QuantituRender_zwz()') == False:
                break

def QuantituRender_zwz():
    inPlayoption = int(mc.textScrollList('myplayoptions',q=True, selectItem=True)[0])
    inshowoption = int(mc.textScrollList('myshowoptions',q=True, selectItem=True)[0])
    mc.setAttr("defaultRenderGlobals.imageFilePrefix","<Scene>/<RenderLayer>/<Camera>/<Camera>",type="string" )
    allLayers = mc.listConnections('renderLayerManager.renderLayerId')
    myAllLayers = []
    AllCameras = []
    if allLayers:
        for Layer in allLayers:
            if mc.getAttr('%s.renderable'%Layer):
                myAllLayers.append(Layer)
    AllCameras = mc.listCameras(p=True)
    tmp = mc.workspace("images",query = True,renderTypeEntry= True)
    fullPath = mc.workspace(expandName = tmp)
    FramePadding = mc.getAttr("defaultRenderGlobals.extensionPadding")
    try:
        mm.eval("RenderViewWindow;")
    except:
        pass
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
    if inshowoption ==1:
        mc.modelEditor(activePlane,e=True,allObjects = 0)
    temp = mc.getAttr('defaultRenderGlobals.currentRenderer')
    mc.setAttr('defaultRenderGlobals.currentRenderer',temp,type='string')
    for myLayer in myAllLayers:
        mc.editRenderLayerGlobals(currentRenderLayer = myLayer)
        StartFrame = EndFrame = 0
        StartFrame = int(mc.getAttr("defaultRenderGlobals.startFrame"))
        EndFrame = int(mc.getAttr("defaultRenderGlobals.endFrame"))
        mc.currentTime(StartFrame,update=True)
        mc.pause(sec=3)
        LayerType = mc.getAttr('defaultRenderGlobals.currentRenderer')
        if LayerType.find('vray')>=0 or LayerType.find('arnold')>=0 :
            sys.stdout.write('%s can`t Render;\n'%LayerType)
            continue
        currentRenderLayer = mc.editRenderLayerGlobals(query=True,currentRenderLayer=True)
        if currentRenderLayer != myLayer:
            mc.editRenderLayerGlobals(currentRenderLayer = myLayer)
        myAllCameras = []
        CameraShape = ''
        if AllCameras:
            for Camera in AllCameras:
                try:
                    CameraShape = mc.listRelatives(Camera,s=True)[0]
                except:
                    pass
                else:
                    if mc.getAttr('%s.renderable'%CameraShape):
                        myAllCameras.append(Camera)
        mc.progressWindow(title = u'批渲染器',progress = 0,status = u'即将开始',min = StartFrame,max =EndFrame,isInterruptable = True)
        imagePath = mc.renderSettings(firstImageName = True)[0]
        Layerpath = imagePath.split('/')
        myLayerName = '/'.join(Layerpath[:2])
        mytypeName = imagePath.split('.')[-1]
        mytypeV = 0
        if mytypeName.find('iff')>=0:
            mytypeV = 1
        elif mytypeName.find('tif')>=0:
            mytypeV = 2
        elif mytypeName.find('png')>=0:
            mytypeV = 3
        for i in xrange(StartFrame,EndFrame+1):
            mc.currentTime(StartFrame, update=True)
            mc.progressWindow(edit = True,progress = i,status = "RenerLayer: %s  / Frame: %s"%(myLayer,i))
            for myCamera in myAllCameras:
                finallyPath = (fullPath + '/' + myLayerName + '/%s/%s.'%(myCamera,myCamera)+str(i).zfill(FramePadding)+'.'+mytypeName)
                if inPlayoption == 1:
                    mc.lookThru(myCamera, myactivePlane)
                    mc.currentTime(StartFrame, update=True)
                mm.eval('updateModelPanelBar %s;'%activePlane)
                #mm.eval('RenderIntoNewWindow;')
                mm.eval('renderWindowRenderCamera render renderView "%s";'%myCamera)
                if mc.progressWindow(q = True,isCancelled = True) or mc.progressWindow(q =True,progress = True)>EndFrame+1:
                    mc.progressWindow(endProgress=True)
                    return False
                mc.setAttr('defaultRenderGlobals.imfkey',"",type="string")
                if mc.file(finallyPath,q=True,exists=True):
                    mc.sysFile(finallyPath,delete=True)
                if mytypeV == 1:
                    mm.eval('renderWindowSaveImageCallback "renderView" "%s" "Maya IFF";'%finallyPath)
                elif mytypeV == 2:
                    mm.eval('renderWindowSaveImageCallback "renderView" "%s" "Tiff";'%finallyPath)
                elif mytypeV == 3:
                    mm.eval('renderWindowSaveImageCallback "renderView" "%s" "PNG";'%finallyPath)
                print "RenerLayer: %s  / Frame: %s"%(myLayer,i)
        mc.progressWindow(endProgress=True)
    return True
