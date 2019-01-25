# -*- coding: utf-8 -*-
import nuke
import os
import sys

UserName = os.environ['COMPUTERNAME']
if UserName:
    if UserName[:4].upper() == 'PCGR' or UserName[:6].upper() == 'RENDER':
        #加载工具
        menuBar = nuke.menu('Nuke')
        m = menuBar.addMenu('&OCT_Nuke_Tools')
        m.addCommand('&Add Images', 'newmenu.AddImages()')
        #检查和拷贝文件工具
        mChild = m.addMenu('&CheckFile and CopyProject')
        mChild.addCommand('Check Frame Integrity', 'newmenu.CopyProject(1)')
        mChild.addCommand('Check File Name Normative', 'newmenu.CopyProject(2)')
        mChild.addCommand('Copy Project', 'newmenu.CopyProject(3)')
        mChild.addCommand('New Copy Project', 'newmenu.CopyProject(4)')
        #刷新素材
        m.addCommand('&Refresh All Read`s Size Or Frames', 'newmenu.RefreshReads()')
        #
        m.addCommand('&Set Read `s message black and checkboard', 'OCT_Nuke_Tools.setAllReadsOnError()')
        m.addCommand('&Search And Replace Read Nodes', 'OCT_Nuke_Tools.ReplaceFileRootPathUI()')
        # m.addCommand('&Replace File Path', 'OCT_Nuke_Tools.replaceFilePath_UI()')
        m.addCommand('&Merge Selected Cameras', 'OCT_Nuke_Tools.doMerge(1)')
        m.addCommand('&Merge Selected Cameras With Shuffle', 'OCT_Nuke_Tools.doMerge(2)')
        m.addCommand('&New Merge Selected Cameras', 'newmenu.NewMeegCameras(1)')
        m.addCommand('&New Merge Selected Cameras With Shuffle', 'newmenu.NewMeegCameras(2)')
        m.addCommand("&Add Exr Read's Shuffles", 'newmenu.AddExrShuffles()')
        # m.addCommand("&New Add Exr Read's Shuffles", 'newmenu.AddExrShuffles_two()')
        m.addCommand('&Interval_Frame_Read', 'OCT_Nuke_Tools.Interval_frame_read_zwz()')
        m.addCommand(u'Import Right Images', 'OCT_AddRightImages_zwz.do_AddRightImages_zwz()')
        m.addCommand(u'Left To Right Images', 'OCT_LeftToRightImages_zwz.do_LeftToRightImages_zwz()')
        m.addCommand(u'CheckFile On Net', 'OCT_CheckFileOnNet_zwz.ChckFileOnnet_uui()')
        m.addCommand(u'AnimationCurve_convert', 'OCT_animationCurve_convert_zxy.animationCurve_convert()')

        m.addCommand(u'Creat Write', 'newmenu.ConersionFormat()')
        m.addCommand(u'OCT_SetContactSheetResolution', 'newmenu.SetContactSheetWH()')

        m.addCommand('&Help', 'OCT_Nuke_Tools.helpDoc()')
    else:
        nuke.message('Program only run in the OCTVISION!')

def CopyProject(mode):
    import OCT_CopyProject_zwz
    myNewJob = OCT_CopyProject_zwz.myCheckFile()
    if mode == 1:
        myNewJob.myJob(1)
    elif mode == 2:
        myNewJob.myJob(2)
    elif mode == 3:
        myNewJob.myJob(3)
    elif mode == 4:
        myNewJob.myJob(4)


def RefreshReads():
    import OCT_RefreshAllReads_YH
    myRefreshJob=OCT_RefreshAllReads_YH.MyFrame()
    myRefreshJob.myOrigFrame()

def AddImages():
    import OCT_ImportImages_YH
    myAddImagesJob = OCT_ImportImages_YH.myFindFrame()
    myAddImagesJob.myFindPanel()

def AddExrShuffles():
    import OCT_Add_Read_Shuffles_YH
    myAddUi = OCT_Add_Read_Shuffles_YH.createChannels()   
    myAddUi.channelsUI()

# def AddExrShuffles_two():
#     import OCT_newChannels_YH
#     myAddUi = OCT_newChannels_YH.newCreateChannels()  
#     myAddUi.channelsUI()

def NewMeegCameras(model):
    import OCT_newMergCamTool_YH
    doSetUp = OCT_newMergCamTool_YH.newMergeCam()
    doSetUp.mergeSelectCamUI(model)

def ConersionFormat():
    import OCT_ConversionFormat_YH
    conver = OCT_ConversionFormat_YH.conversionFormats()
    conver.conversionFormatUI()

def SetContactSheetWH():
    import OCT_SetContactSheetWH
    ContactSheetWH=OCT_SetContactSheetWH.changeContactSheetWH()
    ContactSheetWH.SetWidthHeightUI()
