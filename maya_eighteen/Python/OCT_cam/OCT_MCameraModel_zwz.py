#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import re


def closeAllCamMenu():                  
    '''if mc.windowPref('Cam_1_Model_Win', ex=True):
        mc.windowPref('Cam_1_Model_Win', remove=True)
    if mc.window('Cam_1_Model_Win', ex=True):
        mc.deleteUI('Cam_1_Model_Win', window=True)

    if mc.windowPref('Cam_3_H_Model_Win', ex=True):
        mc.windowPref('Cam_3_H_Model_Win', remove=True)
    if mc.window('Cam_3_H_Model_Win', ex=True):
        mc.deleteUI('Cam_3_H_Model_Win', window=True)

    if mc.windowPref('Cam_3_H_S_Model_Win', ex=True):
        mc.windowPref('Cam_3_H_S_Model_Win', remove=True)
    if mc.window('Cam_3_H_S_Model_Win', ex=True):
        mc.deleteUI('Cam_3_H_S_Model_Win', window=True)

    if mc.window('Cam_3_V_Model_Win', ex=True):
        mc.deleteUI('Cam_3_V_Model_Win', window=True)
    if mc.window('Cam_3_V_Model_Win', ex=True):
        mc.deleteUI('Cam_3_V_Model_Win', window=True)

    if mc.windowPref('Cam_5_Model_Win', ex=True):
        mc.windowPref('Cam_5_Model_Win', remove=True)
    if mc.window('Cam_5_Model_Win', ex=True):
        mc.deleteUI('Cam_5_Model_Win', window=True)

    if mc.windowPref('Cam_9_Model_Win', ex=True):
        mc.windowPref('Cam_9_Model_Win', remove=True)
    if mc.window('Cam_9_Model_Win', ex=True):
        mc.deleteUI('Cam_9_Model_Win', window=True)

    if mc.window('Cam_10_Model_Win', ex=True):
        mc.deleteUI('Cam_10_Model_Win', window=True)
    if mc.window('Cam_10_Model_Win', ex=True):
        mc.deleteUI('Cam_10_Model_Win', window=True)

    if mc.window('Cam_18_Model_Win', ex=True):
        mc.deleteUI('Cam_18_Model_Win', window=True)
    if mc.window('Cam_18_Model_Win', ex=True):
        mc.deleteUI('Cam_18_Model_Win', window=True)

    if mc.window('Cam_3_H_S_for_FKBS_Model_Win1', ex=True):
        mc.deleteUI('Cam_3_H_S_for_FKBS_Model_Win1', window=True)
    if mc.window('Cam_3_H_S_for_FKBS_Model_Win1', ex=True):
        mc.deleteUI('Cam_3_H_S_for_FKBS_Model_Win1', window=True)

    if mc.window('Cam_3_H_S_for_FKBS_Model_Win2', ex=True):
        mc.deleteUI('Cam_3_H_S_for_FKBS_Model_Win2', window=True)
    if mc.window('Cam_3_H_S_for_FKBS_Model_Win2', ex=True):
        mc.deleteUI('Cam_3_H_S_for_FKBS_Model_Win2', window=True)

    if mc.windowPref('Cam_14_Model_Win',ex=True):
        mc.windowPref('Cam_14_Model_Win',remove=True)
    if mc.window('Cam_14_Model_Win',ex=True):
        mc.deleteUI('Cam_14_Model_Win')'''
    allWindow=mc.lsUI(wnd=True)
    for wind in allWindow:
        if 'Model_Win' in wind:
            mc.deleteUI(wind)




def DisplayPoly_zwz(myplane):
    mayaversions = mc.about(v=True)
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
    rendererName = mc.modelEditor(myactivePlane, q=True, rendererName=True)
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


def DeletePlane_zwz():   #删除Plane
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


def SetRightSize_zwz():
    # a = ['', 'F', 'B']
    # b = ['UL_panel', 'U_panel', 'UR_panel', 'L_panel', 'M_panel', 'R_panel', 'DL_panel', 'D_panel', 'DR_panel']
    # for i in a:
    #         for j in b:
    #             if i == 'F' or i == 'B':
    #                 planeName = '%s_%s' % (i, j)
    #             else:
    #                 planeName = j
    #             if mc.modelPanel(planeName, ex=True):
    #                 mycam = mc.modelPanel(planeName, q=True, cam=True)
    #                 mycamS = mc.listRelatives(mycam, c=True, s=True, ni=True)
    #                 for tmp in mycamS:
    #                     if mc.nodeType(tmp) == 'camera':
    #                         mc.camera(tmp, e=True, dr=False, ovr=1)
    allMycamera = mc.listCameras(p=True)
    for myCam in allMycamera:
        mc.camera(myCam, e=True, dr=False, ovr=1,displayFilmGate=False)  #设置相机的分辨率。


def findCamera(Name):
    numName = len(Name)
    allMycamera = mc.listCameras(p=True)
    for myCamera in allMycamera:
        if myCamera[-numName:] == Name:
            return myCamera
    return None


def AddFistGroup():
    tmpCam = findCamera('testLU')
    if not tmpCam:
        tmpCam = findCamera('testL')
    if not tmpCam:
        tmpCam = findCamera('Cam_L')
    if not tmpCam:
        tmpCam = findCamera('RenderCam_U')
    if not tmpCam:
        tmpCam = findCamera('RenderCam_L')
    if not tmpCam:
        tmpCam = findCamera('Ani_Cam_L1')
    if not tmpCam:
        tmpCam = findCamera('CamL_L_L')
    mc.modelPanel('UL_panel', camera=tmpCam, mbv=False, l='UL', p='pane1')
    DisplayPoly_zwz('UL_panel')
    tmpCam = findCamera('testU')
    if not tmpCam:
        tmpCam = findCamera('Cam_M')
    if not tmpCam:
        tmpCam = findCamera('testM')
    if not tmpCam:
        tmpCam = findCamera('RenderCam_M')
    if not tmpCam:
        tmpCam = findCamera('Ani_Cam_L2')
    if not tmpCam:
        tmpCam = findCamera('CamL_M_L')
    mc.modelPanel('U_panel', camera=tmpCam, mbv=False, l='U', p='pane2')
    DisplayPoly_zwz('U_panel')
    tmpCam = findCamera('testRU')
    if not tmpCam:
        tmpCam = findCamera('testR')
    if not tmpCam:
        tmpCam = findCamera('Cam_R')
    if not tmpCam:
        tmpCam = findCamera('RenderCam_D')
    if not tmpCam:
        tmpCam = findCamera('RenderCam_R')
    if not tmpCam:
        tmpCam = findCamera('Ani_Cam_L3')
    if not tmpCam:
        tmpCam = findCamera('CamL_R_L')
    mc.modelPanel('UR_panel', camera=tmpCam, mbv=False, l='UR', p='pane3')
    DisplayPoly_zwz('UR_panel')


def AddSecondGroup():
    tmpCam = findCamera('testL')
    if not tmpCam:
        tmpCam = findCamera('CamR_L_L')
    mc.modelPanel('L_panel', camera=tmpCam, mbv=False, l='L', p='pane4')
    DisplayPoly_zwz('L_panel')

    tmpCam = findCamera('testM')
    if not tmpCam:
        tmpCam = findCamera('CamR_M_L')
    mc.modelPanel('M_panel', camera=tmpCam, mbv=False, l='M', p='pane5')
    DisplayPoly_zwz('M_panel')
 
    tmpCam = findCamera('testR')
    if not tmpCam:
        tmpCam = findCamera('CamR_R_L')
    mc.modelPanel('R_panel', camera=tmpCam, mbv=False, l='R', p='pane6')
    DisplayPoly_zwz('R_panel')


def AddThirdGroup():
    tmpCam = findCamera('testLD')
    mc.modelPanel('DL_panel', camera=tmpCam, mbv=False, l='DL', p='pane7')
    DisplayPoly_zwz('DL_panel')
    tmpCam = findCamera('testD')
    mc.modelPanel('D_panel', camera=tmpCam, mbv=False, l='D', p='pane8')
    DisplayPoly_zwz('D_panel')
    tmpCam = findCamera('testRD')
    mc.modelPanel('DR_panel', camera=tmpCam, mbv=False, l='DR', p='pane9')
    DisplayPoly_zwz('DR_panel')

def AddTwelveGroup():
    tmpCam = findCamera('Cam_4_L_L')
    mc.modelPanel('B_L_panel', camera=tmpCam, mbv=False, l='B_L', p='pane1')
    DisplayPoly_zwz('B_L_panel')
    tmpCam = findCamera('Cam_4_L_M')
    mc.modelPanel('B_M_panel', camera=tmpCam, mbv=False, l='B_M', p='pane2')
    DisplayPoly_zwz('B_M_panel')
    tmpCam = findCamera('Cam_4_L_R')
    mc.modelPanel('B_R_panel', camera=tmpCam, mbv=False, l='B_M', p='pane3')
    DisplayPoly_zwz('B_R_panel')
    tmpCam = findCamera('Cam_3_L_L')
    mc.modelPanel('F_L_panel', camera=tmpCam, mbv=False, l='F_L', p='pane4')
    DisplayPoly_zwz('F_L_panel')
    tmpCam = findCamera('Cam_3_L_M')
    mc.modelPanel('F_M_panel', camera=tmpCam, mbv=False, l='F_M', p='pane5')
    DisplayPoly_zwz('F_M_panel')
    tmpCam = findCamera('Cam_3_L_R')
    mc.modelPanel('F_R_panel', camera=tmpCam, mbv=False, l='F_R', p='pane6')
    DisplayPoly_zwz('F_R_panel')
    tmpCam = findCamera('Cam_2_L_L')
    mc.modelPanel('F_DL_panel', camera=tmpCam, mbv=False, l='F_DL', p='pane7')
    DisplayPoly_zwz('F_DL_panel')
    tmpCam = findCamera('Cam_2_L_M')
    mc.modelPanel('F_D_panel', camera=tmpCam, mbv=False, l='F_D', p='pane8')
    DisplayPoly_zwz('F_D_panel')
    tmpCam = findCamera('Cam_2_L_R')
    mc.modelPanel('F_DR_panel', camera=tmpCam, mbv=False, l='F_DR', p='pane9')
    DisplayPoly_zwz('F_DR_panel')

    tmpCam = findCamera('Cam_1_L_L')
    mc.modelPanel('B_DL_panel', camera=tmpCam, mbv=False, l='B_DL', p='pane11')
    DisplayPoly_zwz('B_DL_panel')
    tmpCam = findCamera('Cam_1_L_M')
    mc.modelPanel('B_D_panel', camera=tmpCam, mbv=False, l='B_D', p='pane12')
    DisplayPoly_zwz('B_D_panel')
    tmpCam = findCamera('Cam_1_L_R')
    mc.modelPanel('B_DR_panel', camera=tmpCam, mbv=False, l='B_DR', p='pane13')
    DisplayPoly_zwz('B_DR_panel')
 

def AddEighteenGroup():
    tmpCam = findCamera('Cam_F_UL')
    mc.modelPanel('F_UL_panel', camera=tmpCam, mbv=False, l='F_UL', p='pane1')
    DisplayPoly_zwz('F_UL_panel')
    tmpCam = findCamera('Cam_F_U')
    mc.modelPanel('F_U_panel', camera=tmpCam, mbv=False, l='F_U', p='pane2')
    DisplayPoly_zwz('F_U_panel')
    tmpCam = findCamera('Cam_F_UR')
    mc.modelPanel('F_UR_panel', camera=tmpCam, mbv=False, l='F_UR', p='pane3')
    DisplayPoly_zwz('F_UR_panel')
    tmpCam = findCamera('Cam_F_L')
    mc.modelPanel('F_L_panel', camera=tmpCam, mbv=False, l='F_L', p='pane4')
    DisplayPoly_zwz('F_L_panel')
    tmpCam = findCamera('Cam_F_M')
    mc.modelPanel('F_M_panel', camera=tmpCam, mbv=False, l='F_M', p='pane5')
    DisplayPoly_zwz('F_M_panel')
    tmpCam = findCamera('Cam_F_R')
    mc.modelPanel('F_R_panel', camera=tmpCam, mbv=False, l='F_R', p='pane6')
    DisplayPoly_zwz('F_R_panel')
    tmpCam = findCamera('Cam_F_DL')
    mc.modelPanel('F_DL_panel', camera=tmpCam, mbv=False, l='F_DL', p='pane7')
    DisplayPoly_zwz('F_DL_panel')
    tmpCam = findCamera('Cam_F_D')
    mc.modelPanel('F_D_panel', camera=tmpCam, mbv=False, l='F_D', p='pane8')
    DisplayPoly_zwz('F_D_panel')
    tmpCam = findCamera('Cam_F_DR')
    mc.modelPanel('F_DR_panel', camera=tmpCam, mbv=False, l='F_DR', p='pane9')
    DisplayPoly_zwz('F_DR_panel')

    tmpCam = findCamera('Cam_B_UL')
    mc.modelPanel('B_UL_panel', camera=tmpCam, mbv=False, l='B_UL', p='pane11')
    DisplayPoly_zwz('B_UL_panel')
    tmpCam = findCamera('Cam_B_U')
    mc.modelPanel('B_U_panel', camera=tmpCam, mbv=False, l='B_U', p='pane12')
    DisplayPoly_zwz('B_U_panel')
    tmpCam = findCamera('Cam_B_UR')
    mc.modelPanel('B_UR_panel', camera=tmpCam, mbv=False, l='B_UR', p='pane13')
    DisplayPoly_zwz('B_UR_panel')
    tmpCam = findCamera('Cam_B_L')
    mc.modelPanel('B_L_panel', camera=tmpCam, mbv=False, l='B_L', p='pane14')
    DisplayPoly_zwz('B_L_panel')
    tmpCam = findCamera('Cam_B_M')
    mc.modelPanel('B_M_panel', camera=tmpCam, mbv=False, l='B_M', p='pane15')
    DisplayPoly_zwz('B_M_panel')
    tmpCam = findCamera('Cam_B_R')
    mc.modelPanel('B_R_panel', camera=tmpCam, mbv=False, l='B_R', p='pane16')
    DisplayPoly_zwz('B_R_panel')
    tmpCam = findCamera('Cam_B_DL')
    mc.modelPanel('B_DL_panel', camera=tmpCam, mbv=False, l='B_DL', p='pane17')
    DisplayPoly_zwz('B_DL_panel')
    tmpCam = findCamera('Cam_B_D')
    mc.modelPanel('B_D_panel', camera=tmpCam, mbv=False, l='B_D', p='pane18')
    DisplayPoly_zwz('B_D_panel')
    tmpCam = findCamera('Cam_B_DR')
    mc.modelPanel('B_DR_panel', camera=tmpCam, mbv=False, l='B_DR', p='pane19')
    DisplayPoly_zwz('B_DR_panel')

def AddSevenGroup_1():
    tmpCam=findCamera('test_CamL_A')
    mc.modelPanel('UL_panel',camera=tmpCam,mbv=False,l='UL',p='pane1')
    DisplayPoly_zwz('UL_panel')
    tmpCam=findCamera('test_CamL_B')
    mc.modelPanel('U_panel',camera=tmpCam,mbv=False,l='U',p='pane2')
    DisplayPoly_zwz('U_panel')
    tmpCam=findCamera('test_CamL_C')
    mc.modelPanel('UR_panel',camera=tmpCam,mbv=False,l='U',p='pane3')
    DisplayPoly_zwz('UR_panel')
    
def AddSevenGroup_2():
    tmpCam=findCamera('test_CamL_D')
    mc.modelPanel('L_panel',camera=tmpCam,mbv=False,l='U',p='pane4')
    DisplayPoly_zwz('L_panel')

def AddSevenGroup_3():
    tmpCam=findCamera('test_CamL_E')
    mc.modelPanel('M_panel',camera=tmpCam,mbv=False,l='M',p='pane5')
    DisplayPoly_zwz('M_panel')
    tmpCam=findCamera('test_CamL_F')
    mc.modelPanel('R_panel',camera=tmpCam,mbv=False,l='M',p='pane6')
    DisplayPoly_zwz('R_panel')
    tmpCam=findCamera('test_CamL_G')
    mc.modelPanel('DL_panel',camera=tmpCam,mbv=False,l='DL',p='pane7')
    DisplayPoly_zwz('DL_panel')


def AddSixGroup():
    tmpCam=findCamera('CamL_2_A')
    mc.modelPanel('UL_panel',camera=tmpCam,mbv=False,l='UL',p='pane1')
    DisplayPoly_zwz('UL_panel')
    tmpCam=findCamera('CamL_2_B')
    mc.modelPanel('U_panel',camera=tmpCam,mbv=False,l='U',p='pane2')
    DisplayPoly_zwz('U_panel')
    tmpCam=findCamera('CamL_2_C')
    mc.modelPanel('UR_panel',camera=tmpCam,mbv=False,l='U',p='pane3')
    DisplayPoly_zwz('UR_panel')
    tmpCam=findCamera('CamL_1_A')
    mc.modelPanel('L_panel',camera=tmpCam,mbv=False,l='U',p='pane4')
    DisplayPoly_zwz('L_panel')
    tmpCam=findCamera('CamL_1_B')
    mc.modelPanel('M_panel',camera=tmpCam,mbv=False,l='M',p='pane5')
    DisplayPoly_zwz('M_panel')
    tmpCam=findCamera('CamL_1_C')
    mc.modelPanel('R_panel',camera=tmpCam,mbv=False,l='M',p='pane6')
    DisplayPoly_zwz('R_panel')
 
def AddThirdGroup_BJCP():
    tmpCam=findCamera('CamL_A')
    mc.modelPanel('UL_panel',camera=tmpCam,mbv=False,l='UL',p='pane1')
    DisplayPoly_zwz('UL_panel')
    tmpCam=findCamera('CamL_B')
    mc.modelPanel('U_panel',camera=tmpCam,mbv=False,l='U',p='pane2')
    DisplayPoly_zwz('U_panel')
    tmpCam=findCamera('CamL_C')
    mc.modelPanel('UR_panel',camera=tmpCam,mbv=False,l='U',p='pane3')
    DisplayPoly_zwz('UR_panel')    



def Cam_1_Model_Win_menu():
    closeAllCamMenu()   #关闭所有的窗口
    DeletePlane_zwz()   #删除plane
    SetRightSize_zwz()  #设置相机的分辨率
    #获取当前激活窗口的摄像机
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
    #激活的摄像机
    myCam = mc.modelEditor(activePlane, q=True, cam=True)

    window = mc.window('Cam_1_Model_Win', t='OCT_1_CamModel', wh=[500, 500], sizeable=True, rtf=True)
    form = mc.formLayout()
    one = mc.paneLayout('pane1', w=502, h=502, configuration='single', p=form, aft=0, st=1)
    mc.modelPanel('U_panel', camera=myCam, mbv=False, l='UL', p='pane1')
    mc.formLayout(form, edit=True,
                      attachForm=[(one, 'left', 1), (one, 'right', 1), (one, 'top', 1), (one, 'bottom', 1)])
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow(window)
    mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')


def Cam_3_H_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_3_H_Model_Win', t='OCT_3_CamModel', wh=[900, 300], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane3, 'right', 5), (pane1, 'top', 5), (pane2, 'top', 5), (pane3, 'top', 5),
                  (pane1, 'bottom', 5), (pane2, 'bottom', 5), (pane3, 'bottom', 5)],
                  attachPosition=[(pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66)])

    AddFistGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_3_H_Model_Win')
    mc.window('Cam_3_H_Model_Win', e=True, wh=[900, 300])
    mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')

def Cam_4_H_T_Model_Win_menu():
    if mc.windowPref('Cam_4_H_T_Model_Win', ex=True):
        mc.windowPref('Cam_4_H_T_Model_Win', remove=True)
    if mc.window('Cam_4_H_T_Model_Win', ex=True):
        mc.deleteUI('Cam_4_H_T_Model_Win', window=True)
    b = ['UL_panel', 'U_panel', 'UR_panel', 'L_panel']
    for j in b:
        if mc.modelPanel(j, ex=True):
            mc.deleteUI(j, panel=True)


    mc.window('Cam_4_H_T_Model_Win', t='OCT_3_CamModel', wh=[722, 547], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 0), (pane4, 'right', 0), (pane1, 'top', 0), (pane2, 'top', 0), (pane3, 'top', 0), (pane4, 'top', 0),
                  (pane1, 'bottom', 0), (pane2, 'bottom', 0), (pane3, 'bottom', 0), (pane4, 'bottom', 0)],
                  attachPosition=[(pane1, 'right', 0, 25), (pane2, 'left', 0, 25), (pane2, 'right', 0, 50), (pane3, 'left', 0, 50), (pane3, 'right', 0, 75), (pane4, 'left', 0, 75)])

    AddFistGroup()
    
    tmpCam = findCamera('testL')
    if not tmpCam:
        tmpCam = findCamera('Ani_Cam_L4')
    mc.modelPanel('L_panel', camera=tmpCam, mbv=False, l='L', p='pane4')
    DisplayPoly_zwz('L_panel')

    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_4_H_T_Model_Win')
    mc.window('Cam_4_H_T_Model_Win', e=True, wh=[1155, 875])
    mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')

def Cam_3_H_S_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_3_H_Model_Win', t='OCT_3_CamModel', wh=[900, 300], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane3, 'right', 5), (pane1, 'top', 5), (pane2, 'top', 5), (pane3, 'top', 5),
                  (pane1, 'bottom', 5), (pane2, 'bottom', 5), (pane3, 'bottom', 5)],
                  attachPosition=[(pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66)])

    AddFistGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_3_H_Model_Win')
    mc.window('Cam_3_H_Model_Win', e=True, wh=[900, 300])
    mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')

def Cam_3_H_S_for_FKBS_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()
    #第一个窗口
    mc.window('Cam_3_H_S_for_FKBS_Model_Win1', t='Cam_3_H_S_for_FKBS_Left', wh=[1284, 645], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=30, h=20, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=48, h=30, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=30, h=20, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 0), (pane3, 'right', 0), (pane1, 'top', 0), (pane2, 'top', 0), (pane3, 'top', 0),
                  (pane1, 'bottom', 0), (pane2, 'bottom', 0), (pane3, 'bottom', 0)],
                  attachPosition=[(pane1, 'right', 0, 30.1), (pane2, 'left', 0, 30.1), (pane2, 'right', 0, 69.17), (pane3, 'left', 0, 69.17)])
    AddFistGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_3_H_S_for_FKBS_Model_Win1')
    mc.window('Cam_3_H_S_for_FKBS_Model_Win1', e=True, wh=[1284, 645])
    #第二个窗口
    mc.window('Cam_3_H_S_for_FKBS_Model_Win2', t='Cam_3_H_S_for_FKBS_Right', wh=[1284, 645], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane4', w=30, h=20, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane5', w=48, h=30, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane6', w=30, h=20, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 0), (pane3, 'right', 0), (pane1, 'top', 0), (pane2, 'top', 0), (pane3, 'top', 0),
                  (pane1, 'bottom', 0), (pane2, 'bottom', 0), (pane3, 'bottom', 0)],
                  attachPosition=[(pane1, 'right', 0, 30.1), (pane2, 'left', 0, 30.1), (pane2, 'right', 0, 69.17), (pane3, 'left', 0, 69.17)])
    AddSecondGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_3_H_S_for_FKBS_Model_Win2')
    mc.window('Cam_3_H_S_for_FKBS_Model_Win2', e=True, wh=[1284, 645])
    mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')


def Cam_3_V_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_3_V_Model_Win', t='OCT_3_CamModel', wh=[535, 909], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5),(pane2, 'left', 5),(pane3, 'left', 5), (pane1, 'right', 5),(pane2, 'right', 5), (pane3, 'right', 5), (pane1, 'top', 5), (pane3, 'bottom', 5)],
                  attachPosition=[(pane1, 'bottom', 0, 33), (pane2, 'top', 0, 33), (pane2, 'bottom', 0, 66), (pane3, 'top', 0, 66)])

    AddFistGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_3_V_Model_Win')
    mc.window('Cam_3_V_Model_Win', e=True,  wh=[536, 909])
    mc.evalDeferred('OCT_cam.OCT_MCameraModel_zwz.SetRightSize_zwz()')


def Cam_5_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_5_Model_Win', t='OCT_9_CamModel', wh=[900, 900], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane8 = mc.paneLayout('pane8', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane9 = mc.paneLayout('pane9', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane4, 'left', 5), (pane7, 'left', 5), (pane3, 'right', 5), (pane6, 'right', 5),
                  (pane9, 'right', 5), (pane7, 'bottom', 5), (pane8, 'bottom', 5), (pane9, 'bottom', 5), (pane1, 'top', 5), (pane2, 'top', 5),
                  (pane3, 'top', 5)],
                  attachPosition=[(pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66),
                  (pane4, 'right', 0, 33), (pane5, 'left', 0, 33), (pane5, 'right', 0, 66), (pane6, 'left', 0, 66),
                  (pane7, 'right', 0, 33), (pane8, 'left', 0, 33), (pane8, 'right', 0, 66), (pane9, 'left', 0, 66),
                  (pane1, 'bottom', 0, 33), (pane4, 'top', 0, 33), (pane4, 'bottom', 0, 66), (pane7, 'top', 0, 66),
                  (pane2, 'bottom', 0, 33), (pane5, 'top', 0, 33), (pane5, 'bottom', 0, 66), (pane8, 'top', 0, 66),
                  (pane3, 'bottom', 0, 33), (pane6, 'top', 0, 33), (pane6, 'bottom', 0, 66), (pane9, 'top', 0, 66)])

    AddFistGroup()
    AddSecondGroup()
    AddThirdGroup()
    if mc.modelPanel('UL_panel', ex=True):
        mc.deleteUI('UL_panel', panel=True)
    if mc.modelPanel('UR_panel', ex=True):
        mc.deleteUI('UR_panel', panel=True)
    if mc.modelPanel('DL_panel', ex=True):
        mc.deleteUI('DL_panel', panel=True)
    if mc.modelPanel('DR_panel', ex=True):
        mc.deleteUI('DR_panel', panel=True)
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_5_Model_Win')
    mc.window('Cam_5_Model_Win', e=True,  wh=[900, 900])


def Cam_5_180degrees_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_5_180degrees_Model_Win_menu', t='OCT_9_CamModel', wh=[900, 900], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=75, h=75, configuration='single', p=form, aft=0, st=1, vis=0)
    pane2 = mc.paneLayout('pane2', w=150, h=75, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=75, h=75, configuration='single', p=form, aft=0, st=1, vis=0)
    pane4 = mc.paneLayout('pane4', w=75, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=75, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=75, h=75, configuration='single', p=form, aft=0, st=1, vis=0)
    pane8 = mc.paneLayout('pane8', w=150, h=75, configuration='single', p=form, aft=0, st=1)
    pane9 = mc.paneLayout('pane9', w=75, h=75, configuration='single', p=form, aft=0, st=1, vis=0)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane4, 'left', 5), (pane7, 'left', 5), (pane3, 'right', 5), (pane6, 'right', 5),
                  (pane9, 'right', 5), (pane7, 'bottom', 5), (pane8, 'bottom', 5), (pane9, 'bottom', 5), (pane1, 'top', 5), (pane2, 'top', 5),
                  (pane3, 'top', 5)],
                  attachPosition=[(pane1, 'right', 0, 25), (pane2, 'left', 0, 25), (pane2, 'right', 0, 75), (pane3, 'left', 0, 75),
                  (pane4, 'right', 0, 25), (pane5, 'left', 0, 25), (pane5, 'right', 0, 75), (pane6, 'left', 0, 75),
                  (pane7, 'right', 0, 25), (pane8, 'left', 0, 25), (pane8, 'right', 0, 75), (pane9, 'left', 0, 75),
                  (pane1, 'bottom', 0, 25), (pane4, 'top', 0, 25), (pane4, 'bottom', 0, 75), (pane7, 'top', 0, 75),
                  (pane2, 'bottom', 0, 25), (pane5, 'top', 0, 25), (pane5, 'bottom', 0, 75), (pane8, 'top', 0, 75),
                  (pane3, 'bottom', 0, 25), (pane6, 'top', 0, 25), (pane6, 'bottom', 0, 75), (pane9, 'top', 0, 75)])

    AddFistGroup()
    AddSecondGroup()
    AddThirdGroup()
    if mc.modelPanel('UL_panel', ex=True):
        mc.deleteUI('UL_panel', panel=True)
    if mc.modelPanel('UR_panel', ex=True):
        mc.deleteUI('UR_panel', panel=True)
    if mc.modelPanel('DL_panel', ex=True):
        mc.deleteUI('DL_panel', panel=True)
    if mc.modelPanel('DR_panel', ex=True):
        mc.deleteUI('DR_panel', panel=True)
    mm.eval('toggleModelEditorBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_5_180degrees_Model_Win_menu')
    mc.window('Cam_5_180degrees_Model_Win_menu', e=True,  wh=[900, 900])


def Cam_9_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_9_Model_Win', t='OCT_9_CamModel', wh=[900, 900], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane8 = mc.paneLayout('pane8', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane9 = mc.paneLayout('pane9', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane4, 'left', 5), (pane7, 'left', 5), (pane3, 'right', 5), (pane6, 'right', 5),
                  (pane9, 'right', 5), (pane7, 'bottom', 5), (pane8, 'bottom', 5), (pane9, 'bottom', 5), (pane1, 'top', 5), (pane2, 'top', 5),
                  (pane3, 'top', 5)],
                  attachPosition=[(pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66),
                  (pane4, 'right', 0, 33), (pane5, 'left', 0, 33), (pane5, 'right', 0, 66), (pane6, 'left', 0, 66),
                  (pane7, 'right', 0, 33), (pane8, 'left', 0, 33), (pane8, 'right', 0, 66), (pane9, 'left', 0, 66),
                  (pane1, 'bottom', 0, 33), (pane4, 'top', 0, 33), (pane4, 'bottom', 0, 66), (pane7, 'top', 0, 66),
                  (pane2, 'bottom', 0, 33), (pane5, 'top', 0, 33), (pane5, 'bottom', 0, 66), (pane8, 'top', 0, 66),
                  (pane3, 'bottom', 0, 33), (pane6, 'top', 0, 33), (pane6, 'bottom', 0, 66), (pane9, 'top', 0, 66)])

    AddFistGroup()
    AddSecondGroup()
    AddThirdGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_9_Model_Win')
    mc.window('Cam_9_Model_Win', e=True,  wh=[900, 900])


def Cam_10_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_10_Model_Win', t='OCT_10_CamModel', wh=[1400, 700], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane8 = mc.paneLayout('pane8', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane9 = mc.paneLayout('pane9', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane11 = mc.paneLayout('pane11', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane12 = mc.paneLayout('pane12', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane13 = mc.paneLayout('pane13', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane14 = mc.paneLayout('pane14', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane15 = mc.paneLayout('pane15', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane16 = mc.paneLayout('pane16', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane17 = mc.paneLayout('pane17', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    pane18 = mc.paneLayout('pane18', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane19 = mc.paneLayout('pane19', w=150, h=150, configuration='single', p=form, aft=0, st=1, vis=0)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane4, 'left', 5), (pane7, 'left', 5), (pane13, 'right', 5), (pane16, 'right', 5),
                  (pane19, 'right', 5), (pane7, 'bottom', 5), (pane8, 'bottom', 5), (pane9, 'bottom', 5),  (pane17, 'bottom', 5),
                  (pane18, 'bottom', 5), (pane19, 'bottom', 5), (pane1, 'top', 5), (pane2, 'top', 5), (pane3, 'top', 5),
                  (pane11, 'top', 5), (pane12, 'top', 5), (pane13, 'top', 5)],
                  attachPosition=[
                  (pane1, 'left', 0, 2), (pane1, 'right', 0, 18), (pane2, 'left', 0, 18), (pane2, 'right', 0, 34), (pane3, 'left', 0, 34), (pane3, 'right', 0, 50),
                  (pane11, 'left', 0, 50), (pane11, 'right', 0, 66), (pane12, 'left', 0, 66), (pane12, 'right', 0, 82), (pane13, 'left', 0, 82), (pane13, 'right', 0, 98),

                  (pane4, 'left', 0, 2), (pane4, 'right', 0, 18), (pane5, 'left', 0, 18), (pane5, 'right', 0, 34), (pane6, 'left', 0, 34), (pane6, 'right', 0, 50),
                  (pane14, 'left', 0, 50), (pane14, 'right', 0, 66), (pane15, 'left', 0, 66), (pane15, 'right', 0, 82), (pane16, 'left', 0, 82), (pane16, 'right', 0, 98),

                  (pane7, 'left', 0, 2), (pane7, 'right', 0, 18), (pane8, 'left', 0, 18), (pane8, 'right', 0, 34), (pane9, 'left', 0, 34), (pane9, 'right', 0, 50),
                  (pane17, 'left', 0, 50), (pane17, 'right', 0, 66), (pane18, 'left', 0, 66), (pane18, 'right', 0, 82), (pane19, 'left', 0, 82), (pane19, 'right', 0, 98),

                  (pane1, 'top', 0, 2), (pane1, 'bottom', 0, 34), (pane4, 'top', 0, 34), (pane4, 'bottom', 0, 66), (pane7, 'top', 0, 66), (pane7, 'bottom', 0, 98),
                  (pane2, 'top', 0, 2), (pane2, 'bottom', 0, 34), (pane5, 'top', 0, 34), (pane5, 'bottom', 0, 66), (pane8, 'top', 0, 66), (pane8, 'bottom', 0, 98),
                  (pane3, 'top', 0, 2), (pane3, 'bottom', 0, 34), (pane6, 'top', 0, 34), (pane6, 'bottom', 0, 66), (pane9, 'top', 0, 66), (pane9, 'bottom', 0, 98),
                  (pane11, 'top', 0, 2), (pane11, 'bottom', 0, 34), (pane14, 'top', 0, 34), (pane14, 'bottom', 0, 66), (pane17, 'top', 0, 66), (pane17, 'bottom', 0, 98),
                  (pane12, 'top', 0, 2), (pane12, 'bottom', 0, 34), (pane15, 'top', 0, 34), (pane15, 'bottom', 0, 66), (pane18, 'top', 0, 66), (pane18, 'bottom', 0, 98),
                  (pane13, 'top', 0, 2), (pane13, 'bottom', 0, 34), (pane16, 'top', 0, 34), (pane16, 'bottom', 0, 66), (pane19, 'top', 0, 66), (pane19, 'bottom', 0, 98)])

    AddEighteenGroup()
    if mc.modelPanel('F_UL_panel', ex=True):
        mc.deleteUI('F_UL_panel', panel=True)
    if mc.modelPanel('F_UR_panel', ex=True):
        mc.deleteUI('F_UR_panel', panel=True)
    if mc.modelPanel('F_DL_panel', ex=True):
        mc.deleteUI('F_DL_panel', panel=True)
    if mc.modelPanel('F_DR_panel', ex=True):
        mc.deleteUI('F_DR_panel', panel=True)
    if mc.modelPanel('B_UL_panel', ex=True):
        mc.deleteUI('B_UL_panel', panel=True)
    if mc.modelPanel('B_UR_panel', ex=True):
        mc.deleteUI('B_UR_panel', panel=True)
    if mc.modelPanel('B_DL_panel', ex=True):
        mc.deleteUI('B_DL_panel', panel=True)
    if mc.modelPanel('B_DR_panel', ex=True):
        mc.deleteUI('B_DR_panel', panel=True)
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_10_Model_Win')
    mc.window('Cam_10_Model_Win', e=True,  wh=[1400, 700])

def Cam_12_H_T_Model_Win_menu():
    if mc.window('Cam_12_V_T_Model_Win', ex=True):
        mc.deleteUI('Cam_12_V_T_Model_Win', window=True)
    if mc.window('Cam_12_V_T_Model_Win', ex=True):
        mc.deleteUI('Cam_12_V_T_Model_Win', window=True)
    a = ['F', 'B']
    b = ['L_panel', 'M_panel', 'R_panel', 'DL_panel', 'D_panel', 'DR_panel']
    for i in a:
            for j in b:
                if i == 'F' or i == 'B':
                    planeName = '%s_%s' % (i, j)
                else:
                    planeName = j
                if mc.modelPanel(planeName, ex=True):
                    mc.deleteUI(planeName, panel=True)

    SetRightSize_zwz()

    mc.window('Cam_12_V_T_Model_Win', t='OCT_12_V_T_CamModel', wh=[722, 1089], sizeable=True, rtf=True)

    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane8 = mc.paneLayout('pane8', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane9 = mc.paneLayout('pane9', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane11 = mc.paneLayout('pane11', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane12 = mc.paneLayout('pane12', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane13 = mc.paneLayout('pane13', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 1), (pane4, 'left', 1), (pane7, 'left', 1), (pane11, 'left', 1),
                  (pane3, 'right', 1), (pane6, 'right', 1), (pane9, 'right', 1), (pane13, 'right', 1),
                  (pane11, 'bottom', 1), (pane12, 'bottom', 1), (pane13, 'bottom', 1), 
                  (pane1, 'top', 1), (pane2, 'top', 1), (pane3, 'top', 1)],
                  attachPosition=[(pane1, 'right', 0, 33), (pane2, 'left', 0, 33), (pane2, 'right', 0, 66), (pane3, 'left', 0, 66),
                  (pane4, 'right', 0, 33), (pane5, 'left', 0, 33), (pane5, 'right', 0, 66), (pane6, 'left', 0, 66),
                  (pane7, 'right', 0, 33), (pane8, 'left', 0, 33), (pane8, 'right', 0, 66), (pane9, 'left', 0, 66),
                  (pane11, 'right', 0, 33), (pane12, 'left', 0, 33), (pane12, 'right', 0, 66), (pane13, 'left', 0, 66),
                  (pane1, 'bottom', 0, 25), (pane4, 'top', 0, 25), (pane4, 'bottom', 0, 50), (pane7, 'top', 0, 50), (pane7, 'bottom', 0, 75), (pane11, 'top', 0, 75),
                  (pane2, 'bottom', 0, 25), (pane5, 'top', 0, 25), (pane5, 'bottom', 0, 50), (pane8, 'top', 0, 50), (pane8, 'bottom', 0, 75), (pane12, 'top', 0, 75),
                  (pane3, 'bottom', 0, 25), (pane6, 'top', 0, 25), (pane6, 'bottom', 0, 50), (pane9, 'top', 0, 50), (pane9, 'bottom', 0, 75), (pane13, 'top', 0, 75)])
    AddTwelveGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_12_V_T_Model_Win')
    mc.window('Cam_12_V_T_Model_Win', e=True, wh=[596, 899])

def Cam_18_Model_Win_menu():
    closeAllCamMenu()
    DeletePlane_zwz()
    SetRightSize_zwz()

    mc.window('Cam_18_Model_Win', t='OCT_18_CamModel', wh=[1400, 700], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane8 = mc.paneLayout('pane8', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane9 = mc.paneLayout('pane9', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane11 = mc.paneLayout('pane11', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane12 = mc.paneLayout('pane12', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane13 = mc.paneLayout('pane13', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane14 = mc.paneLayout('pane14', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane15 = mc.paneLayout('pane15', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane16 = mc.paneLayout('pane16', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane17 = mc.paneLayout('pane17', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane18 = mc.paneLayout('pane18', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane19 = mc.paneLayout('pane19', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form, edit=True,
                  attachForm=[(pane1, 'left', 5), (pane4, 'left', 5), (pane7, 'left', 5), (pane13, 'right', 5), (pane16, 'right', 5),
                  (pane19, 'right', 5), (pane7, 'bottom', 5), (pane8, 'bottom', 5), (pane9, 'bottom', 5),  (pane17, 'bottom', 5),
                  (pane18, 'bottom', 5), (pane19, 'bottom', 5), (pane1, 'top', 5), (pane2, 'top', 5), (pane3, 'top', 5),
                  (pane11, 'top', 5), (pane12, 'top', 5), (pane13, 'top', 5)],
                  attachPosition=[
                  (pane1, 'left', 0, 2), (pane1, 'right', 0, 18), (pane2, 'left', 0, 18), (pane2, 'right', 0, 34), (pane3, 'left', 0, 34), (pane3, 'right', 0, 50),
                  (pane11, 'left', 0, 50), (pane11, 'right', 0, 66), (pane12, 'left', 0, 66), (pane12, 'right', 0, 82), (pane13, 'left', 0, 82), (pane13, 'right', 0, 98),

                  (pane4, 'left', 0, 2), (pane4, 'right', 0, 18), (pane5, 'left', 0, 18), (pane5, 'right', 0, 34), (pane6, 'left', 0, 34), (pane6, 'right', 0, 50),
                  (pane14, 'left', 0, 50), (pane14, 'right', 0, 66), (pane15, 'left', 0, 66), (pane15, 'right', 0, 82), (pane16, 'left', 0, 82), (pane16, 'right', 0, 98),

                  (pane7, 'left', 0, 2), (pane7, 'right', 0, 18), (pane8, 'left', 0, 18), (pane8, 'right', 0, 34), (pane9, 'left', 0, 34), (pane9, 'right', 0, 50),
                  (pane17, 'left', 0, 50), (pane17, 'right', 0, 66), (pane18, 'left', 0, 66), (pane18, 'right', 0, 82), (pane19, 'left', 0, 82), (pane19, 'right', 0, 98),

                  (pane1, 'top', 0, 2), (pane1, 'bottom', 0, 34), (pane4, 'top', 0, 34), (pane4, 'bottom', 0, 66), (pane7, 'top', 0, 66), (pane7, 'bottom', 0, 98),
                  (pane2, 'top', 0, 2), (pane2, 'bottom', 0, 34), (pane5, 'top', 0, 34), (pane5, 'bottom', 0, 66), (pane8, 'top', 0, 66), (pane8, 'bottom', 0, 98),
                  (pane3, 'top', 0, 2), (pane3, 'bottom', 0, 34), (pane6, 'top', 0, 34), (pane6, 'bottom', 0, 66), (pane9, 'top', 0, 66), (pane9, 'bottom', 0, 98),
                  (pane11, 'top', 0, 2), (pane11, 'bottom', 0, 34), (pane14, 'top', 0, 34), (pane14, 'bottom', 0, 66), (pane17, 'top', 0, 66), (pane17, 'bottom', 0, 98),
                  (pane12, 'top', 0, 2), (pane12, 'bottom', 0, 34), (pane15, 'top', 0, 34), (pane15, 'bottom', 0, 66), (pane18, 'top', 0, 66), (pane18, 'bottom', 0, 98),
                  (pane13, 'top', 0, 2), (pane13, 'bottom', 0, 34), (pane16, 'top', 0, 34), (pane16, 'bottom', 0, 66), (pane19, 'top', 0, 66), (pane19, 'bottom', 0, 98)])

    AddEighteenGroup()
    mm.eval('toggleMenuBarsInAllPanels 1;')
    mc.showWindow('Cam_18_Model_Win')
    mc.window('Cam_18_Model_Win', e=True,  wh=[1400, 700])


def Cam_6_Model_Win_menu():
    closeAllCamMenu()
    allWindow=mc.lsUI(wnd=True)
    #for wind in allWindow:
    #    if 'Model_Win' in wind:
    #        mc.deleteUI(wind)
    DeletePlane_zwz()
    SetRightSize_zwz()
    mc.window('Cam_6_Model_Win', t='OCT_6_CamModel', wh=[752, 502], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1,vis=0)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1,vis=0)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)

    
    mc.formLayout(form,edit=True,
        attachForm=[(pane1,'left',1),(pane1,'top',1),(pane2,'top',1),(pane3,'top',1),(pane3,'right',1),(pane4,'left',1),(pane4,'bottom',1),
        (pane5,'bottom',1),(pane6,'right',1),(pane6,'bottom',1)],

        attachPosition=[(pane1,'left',0,0),(pane1,'right',0,28),(pane2,'left',0,28),(pane2,'right',0,71),(pane3,'left',0,71),(pane3,'right',0,99),(pane4,'left',0,0),(pane4,'right',0,28),
        (pane5,'left',0,28),(pane5,'right',0,71),(pane6,'left',0,71),(pane6,'right',0,99),(pane1,'top',0,0),(pane1,'bottom',0,45),(pane2,'top',0,0),(pane2,'bottom',0,45),
        (pane3,'top',0,0),(pane3,'bottom',0,45),(pane4,'top',0,45),(pane4,'bottom',0,99),(pane5,'top',0,45),(pane5,'bottom',0,99),(pane6,'top',0,45),(pane6,'bottom',0,99)])
   
    AddSixGroup()
    mm.eval('toggleModelEditorBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_6_Model_Win')
    mc.window('Cam_6_Model_Win', e=True, wh=[752, 502])


def Cam_7_Model_Win_menu():
    closeAllCamMenu()
    #allWindow=mc.lsUI(wnd=True)
    #for wind in allWindow:
    #    if 'Model_Win' in wind:
    #        mc.deleteUI(wind)
    #第一个窗口
    DeletePlane_zwz()
    SetRightSize_zwz()
    mc.window('Cam_7_Model_Win1', t='OCT_7_CamModel_ABC', wh=[500, 500], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    
    mc.formLayout(form,edit=True,
        attachForm=[(pane1,'left',1),(pane1,'top',1),(pane2,'top',1),(pane3,'top',1),(pane3,'right',1),(pane1,'bottom',1),(pane2,'bottom',1),(pane3,'bottom',1)],
        attachPosition=[(pane1,'left',0,0),(pane1,'right',0,33),(pane2,'left',0,33),(pane2,'right',0,66),(pane3,'left',0,66),(pane3,'right',0,99)])

    AddSevenGroup_1()
    mm.eval('toggleModelEditorBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_7_Model_Win1')
    mc.window('Cam_7_Model_Win1', e=True, wh=[1000, 500])

    #第二个窗口
    mc.window('Cam_7_Model_Win2', t='OCT_7_CamModel_D', wh=[300, 300], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane4 = mc.paneLayout('pane4', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form,edit=True,attachForm=[(pane4,'left',1),(pane4,'top',1),(pane4,'right',1),(pane4,'bottom',1)],
        attachPosition=[(pane4,'left',0,0),(pane4,'right',0,100)])

    AddSevenGroup_2()
    mm.eval('toggleModelEditorBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_7_Model_Win2')
    mc.window('Cam_7_Model_Win2', e=True, wh=[300, 300])

    #第三个窗口
    mc.window('Cam_7_Model_Win3', t='OCT_7_CamMode1_EFG', wh=[500, 500], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane5 = mc.paneLayout('pane5', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane6 = mc.paneLayout('pane6', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane7 = mc.paneLayout('pane7', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    mc.formLayout(form,edit=True,
        attachForm=[(pane5,'left',1),(pane5,'top',1),(pane6,'top',1),(pane7,'top',1),(pane7,'right',1),(pane5,'bottom',1),(pane6,'bottom',1),(pane7,'bottom',1)],
        attachPosition=[(pane5,'left',0,0),(pane5,'right',0,33),(pane6,'left',0,33),(pane6,'right',0,66),(pane7,'left',0,66),(pane7,'right',0,99)])


    AddSevenGroup_3()
    mm.eval('toggleModelEditorBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_7_Model_Win3')
    mc.window('Cam_7_Model_Win3', e=True, wh=[1000, 500])
    #Cam_Window_Scale()
    
def Cam_3_Model_Win_menu_BJCP():
    closeAllCamMenu()
    #allWindow=mc.lsUI(wnd=True)
    #for wind in allWindow:
        #if 'Model_Win' in wind:
          #  mc.deleteUI(wind)
    DeletePlane_zwz()
    SetRightSize_zwz()
    mc.window('Cam_3_Model_Win_menu_BJCP', t='Cam_3_Model_Win_menu_BJCP', wh=[500, 500], sizeable=True, rtf=True)
    form = mc.formLayout(numberOfDivisions=100)
    pane1 = mc.paneLayout('pane1', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane2 = mc.paneLayout('pane2', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    pane3 = mc.paneLayout('pane3', w=150, h=150, configuration='single', p=form, aft=0, st=1)
    
    mc.formLayout(form,edit=True,
        attachForm=[(pane1,'left',1),(pane1,'top',1),(pane2,'top',1),(pane3,'top',1),(pane3,'right',1),(pane1,'bottom',1),(pane2,'bottom',1),(pane3,'bottom',1)],
        attachPosition=[(pane1,'left',0,0),(pane1,'right',0,33),(pane2,'left',0,33),(pane2,'right',0,66),(pane3,'left',0,66),(pane3,'right',0,99)])
    
    AddThirdGroup_BJCP()
    mm.eval('toggleModelEditorBarsInAllPanels 1;')
    mm.eval('toggleMenuBarsInAllPanels 0;')
    mc.showWindow('Cam_3_Model_Win_menu_BJCP')
    mc.window('Cam_3_Model_Win_menu_BJCP', e=True, wh=[1000, 500])
    #Cam_Window_Scale()


camWH={}
def Cam_Window_Scale():
    camWH.clear()
    allCamWin=[]
    allWindow = list(set(mc.lsUI(wnd=True))-set(['scriptEditorPanel1Window','MayaWindow']))
    for win in allWindow:
        if 'Model_Win' in win:
            allCamWin.append(win)
            win_H=mc.window(win,q=True,h=True)
            win_W=mc.window(win,q=True,w=True)
            camWH.update({win:[win_W,win_H]})
    if not allCamWin:
        mc.confirmDialog(t=u'提示',message=u'没有找到相机窗口！')
        if mc.window('Reset_Cam_Window_Scale1',ex=True):
            mc.deleteUI('Reset_Cam_Window_Scale1')
    else:
        if mc.window('Reset_Cam_Window_Scale1',ex=True):
            mc.deleteUI('Reset_Cam_Window_Scale1')
        mc.window('Reset_Cam_Window_Scale1',t='Reset_Cam_Window_Scale',wh=[100,60],sizeable=True, rtf=True)
        mc.frameLayout(bs='etchedIn',label=u'重置相机窗口',h=40)
        mc.columnLayout()
        mc.floatSliderButtonGrp('Scale',pre=True,v=1,label='Reset Scale',field=True,buttonLabel='RESET',min=0.3,max=3,symbolButtonDisplay=False,cl4=('left','left','left','left'),cw4=(60,60,180,10),changeCommand='OCT_cam.OCT_MCameraModel_zwz.slider(%d)'%1,bc="OCT_cam.OCT_MCameraModel_zwz.slider(%d)"%0)
        mc.showWindow('Reset_Cam_Window_Scale1')

'''def sliderButton(camWH,model):
    try:
        field=mc.floatSliderButtonGrp('Scale',q=True,v=True)
        for key in camWH.keys():
            if model==1:
                newWin_W=field*camWH[key][0]
                newWin_H=field*camWH[key][1]
                if mc.window(key,ex=True):
                    mc.window(key,e=True,wh=[newWin_W,newWin_H])
                else:
                    del camWH[key]
                    continue
            elif model==0:
                if mc.window(key,ex=True):
                    mc.window(key,e=True,wh=[camWH[key][0],camWH[key][1]])
                else:
                    del camWH[key]
                    continue
                mc.floatSliderButtonGrp('Scale',e=True,v=1.0)
    except:
        return'''

def slider(model):
    allWindow = list(set(mc.lsUI(wnd=True))-set(['scriptEditorPanel1Window','MayaWindow']))
    for win in allWindow:
        if 'Model_Win' in win:
            if win not in camWH.keys():
                win_H=mc.window(win,q=True,h=True)
                win_W=mc.window(win,q=True,w=True)
                camWH.update({win:[win_W,win_H]})

    field=mc.floatSliderButtonGrp('Scale',q=True,v=True)            
    for key in camWH.keys():
        if mc.window(key,ex=True):
            if model==1:
                newWin_W=field*camWH[key][0]
                newWin_H=field*camWH[key][1]
                mc.window(key,e=True,wh=[newWin_W,newWin_H])
            elif model==0:
                mc.window(key,e=True,wh=[camWH[key][0],camWH[key][1]])
                mc.floatSliderButtonGrp('Scale',e=True,v=1.0)
        else:
            del camWH[key]

   