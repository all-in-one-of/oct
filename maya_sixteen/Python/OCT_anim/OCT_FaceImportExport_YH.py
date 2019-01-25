#!/usr/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import re
import os 
class importExportTool():
    def __init__(self):
        pass
        
    def importExport(self):
        if not mc.pluginInfo("animImportExport.mll",q=True,loaded=True):
            mc.loadPlugin("animImportExport.mll")
            
        if mc.window('importExport',q=True,exists=True):
            mc.deleteUI('importExport')
        mc.window('importExport', title=u'表情导入/导出工具', widthHeight=(200,150))
        mc.columnLayout(adjustableColumn=True)
        mc.button(label=u"表情导出",h=40,bgc=[0.1,0.5,0.3],c=lambda*args: self.exportFile())
        mc.button(label=u"表情导入",h=40,bgc=[0.1,0.1,0.3],c=lambda*args: self.importFile())
        
        mc.showWindow("importExport")
        
    def exportFile(self):
        allSelect=mc.ls(selection=True)
        if allSelect:
            if mc.objectType(allSelect[0])=="transform":
                nurbs=mc.listRelatives(allSelect[0],c=True,s=True)
                if mc.objectType(nurbs)!="nurbsCurve":
                    mc.confirmDialog(message=u"请选择曲线！")
                    return

            elif mc.objectType(allSelect[0])!="nurbsCurve":
                mc.confirmDialog(message=u"请选择曲线！")
                return 
            else:
                mc.confirmDialog(message=u"请选择曲线！")
                return 
            #startTime=int(mc.playbackOptions(q=True,min=True))
            endTime=int(mc.playbackOptions(q=True,max=True))    
            path=mc.fileDialog2(fileFilter="animExport(*.anim)",caption="Export Selection",dialogStyle=2)
            if path:
                path_1=os.path.split(path[0])
                path_2=path_1[1].split(".") 
                frameRate=mc.currentUnit(q=True,time=True)
                print frameRate
                myFrameRate=self.frames(frameRate)
                print myFrameRate
                path=str(path_1[0]+"/"+path_2[0]+"-"+str(myFrameRate)+"fps-"+str(endTime)+"."+path_2[1])
                
                mc.file(path,force=True,options="precision=17;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1",typ="animExport",pr=True,es=True)
        else:
            mc.confirmDialog(message=u"请选择曲线！")
        
    def importFile(self):
        allSelect=mc.ls(selection=True)
        if allSelect:
            if mc.objectType(allSelect[0])=="transform":
                nurbs=mc.listRelatives(allSelect[0],c=True,s=True)
                if mc.objectType(nurbs)!="nurbsCurve":
                    mc.confirmDialog(message=u"请选择曲线！")
                    return        
            elif mc.objectType(allSelect[0])!="nurbsCurve":
                mc.confirmDialog(message=u"请选择曲线！")
                return
            else:
                mc.confirmDialog(message=u"请选择曲线！")
                return  
            if mc.window("frame_rate1",q=True,exists=True):
                mc.deleteUI("frame_rate1")
            mc.window("frame_rate1",title="seting Time",w=70,h=40)
            mc.columnLayout(adjustableColumn=True)
            mc.text(u"请选择帧率",h=40)
            mc.radioButtonGrp("frame_m",numberOfRadioButtons=2, w=50,label=u'帧率:', labelArray2=[u'24帧', u'48帧'],cw3=[40, 40, 50])
            mc.button(label="OK",c=lambda*args: self.frameRate(),w=50)
            mc.showWindow("frame_rate1")
        else:
            mc.confirmDialog(message=u"请选择曲线！")
            return
            

    def frameRate(self):
        allSelect=mc.ls(selection=True)
        if not allSelect:
            mc.confirmDialog(message=u"请选择曲线！")
            mc.deleteUI("frame_rate1")
            return
            
        if mc.radioButtonGrp("frame_m", q=True,sl=True)==1:
            path=mc.fileDialog2(fileMode=1,fileFilter="animExport(*.anim)",caption="import",dialogStyle=2)
            if not path:
                return
            name=os.path.splitext(path[0])[0].split("/")[-1]
            Time=name.split("-")
            times=self.myFrames(Time[1])
            mc.currentUnit(time=times)
            endTime=mc.playbackOptions(max=Time[-1])

            mc.file(path,i=True,type="animImport",ra=True,mergeNamespacesOnClash=False,namespace=name,options="targetTime=4;copies=1;option=replace;pictures=0;connect=0;",pr=True,loadReferenceDepth="all") 
            
            mc.currentUnit(time='film')
            #frameRate=mc.playbackOptions(min=Time[1])
            #endTime=mc.playbackOptions(max=Time[-1])
            frame=self.frames(Time[1])
            
            frameRates=24/float(frame)*float(Time[-1])
            if frameRates%1>0:
                frameRates=frameRates//1+1
    
            startTime=mc.playbackOptions(min=1)
            endTime=mc.playbackOptions(max=frameRates)
            
            #startTime=mc.playbackOptions(q=True,min=True)
            #endTime=mc.playbackOptions(q=True,max=True)
            
            mc.bakeResults(allSelect[0],simulation=False,t=(startTime,endTime),hierarchy='below',sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=True,bakeOnOverrideLayer=False,minimizeRotation=True,controlPoints=False,shape=True)
        elif mc.radioButtonGrp("frame_m", q=True,sl=True)==2:
            path=mc.fileDialog2(fileMode=1,fileFilter="animExport(*.anim)",caption="import",dialogStyle=2)
            if not path:
                return 
                
            name=os.path.splitext(path[0])[0].split("/")[-1]
            Time=name.split("-")
            times=self.myFrames(Time[1])
            mc.currentUnit(time=times)
            
            endTime=mc.playbackOptions(max=Time[-1])
            mc.file(path,i=True,type="animImport",ra=True,mergeNamespacesOnClash=False,namespace=name,options="targetTime=4;copies=1;option=replace;pictures=0;connect=0;",pr=True,loadReferenceDepth="all")
            #frameRate=mc.playbackOptions(min=Time[1])
            #endTime=mc.playbackOptions(max=Time[-1])
            mc.currentUnit(time='show')

            frame=self.frames(Time[1])
            frameRates=48/float(frame)*float(Time[-1])
            #print frameRates
            if frameRates%1>0:
                frameRates=frameRates//1+1

            startTime=mc.playbackOptions(min=1)
            endTime=mc.playbackOptions(max=frameRates)

            #startTime=mc.playbackOptions(q=True,min=True)
            #endTime=mc.playbackOptions(q=True,max=True)
        
            mc.bakeResults(allSelect[0],simulation=False,t=(startTime,endTime),hierarchy='below',sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=True,bakeOnOverrideLayer=False,minimizeRotation=True,controlPoints=False,shape=True)
        else:
            path=mc.fileDialog2(fileMode=1,fileFilter="animExport(*.anim)",caption="import",dialogStyle=2)
        
            name=os.path.splitext(path[0])[0].split("/")[-1]
            Time=name.split("-")
            times=self.myFrames(Time[1])
            mc.currentUnit(time=times)    
            
            endTime=mc.playbackOptions(max=Time[-1])    
            mc.file(path,i=True,type="animImport",ra=True,mergeNamespacesOnClash=False,namespace=name,options="targetTime=4;copies=1;option=replace;pictures=0;connect=0;",pr=True,loadReferenceDepth="all")
            
        mc.deleteUI("frame_rate1")

    def frames(self,frameRate):
        frame=""
        if frameRate=="game" or frameRate=="15fps":
            frame=15
        elif frameRate=="film" or frameRate=="24fps":
            frame=24
        elif frameRate=="pal" or frameRate=="25fps":
            frame=25
        elif frameRate=="ntsc" or frameRate=="30fps":
            frame=30
        elif frameRate=="show" or frameRate=="48fps":
            frame=48
        elif frameRate=="palf" or frameRate=="50fps":
            frame=50
        elif frameRate=="ntscf" or frameRate=="60fps":
            frame=60
        else:
            frame=frameRate[:-3]
        return frame

    def myFrames(self,frameRate):
        frame=""
        print frameRate
        if frameRate=="game" or frameRate=="15fps":
            frame="game"
        elif frameRate=="film" or  frameRate=="24fps":
            frame="film"
        elif frameRate=="pal" or frameRate=="25fps":
            frame="pal"
        elif frameRate=="ntsc" or frameRate=="30fps":
            frame="ntsc"
        elif frameRate=="show" or frameRate=="48fps":
            frame="show"
        elif frameRate=="palf" or frameRate=="50fps":
            frame="palf"
        elif frameRate=="ntscf" or frameRate=="60fps":
            frame="ntscf"
        else:
            frame=frameRate
        return frame