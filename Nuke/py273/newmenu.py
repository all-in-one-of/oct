# -*- coding: utf-8 -*-
import nuke
import os
import sys


UserName = os.environ['COMPUTERNAME']
if UserName:
    if UserName[:4].upper() == 'PCGR' or UserName[:6].upper() == 'RENDER' or UserName[:2].upper() == 'SM' or UserName[:3].upper() == 'WIN' or UserName[:3].upper() == 'win' or UserName[:2].upper() == 'XR' or UserName[:6].upper() == "HW1-RD" or UserName[:6].upper() == "hw1-rd" or UserName[:2].upper() == "RD"or UserName[:2].upper() == "rd":
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
        #特效工具
        myVFxTool = m.addMenu('&FX')
        myVFxTool.addCommand('Check FX', 'newmenu.check_VFX()')
        # myVFxTool.addCommand('&check sequence tool', 'newmenu.inforMation(1)')
        # myVFxTool.addCommand('&check sequence tool without merge Cam', 'newmenu.inforMation(2)')
        myVFxTool.addCommand('&check sequence tool new', 'newmenu.check_VFX_Seq()')
        myVFxTool.addCommand('&create Write outMov', 'newmenu.createWriteOutPut()')

        myVFxTool.addCommand('&SubmitToDeadline', 'newmenu.submitToDeadlines()')
        myVFxTool.addCommand('&copyVFXNukeFile', 'newmenu.copyVFXNukeFile()')

        #刷新素材
        m.addCommand('&Refresh All Read`s Size Or Frames', 'newmenu.RefreshReads()')

        m.addCommand('&Set Read `s message black and checkboard', 'OCT_Nuke_Tools.setAllReadsOnError()')
        m.addCommand('&Search And Replace Read Nodes', 'OCT_Nuke_Tools.ReplaceFileRootPathUI()')
        # m.addCommand('&Replace File Path', 'OCT_Nuke_Tools.replaceFilePath_UI()')
        m.addCommand('&Merge Selected Cameras', 'OCT_Nuke_Tools.doMerge(1)')
        m.addCommand('&Merge Selected Cameras With Shuffle', 'OCT_Nuke_Tools.doMerge(2)')
        m.addCommand('&New Merge Selected Cameras', 'newmenu.NewMeegCameras(1)')
        m.addCommand('&New Merge Selected Cameras With Shuffle', 'newmenu.NewMeegCameras(2)')

        m.addCommand('&FKBS Merge Selected Cameras', 'newmenu.FKBSMergCams(1)')
        m.addCommand('&FKBS Merge Selected Cameras With Shuffle', 'newmenu.FKBSMergCams(2)')

        m.addCommand('&MSS_SC14 MergSelected Cameras', 'newmenu.MSS_SC14MergCamTool()')
        
        m.addCommand("&Add Exr Read's Shuffles", 'newmenu.AddExrShuffles()')
        m.addCommand("&Add Exr Read's Shuffles Simple", 'newmenu.suffleSimple()')
        # m.addCommand("&New Add Exr Read's Shuffles", 'newmenu.AddExrShuffles_two()')
        m.addCommand('&Interval_Frame_Read', 'OCT_Nuke_Tools.Interval_frame_read_zwz()')
        m.addCommand(u'Import Right Images', 'OCT_AddRightImages_zwz.do_AddRightImages_zwz()')
        m.addCommand(u'Left To Right Images', 'OCT_LeftToRightImages_zwz.do_LeftToRightImages_zwz()')
        #m.addCommand(u'Left Right connect', 'newmenu.LeftRightCon()')
        m.addCommand(u'Left Right Images connect', 'newmenu.MergeCamLeftRightCon()',"alt+M")

        m.addCommand(u'CheckFile On Net', 'OCT_CheckFileOnNet_zwz.ChckFileOnnet_uui()')
        m.addCommand(u'AnimationCurve_convert', 'OCT_animationCurve_convert_zxy.animationCurve_convert()')
        m.addCommand(u'AnimationOffset_Frame', 'OCT_AnimationOffset_Frame.animationOffset_Frame()')


        m.addCommand(u'Creat Write', 'newmenu.ConersionFormat()')
        m.addCommand(u'OCT_SetContactSheetResolution', 'newmenu.SetContactSheetWH()')

        m.addCommand(u'OCT_Bulk_Samples_Conversion', 'newmenu.Bulk_Samples_Conversion()')

        m.addCommand('&output mov', 'newmenu.outPutMov()')

        m.addCommand('&copyImageAndRename', 'newmenu.copyImageAndRename()')
        m.addCommand('&CmdLineRender', 'newmenu.CmdLineRender()')
        
        m.addCommand('&OCT_MergeFYNLJCam', 'newmenu.MergeFYNLJCams()')

        m.addCommand('&read Node Path', 'newmenu.readNodePath()')
        m.addCommand('&Combine Read Nodes', 'newmenu.combineReadNodes()')
        m.addCommand('&Comparison Of Folder', 'newmenu.comparisonOfFolder()')
        #============add by zhangben 2018 12 14  for Project DNTG=========================================
        m.addSeparator()
        m.addSeparator()
        m.addCommand("&DNTG Switch R L Stuffs",'newmenu.dntgCmd()','alt+r')
        m.addCommand("pcik Stuffs", 'newmenu.pickStr()')
        m.addSeparator()
        m.addSeparator()
        # add by zhangben 2018 12 13 =======to dntg  project add a hot key
        # nuke.menu('Nuke').addCommand("",
        m.addCommand(u"New Merg CamTools HotKey", "import OCT_newMergCamTool_YH as nmc\nreload(nmc)\ndoSetUp = nmc.newMergeCam()\ndoSetUp.mergeCams_dntg(None,3,\"DNTG\")", "ctrl+d")
        #=================================================================================================
        m.addCommand('&Help', 'OCT_Nuke_Tools.helpDoc()',)


    else:
        nuke.message('Program only run in the OCTVISION!')

def comparisonOfFolder():
    os.system(r'\\octvision.com\cg\Tech\Nuke\py273\ComparisonOfFolder.exe')

def copyVFXNukeFile():
    import copyVFXNukeFile_v1
    copyVFXNukeFile_v1.copy_CompAndSequence()

def check_VFX_Seq():
    import OCT_showInformation
    informat = OCT_showInformation.OCT_ReformatTexts()
    informat.checkSequece()

def readNodePath():
    import OCT_ReadNodePath
    i = OCT_ReadNodePath.myFindFrame()
    i.myFindPanel()

def check_VFX():
    import OCT_Check_Fx
    i = OCT_Check_Fx.OCT_Check_fx()
    i.check_Fx()

def MSS_SC14MergCamTool():
    import OCT_MSS_SC14MergCamTool
    i = OCT_MSS_SC14MergCamTool.MergeMSS_sc14_Cam()
    i.mergeMSSCam()

def CmdLineRender():
    import CmdLineRender
    CmdLineRender.CLrender(nuke.selectedNodes())

def MergeFYNLJCams():
    import OCT_MergeFYNLJCam
    i = OCT_MergeFYNLJCam.MergeFYNLJCam()
    i.mergeFYNLJCamera()

def FKBSMergCams(model):
    import OCT_FKBSMerg6CamLeftRight
    i=OCT_FKBSMerg6CamLeftRight.FKBSMergCamLeftRight()
    i.FKBSMergCam(model)

def copyImageAndRename():
    import OCT_changeImage
    i=OCT_changeImage.OCT_changeImage()
    i.myFindPanel()

def MergeCamLeftRightCon():
    import OCT_MergeCamLeftRightCon_YH
    i=OCT_MergeCamLeftRightCon_YH.MergeCamLeftRightCon()
    i.oldMergeCamera()

def Bulk_Samples_Conversion():
    import OCT_Bulk_Samples_Conversion
    i=OCT_Bulk_Samples_Conversion.OCT_Bulk_Samples_Conversion()
    i.GetReadNodeAndContactSheet()

def submitToDeadlines():
    message="是否提交deadline渲染?"
    Sub = nuke.ask( message )
    print Sub
    if Sub:
        print Sub  
        import SubmitToDeadline
        SubmitToDeadline.SubmitToDeadline()

def outPutMov():
    import OCT_OutputMOV
    outputs=OCT_OutputMOV.OCT_OutputMOV()
    outputs.OutputMOV()

def createWriteOutPut():
    import OCT_OutputMOV
    outputs=OCT_OutputMOV.OCT_OutputMOV()
    outputs.createWriteOutMov()

def LeftRightCon():
    import OCT_LeftRightCon
    OCT_LeftRightCon.do_LeftRightConnection()

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

def inforMation(model):
    import OCT_showInformation
    informat=OCT_showInformation.OCT_ReformatTexts()
    rs=informat.reformatText(model)
    if rs:
        message="是否提交deadline渲染?"
        Sub=nuke.ask( message )
        if Sub:
            import SubmitToDeadline

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

def combineReadNodes():
    import CombineReadNodes
    dialog = CombineReadNodes.Combine_Read_Nodes()
    dialog.run()

def dntgCmd():
    import OTC_convenientKits
    insck = OTC_convenientKits.OTC_convenientKits()
    insck.SwitchRL()
def pickStr():
    import zb_PickStuffs_tools
    reload(zb_PickStuffs_tools)
    zb_PickStuffs_tools.main()
def suffleSimple():# cryptomatte   shuffle simple edition
    import OCT_Nuke_Tools as octnt
    reload(octnt)
    octnt.stuffShuffleSimple()
