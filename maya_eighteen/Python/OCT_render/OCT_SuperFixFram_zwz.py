#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os
import sys

fixFrameList_zwz = []


def SuperFixFream_mmenu_zwz():
    fixFrameList_zwz = []
    if not mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
        mc.loadPlugin('Mayatomr.mll')
    global fixFrameList_zwz
    if mc.windowPref('OCT_SuperFixFrame_UUI_zwz', exists=True):
        mc.windowPref('OCT_SuperFixFrame_UUI_zwz', remove=True)
    if mc.window('OCT_SuperFixFrame_UUI_zwz', exists=True):
        mc.deleteUI('OCT_SuperFixFrame_UUI_zwz', window=True)
    mc.window("OCT_SuperFixFrame_UUI_zwz", title=u"OCT_SuperFixFram_zwz(目前只支持单个文件多任务补帧渲染)", menuBar=True, widthHeight=(350, 340), resizeToFitChildren=True, sizeable=True)
    mc.formLayout('formLyt', numberOfDivisions=100)

    one = mc.columnLayout('First_Set', parent='formLyt', adj=True)

    mc.rowLayout('oneRow', numberOfColumns=2, cal=[1, 'left'], columnWidth2=[70, 230], adj=2, parent='First_Set')
    mc.text(label=u'详细文件名:', w=70, parent='oneRow')
    mc.textField('myFileAddress', text='D:\work\Test\scenes\Test.mb', width=100, parent='oneRow')
    mc.rowLayout('twoRow', numberOfColumns=2, cal=[1, 'left'], columnWidth2=[70, 230], adj=2, parent='First_Set')
    mc.text(label=u'渲染层(单个):', w=70, parent='twoRow')
    mc.textField('myLayersAddress', text='masterLayer', width=100, parent='twoRow')
    mc.rowLayout('threeRow', numberOfColumns=2, cal=[1, 'left'], columnWidth2=[70, 230], adj=2, parent='First_Set')
    mc.text(label=u'摄像机(多个):', w=70, parent='threeRow')
    mc.textField('myCamerasAddress', text='camL_L  camL_M  camL_R', width=100, parent='threeRow')
    mc.rowLayout('fourRow', numberOfColumns=2, cal=[1, 'left'], columnWidth2=[70, 230], adj=2, parent='First_Set')
    mc.text(label=u'帧数(多个):', w=70, parent='fourRow')
    mc.textField('myFrameAddress', text='1  2  3  4-6  7-10', width=100, parent='fourRow')
    mc.radioButtonGrp('Playoption', label=u'Playblast:', labelArray2=[u'1  (是)', u'2  (否)'], numberOfRadioButtons=2, columnAlign=[1, 'left'], columnAlign2=['left', 'left'], cw3=[85, 130, 90], sl=1, parent='First_Set')
    mc.radioButtonGrp('showoption', label=u'物体是否显示:', labelArray2=[u'1  (不显示)', u'2  (文件默认)'], numberOfRadioButtons=2, columnAlign=[1, 'left'], columnAlign2=['left', 'left'], cw3=[85, 130, 90], sl=1, parent='First_Set')
    mc.rowLayout('buttonM', numberOfColumns=2, columnWidth2=[150, 150], parent='First_Set')
    mc.button(label=u'加  载', width=150, command='OCT_render.OCT_SuperFixFram_zwz.addAddress_zwz()', backgroundColor=(0.9, 0.5, 0), annotation=u"确认名字和选项", parent='buttonM')
    mc.button(label=u'修 改', width=150, command='OCT_render.OCT_SuperFixFram_zwz.modifyAddress_zwz()', backgroundColor=(0.3, 0.7, 0.3), annotation=u"确认名字和选项", parent='buttonM')

    two = mc.text('Cameras_Set', label=u'渲染文件清单(面板可拉伸)', parent='formLyt', fn="boldLabelFont", al='left', w=150)
    two_one = mc.textScrollList('allMyAddress', append=u'文件地址：', sc="OCT_render.OCT_SuperFixFram_zwz.lsRenderlist_zwz('allMyAddress')", h=100, width=50, parent='formLyt')
    two_two = mc.textScrollList('layeroptions', append=u'渲染层：', sc="OCT_render.OCT_SuperFixFram_zwz.lsRenderlist_zwz('layeroptions')", h=100, width=95, parent='formLyt')
    two_three = mc.textScrollList('cameraoptions', append=u'摄像机：', sc="OCT_render.OCT_SuperFixFram_zwz.lsRenderlist_zwz('cameraoptions')", h=100, width=100, parent='formLyt')

    three = mc.columnLayout('Second_Set', parent='formLyt', w=320)
    mc.button('clearlist', label=u'删除选中的清单', width=320, command='OCT_render.OCT_SuperFixFram_zwz.clearLslist_zwz()', backgroundColor=(0.9, 0.3, 0.3), parent='Second_Set')
    mc.button('doRender', label=u'开始渲染', width=320, command='OCT_render.OCT_SuperFixFram_zwz.Do_QuantituRender_zwz()', backgroundColor=(0.3, 0.7, 0.3), parent='Second_Set')

    mc.formLayout('formLyt', e=True,
                  attachForm=[(one, 'top', 5), (one, 'left', 5), (one, 'right', 5), (two, 'left', 5), (two, 'top', 159), (two_one, 'top', 178), (two_two, 'top', 178), (two_three, 'top', 178), (two_one, 'left', 5), (two_three, 'right', 5), (three, 'left', 5), (three, 'bottom', 5)],
                  attachControl=[(two_one, 'right', 1, two_two), (two_two, 'right', 1, two_three),  (two_one, 'bottom', 1, three), (two_two, 'bottom', 1, three), (two_three, 'bottom', 1, three)],
                  attachNone=[(three, 'top')],
                  attachPosition=[]
                  )
    mayaversions = mc.about(v=True)
    if mayaversions.find('2009') >= 0:
        mc.formLayout('formLyt', e=True, attachForm=[(two, 'top', 145), (two_one, 'top', 165), (two_two, 'top', 165), (two_three, 'top', 165)])
    mc.showWindow('OCT_SuperFixFrame_UUI_zwz')


def addAddress_zwz():
    temp = u'%s' % mc.textField('myFileAddress', q=True, text=True)
    temp = temp.strip()
    if os.path.isfile(r'%s' % temp):
        textFileAddress = temp
    else:
        mc.confirmDialog(title=u'温馨提示：', message=u'输入的文件地址有误！\n请检查该地址是否有该文件！\n或文件名字是否有输入错误！', button=['OK'], defaultButton='Yes', dismissString='No')
        return
    textLayersAddress = mc.textField('myLayersAddress', q=True, text=True)
    textCameraAddress = mc.textField('myCamerasAddress', q=True, text=True)
    textFrameAddress = mc.textField('myFrameAddress', q=True, text=True)
    if not textLayersAddress or not textCameraAddress or not textFrameAddress:
        mc.confirmDialog(title=u'温馨提示：', message=u'不能输入空值！', button=['OK'], defaultButton='Yes', dismissString='No')
        return
    temp = checkFrames(textFrameAddress)
    if temp:
        textFrameAddress = temp
    else:
        return
    optionPlay = mc.radioButtonGrp('Playoption', q=True, sl=True)
    optionShow = mc.radioButtonGrp('showoption', q=True, sl=True)
    mc.textScrollList('allMyAddress', e=True, append=textFileAddress)
    mc.textScrollList('layeroptions', e=True, append=textLayersAddress)
    mc.textScrollList('cameraoptions', e=True, append=textCameraAddress)
    fixFrameList_zwz.append([textFileAddress, textLayersAddress, textCameraAddress, textFrameAddress, optionPlay, optionShow])


def lsRenderlist_zwz(lsList):
    tmp = mc.textScrollList(lsList, q=True, sii=True)
    mc.textScrollList('allMyAddress', e=True, deselectAll=True)
    mc.textScrollList('layeroptions', e=True, deselectAll=True)
    mc.textScrollList('cameraoptions', e=True, deselectAll=True)
    mc.textScrollList('allMyAddress', e=True, sii=tmp)
    mc.textScrollList('layeroptions', e=True, sii=tmp)
    mc.textScrollList('cameraoptions', e=True, sii=tmp)
    if tmp[0] > 1:
        mc.textField('myFileAddress', e=True, text=fixFrameList_zwz[tmp[0]-2][0])
        mc.textField('myLayersAddress', e=True, text=fixFrameList_zwz[tmp[0]-2][1])
        mc.textField('myCamerasAddress', e=True, text=fixFrameList_zwz[tmp[0]-2][2])
        textFrameAddress = ''
        for i in fixFrameList_zwz[tmp[0]-2][3]:
            textFrameAddress = textFrameAddress+'%s' % i + '  '
        mc.textField('myFrameAddress', e=True, text=textFrameAddress)
        mc.radioButtonGrp('Playoption', e=True, sl=fixFrameList_zwz[tmp[0]-2][4])
        mc.radioButtonGrp('showoption', e=True, sl=fixFrameList_zwz[tmp[0]-2][5])


def modifyAddress_zwz():
    tmp = mc.textScrollList('allMyAddress', q=True, sii=True)
    if tmp:
        if tmp[0] > 1:
            temp = mc.textField('myFileAddress', q=True, text=True)
            if os.path.isfile(r'%s' % temp):
                textFileAddress = temp
            else:
                mc.confirmDialog(title=u'温馨提示：', message=u'输入的文件地址有误！\n请检查该地址是否有该文件！\n或文件名字是否有输入错误！', button=['OK'], defaultButton='Yes', dismissString='No')
                return
            textLayersAddress = mc.textField('myLayersAddress', q=True, text=True)
            textCameraAddress = mc.textField('myCamerasAddress', q=True, text=True)
            textFrameAddress = mc.textField('myFrameAddress', q=True, text=True)
            if not textLayersAddress or not textCameraAddress or not textFrameAddress:
                mc.confirmDialog(title=u'温馨提示：', message=u'不能输入空值！', button=['OK'], defaultButton='Yes', dismissString='No')
                return
            temp = checkFrames(textFrameAddress)
            if temp:
                textFrameAddress = temp
            else:
                return
            optionPlay = mc.radioButtonGrp('Playoption', q=True, sl=True)
            optionShow = mc.radioButtonGrp('showoption', q=True, sl=True)
            fixFrameList_zwz[tmp[0]-2] = [textFileAddress, textLayersAddress, textCameraAddress, textFrameAddress, optionPlay, optionShow]
            mc.textScrollList('allMyAddress', e=True, rii=tmp[0])
            mc.textScrollList('layeroptions', e=True, rii=tmp[0])
            mc.textScrollList('cameraoptions', e=True, rii=tmp[0])
            mc.textScrollList('allMyAddress', e=True, ap=[tmp[0], textFileAddress])
            mc.textScrollList('layeroptions', e=True, ap=[tmp[0], textLayersAddress])
            mc.textScrollList('cameraoptions', e=True, ap=[tmp[0], textCameraAddress])
            mc.textScrollList('allMyAddress', e=True, sii=tmp[0])
            lsRenderlist_zwz('allMyAddress')


def clearLslist_zwz():
    tmp = mc.textScrollList('allMyAddress', q=True, sii=True)
    if tmp:
        if tmp[0] > 1:
            mc.textScrollList('allMyAddress', e=True, rii=tmp[0])
            mc.textScrollList('layeroptions', e=True, rii=tmp[0])
            mc.textScrollList('cameraoptions', e=True, rii=tmp[0])
            mc.textScrollList('allMyAddress', e=True, sii=tmp[0])
            lsRenderlist_zwz('allMyAddress')
            fixFrameList_zwz.remove(fixFrameList_zwz[tmp[0]-2])


def checkFrames(textFrameAddress):
    usefulFrame = []
    InFrames = textFrameAddress.split(' ')
    for Frames in InFrames:
        if Frames:
            if Frames.count('-') == 1:
                lineFrames = Frames.split('-')
                gv1 = lineFrames[0]
                gv2 = lineFrames[1]
                if (u'%s' % gv1).isnumeric() and (u'%s' % gv2).isnumeric():
                    if int(gv1) < int(gv2):
                        usefulFrame.append("%s-%s" % (gv1, gv2))
                    else:
                        mc.confirmDialog(title=u'温馨提示：', message=u'输入的序列帧%s有误!\n%s  不应该大于  %s' % (Frames, gv1, gv2), button=['OK'], defaultButton='Yes', dismissString='No')
                        return
                else:
                    mc.confirmDialog(title=u'温馨提示：', message=u'输入的序列帧%s有误\n序列帧内含非数字输入' % Frames, button=['OK'], defaultButton='Yes', dismissString='No')
                    return
            elif Frames.count('-') == 0:
                if (u'%s' % Frames).isnumeric():
                    usefulFrame.append(int(Frames))
                else:
                    mc.confirmDialog(title=u'温馨提示：', message=u'输入的单帧%s有误\n单帧含非数字输入' % Frames, button=['OK'], defaultButton='Yes', dismissString='No')
                    return
            else:
                mc.confirmDialog(title=u'温馨提示：', message=u'输入的序列帧%s有误\n含有超过2个  -  符号' % Frames, button=['OK'], defaultButton='Yes', dismissString='No')
                return
    return usefulFrame


def Do_QuantituRender_zwz():
    listNum = len(fixFrameList_zwz)
    if listNum:
        inFiles = []
        FileTypeNum = []
        for i in range(listNum):
            inFiles.append(fixFrameList_zwz[i][0])
        for tmp in set(inFiles):
            temp = []
            for j in range(listNum):
                if fixFrameList_zwz[j][0] == tmp:
                    temp.append(j)
            FileTypeNum.append(temp)
        if len(FileTypeNum) != 1:
            mc.confirmDialog(title=u'温馨提示：', message=u'目前只支持单个文件补帧渲染', button=['OK'], defaultButton='Yes', dismissString='No')
            return
        if not mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
            mc.loadPlugin('Mayatomr.mll')
        for each in FileTypeNum:
            inAddress = fixFrameList_zwz[each[0]][0]
            mc.file(f=True, new=True)
            myaddress = inAddress
            myScenesAddress = '/'.join(inAddress.split('\\')[:-2])
            mm.eval('setProject "%s";' % myScenesAddress)
            mc.file(r"%s" % myaddress, force=True, open=True)
            mc.pause(sec=3)
            for eachL in each:
                mc.textScrollList('allMyAddress', e=True, sii=eachL+2)
                lsRenderlist_zwz('allMyAddress')
                RenderV = QuantituRender_zwz(eachL)
                if RenderV is False:
                    return
                else:
                    pass
    else:
        mc.confirmDialog(title=u'温馨提示：', message=u'空列表！', button=['OK'], defaultButton='Yes', dismissString='No')


def QuantituRender_zwz(eachL):
    try:
        mc.deleteUI("hyperShadePanel1Window")
    except:
        pass
    #for eachL in fileLists:
    #读取工程目录名字
    inPlayoption = fixFrameList_zwz[eachL][4]
    inshowoption = fixFrameList_zwz[eachL][5]
    mayaversions = mc.about(v=True)
    if mayaversions.find('2009') >= 0:
        tmp = mc.workspace("images", query=True, renderTypeEntry=True)
    else:
        tmp = mc.workspace("images", query=True, fileRuleEntry=True)
    fullPath = mc.workspace(expandName=tmp)
    FramePadding = mc.getAttr("defaultRenderGlobals.extensionPadding")
    try:
        mm.eval("RenderViewWindow;")
    except:
        pass
    mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
    myactivePlane = ''
    i = 1
    while(i):
        try:
            tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
        except:
            pass
        else:
            if tmp:
                myactivePlane = 'modelPanel%d' % i
                break
        i += 1
    if inshowoption == 1:
        mc.modelEditor(myactivePlane, e=True, allObjects=False)

    mc.setAttr("defaultRenderGlobals.imageFilePrefix", "<Scene>/<RenderLayer>/<Camera>/<Camera>", type="string")
    #读取渲染层，摄像机
    myAllCameras = []
    myOkCameras = []
    AllCameras = mc.listCameras(p=True)
    temp = fixFrameList_zwz[eachL][2]
    tempG = temp.split(' ')
    for tmp in tempG:
        if tmp:
            myAllCameras.append(tmp)
    for each in myAllCameras:
        if each in AllCameras:
            myOkCameras.append(each)

    myOkLayer = ''
    myLayer = u'%s' % fixFrameList_zwz[eachL][1]
    myLayer = myLayer.strip()
    if myLayer == 'masterLayer':
        myOkLayer = 'defaultRenderLayer'
    else:
        allLayers = mc.listConnections('renderLayerManager.renderLayerId')
        if myLayer in allLayers:
            myOkLayer = myLayer
    #读取渲染帧数组：

    temp = mc.getAttr('defaultRenderGlobals.currentRenderer')
    mc.setAttr('defaultRenderGlobals.currentRenderer', temp, type='string')

    #设置渲染为当前层
    currentRenderLayer = mc.editRenderLayerGlobals(query=True, currentRenderLayer=True)
    if currentRenderLayer != myOkLayer:
        mc.editRenderLayerGlobals(currentRenderLayer=myLayer)
    StartFrame = EndFrame = 0
    StartFrame = int(mc.getAttr("defaultRenderGlobals.startFrame"))
    EndFrame = int(mc.getAttr("defaultRenderGlobals.endFrame"))
    mc.currentTime(StartFrame, update=True)
    mc.pause(sec=3)

    LayerType = mc.getAttr('defaultRenderGlobals.currentRenderer')
    if LayerType.find('vray') >= 0 or LayerType.find('arnold') >= 0:
        sys.stdout.write('%s can`t Render;\n' % LayerType)
        return

    imagePath = mc.renderSettings(firstImageName=True)[0]
    Layerpath = imagePath.split('/')
    myLayerName = '/'.join(Layerpath[:2])
    mytypeName = imagePath.split('.')[-1]
    mytypeV = 0
    if mytypeName.find('iff') >= 0:
        mytypeV = 1
    elif mytypeName.find('tif') >= 0:
        mytypeV = 2
    elif mytypeName.find('png') >= 0:
        mytypeV = 3

    myOkFrames = fixFrameList_zwz[eachL][3]
    lenOkFreames = len(myOkFrames)
    mc.progressWindow(title=u'渲染层:%s' % myOkLayer, progress=0, status=u'即将开始', min=0, max=lenOkFreames, isInterruptable=True)
    i = 0
    for myFrames in myOkFrames:
        i += 1
        if str(type(myFrames)).find('int') >= 0:
            StartFrame = myFrames
            EndFrame = myFrames
        else:
            myListFrames = myFrames.split('-')
            StartFrame = int(myListFrames[0])
            EndFrame = int(myListFrames[1])
        while(StartFrame < EndFrame+1):
            mc.currentTime(StartFrame, update=True)
            for myCamera in myOkCameras:
                finallyPath = (fullPath + '/' + myLayerName + '/%s/%s.' % (myCamera, myCamera)+str(StartFrame).zfill(FramePadding)+'.'+mytypeName)
                if inPlayoption == 1:
                    mc.lookThru(myCamera, myactivePlane)
                    mc.currentTime(StartFrame, update=True)
                mm.eval('updateModelPanelBar %s;' % myactivePlane)
                mm.eval('renderWindowRenderCamera render renderView "%s";' % myCamera)
                mc.progressWindow(edit=True, progress=i, status=u"帧数包:\" %s \"  第  %s  帧  \n摄像机:%s" % (myFrames, StartFrame, myCamera))
                if mc.progressWindow(q=True, isCancelled=True) or mc.progressWindow(q=True, progress=True) > EndFrame+1:
                    mc.progressWindow(endProgress=True)
                    return False
                mc.setAttr('defaultRenderGlobals.imfkey', "", type="string")
                if mc.file(finallyPath, q=True, exists=True):
                    mc.sysFile(finallyPath, delete=True)
                if mytypeV == 1:
                    mm.eval('renderWindowSaveImageCallback "renderView" "%s" "Maya IFF";' % finallyPath)
                elif mytypeV == 2:
                    mm.eval('renderWindowSaveImageCallback "renderView" "%s" "Tiff";' % finallyPath)
                elif mytypeV == 3:
                    mm.eval('renderWindowSaveImageCallback "renderView" "%s" "PNG";' % finallyPath)
                sys.stdout.write("RenerLayer: %s  / Camera: %s  / Frame: %s\n" % (myOkLayer, myCamera, StartFrame))
            StartFrame += 1
    mc.progressWindow(endProgress=True)
    return True
