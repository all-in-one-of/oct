#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import OCT_CmeraCurves_zwz
import OCT_MCameraModel_zwz
import zwz_CreateStereoCamera

def Cam_3_H_Model():
    import OCT_Cam_3_H_Model_Win
    i = OCT_Cam_3_H_Model_Win.Cam_3_H_Model_Win()
    i.Cam_3_H_Model_Win_UI()

def Cam_Ring_new():
    import OCT_Cam_Ring_new
    Ring_Cam = OCT_Cam_Ring_new.Ring_Cam_Win()
    Ring_Cam.cam_Main_Win()
    

def newCamerasTools(Name):
    import OCT_NewMCameraModel_YH
    myCameraTool = OCT_NewMCameraModel_YH.multipleCameraPanels()
    if Name == 'MODOU':
        myCameraTool.Cam_3_Model_Win_menu_MoDou()
    elif Name == 'FKBS_Around':
        myCameraTool.Cam_7_Model_Win_menu()
    #elif Name == "MODOU BALL":
    #    myCameraTool.Cam_6_Model_Win_menu()
    elif Name == "MODOU AROUND":
        myCameraTool.Cam_7_Model_Win_menu()
    elif Name == "FKBS_Six":
        myCameraTool.Cam_6_Model_Win_menu_FKBS()
    elif Name == "FKBS_Four":
        myCameraTool.Cam_4_Model_Win_menu_FKBS()
    elif Name == 'CDFKBS':
        myCameraTool.Cam_6_Model_Win_menu_CDFKBS()
    elif Name == "SH_Six":
        myCameraTool.Cam_6_Model_Win_menu_SH()
    elif Name == "SDGT_Two":
        myCameraTool.Cam_2_Model_Win_menu_SDGT()
    elif Name=="Open":
        myCameraTool.toggleModelOpen()
    elif Name=="Close":
        myCameraTool.toggleModelClose()
        