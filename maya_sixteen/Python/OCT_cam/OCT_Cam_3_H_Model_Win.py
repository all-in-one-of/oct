#/usr/bin/env python
#-*-coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

#环幕相机预览,自定义相机
class Cam_3_H_Model_Win():
    def __init__(self):
        self.allCameras = ""
        self.uiTextSCameras = ""
        self.errSelect = []

        self.allCamModel = {}

        self.myactivePlane = ''
        i = 1
        while(i):
            try:
                tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
            except:
                pass
            else:
                if tmp:
                    self.myactivePlane = 'modelPanel%d' % i
                    break
            i += 1
        
    def Cam_3_H_Model_Win_UI(self):
        #环幕
        self.allCameras = mc.listCameras(p = True)
        if mc.window('Cam_Win_UI', ex = True):
            mc.deleteUI("Cam_Win_UI")
        win = mc.window('Cam_Win_UI', t='OCT_3_CamModel', wh=[500, 300], sizeable=True, rtf=True)

        mc.formLayout('formLyt', numberOfDivisions=100)

        two = mc.frameLayout('Cameras_Set', label=u'请选择需要预览的摄像机(面板可拉伸)', labelAlign='top', borderStyle='etchedOut', w=450, parent='formLyt')
        mc.columnLayout(rowSpacing=5)
        for cam in self.allCameras:
            mc.rowLayout(numberOfColumns=4, columnWidth4=(150, 100, 100, 100))
            mc.text(cam, l = cam)
            mc.checkBox("%sL"%cam, l = "L")
            mc.checkBox("%sM"%cam, l = "M")
            mc.checkBox("%sR"%cam, l = "R")
            mc.setParent('..')
        # self.uiTextSCameras = mc.textScrollList('selectCameras', append = self.allCameras, aas=True, allowMultiSelection=True, h=100, parent='Cameras_Set')
        mc.setParent('..')
        three = mc.columnLayout('Second_Set', parent='formLyt')
        mc.button('SetAll', label=u'Go', width=460, h=25, command=lambda*args:self.Cam_1_Model_Win_menu(), backgroundColor=(0.2, 0.8, 0.3), parent='Second_Set')
        mc.button('CloseWin', label=u'正常退出', width=460, h=25, command="", backgroundColor=(0.8, 0.2, 0.3), parent='Second_Set')
        mc.formLayout('formLyt', e=True,
                  attachForm=[(two, 'top', 5), (two, 'left', 5), (two, 'right', 5), (three, 'left', 5), (three, 'bottom', 5)],
                  attachControl=[(two, 'bottom', 1, three)],
                  attachNone=[(three, 'top')],
                  attachPosition=[(two, 'left', 0, 0), (two, 'top', 0, 0)])
        mc.showWindow(win)
        
    def DisplayPoly_zwz(self, myplane):
        mayaversions = mc.about(v=True)
        
        rendererName = mc.modelEditor(self.myactivePlane, q=True, rendererName=True)   
        
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

    def DeletePlane_zwz(self):   #删除Plane
        a = ['', 'F', 'B']
        b = ['UL_panel', 'U_panel', 'UR_panel', 'L_panel', 'M_panel', 'R_panel', 'DL_panel', 'D_panel', 'DR_panel']
        for i in a:
                for j in b:
                    if i == 'F' or i == 'B':
                        planeName = '%s_%s' % (i, j)
                    else:
                        planeName = j
                    if mc.modelPanel(planeName, ex=True):
                        mc.deleteUI(planeName, panel=True)

    def Cam_1_Model_Win_menu(self):
        allWindow=mc.lsUI(wnd=True)
        for wind in allWindow:
            if 'Model_Win' in wind:
                mc.deleteUI(wind)
        self.DeletePlane_zwz()   #删除plane

        allMycamera = mc.listCameras(p=True)
        for myCam in allMycamera:
            mc.camera(myCam, e=True, dr=False, ovr=1,displayFilmGate=False)  #设置相机的分辨率。

        self.allCamModel.clear()
        self.errSelect = []
        #获取选择的相机
        for cam in self.allCameras:
            camL = mc.checkBox("%sL"%cam, q = True, v = True)
            camM = mc.checkBox("%sM"%cam, q = True, v = True)
            camR = mc.checkBox("%sR"%cam, q = True, v = True)
            if camL and camM and camR:
                self.errSelect.append(cam)
            elif camL and camM:
                self.errSelect.append(cam)
            elif camL and camR:
                self.errSelect.append(cam)
            elif camM and camR:
                self.errSelect.append(cam)
            elif camL:
                self.allCamModel.update({cam:"L"})
            elif camM:
                self.allCamModel.update({cam:"M"})
            elif camR:
                self.allCamModel.update({cam:"R"})

        
        if self.errSelect:
            mc.confirmDialog(title=u'警告', message=u'不能一个相机同时选择LMR', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        if len(self.allCamModel) != 3:
            mc.confirmDialog(title=u'警告', message=u'请选择三个相机分别为LMR', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        if mc.window('Cam_3_H_Model_Win', ex = True):
            mc.deleteUI('Cam_3_H_Model_Win')

        mc.window('Cam_3_H_Model_Win', t='OCT_3_CamModel', wh=[900, 300], sizeable=True, rtf=True)
        form = mc.formLayout(numberOfDivisions=100)

        pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)

        myDirt = {}
        for key in self.allCamModel.keys():
            horizontalFilm = mc.getAttr("%s.horizontalFilmAperture"%key)
            verticalFilm = mc.getAttr("%s.verticalFilmAperture"%key)

            myDirt.update({key:[horizontalFilm, verticalFilm]})

            if self.allCamModel[key] == 'L':
                mc.modelPanel('L_panel', camera= key, mbv=False, l='L', p='pane1')
                self.DisplayPoly_zwz('L_panel')
            elif self.allCamModel[key] == 'M':
                mc.modelPanel('M_panel', camera= key, mbv=False, l='M', p='pane2')
                self.DisplayPoly_zwz('M_panel')
            elif self.allCamModel[key] == 'R':
                mc.modelPanel('R_panel', camera= key, mbv=False, l='R', p='pane3')
                self.DisplayPoly_zwz('R_panel')

        num = float(myDirt.values()[0][0])+float(myDirt.values()[1][0])+float(myDirt.values()[2][0])
        number = 100/(num)
        number1 = int(number * (float(myDirt.values()[0][0])))
        number2 = int(number * (float(myDirt.values()[1][0])) + number1)
        number3 = int(number * (float(myDirt.values()[1][0])) + number2)

        mc.formLayout(form, e=True,
                    attachForm=[(pane1, 'left', 1), (pane1 , 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane1, 'bottom', 1), (pane2, 'bottom', 1), (pane3, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, number1), (pane2, 'left', 0, number1), (pane2, 'right', 0, number2), (pane3, 'left', 0, number2), (pane3, 'right', 0, number3)])
        
        _h = ""

        if myDirt.values()[0][1] >= float(myDirt.values()[1][1]):
            _h = myDirt.values()[0][1]
        else:
            _h = myDirt.values()[1][1]

        if myDirt.values()[2][1] >= _h:
            _h = myDirt.values()[2][1]

        _w = myDirt.values()[0][0] + myDirt.values()[1][0] + myDirt.values()[2][0]

        _hight = int(_h*200)
        _width = int(_w*200)

        #mc.showWindow("Cam_3_H_Model_Win")
        mm.eval('toggleMenuBarsInAllPanels 1;')
        mc.showWindow('Cam_3_H_Model_Win')
        mc.window('Cam_3_H_Model_Win', e=True, wh=[_width, _hight])
        mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')
           
        

#Cam_3_H_Model_Win().Cam_3_H_Model_Win_UI()