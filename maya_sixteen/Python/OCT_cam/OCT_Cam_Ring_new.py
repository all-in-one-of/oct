#/usr/bin/env python
#-*-coding: utf-8 -*-
#import time
import maya.cmds as mc
import maya.mel as mm


class Ring_Cam_Win(object):
    def __init__(self):
        self.camList = mc.listCameras(p=True)
        self.minCameraNum = 2
        self.maxCameraNum = 6

        self.main_win_width = 400
        self.main_win_Heigh = 25

        self.view_win_width = 900
        self.view_win_heigh = 150

        self.camNumField = ''


    # --------------
    # 相机设置窗口
    # --------------
    def cam_Main_Win(self):
        if mc.window('Ring_Cam_UI', ex = True):
            mc.deleteUI("Ring_Cam_UI")
        self.main_win = mc.window('Ring_Cam_UI', t=u'环幕相机', wh=[self.main_win_width, self.main_win_Heigh], rtf=True, sizeable=False)
        mc.window(self.main_win, e =True, h = 25)
        mainFormLayout = mc.formLayout()
        rowLay = mc.rowLayout(nc=6, h = 25, rowAttach=[(1,'top', 4), (2,'top', 2), (3,'top', 0), (4,'top', 0), (5,'top', 0), (6,'top', 0)])
        mc.text(l=u'视图数', w=50)
        self.camNumField = mc.intField(v=2, w=30, min = self.minCameraNum, max = self.maxCameraNum)
        mc.button(l=u'生成', w=50, c = lambda *arge:self.build_Cam())
        mc.text(l='', w=self.main_win_width-240)
        self.allChangeZero_button = mc.button(l = u"全归0", w = 30, vis = False)
        self.open_cam_view_button = mc.button(l=u'打开相机视图', w=80, vis = False)
        mc.setParent('..')
        self.camPaneLay = mc.paneLayout(cn = 'single')
        self.camColumnLay = mc.columnLayout()
        mc.formLayout(mainFormLayout, e =True,
                      attachForm = [(rowLay, 'top', 5), (rowLay, 'left', 5), (rowLay, 'right', 5), (self.camPaneLay, 'bottom', 5)],
                      attachControl = [(rowLay, 'bottom', 5, self.camPaneLay)])

        mc.showWindow(self.main_win)

    def build_Cam(self):
        self.camList = mc.listCameras(p=True)
        self.delete_camColumnLay_UI()
        camNum = self.getCamNum_intField()
        self.camColumnLay = mc.columnLayout( adjustableColumn=True, rowSpacing=10, p = self.camPaneLay )
        mc.text(l = u'请分配好相机位,不使用的相机放到0位，其他相机位按左到右依次排列', p = self.camColumnLay, h = 10, al = 'left')
        self.cam_Main_Win_Heigh_Anim()
        for camName in self.camList:
            self.radioButtonGrp_ui(camName, int(camNum))
        
        mc.button(self.open_cam_view_button, e =True, c = lambda *arge:self.cam_View_Win(), vis = True)
        mc.button(self.allChangeZero_button, e =True, c = lambda *arge:self.allChangeZero(), vis = True)

    def cam_Main_Win_Heigh_Anim(self):
        camera_num = len(self.camList)
        for height in xrange(35, camera_num*35+60):
            mc.window(self.main_win, e =True, h = height)
            #time.sleep(0.0009)

    def radioButtonGrp_ui(self, cameraName, cameraNum):
        mc.rowLayout(nc=100, p = self.camColumnLay, h = 25)
        mc.text(l=cameraName, w=100, h =25)
        cam_radio_name = '%s_radio' %(cameraName)
        mc.radioCollection(cam_radio_name)
        for num in xrange(cameraNum+1):
            cam_radioButton_name = '%s_%s' %(cameraName, str(num))
            mc.radioButton(cam_radioButton_name, label=str(num))
        mc.setParent('..')
        mc.radioCollection(cam_radio_name, e =True, sl = '%s_0' %(cameraName))

    def delete_camColumnLay_UI(self):
        resule = mc.columnLayout(self.camColumnLay, q =True, ex = True)
        if resule:
            mc.deleteUI(self.camColumnLay)

    def allChangeZero(self):
        for camName in self.camList:
            cam_radio_name = '%s_radio' %(camName)
            mc.radioCollection(cam_radio_name, e = True, sl = '%s_0' %(camName))

    # --------------
    # 相机视图窗口
    # --------------
    def OpenCamViewWin_before(self):
        if mc.window('Ring_Cam_View', ex = True):
            mc.deleteUI('Ring_Cam_View')

        self.CalculationCamViewInfo()
        self.CalculationFilmAperture()

    def cam_View_Win(self):
        self.OpenCamViewWin_before()
        
        self.view_win = mc.window('Ring_Cam_View', t=u'相机视图', wh=[self.view_win_width, self.view_win_heigh], sizeable=True, rtf=True)
        form = mc.formLayout(numberOfDivisions=100)
        
        camNum = len(self.camViewInfo)
        
        for num in xrange(camNum):
            if (int(num)+1) not in self.camViewInfo:
                mc.error(u'%d号位置没有相机，请确定相机' %(int(num)+1))
            camName = self.camViewInfo[int(num)+1]
            panelName = '%s_panel' %camName
            modelPanelName = '%s_modelPanel' %camName
            self.deleteModelPanel(modelPanelName)
            mc.paneLayout(panelName, w=150, h=150, configuration='single', p=form, st=1)
            mc.modelPanel(modelPanelName, camera= camName, mbv=False, p=panelName)
            self.DisplayPoly_zwz(modelPanelName)
        
        (_h, _v) = self.formLayout_Edit(form)
        self.view_win_width = _h * 200
        self.view_win_heigh = _v * 200
        mc.window('Ring_Cam_View', e = True, wh = [self.view_win_width, self.view_win_heigh])
        mc.showWindow(self.view_win)
        mm.eval('toggleMenuBarsInAllPanels 1;')

    def formLayout_Edit(self, form):
        count = len(self.camViewInfo)
        
        sumHor = 0
        maxVer = 0
        for [hor, ver] in self.camFilmAperture.values():
            sumHor += hor
            maxVer = max(maxVer, ver)
        perHor = 100/sumHor

        camPanelLeftDistance = 0
        for num in xrange(count):
            camName = self.camViewInfo[int(num)+1]
            panelHorNum = int(self.camFilmAperture[camName][0] * perHor)
            panelName = '%s_panel' %camName
            
            mc.camera(camName, e=True, dr=False, ovr=1,displayFilmGate=False)

            mc.formLayout(form, e = True, 
                          attachForm = [(panelName, 'top', 1), (panelName, 'bottom', 1)], 
                          attachPosition = [(panelName, 'left', 0, camPanelLeftDistance), (panelName, 'right', 0, (camPanelLeftDistance+panelHorNum))]
                          )
            camPanelLeftDistance += panelHorNum
        return (sumHor, maxVer)

    def DisplayPoly_zwz(self, myplane):
        mayaversions = mc.about(v=True)
        activePlane = self.getActivePlane()
        rendererName = mc.modelEditor(activePlane, q=True, rendererName=True)   
        
        if mayaversions.find('2009') >= 0:
            mc.modelEditor(myplane, e=True, polymeshes=True, nurbsCurves=False, nurbsSurfaces=False, subdivSurfaces=False,
                           planes=False, lights=False, cameras=False, joints=False, ikHandles=False, deformers=False,
                           dynamics=False, fluids=True, hairSystems=False, follicles=False, nCloths=False, nParticles=False,
                           nRigids=False, dynamicConstraints=False, locators=False, dimensions=False, pivots=False, handles=False,
                           textures=False, strokes=False, manipulators=False, grid=False, hud=False, rendererName = rendererName)

        else:
            mc.modelEditor(myplane, e=True, polymeshes=True, nurbsCurves=False, nurbsSurfaces=False, subdivSurfaces=False,
                           planes=False, lights=False, cameras=False, joints=False, ikHandles=False, deformers=False,
                           dynamics=False, fluids=True, hairSystems=False, follicles=False, nCloths=False, nParticles=False,
                           nRigids=False, dynamicConstraints=False, locators=False, dimensions=False, pivots=False, handles=False,
                           textures=False, strokes=False, motionTrails=False, manipulators=False, clipGhosts=False, grid=False, hud=False, rendererName = rendererName)

    def getActivePlane(self):
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
        return activePlane

    def deleteModelPanel(self, planeName):
        if mc.modelPanel(planeName, ex=True):
            mc.deleteUI(planeName, panel=True)

    # --------------
    # 公用Function
    # --------------
    def getCamNum_intField(self):
        if self.camNumField:
            camNum = mc.intField(self.camNumField, q = True, v = True)
        else:
            camNum = 0
        return camNum

    def CalculationCamViewInfo(self):
        self.camViewInfo = {}
        for camName in self.camList:
            cam_radio_name = '%s_radio' %(camName)
            cam_radio_Item = mc.radioCollection(cam_radio_name, q = True, sl = True)
            cam_Index = int(cam_radio_Item[-1])
            if (cam_Index > 0):
                if cam_Index in self.camViewInfo:
                    mc.error(u'请不要在同一个相机位选择2个不同的相机')
                else:
                    self.camViewInfo[cam_Index] = camName
        if not self.camViewInfo:
            mc.error(u'没有相机，请选择相机后再打开视图窗口！')

    def CalculationFilmAperture(self):
        self.camFilmAperture = {}
        for camName in self.camViewInfo.values():
            horizontalFilm = mc.getAttr("%s.horizontalFilmAperture"%camName)
            verticalFilm = mc.getAttr("%s.verticalFilmAperture"%camName)
            self.camFilmAperture[camName] = [horizontalFilm, verticalFilm]




