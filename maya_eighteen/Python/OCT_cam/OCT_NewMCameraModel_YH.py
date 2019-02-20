#/usr/bin/env python
#-*-coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

class multipleCameraPanels():
    def __init__(self):
        #存放显示的窗口和窗口的大小
        self.camWH={}
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
            
    #关闭所有的相机窗口
    def closeAllCamMenu(self):
        allWindow=mc.lsUI(wnd=True)
        if allWindow:
            for wind in allWindow:
                if 'Model_Win' in wind:
                    mc.deleteUI(wind)
    
    #显示物体
    def DisplayPoly(self,myPlane):
        mayaversions=mc.about(v=True)
        
        rendererName = mc.modelEditor(self.myactivePlane, q=True, rendererName=True)   
        
        if mayaversions.find('2009')>=0:
            mc.modelEditor(myPlane, e=True, polymeshs=True, nurbsCurves=False, nurbsSurfaces=False, subdivSurfaces=False,
                            planes=True, light=False, cameras=False, joints=False, ikHandles=False, deformers=False, dynamics=False,
                            fluids=True, hairSystems=False, follicles=False, nCloths=False, nParticles=False, nRigids=False,
                            dynamicConstraints=False, locators=False, dimension=False, pivots=False, handles=False, textures=False,
                            strokes=False, manipulators=False, grid=False, hud=False, rendererName = rendererName)
        else:
            mc.modelEditor(myPlane, e=True, polymeshes=True, nurbsCurves=False, nurbsSurfaces=False, subdivSurfaces=False,
                            planes=False, lights=False, cameras=False, joints=False, ikHandles=False, deformers=False,
                            dynamics=False, fluids=True, hairSystems=False, follicles=False, nCloths=False, nParticles=False,
                            nRigids=False, dynamicConstraints=False, locators=True, dimensions=False, pivots=False, handles=False,
                            textures=False, strokes=False, motionTrails=False, manipulators=False, clipGhosts=False, grid=False, hud=False, rendererName = rendererName)
    
    #删除所有的panel
    def DeletePlane(self):
        a=['', 'F', 'B']
        b=['UL_panel', 'U_panel', 'UR_panel', 'L_panel', 'M_panel', 'R_panel', 'DL_panel', 'D_panel', 'DR_panel']
        for i in a:
            for j in b:
                if i=='F' or i=='B':
                    planeName='%s_%s' %(i, j)
                else:
                    planeName=j
                if mc.modelPanel(planeName, ex=True):
                    mc.deleteUI(planeName, panel=True)

    #设置相机的分辨率
    def SetRightSize(self):
        allMycamera=mc.listCameras(p=True)
        for myCam in allMycamera:
            mc.camera(myCam, e=True, dr=False, ovr=1, displayFilmGate=False)
            
            
    #查找相机
    def findCamera(self,name):
        numName=len(name)
        allMyCamera=mc.listCameras(p=True)
        for myCamera in allMyCamera:
            if myCamera[-numName:]==name:
                return myCamera
        return None

    def unLockOverscan(self):
        allMyCamera=mc.listCameras(p=True)
        for myCamera in allMyCamera:
            mc.setAttr(myCamera+".overscan",l=False)
            mc.setAttr(myCamera+".overscan",1)
    #添加六个panel的组
    def AddSixGroup(self):
        tmpCam=self.findCamera('CamL_A')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_A')
        mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
        self.DisplayPoly('UL_panel')

        tmpCam=self.findCamera('CamL_B')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_B')
        mc.modelPanel('U_panel', camera=tmpCam, mbv=False, l='U', p='pane2')
        self.DisplayPoly('U_panel')

        tmpCam=self.findCamera('CamL_C')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_C')
        mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
        self.DisplayPoly('UR_panel')

        tmpCam=self.findCamera('CamL_A')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_2_A')
        mc.modelPanel('L_panel', camera=tmpCam, mbv=False, l='L', p='pane4')
        self.DisplayPoly('L_panel')

        tmpCam=self.findCamera('CamL_B')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_2_B')
        mc.modelPanel('M_panel', camera=tmpCam, mbv=False, l='M',p='pane5')
        self.DisplayPoly('M_panel')

        tmpCam=self.findCamera('CamL_C')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_2_C')
        mc.modelPanel('R_panel',camera=tmpCam, mbv=False, l='R', p='pane6')
        self.DisplayPoly('R_panel')
        
    #添加六个panel的组
    def AddSixGroup_FKBS(self):
        tmpCam=self.findCamera('test_Cam_1_A')
        mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
        self.DisplayPoly('UL_panel')

        tmpCam=self.findCamera('test_Cam_1_B')
        mc.modelPanel('U_panel', camera=tmpCam, mbv=False, l='U', p='pane2')
        self.DisplayPoly('U_panel')

        tmpCam=self.findCamera('test_Cam_1_C')
        mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
        self.DisplayPoly('UR_panel')

        tmpCam=self.findCamera('test_Cam_2_A')
        print tmpCam
        mc.modelPanel('L_panel', camera=tmpCam, mbv=False, l='L', p='pane4')
        self.DisplayPoly('L_panel')

        tmpCam=self.findCamera('test_Cam_2_B')
        mc.modelPanel('M_panel', camera=tmpCam, mbv=False, l='M',p='pane5')
        self.DisplayPoly('M_panel')

        tmpCam=self.findCamera('test_Cam_2_C')
        mc.modelPanel('R_panel',camera=tmpCam, mbv=False, l='R', p='pane6')
        self.DisplayPoly('R_panel')
        
    #神话相机
    def AddTwelve_SH(self):
        tmpCam=self.findCamera('camL_1_A')
        mc.modelPanel('F_UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
        self.DisplayPoly('F_UL_panel')

        tmpCam=self.findCamera('camL_1_B')
        mc.modelPanel('F_U_panel', camera=tmpCam, mbv=False, l='U', p='pane2')
        self.DisplayPoly('F_U_panel')

        tmpCam=self.findCamera('camL_1_C')
        mc.modelPanel('F_UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
        self.DisplayPoly('F_UR_panel')

        tmpCam=self.findCamera('camL_1_D')
        mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane4')
        self.DisplayPoly('UR_panel')

        tmpCam=self.findCamera('camL_2_A')
        mc.modelPanel('F_L_panel', camera=tmpCam, mbv=False, l='L', p='pane5')
        self.DisplayPoly('F_L_panel')

        tmpCam=self.findCamera('camL_2_B')
        mc.modelPanel('F_M_panel', camera=tmpCam, mbv=False, l='M',p='pane6')
        self.DisplayPoly('F_M_panel')

        tmpCam=self.findCamera('camL_2_C')
        mc.modelPanel('B_R_panel',camera=tmpCam, mbv=False, l='R', p='pane7')
        self.DisplayPoly('B_R_panel')

        tmpCam=self.findCamera('camL_2_D')
        mc.modelPanel('B_UR_panel', camera=tmpCam, mbv=False, l='L', p='pane8')
        self.DisplayPoly('B_UR_panel')

        tmpCam=self.findCamera('camL_3_A')
        mc.modelPanel('B_M_panel', camera=tmpCam, mbv=False, l='M',p='pane9')
        self.DisplayPoly('B_M_panel')

        tmpCam=self.findCamera('camL_3_B')
        mc.modelPanel('B_DL_panel',camera=tmpCam, mbv=False, l='R', p='pane10')
        self.DisplayPoly('B_DL_panel')

        tmpCam=self.findCamera('camL_3_C')
        mc.modelPanel('B_D_panel',camera=tmpCam, mbv=False, l='R', p='pane11')
        self.DisplayPoly('B_D_panel')

        tmpCam=self.findCamera('camL_3_D')
        mc.modelPanel('B_DR_panel',camera=tmpCam, mbv=False, l='R', p='pane12')
        self.DisplayPoly('B_DR_panel')

    def AddSevenGroup_1(self):
        tmpCam=self.findCamera('test_CamL_A')
        if not tmpCam:
            tmpCam=self.findCamera('test_CamL_1_A')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_A')    
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_A')          
        mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
        self.DisplayPoly('UL_panel')

        tmpCam=self.findCamera('test_CamL_B')
        if not tmpCam:      
            tmpCam=self.findCamera('test_CamL_1_B')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_B')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_B')
        mc.modelPanel('U_panel', camera=tmpCam,mbv=False, l='U', p='pane2')
        self.DisplayPoly('U_panel')

        tmpCam=self.findCamera('test_CamL_C')
        if not tmpCam:
            tmpCam=self.findCamera('test_CamL_1_C')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_C')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_C')
        mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
        self.DisplayPoly('UR_panel')
    
    def AddSevenGroup_2(self):
        tmpCam=self.findCamera('test_CamL_D')
        if not tmpCam:
            tmpCam=self.findCamera('test_CamL_1_D')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_D')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_D')
        mc.modelPanel('L_panel', camera=tmpCam, mbv=False, l='L', p='pane4')
        self.DisplayPoly('L_panel')
    
    def AddSevenGroup_3(self):
        tmpCam=self.findCamera('test_CamL_E')
        if not tmpCam:
            tmpCam=self.findCamera('test_CamL_1_E')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_E')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_E')  
        mc.modelPanel('M_panel', camera=tmpCam, mbv=False, l='M', p='pane5')
        self.DisplayPoly('M_panel') 

        tmpCam=self.findCamera('test_CamL_F')
        if not tmpCam:
            tmpCam=self.findCamera('test_CamL_1_F')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_F')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_F')      
        mc.modelPanel('R_panel', camera=tmpCam, mbv=False, l='R', p='pane6')
        self.DisplayPoly('R_panel') 

        tmpCam=self.findCamera('test_CamL_G')
        if not tmpCam:
            tmpCam=self.findCamera=('test_CamL_1_G')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_G')
        if not tmpCam:
            tmpCam=self.findCamera('CamL_1_G')
        mc.modelPanel('DL_panel', camera=tmpCam,mbv=False, l='DL', p='pane7')
        self.DisplayPoly('DL_panel') 

    def AddSixGroup_1(self):
        tmpCam=self.findCamera('test_CamL_1_A')   
        mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
        self.DisplayPoly('UL_panel')

        tmpCam=self.findCamera('test_CamL_1_B')
        mc.modelPanel('U_panel', camera=tmpCam,mbv=False, l='U', p='pane2')
        self.DisplayPoly('U_panel')

        tmpCam=self.findCamera('test_CamL_1_C')
        mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
        self.DisplayPoly('UR_panel')
            
    def AddSixGroup_2(self):
        tmpCam=self.findCamera('CamL_1_E')  
        mc.modelPanel('M_panel', camera=tmpCam, mbv=False, l='M', p='pane5')
        self.DisplayPoly('M_panel') 

        tmpCam=self.findCamera('CamL_1_F')      
        mc.modelPanel('R_panel', camera=tmpCam, mbv=False, l='R', p='pane6')
        self.DisplayPoly('R_panel') 

        tmpCam=self.findCamera('CamR_1_G')
        mc.modelPanel('DL_panel', camera=tmpCam,mbv=False, l='DL', p='pane7')
        self.DisplayPoly('DL_panel') 

    def AddThirdGroup_1(self):
        tmpCam=self.findCamera('test_1_A') 
        mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='M', p='pane1')
        self.DisplayPoly('UL_panel') 

        tmpCam=self.findCamera('test_1_B')      
        mc.modelPanel('U_panel', camera=tmpCam, mbv=False, l='R', p='pane2')
        self.DisplayPoly('U_panel') 

        tmpCam=self.findCamera('test_1_C')
        mc.modelPanel('UR_panel', camera=tmpCam,mbv=False, l='DL', p='pane3')
        self.DisplayPoly('UR_panel') 

    def AddTwoGroup(self):
        tmpCam = self.findCamera('upCam')
        mc.modelPanel('U_panel', camera = tmpCam, mbv = False, l = 'U', p = 'pane1')
        self.DisplayPoly('U_panel')

        tmpCam = self.findCamera('downCam')
        mc.modelPanel('D_panel', camera = tmpCam, mbv = False, l = 'D', p = 'pane2')
        self.DisplayPoly('D_panel')

    def Add_CDFKBS_SixGroup(self):
        tmpCam=self.findCamera('cam1L')   
        mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
        self.DisplayPoly('UL_panel')

        tmpCam=self.findCamera('cam2L')
        mc.modelPanel('U_panel', camera=tmpCam,mbv=False, l='U', p='pane2')
        self.DisplayPoly('U_panel')

        tmpCam=self.findCamera('cam3L')
        mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
        self.DisplayPoly('UR_panel')

        tmpCam=self.findCamera('cam4L')
        mc.modelPanel('M_panel', camera=tmpCam, mbv=False, l='M', p='pane4')
        self.DisplayPoly('M_panel') 

        tmpCam=self.findCamera('cam5L')
        mc.modelPanel('R_panel', camera=tmpCam, mbv=False, l='R', p='pane5')
        self.DisplayPoly('R_panel') 

        tmpCam=self.findCamera('cam6L')
        mc.modelPanel('DL_panel', camera=tmpCam, mbv=False, l='DL', p='pane6')
        self.DisplayPoly('DL_panel')


    #创建窗口   
    '''def Cam_6_Model_Win_menu(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize() 
        if mc.window('Cam_6_Model_Win', ex=True):
            mc.deleteUI('Cam_6_Model_Win')
        mc.window('Cam_6_Model_Win', t='OCT_6_CamModel', wh=[725, 502], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane4=mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane5=mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane6=mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane4, 'left', 1), (pane4, 'bottom', 1),
                    (pane5, 'bottom', 1), (pane6, 'right', 1), (pane6, 'bottom', 1)],
                    
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 28), (pane2, 'left', 0, 28), (pane2, 'right', 0, 71), (pane3, 'left', 0, 71), (pane3, 'right', 0, 99), 
                    (pane4, 'left', 0, 0), (pane4, 'right', 0, 28), (pane5, 'left', 0, 28), (pane5, 'right', 0, 71), (pane6, 'left', 0, 71), (pane6, 'right', 0, 99), (pane1, 'top', 0, 0), 
                    (pane1, 'bottom', 0, 55), (pane2, 'top', 0, 0), (pane2, 'bottom', 0, 55), (pane3, 'top', 0, 0), (pane3, 'bottom', 0, 55), (pane4, 'top', 0, 55), (pane4, 'bottom', 0, 99), 
                    (pane5, 'top', 0, 55), (pane5, 'bottom', 0, 99), (pane6, 'top', 0, 55), (pane6, 'bottom', 0, 99)])
        
        self.AddSixGroup()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_6_Model_Win')
        mc.window('Cam_6_Model_Win', e=True, wh=[700, 367])'''    
    
    '''def Cam_7_Model_Win_menu(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        #第一个窗口
        if mc.window('Cam_7_Model_Win1', ex=True):
            mc.deleteUI('Cam_7_Model_Win1')
        mc.window('Cam_7_Model_Win1', t='OCT_7_CamModel_ABC', wh=[500, 500], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane1, 'bottom', 1), (pane2, 'bottom', 1), (pane3, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66), (pane3, 'right', 0, 99)])      
        self.AddSevenGroup_1()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_7_Model_Win1')
        mc.window('Cam_7_Model_Win1', e=True, wh=[904, 461])
        
        #第二个窗口
        if mc.window('Cam_7_Model_Win2', ex=True):
            mc.deleteUI('Cam_7_Model_Win2')
        mc.window('Cam_7_Model_Win2', t='OCT_7_CamModel_D', wh=[300, 300], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)

        pane4=mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form, e=True,
                    attachForm=[(pane4, 'left', 1), (pane4, 'top', 1), (pane4, 'right', 1), (pane4, 'bottom', 1)],
                    attachPosition=[(pane4, 'left', 0, 0), (pane4, 'right', 0, 100)])
        self.AddSevenGroup_2()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_7_Model_Win2')
        mc.window('Cam_7_Model_Win2', e=True, wh=[304, 605])
        
        #第三个窗口
        if mc.window('Cam_7_Model_Win3', ex=True):
            mc.deleteUI('Cam_7_Model_Win3')
        mc.window('Cam_7_Model_Win3', t='OCT_7_CamModel_EFG', wh=[500, 500], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane5=mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane6=mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane7=mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form, e=True,
                    attachForm=[(pane5, 'left', 1), (pane5, 'top', 1), (pane6, 'top', 1), (pane7, 'top', 1), (pane7, 'right', 1), (pane5, 'bottom', 1), (pane6, 'bottom', 1), (pane7, 'bottom', 1)],
                    attachPosition=[(pane5, 'left', 0, 0), (pane5, 'right', 0, 33), (pane6, 'left', 0, 33), (pane6, 'right', 0 ,66), (pane7, 'left', 0, 66), (pane7, 'right', 0, 99)])
        self.AddSevenGroup_3()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_7_Model_Win3')
        mc.window('Cam_7_Model_Win3', e=True, wh=[904, 461])'''

    '''#柳州魔豆
    def Cam_3_Model_Win_menu_MoDou(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        if mc.window('Cam_3_Model_Win_menu_MoDou',ex=True):
            mc.deleteUI('Cam_3_Model_Win_menu_MoDou')
        mc.window('Cam_3_Model_Win_menu_MoDou',t='Cam_3_Model_Win_menu_MoDou',wh=[500,500],sizeable=True,rtf=True)
        format=mc.formLayout(numberOfDivisions=100)

        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        
        mc.formLayout(form, e=True,
                    attachForm=[(pane1, 'left', 1), (pane1 , 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane1, 'bottom', 1), (pane2, 'bottom', 1), (pane3, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66), (pane3, 'right', 0, 99)])
                
        self.AddSevenGroup_1()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_3_Model_Win_menu_MoDou')
        mc.window('Cam_3_Model_Win_menu_MoDou', e=True, wh=[1000, 500])'''

        
    def Cam_3_Model_Win_menu_MoDou(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        if mc.window('Cam_3_Model_Win_menu_MoDou', ex=True):
            mc.deleteUI('Cam_3_Model_Win_menu_MoDou')
        mc.window('Cam_3_Model_Win_menu_MoDou', t='Cam_3_Model_Win_menu_MoDou', wh=[500, 500],sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        
        mc.formLayout(form, e=True,
                    attachForm=[(pane1, 'left', 1), (pane1 , 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane1, 'bottom', 1), (pane2, 'bottom', 1), (pane3, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66), (pane3, 'right', 0, 99)
])
                
        self.AddSevenGroup_1()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_3_Model_Win_menu_MoDou')
        mc.window('Cam_3_Model_Win_menu_MoDou', e=True, wh=[607, 702])


    def Cam_6_Model_Win_menu_FKBS(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        #第一个窗口
        if mc.window('Cam_6_Model_Win1', ex=True):
            mc.deleteUI('Cam_6_Model_Win1')
        mc.window('Cam_6_Model_Win1', t='OCT_6_CamModel_ABC', wh=[500, 500], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane1, 'bottom', 1), (pane2, 'bottom', 1), (pane3, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66), (pane3, 'right', 0, 99)])      
        self.AddSixGroup_1()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_6_Model_Win1')
        mc.window('Cam_6_Model_Win1', e=True, wh=[1502, 752])
        
        #第二个窗口
        if mc.window('Cam_6_Model_Win2', ex=True):
            mc.deleteUI('Cam_6_Model_Win2')
        mc.window('Cam_6_Model_Win2', t='OCT_6_CamModel_EFG', wh=[500, 500], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane5=mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane6=mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane7=mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form, e=True,
                    attachForm=[(pane5, 'left', 1), (pane5, 'top', 1), (pane6, 'top', 1), (pane7, 'top', 1), (pane7, 'right', 1), (pane5, 'bottom', 1), (pane6, 'bottom', 1), (pane7, 'bottom', 1)],
                    attachPosition=[(pane5, 'left', 0, 0), (pane5, 'right', 0, 33), (pane6, 'left', 0, 33), (pane6, 'right', 0 ,66), (pane7, 'left', 0, 66), (pane7, 'right', 0, 99)])
        self.AddSixGroup_2()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_6_Model_Win2')
        mc.window('Cam_6_Model_Win2', e=True, wh=[1502, 752])

    def Cam_4_Model_Win_menu_FKBS(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        self.unLockOverscan()
        #第一个窗口
        if mc.window('Cam_3_Model_Win_FKBS', ex=True):
            mc.deleteUI('Cam_3_Model_Win_FKBS')
        mc.window('Cam_3_Model_Win_FKBS', t='OCTCam_3_Model_Win_FKBS', wh=[500, 500], sizeable=True, rtf=True)

        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane4=mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane5=mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane6=mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane3, 'right', 1), (pane4, 'left', 1), (pane4, 'bottom', 1),
                    (pane5, 'bottom', 1), (pane6, 'right', 1), (pane6, 'bottom', 1)],
                    
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66), (pane3, 'right', 0, 99), 
                    (pane4, 'left', 0, 0), (pane4, 'right', 0, 33), (pane5, 'left', 0, 33), (pane5, 'right', 0, 66), (pane6, 'left', 0, 66), (pane6, 'right', 0, 99), (pane1, 'top', 0, 0), 
                    (pane1, 'bottom', 0, 66), (pane2, 'top', 0, 0), (pane2, 'bottom', 0, 66), (pane3, 'top', 0, 0), (pane3, 'bottom', 0, 66), (pane4, 'top', 0, 66), (pane4, 'bottom', 0, 99), 
                    (pane5, 'top', 0, 66), (pane5, 'bottom', 0, 99), (pane6, 'top', 0, 66), (pane6, 'bottom', 0, 99)])

        self.AddSixGroup_FKBS()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_3_Model_Win_FKBS')
        mc.window('Cam_3_Model_Win_FKBS', e=True, wh=[962, 482])

    def Cam_6_Model_Win_menu_CDFKBS(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        #创建窗口
        if mc.window('Cam_6_Model_Win_menu_CDFKBS', ex=True):
            mc.deleteUI('Cam_6_Model_Win_menu_CDFKBS')
        mc.window('Cam_6_Model_Win_menu_CDFKBS', t='Cam_6_Model_Win_menu_CDFKBS', wh=[500, 500], sizeable=True, rtf=True)
        form = mc.formLayout(numberOfDivisions=100)
        pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane4, 'top', 1), (pane5, 'top', 1), (pane6, 'top', 1), 
                            (pane6, 'right', 1), (pane1, 'bottom', 1), (pane2, 'bottom', 1), (pane3, 'bottom', 1), (pane4, 'bottom', 1), (pane5, 'bottom', 1), (pane6, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 16.6), (pane2, 'left', 0, 16.6), (pane2, 'right', 0, 33.2), (pane3, 'left', 0, 33.2), (pane3, 'right', 0, 49.8),
                            (pane4, 'left', 0, 49.8), (pane4, 'right', 0, 66.4), (pane5, 'left', 0, 66.4), (pane5, 'right', 0, 83), (pane6, 'left', 0, 83), (pane6, 'right', 0, 99.6)])      
        
        self.Add_CDFKBS_SixGroup()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_6_Model_Win_menu_CDFKBS')
        mc.window('Cam_6_Model_Win_menu_CDFKBS', e=True, wh=[2127, 476])


    def Cam_6_Model_Win_menu_SH(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()
        #创建窗口
        if mc.window('Cam_6_Model_Win_menu_SH', ex=True):
            mc.deleteUI('Cam_6_Model_Win_menu_SH')
        mc.window('Cam_6_Model_Win_menu_SH', t='OCT_Cam_6_Model_Win_menu_SH', wh=[500, 500], sizeable=True, rtf=True)

        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane3=mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane4=mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane5=mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane6=mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane7=mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane8=mc.paneLayout('pane8', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane9=mc.paneLayout('pane9', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane10=mc.paneLayout('pane10', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane11=mc.paneLayout('pane11', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        pane12=mc.paneLayout('pane12', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1), (pane4, 'top', 1), (pane4, 'right', 1),
                    (pane5, 'left', 1), (pane8, 'right', 1), (pane9, 'bottom', 1), (pane9, 'left', 1), (pane10, 'bottom', 1), (pane11, 'bottom', 1), 
                    (pane12, 'right', 1),(pane12, 'bottom', 1)],

                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 25), (pane2, 'left', 0, 25), (pane2, 'right', 0, 50), (pane3, 'left', 0, 50), (pane3, 'right', 0, 75), 
                    (pane4, 'left', 0, 75), (pane4, 'right', 0, 100), (pane5, 'left', 0, 0), (pane5, 'right', 0, 25), (pane6, 'left', 0, 25), (pane6, 'right', 0, 50),(pane7, 'left', 0, 50),
                    (pane7, 'right', 0, 75), (pane8, "left", 0, 75), (pane8, "right", 0, 100), (pane9, "left", 0, 0), (pane9, "right", 0, 25), (pane10, "left", 0, 25), (pane10, "right", 0, 50), 
                    (pane11, "left", 0, 50), (pane11, "right", 0, 75), (pane12, "left", 0, 75), (pane12, "right", 0,100), (pane1, 'top', 0, 0), (pane1, 'bottom', 0, 33), (pane2, 'top', 0, 0),
                    (pane2, 'bottom', 0, 33), (pane3, 'top', 0, 0), (pane3, 'bottom', 0, 33), (pane4, 'top', 0, 0), (pane4, 'bottom', 0, 33), (pane5, 'top', 0, 33), (pane5, 'bottom', 0, 66),
                    (pane6, 'top', 0, 33), (pane6, 'bottom', 0, 66), (pane7, 'top', 0, 33), (pane7, 'bottom', 0, 66), (pane8, 'top', 0, 33), (pane8, 'bottom', 0, 66), (pane9, 'top', 0, 66), 
                    (pane9, 'bottom', 0, 99), (pane10, 'top', 0, 66), (pane10, 'bottom', 0, 99), (pane11, 'top', 0, 66), (pane11, 'bottom', 0, 99), (pane12, 'top', 0, 66), (pane12, 'bottom', 0, 99)])
        
        self.AddTwelve_SH()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_6_Model_Win_menu_SH')
        mc.window('Cam_6_Model_Win_menu_SH', e=True, wh=[960, 722])

    #圣地古塔
    def Cam_2_Model_Win_menu_SDGT(self):
        self.closeAllCamMenu()
        self.DeletePlane()
        self.SetRightSize()

        #创建窗口
        if mc.window('Cam_2_Model_Win_menu_SDGT', ex=True):
            mc.deleteUI('Cam_2_Model_Win_menu_SDGT')
        mc.window('Cam_2_Model_Win_menu_SDGT', t='Cam_2_Model_Win_menu_SDGT', wh=[500, 500], sizeable=True, rtf=True)
        form=mc.formLayout(numberOfDivisions=100)
        pane1=mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        pane2=mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
        mc.formLayout(form,e=True,
                    attachForm=[(pane1, 'left', 1), (pane1, 'top', 1), (pane1, 'right', 1), (pane2, 'left', 1),(pane2, 'right', 1), (pane2, 'bottom', 1)],
                    attachPosition=[(pane1, 'left', 0, 0), (pane1, 'right', 0, 100), (pane1, 'top', 0, 0), (pane1, 'bottom', 0, 50), 
                    (pane2, 'left', 0, 0), (pane2, 'right', 0, 100),(pane2, 'top', 0, 50), (pane2, 'bottom', 0, 100)])

        self.AddTwoGroup()
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
        mc.showWindow('Cam_2_Model_Win_menu_SDGT')
        mc.window('Cam_2_Model_Win_menu_SDGT', e = True, wh= [960, 1428])       

    #实现缩放窗口的功能              
    def Cam_Window_Scale(self):
        self.camWH.clear()
        allCamWin=[]
        allWindow=list(set(mc.lsUI(wnd=True))-set(['scriptEditorPanel1Window','MayaWindow']))
        for win in allWindow:
            if 'Model_Win' in win:
                allCamWin.append(win)
                win_H=mc.window(win, q=True, h=True)
                win_W=mc.window(win ,q=True, w=True)
                self.camWH.update({win:[win_W, win_H]})
        
        if not allCamWin:
            mc.confirmDialog(t=u'提示', message=u'没有找到相机窗口！')
            if mc.window('Reset_Cam_Window_Scale1', ex=True):
                mc.deleteUI('Reset_Cam_Window_Scale1')
        else:
            if mc.window('Reset_Cam_Window_Scale1', ex=True):
                mc.deleteUI('Reset_Cam_Window_Scale1')
            mc.window('Reset_Cam_Window_Scale1', t='Reset_Cam_Window_Scale', wh=[100, 60], sizeable=True, rtf=True)
            mc.frameLayout(bs='etchedIn', label=u'重置相机窗口', h=40)
            mc.columnLayout()
            mc.floatSliderButtonGrp('Scale', pre=True, v=1, label='Reset Scale',field=True, buttonLabel='RESET', min=0.3, max=3, symbolButtonDisplay=False, 
                                    cl4=('left', 'left', 'left', 'left'), cw4=(60, 60, 180, 10),changeCommand=lambda*args: self.sliderReset(1), bc=lambda*args: self.sliderReset(0))
            mc.showWindow('Reset_Cam_Window_Scale1')
    
    #滑动条的设置窗口与重置窗口  
    def sliderReset(self, model):
        #print self.camWH
        allWindow=list(set(mc.lsUI(wnd=True))-set(['scriptEditorPanel1Window','MayaWindow']))
        #判断字典中是否保存的显示相机窗口，若没有保存在字典中
        for win in allWindow:
            if 'Model_Win' in win:
                if win not in self.camWH.keys():
                    win_H=mc.window(win, q=True, h=True)
                    win_W=mc.window(win, q=True, w=True)
                    self.camWH.update({win:[win_W, win_H]})
        field=mc.floatSliderButtonGrp('Scale', q=True, v=True)
        for key in self.camWH.keys():
            if mc.window(key, ex=True):
                #根据滑调设置窗口大小
                if model==1:
                    newWin_W=field*self.camWH[key][0]
                    newWin_H=field*self.camWH[key][1]
                    mc.window(key, e=True, wh=[newWin_W, newWin_H])
                #根据按钮重置窗口
                elif model==0:
                    mc.window(key,e=True,wh=[self.camWH[key][0], self.camWH[key][1]])
                    #print self.camWH
                    mc.floatSliderButtonGrp('Scale',e=True,v=1.0)
            else:
                del self.camWH[key]

    def toggleModelOpen(self):
        mm.eval('toggleModelEditorBarsInAllPanels 0;')
        mm.eval('toggleMenuBarsInAllPanels 1;')

    def toggleModelClose(self):
        mm.eval('toggleModelEditorBarsInAllPanels 1;')
        mm.eval('toggleMenuBarsInAllPanels 0;')
#b=multipleCameraPanels()
#b.Cam_6_Model_Win_menu_CDFKBS()

