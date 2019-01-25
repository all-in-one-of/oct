#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
import os
class  renameReferenceFile():
    def __init__(self):
        pass
        #self.ReferenceFiles=[]
        
    def renameReferenceFileUI(self):
        if mc.window('ReferenceFile',q=True,exists=True):
            mc.deleteUI('ReferenceFile')
        mc.window('ReferenceFile', title=u'Reference Low To High', widthHeight=(300, 200),sizeable=True)
        mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center') 
        mc.text("")
        mc.radioButtonGrp('ReferenceOption',columnAlign3=('left','left','left'),columnWidth3=(100,100,70),numberOfRadioButtons=2,label='Reference Options:',labelArray2=('ALL','Select'),sl=1,enable=True)
        mc.setParent('..')
        #mc.columnLayout(adjustableColumn=True)
        mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
        mc.button(label="L",w=270,h=30,c=lambda*args: self.renameReferenceFileL())
        mc.button(label="M",w=270,h=30,c=lambda*args: self.renameReferenceFileM())
        mc.button(label="H",w=270,h=30,c=lambda*args: self.renameReferenceFileH())

        mc.button(label=u"_h_msNoTex_转换成_h_msAnim_",w=270,h=30,c=lambda*args: self.renameReferenceFileNoTex())
        mc.button(label=u"_h_msAnim__转换成_h_msNoTex_",w=270,h=30,c=lambda*args: self.renameReferenceFileAnim())

        mc.button(label=u"_mc_msAnim转换成_h_msAnim",w=270,h=30,c=lambda*args: self.renameReferencemc_AnimChangeToh_Anim())
        mc.button(label=u"_h_msAnim__转换成_mc_msAnim",w=270,h=30,c=lambda*args: self.renameReferenceh_AnimChangeTomc_Anim())

        mc.button(label=u"_tx.转换成_msAnim.",w=270,h=30,c=lambda*args: self.Reference_texToMaster())

        mc.button(label=u"_rg.转换成_msAnim.",w=270,h=30,c=lambda*args: self.Reference_rigToMaster())
        mc.showWindow("ReferenceFile")
        
    def ChangeReferenceFiles(self,*args):
        ReferenceFiles=[]
        referenceOptions=mc.radioButtonGrp("ReferenceOption",sl=True,q=True)
        if referenceOptions==1:
            ReferenceFiles=mc.file(q=True,reference=True)
            return ReferenceFiles
        else:
            gReferenceEditorPanel=mm.eval("global string $gReferenceEditorPanel;string $temp = $gReferenceEditorPanel;")
            ReferenceFiles=mc.sceneEditor(gReferenceEditorPanel,q=True,selectItem=True)
            return ReferenceFiles
            # allSelects=mc.ls(sl=True)
            # if allSelects:
            #     for se in allSelects:
            #         ReferenceNodeName=mc.listConnections(se,s=False,d=True)
            #         if mc.objectType(ReferenceNodeName[0])=="reference":
            #             fileName=mc.referenceQuery(ReferenceNodeName[0],filename=True)
            #             print fileName
            #             ReferenceFiles.append(fileName)
                
            #     return ReferenceFiles
            if not allSelects:
                mc.confirmDialog(m=u"请在大纲处选择要转换参考的reference节点!")
                return
                
    def renameReferenceFileL(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            #print ReferenceFile
            fileName=ReferenceFile.split("/")
            buf=fileName[-1].split("_")
            Name=""
            Names=""
            if 'h' in buf:
                flag=False
                if buf[2]=='h':
                    Name=buf[0]+"_"+buf[1]+"_"+"l"+'_'+buf[3]
                    Names=buf[0]+"_"+buf[1]+"_"+"l_msAnim.mb"
                    flag=True
                elif buf[3]=='h':
                    Name=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"l"+'_'+buf[4]
                    Names=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"l_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)
                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)

            elif 'm' in buf:
                flag=False
                if buf[2]=='m':
                    Name=buf[0]+"_"+buf[1]+"_"+"l"+'_'+buf[3]
                    Names=buf[0]+"_"+buf[1]+"_"+"l_msAnim.mb"
                    flag=True
                elif buf[3]=='m':
                    Name=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"l"+'_'+buf[4]
                    Names=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"l_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #print descfile
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)

                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)
        
                
    def renameReferenceFileM(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        #ReferenceFiles=mc.file(q=True,reference=True)
        for ReferenceFile in ReferenceFiles:
            #print ReferenceFile
            fileName=ReferenceFile.split("/")
            buf=fileName[-1].split("_")
            Name=""
            Names=""
            if 'l' in buf :
                flag=False
                if buf[2]=='l':
                    Name=buf[0]+"_"+buf[1]+"_"+"m"+'_'+buf[3]
                    Names=buf[0]+"_"+buf[1]+"_"+"m_msAnim.mb"
                    flag=True

                elif buf[3]=='l':
                    Name=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"m"+'_'+buf[4]
                    Names=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"m_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)

                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)

            elif 'h' in buf:
                flag=False
                #print ReferenceFile
                if buf[2]=='h':
                    Name=buf[0]+"_"+buf[1]+"_"+"m"+'_'+buf[3]
                    Names=buf[0]+"_"+buf[1]+"_"+"m_msAnim.mb"
                    flag=True
                elif buf[3]=='h':
                    Name=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"m"+'_'+buf[4]
                    Names=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"m_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print fileNames
                    #print os.path.isfile(fileNames)

                if os.path.isfile(fileNames):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(descfile,loadReference=referenceNode)

    def renameReferenceFileH(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        #ReferenceFiles=mc.file(q=True,reference=True)
        for ReferenceFile in ReferenceFiles:
            #print ReferenceFile
            fileName=ReferenceFile.split("/")
            buf=fileName[-1].split("_")
            Name=""
            Names=""
            if 'l' in buf:
                flag=False
                if buf[2]=='l':
                    Name=buf[0]+"_"+buf[1]+"_"+"h"+'_'+buf[3]
                    Names=buf[0]+"_"+buf[1]+"_"+"h_msAnim.mb"
                    flag=True
                elif buf[3]=='l':
                    Name=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"h"+'_'+buf[4]
                    Names=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"h_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)

                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)

            elif 'm' in buf:
                flag=False
                if buf[2]=='m':
                    Name=buf[0]+"_"+buf[1]+"_"+"h"+'_'+buf[3]
                    Names=buf[0]+"_"+buf[1]+"_"+"h_msAnim.mb"
                    flag=True
                elif buf[3]=='m':
                    Name=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"h"+'_'+buf[4]
                    Names=buf[0]+"_"+buf[1]+"_"+buf[2]+"_"+"h_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #print descfile
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print fileNames
                    #print os.path.isfile(fileNames)

                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)


    def renameReferenceFileNoTex(self):
        #eferenceFiles=mc.file(q=True,reference=True)
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            if "_h_msNoTex" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_h_msNoTex","_h_msAnim")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def renameReferenceFileAnim(self):
        #eferenceFiles=mc.file(q=True,reference=True)
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            if "_h_msAnim" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_h_msAnim","_h_msNoTex")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def renameReferencemc_AnimChangeToh_Anim(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            if "_mc_msAnim" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_mc_msAnim","_h_msAnim")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def renameReferenceh_AnimChangeTomc_Anim(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            if "_h_msAnim" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_h_msAnim","_mc_msAnim")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def Reference_texToMaster(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            referenList=ReferenceFile.split("/")
            if referenList[-2]=="texture":
                referenceName=referenList[-1].replace("_tx.","_msAnim.")
                referenceName=referenceName.split("{")[0]
                pathFileName="/".join(referenList[0:-2])+"/master/"+referenceName
                if os.path.isfile(pathFileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(pathFileName,loadReference=referenceNode)

    def Reference_rigToMaster(self):
        ReferenceFiles=self.ChangeReferenceFiles()
        for ReferenceFile in ReferenceFiles:
            referenList=ReferenceFile.split("/")
            if referenList[-2]=="rigging":
                referenceName=referenList[-1].replace("_rg.","_msAnim.")
                referenceName=referenceName.split("{")[0]
                pathFileName="/".join(referenList[0:-2])+"/master/"+referenceName
                if os.path.isfile(pathFileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(pathFileName,loadReference=referenceNode)