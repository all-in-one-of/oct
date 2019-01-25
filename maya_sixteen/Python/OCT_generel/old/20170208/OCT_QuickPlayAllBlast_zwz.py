# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sip
import time
import thread 
from PyQt4 import QtGui, QtCore

import maya.cmds as mc
import maya.mel as mm
import maya.OpenMayaUI as apiUI
import maya.OpenMaya as om

class QuickPlayAllBlast_C_zwz():
    def __init__(self):
        #UI
        self._windowSize = (350, 340)
        self._windowName = 'QuickPlayAllBlast_zwz_UUII'
        self.myHideGroup = []
        #Project
        self.allCameras = mc.listCameras(p=True)
        self.myStartFrameV = mc.getAttr("defaultRenderGlobals.startFrame")
        self.myEndFrameV = mc.getAttr("defaultRenderGlobals.endFrame")
        self.myRenderwidth = mc.getAttr("defaultResolution.width")
        self.myRenderheight = mc.getAttr("defaultResolution.height")
        #movieAdress
        self.movieFullPath = ''
        #Windows
        self.myAllWindows = []
        self.myAllModePlanes = []
        self.MenuUIFlag = 0
        self.IconUIFlag = 0
        self.ActiveModePlane = ""
        self.ActiveModePlaneModel = ""
        #TexModel
        self.TexModel = 'tif'

    def closeWin(self, myWinName):
        if mc.window(myWinName, q=True, exists=True):
            mc.deleteUI(myWinName, window=True)
        if mc.windowPref(myWinName, q=True, exists=True):
            mc.windowPref(myWinName, remove=True)

    def show(self):
        #获取当前movie的地址
        movieSpace = mc.workspace("movie", query=True, fileRuleEntry=True)
        moviePaht = mc.workspace(expandName=movieSpace)
        myScneName = mc.file(q=True, sn=True, shn=True).split('.')[0]
        if myScneName == '':
            myScneName = 'untitled'
        myMovieFullPath = os.path.join(moviePaht, myScneName)
        myMovieFullPath = os.path.abspath(myMovieFullPath)
        #删除以往的窗口
        self.closeWin(self._windowName)
        #创建窗口
        win = mc.window(self._windowName, title=u"OCT_QuickPlayAllBlast_zwz", menuBar=True, widthHeight=(350, 340), resizeToFitChildren=True, sizeable=True)
        mc.formLayout('formLyt', numberOfDivisions=100)

        one = mc.columnLayout('First_Set', parent='formLyt')

        mc.rowLayout('projectRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[5, 320, 35], columnOffset3=[2, 2, 2], adjustableColumn3=True, parent='First_Set')
        mc.text(label=u'输出地址', w=68, parent='projectRow')
        self.uiTextMovieP = mc.textField('MovieAddress', text=myMovieFullPath, width=395, alwaysInvokeEnterCommandOnReturn=True, parent='projectRow')
    
        mc.rowLayout('oneRow', numberOfColumns=5, columnAttach5=['left', 'left', 'left', 'left', 'left'], columnWidth5=[5, 68, 70, 170, 80], columnOffset5=[2, 2, 10, 15, 24], adjustableColumn5=True, parent='First_Set')
        mc.text(label=u'开始帧：', w=68, parent='oneRow')
        self.uiTextStartF = mc.textField('startFrame', text=int(self.myStartFrameV), width=60, alwaysInvokeEnterCommandOnReturn=True, parent='oneRow')
        mc.text(label=u'结束帧：', w=68, parent='oneRow')
        self.uiTextEndF = mc.textField('endFrame', text=int(self.myEndFrameV), width=60, alwaysInvokeEnterCommandOnReturn=True, parent='oneRow')
        mc.button(label=u'设置', width=50, command=self.SetRenderStarFram_zwz, backgroundColor=(0.9, 0.5, 0), annotation=u"请输入帧数范围", parent='oneRow')

        mc.rowLayout('twoRow', numberOfColumns=5, columnAttach5=['left', 'left', 'left', 'left', 'left'], columnWidth5=[5, 68, 70, 170, 80], columnOffset5=[2, 2, 10, 15, 24], adjustableColumn5=True, parent='First_Set')
        mc.text(label=u'宽：', w=68, parent='twoRow')
        self.uiTextWidthR = mc.textField('RenderWidth', text=self.myRenderwidth, width=60, alwaysInvokeEnterCommandOnReturn=True, parent='twoRow')
        mc.text(label=u'高：', w=68, parent='twoRow')
        self.uiTextheightR = mc.textField('RenderHeight', text=self.myRenderheight, width=60, alwaysInvokeEnterCommandOnReturn=True, parent='twoRow')
        mc.button(label=u'设置', width=50, command=self.SetRenderWH_zwz, backgroundColor=(0.9, 0.5, 0), annotation=u"请输入渲染尺寸", parent='twoRow')

        self.uiRadioB_TexMG = mc.radioButtonGrp(numberOfRadioButtons=2, cal=[1, 'left'], cw3=[72, 180, 180], label=u'   贴图格式:', labelArray2=[u'jpg(图片一般清晰、文件小)', u'tif(图片清晰、文件大)',], sl=0, parent='First_Set')

        #mc.rowLayout('threeRow', numberOfColumns=6, columnAttach6=['left', 'left', 'left', 'left', 'left', 'left'], columnWidth6=[72, 98, 80, 80, 80, 80], columnOffset5=[2, 2, 10, 15, 24], adjustableColumn6=True, parent='First_Set')
        mc.rowLayout('threeRow', numberOfColumns=7, columnAttach6=['left', 'left', 'left', 'left', 'left', 'left'],columnWidth6=[72, 98, 80, 80, 80, 80],columnOffset5=[2, 2, 10, 15, 24],parent='First_Set')
        mc.text(label=u'显示模式：')
        self.uiCheckB_Nurbs = mc.checkBox("NurbsS_CBox", label='Nurbs Surface', v=False)
        self.uiCheckB_Fluids = mc.checkBox("Fluids_CBox", label='Fluids', v=False)
        self.uiCheckB_Dynamics = mc.checkBox("Dynamics_CBox", label='Dynamics', v=False)
        self.uiCheckB_nParticles = mc.checkBox("nParticles_CBox", label='nParticles', v=False)
        self.uiCheckB_Tex = mc.checkBox("Texture_CBox", label=u'贴图', v=False)
        self.uiCheckB_Locators = mc.checkBox("Locators_CBox", label=u'Locators', v=False)

        # mc.rowLayout('fourRow', numberOfColumns=3, columnAttach3=['left', 'left', 'left'], columnWidth3=[72, 98, 80], columnOffset3=[2, 2, 10], adjustableColumn3=True, parent='First_Set')
        # mc.text(label=u'灯光模式：')
        # self.uiCheckB_Nolight = mc.checkBox("NoLights", label='Use No Lights', v=False)
        # self.uiCheckB_TwoLight = mc.checkBox("Two_Lighting", label='Two Sided Lighting', v=True)
        self.uiRadioB_LightG = mc.radioButtonGrp(numberOfRadioButtons=3, cal=[1, 'left'], cw4=[72, 98, 80, 90], label=u'   灯光模式:', labelArray3=['Default Lighting', 'All Lights', 'No Lights'], sl=0, parent='First_Set')


        two = mc.frameLayout('Cameras_Set', label=u'请选择需要Play Blast的摄像机(面板可拉伸)', labelAlign='top', borderStyle='etchedOut', w=300, h=100, parent='formLyt')
        self.uiTextSCameras = mc.textScrollList('selectCameras', append=self.allCameras, aas=True, allowMultiSelection=True, h=100, parent='Cameras_Set')

        three = mc.columnLayout('Second_Set', parent='formLyt')
        mc.button('SetAll', label=u'Go', width=460, h=25, command=self.Make_it, backgroundColor=(0.2, 0.8, 0.3), parent='Second_Set')
        mc.button('CloseWin', label=u'正常退出', width=460, h=25, command=self.CorrectQuit, backgroundColor=(0.8, 0.2, 0.3), parent='Second_Set')

        mc.formLayout('formLyt', e=True,
                      attachForm=[(one, 'top', 5), (one, 'left', 5), (two, 'right', 5), (two, 'top', 135), (two, 'left', 5), (three, 'left', 5), (three, 'bottom', 5)],
                      attachControl=[(two, 'bottom', 1, three)],
                      attachNone=[(three, 'top')],
                      attachPosition=[(one, 'left', 0, 0), (one, 'top', 0, 0)])
        mc.showWindow(win)

    #设置开始结束帧
    def SetRenderStarFram_zwz(self, *args):
        mc.setAttr("defaultRenderGlobals.animation", 1)
        mc.setAttr("defaultRenderGlobals.putFrameBeforeExt", 1)
        mc.setAttr("defaultRenderGlobals.periodInExt", 1)
        if mc.getAttr("defaultRenderGlobals.outFormatControl") == 1:
            mc.setAttr("defaultRenderGlobals.outFormatControl", 0)
        mc.setAttr("defaultRenderGlobals.extensionPadding", 4)
        self.myStartFrameV = mc.textField(self.uiTextStartF, query=True, text=True)
        self.myEndFrameV = mc.textField(self.uiTextEndF, query=True, text=True)
        mc.setAttr("defaultRenderGlobals.startFrame", self.myStartFrameV)
        mc.setAttr("defaultRenderGlobals.endFrame", self.myEndFrameV)

    #设置PlayBlast的尺寸大小
    def SetRenderWH_zwz(self, *args):
        self.myRenderwidth = float(mc.textField(self.uiTextWidthR, query=True, text=True))
        self.myRenderheight = float(mc.textField(self.uiTextheightR, query=True, text=True))
        mc.setAttr("defaultResolution.width", self.myRenderwidth)
        mc.setAttr("defaultResolution.height", self.myRenderheight)

    #关闭所有弹出来的窗口和plane
    def CloseAllPBWin(self, *args):
        AllWindows = mc.lsUI(windows=True)
        for win in AllWindows:
            # win = str(win)
            if win.find('OCT_QuickPBWin_') >= 0:
                self.closeWin(win)
        AllPlanes = mc.lsUI(p=True)
        for plane in AllPlanes:
            if plane.find('OCT_QuickPBWin_') >= 0:
                mc.deleteUI(plane, panel=True)

    #创建窗口的大小
    def MyWindows_model_zwz(self, myWinName, myCamera):
        myPaneLayoutName = '%s_p' % myWinName
        myModelPanelName = '%s_m' % myWinName
        myCameraShortName = myCamera.split(":")[-1]
        myCameraShortName = myCameraShortName.replace('|','')
        mc.window(myWinName, t=myCameraShortName, w=10, h=10, s=True, rtf=True)
        mc.paneLayout(myPaneLayoutName, w=int(self.myRenderwidth)+4, h=int(self.myRenderheight)+5, configuration='single', aft=0, st=1)
        mc.modelPanel(myModelPanelName, camera=myCamera, mbv=False)
        mc.showWindow(myWinName)
        # mc.paneLayout(myPaneLayoutName, e=True, w=self.myRenderwidth+4, h=self.myRenderheight+5)
        self.myAllWindows.append(myWinName)
        self.myAllModePlanes.append(myModelPanelName)
        return myWinName

    #优化窗口
    def OptimizeWin(self, *args):
        #改变激活窗口的现实效果
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
        self.ActiveModePlane = myactivePlane
        self.ActiveModePlaneModel = mc.modelEditor(myactivePlane, q=True, da=True)
        mc.modelEditor(myactivePlane, e=True, da='boundingBox')
        #改变显示效果
        for myModePlane in self.myAllModePlanes:
            mc.modelEditor(myModePlane, e=True, polymeshes=True, nurbsCurves=False, nurbsSurfaces=False, subdivSurfaces=False,
                   planes=False, lights=False, cameras=False, joints=False, ikHandles=False, deformers=False,
                   dynamics=False, fluids=False, hairSystems=False, follicles=False, nCloths=False, nParticles=False,
                   nRigids=False, dynamicConstraints=False, locators=False, dimensions=False, pivots=False, handles=False,
                   textures=False, strokes=True, motionTrails=False, manipulators=False, clipGhosts=False, grid=False, hud=False)
            mm.eval('updateModelPanelBar %s' % myModePlane)
        #同时播放
        mc.playbackOptions(e=True, v="all")
        #改变窗口的显示
        nurbsCBV = mc.checkBox(self.uiCheckB_Nurbs, q=True, v=True)
        fluidsBV = mc.checkBox(self.uiCheckB_Fluids, q=True, v=True)
        DynamicCBV = mc.checkBox(self.uiCheckB_Dynamics, q=True, v=True)
        nParticleCBV = mc.checkBox(self.uiCheckB_nParticles, q=True, v=True)
        texCBV = mc.checkBox(self.uiCheckB_Tex, q=True, v=True)
        LocatorsCBV = mc.checkBox(self.uiCheckB_Locators, q = True, v = True)
        print texCBV
        # noLightCBV = mc.checkBox(self.uiCheckB_Nolight, q=True, v=True)
        # twoLightCBV = mc.checkBox(self.uiCheckB_TwoLight, q=True, v=True)
        LightRBV = mc.radioButtonGrp(self.uiRadioB_LightG, q=True, sl=True)
        myFinalLightV = ''
        if LightRBV == 1:
            myFinalLightV = "default"
        elif LightRBV == 2:
            myFinalLightV = "all"
        else:
            myFinalLightV = "none"
        for myModePlane in self.myAllModePlanes:
            mc.modelEditor(myModePlane, e=True, displayAppearance="smoothShaded", nurbsSurfaces=nurbsCBV, dl=myFinalLightV, twoSidedLighting=True,
                           fluids=fluidsBV, dynamics=DynamicCBV, nParticles=nParticleCBV,locators = LocatorsCBV,
                           displayTextures=texCBV)
            mm.eval('updateModelPanelBar %s' % myModePlane)
        return True


    #创所有窗口
    def CreateMyWindows_zwz(self, *args):
        self.CloseAllPBWin()
        self.myAllWindows = []
        #self.myAllModePlanes = []
        allSelectCameras = mc.textScrollList(self.uiTextSCameras, q=True, si=True)
        if allSelectCameras:
            for myCamera in allSelectCameras:
                self.myAllModePlanes = []
                myCameraShortName = myCamera.split(":")[-1]
                myCameraShortName = myCameraShortName.replace('|','')
                myWinname = 'OCT_QuickPBWin_%s' % myCameraShortName
                myTmpWinname = self.MyWindows_model_zwz(myWinname, myCamera)
                mc.camera(myCamera, e=True, dr=False, ovr=1)
                mc.window(myTmpWinname, e=True, i=True)
                self.QuickBlast_zwz()
            return True
        else:
            mc.warning(u"请选择摄像机！")
            return False

    #保存图片
    def SavePic_zwz(self, myModelPlane, Frame):
        view = apiUI.M3dView()
        apiUI.M3dView.getM3dViewFromModelPanel(myModelPlane, view)
        myCamera = mc.modelPanel(myModelPlane, q=True, camera=True)
        myCameraShortName = myCamera.split(":")[-1]
        myCameraShortName = myCameraShortName.replace('|','')
        img = om.MImage()
        view.readColorBuffer(img, True)
        myPath = '%s\\%s' % (self.movieFullPath, myCameraShortName)
        if not os.path.isdir(myPath):
            os.makedirs(myPath)
        fileName = str('%s\\%s.%04d.%s' % (myPath, myCameraShortName, Frame, self.TexModel)).encode('gb2312')
        img.writeToFile(fileName, self.TexModel)

    def QuickBlast_zwz(self, *args):
        self.OptimizeWin()
        myStartNum = int(self.myStartFrameV)
        myEndNum = int(self.myEndFrameV)
        mc.select(cl=True)
        mc.currentTime(myStartNum)
        mc.progressWindow(endProgress=True)
        if myEndNum >= myStartNum:
            mc.progressWindow(title=u'准备PlayBlast中', status=u'即将开始', progress=0, min=myStartNum, max=myEndNum, isInterruptable=True)
            for i in range(myStartNum, myEndNum+1):
                if i == myStartNum:
                    mc.progressWindow(edit=True, title=u'超级努力的PlayBlast中：', status=u'祝君好运！O(∩_∩)O~',)
                if mc.progressWindow(q=True, isCancelled=True):
                    mc.progressWindow(endProgress=True)
                    mm.eval('toggleMenuBarsInAllPanels %s;' % self.MenuUIFlag)
                    mm.eval('toggleModelEditorBarsInAllPanels %s;' % self.IconUIFlag)
                    mc.modelEditor(self.ActiveModePlane, e=True, da=self.ActiveModePlaneModel)
                    self.CloseAllPBWin()
                    return False
                mc.progressWindow(edit=True, progress=i)
                mc.currentTime(i)
                for myModelPlane in self.myAllModePlanes:
                    self.SavePic_zwz(myModelPlane, i)
            mc.progressWindow(endProgress=True)
            mm.eval('toggleMenuBarsInAllPanels %s;' % self.MenuUIFlag)
            mm.eval('toggleModelEditorBarsInAllPanels %s;' % self.IconUIFlag)
            mc.modelEditor(self.ActiveModePlane, e=True, da=self.ActiveModePlaneModel)
            self.CloseAllPBWin()
            return True
        self.CloseAllPBWin()

    def Make_it(self, *args):
        saveFlag = mc.confirmDialog(title=u'温馨提示', message=u'拍屏工具存在风险，是否先保存文件？', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='Nn')
        if saveFlag == 'Yes':
            mm.eval("SaveScene")
        elif saveFlag == 'Nn':
            return
        TexMRBV = mc.radioButtonGrp(self.uiRadioB_TexMG, q=True, sl=True)
        if TexMRBV == 1:
            self.TexModel = 'jpg'
        else:
            self.TexModel = 'tif'
        self.SetRenderWH_zwz()
        self.SetRenderStarFram_zwz()
        self.movieFullPath = mc.textField(self.uiTextMovieP, q=True, text=True)
        if not os.path.isdir(self.movieFullPath):
            os.makedirs(self.movieFullPath)
        self.MenuUIFlag = mc.optionVar(q='allowMenusInPanels')
        self.IconUIFlag = mc.optionVar(q='collapseIconBarsInPanels')
        if self.MenuUIFlag == 1:
            mm.eval('toggleMenuBarsInAllPanels 0;')
        if self.IconUIFlag == 0:
            mm.eval('toggleModelEditorBarsInAllPanels 1;')
        if self.CreateMyWindows_zwz():
            #mc.evalDeferred(self.QuickBlast_zwz)
            os.startfile(str(self.movieFullPath).encode('gb2312'))

    #正常退出
    def CorrectQuit(self, *args):
        self.closeWin(self._windowName)
        self.CloseAllPBWin()
        try:
            mc.progressWindow(endProgress=True)
        except:
            pass


# i = QuickPlayAllBlast_C_zwz()
# i.show()