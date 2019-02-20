#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mm
import os 
import time,re
import subprocess

IMAGESFLODER_NAME = r"\\file.com\share\VFX\Images"
#IMAGESFLODER_NAME = r'D:\aa'
PROJECT_PATH = mm.eval('getenv "OCTV_PROJECTS"')

FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\FastCopy341\FastCopy.exe'
CPAY_SPATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'

REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'
USERNAME = os.environ['USER']

class OCT_RenderDeepSet():
    def __init__(self):
        self.fileSName = mc.file(q=True, sn=True, shn=True)
    def OCT_RenderDeepSet_UI(self):
        if mc.window('OCT_RenderDeepSet_UI', exists=True):
            mc.deleteUI('OCT_RenderDeepSet_UI', window=True)

        myRenderwidth = mc.getAttr("defaultResolution.width")
        myRenderheight = mc.getAttr("defaultResolution.height")
        myRenderGlobals=mc.getAttr("defaultRenderGlobals.currentRenderer")
        numberRender=1
        if myRenderGlobals=='vray':
            numberRender=1
        elif myRenderGlobals=='arnold':
            numberRender=2

        getWindow=mc.window('OCT_RenderDeepSet_UI',wh=(300,150),resizeToFitChildren=1,sizeable=True) 
        mc.formLayout('formLyt', numberOfDivisions=100)
        one = mc.columnLayout('First_Set',parent = 'formLyt')   
        mc.rowLayout('projectRow',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [5,200,35],columnOffset3 =[2,2,2],adjustableColumn3 = True,parent = 'First_Set')
        #mc.columnLayout(rowSpacing=2,columnWidth=100,columnAlign='center') 
        mc.radioButtonGrp('RenderSet',columnAlign3=('left','left','left'),columnWidth3=(90,80,90),numberOfRadioButtons=2,label=u'渲染器设置:',labelArray2=('vray','arnold'),sl=numberRender,enable=True)
        mc.setParent('..')
        mc.columnLayout()
        mc.text("")
        mc.setParent("..")
        #mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
        mc.rowLayout('fiveRow',numberOfColumns = 3,columnAttach3 = ['left','left','left',],columnWidth3 = [90,30,10],columnOffset3 =[2,2,10],adjustableColumn3 = True,parent = 'First_Set')
        mc.text(label=u'分辨率：',w = 68,parent = 'fiveRow')
        mc.text(label=u'宽：',w = 68,parent = 'fiveRow')
        mc.textField('RenderWidth',text = myRenderwidth ,width = 60,alwaysInvokeEnterCommandOnReturn= True,parent = 'fiveRow')
        mc.setParent('..')
        mc.columnLayout()
        mc.text("")
        mc.setParent("..")
        mc.rowLayout('fiveRow1',numberOfColumns = 3,columnAttach3 = ['left','left','left',],columnWidth3 = [90,30,10],columnOffset3 =[2,2,10],adjustableColumn3 = True,parent = 'First_Set')
        mc.text(label=u'',w = 68,parent = 'fiveRow1')
        mc.text(label=u'高：',w = 68,parent = 'fiveRow1')
        mc.textField('RenderHeight',text = myRenderheight,width = 60,alwaysInvokeEnterCommandOnReturn= True,parent = 'fiveRow1')
        mc.setParent("..")
        mc.columnLayout()
        mc.text("")
        mc.setParent("..")
        mc.rowLayout(numberOfColumns=4,columnWidth4=(80,120,120,20),columnAlign4=('center','center','center','center'))
        mc.text(l='',vis=0)
        mc.button(l='OK',w=80,h=30,backgroundColor = (0.0,0.7,0),align='center',c=lambda *args:self.OCT_StartDeepRenderSet())
        mc.button(l='Close',width=80,h=30,backgroundColor = (0.7,0.0,0),c=('mc.deleteUI(\"'+getWindow+'\",window=True)'))
        mc.text(l='',vis=0)
        mc.showWindow(getWindow)

    def OCT_StartDeepRenderSet(self):
        VRayLoaded=mc.pluginInfo("vrayformaya.py",q=True,loaded=True)
        AroldLoaded=mc.pluginInfo("mtoa",q=True,loaded=True)
        lights=[]
        if VRayLoaded and AroldLoaded:
            lights = mc.ls(lt = True,type=['VRayLightSphereShape','VRayLightIESShape','VRayLightDomeShape','VRayLightRectShape','aiAreaLight','aiSkyDomeLight','aiPhotometricLight','pointLight','spotLight','areaLight'])
        elif VRayLoaded:
            lights = mc.ls(lt = True,type=['VRayLightSphereShape','VRayLightIESShape','VRayLightDomeShape','VRayLightRectShape'])
        elif AroldLoaded:
            lights = mc.ls(lt = True,type=['aiAreaLight','aiSkyDomeLight','aiPhotometricLight','pointLight','spotLight','areaLight'])
        if lights:
            for lt in lights:
                if not mc.referenceQuery(lt,inr = True):
                    try:
                        trans=mc.listRelatives(lt,p=True)
                        mc.delete(trans[0])
                        mc.delete(lt)
                    except:
                        pass
                        

        RenderWidth=mc.textField('RenderWidth',q=True,text=True)
        RenderHeight=mc.textField('RenderHeight',q=True,text=True)
        if not RenderWidth or not RenderHeight:
            fileResult=mc.confirmDialog(title=u'温馨提示', message=u'分辨率必须设置！')
            return
        
        RenderSet=mc.radioButtonGrp('RenderSet',q=True,sl=True)
        print RenderSet
        if RenderSet==1 and mc.objExists('vraySettings'):
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'vray',type='string')
            mc.setAttr("vraySettings.fileNamePrefix", "<Scene>/<Layer>/<Camera>/<Camera>", type="string")
            mc.setAttr("vraySettings.imageFormatStr","exr (deep)",type="string")
            mc.setAttr("vraySettings.width", float(RenderWidth))
            mc.setAttr("vraySettings.height", float(RenderHeight))
            mc.setAttr("vraySettings.relements_enableall",0)
            mc.setAttr("vraySettings.giOn",0)
            mc.setAttr("vraySettings.globopt_light_doDefaultLights",1)
            mc.setAttr("vraySettings.cam_environmentVolumeOn",0)
            mc.setAttr("vraySettings.globopt_light_doLights",0)
            mc.setAttr("vraySettings.globopt_light_doShadows",0)
            mc.setAttr("vraySettings.globopt_mtl_reflectionRefraction",0)
            #mc.setAttr("vraySettings.globopt_mtl_SSSEnabled",0)

        elif RenderSet==2:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold',type='string')
            mc.setAttr("defaultRenderGlobals.imageFilePrefix","<Scene>/<RenderLayer>/<Camera>/<Camera>",type="string")
            mc.setAttr("defaultArnoldDriver.aiTranslator","deepexr",type="string")
            mc.setAttr("defaultResolution.width", float(RenderWidth))
            mc.setAttr("defaultResolution.height", float(RenderHeight))

            try:
                name=mc.createNode('aiSkyDomeLight')
                transName=mc.listRelatives(name,p=True)[0]
                mc.connectAttr('%s.instObjGroups[0]'%transName,'defaultLightSet.dagSetMembers[1]')
            except:
                pass

        mc.deleteUI('OCT_RenderDeepSet_UI', window=True)
        #result=mc.confirmDialog(t=u'温馨提示',message=u'是否提交渲染？', button=['submit dealine', 'current Render'], defaultButton='提交dealine', cancelButton='本机渲染', dismissString='本机渲染')
        result=mc.confirmDialog(title=u'温馨提示',message=u'是否提交渲染？', button=[u'submit dealine', u'current Render', u'Save as deep'], defaultButton=u'submit dealine', cancelButton=u'current Render', dismissString=u'current Render')
        
        if result=='submit dealine':
            import OCT_deadline_submit_zwz 
            usename = os.environ['USERNAME']
            fPath = r'\\octvision.com\cg\Tech\maya\2013\Python\OCT_generel\Deadline\Deadline_User.cfg'
            f = file(fPath, 'r')
            infoStr = f.readlines()
            f.close()
            for i in range(len(infoStr)):
                infoStr[i] = infoStr[i][:-2]
            if usename in infoStr:
                i = OCT_deadline_submit_zwz.AssetDeadline()
                if i.checkFile(4):
                    i.show()
            else:
                mc.confirmDialog(title=u'温馨提示：', message=u'提交功能仅支持灯光组和后期组使用本工具！', button=['OK'], defaultButton='Yes', dismissString='No')
                sys.stderr.write(u'提交功能仅支持灯光组和后期组使用本工具！')
        elif result=='Save as deep':
            import OCT_deadline_submit_zwz 
            i = OCT_deadline_submit_zwz.AssetDeadline()
            if i.checkFile(1):
                myFileFullName = self.mySaveFile()
                myfileBaseName = os.path.basename(myFileFullName)
                myfileBaseName = os.path.splitext(myfileBaseName)[0]
                self.serveImages = self.myCreateDeepImagesFolder()

                mm.eval(r'global string $myFileName = "%s"' % myfileBaseName)
                mm.eval(r'global string $myDeadlineImagesPath = "%s"' % self.serveImages.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineSceneFile = "%s"' % myFileFullName.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineProjectPath= "%s"' % self.serveProject.replace('\\', '/'))
                mm.eval('source "SubmitMayaToDeadline_zwz";')
                mm.eval('SubmitMayaToDeadline_zwz')

        elif result=='current Render':
            fileSN = self.fileSName.split('_')
            while '' in fileSN:
                fileSN.remove('')
            if len(fileSN) >= 3:
                #判断服务器是否存在该工程
                serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation', fileSN[1], fileSN[2])
                if os.path.isdir(serFilePath):
                    if mc.file(q=True, amf=True):   
                        saveFlag = mc.confirmDialog(title=u'温馨提示', message=u'文件已被修改过，请问是否先保存再继续提交？', button=[u'Save', u'Save as',u'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                        if saveFlag == 'Save':
                            mm.eval("SaveScene")
                        elif saveFlag == 'Save as':
                            fileLName = mc.file(q=True, sn=True)
                            fileLName=os.path.splitext(fileLName)[0]+'deep'
                            mc.file(rename=fileLName)
                            mm.eval("SaveScene")
                else:
                    mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                    return False
            else:
                mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                return False

            myProjectAddress = os.path.join(IMAGESFLODER_NAME, fileSN[0], r'Deep', fileSN[1], fileSN[2])
            print myProjectAddress
            if not os.path.isdir(myProjectAddress):
                try:
                    os.makedirs(myProjectAddress)
                except:
                    mc.confirmDialog(title=u'温馨提示：', message=u'请检查您是否有%s的写权限！'%IMAGESFLODER_NAME, button=['OK'], defaultButton='Yes', dismissString='No')
                    return


            #mm.eval('setProject "%s"' % myProjectAddress)

            Render_Tool=mc.getAttr("defaultRenderGlobals.currentRenderer")
            maya_render=os.getenv('MAYA_LOCATION').split("/")[-1]
            startFrame=mc.getAttr("defaultRenderGlobals.startFrame")
            endFrame=mc.getAttr("defaultRenderGlobals.endFrame")
            render_file=mc.file(q=True, sn=True)
            image_save=myProjectAddress

            myProjecttxt=os.path.join(myProjectAddress,r'deepRendertxt.txt')
            if os.path.isfile(myProjecttxt):
                os.remove(myProjecttxt)

            f=open(myProjecttxt,'wt')
            f.write("render_Tool "+Render_Tool+"\n")
            f.write('maya_render '+maya_render+"\n")
            f.write('maya_Frame '+str(startFrame)+" "+str(endFrame)+"\n")
            f.write('render_file '+render_file+"\n")
            f.write('image_save '+image_save+"\n")
            f.close()


            myProjectbat=os.path.join(myProjectAddress,r'deepRenderbat.bat')
            if os.path.isfile(myProjectbat):
                os.remove(myProjectbat)
            f=open(myProjectbat,'wt')
            strs=r'start \\octvision.com\cg\Tech\Vfx\maya\dist\deepRender.exe %s'%myProjecttxt
            #strs1=r'start deepRender.exe %s'%myProjecttxt
            f.write("echo off\n")
            f.write(strs+"\n")
            f.close()
            os.system(myProjectbat)

    #保存文件
    def mySaveFile(self):
        driveFlag = False
        myDrives = ['D:', 'E:', 'C:']
        type_file = 'scenes'
        myFileFullpath = mc.file(q=True, sn=True)
        self.serveProject = myFileFullpath.split("/scenes/")[0]

        fileSize = os.path.getsize(myFileFullpath)
        for drive in myDrives:
            freeSV = mm.eval('strip(system("wmic LogicalDisk where Caption=\'%s\' get FreeSpace /value"))' % drive)
            freeMV = re.sub("\D", "", freeSV)
            if freeMV:
                freeLV = long(freeMV)
                if freeLV > fileSize:
                    driveFlag = True
                    break

        if driveFlag:
            localTempPath = r'%s\octvTemp' % drive
            if not os.path.isdir(localTempPath):
                os.mkdir(localTempPath)

            myTyprName = 'mayaBinary'
            NewFileName = ""
            if self.fileSName.lower().find('mb')>=0:
                myTyprName = 'mayaBinary'
                NewFileName = os.path.splitext(self.fileSName)[0]+"_deep.mb"
            else:
                myTyprName = 'mayaAscii'
                NewFileName = os.path.splitext(self.fileSName)[0]+"_deep.ma"

            locaoFileName = os.path.join(localTempPath, NewFileName)
            mc.file(rename=locaoFileName)
            mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
            time.sleep(2)
            mySourceFile = locaoFileName

            serFileName = os.path.dirname(myFileFullpath)
            fileserName = os.path.join(serFileName, NewFileName)

            myDestFile = serFileName 

            cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE /bufsize=32 \"%s\" /to=\"%s\""' % (CPAY_SPATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, mySourceFile, myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break

            myProjectAddress = self.serveProject.replace('\\', '/')
            mm.eval('setProject "%s"' % myProjectAddress)

            return fileserName
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'本地盘符不够空间来临时存储文件！\n请清理空间', button=['OK'], defaultButton='Yes', dismissString='No')
            return False


    #创建deep输出素材的路径  
    def myCreateDeepImagesFolder(self):
        fileSNameSplit = self.fileSName.split('_')
        # ProjectName = os.path.splitext(self.fileSName)[0]
        serveProject = os.path.join(r"\\file.com\share\VFX\Images", fileSNameSplit[0], r'Deep', fileSNameSplit[1], fileSNameSplit[2], USERNAME)
        if not os.path.isdir(serveProject):
            self.myCreateDeepFolder(serveProject)
        return serveProject

     #创建在W盘渲染deep的文件夹
    def myCreateDeepFolder(self, address):
        try:
            os.makedirs(address)
        except:
            print address
            cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (CPAY_SPATH, r'octvision\rd', r'rd1234', address)
            print cmd
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
                else:
                    time.sleep(0.001)
        time.sleep(0.1)


#OCT_RenderDeepSet().OCT_RenderDeepSet_UI()

