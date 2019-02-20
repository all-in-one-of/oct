#!/usr/bin/python
# -*- coding: utf-8 -*- 
import maya.cmds as mc
import maya.mel as mm
import os 
import subprocess
import time
import shutil 
import re 
PROJECT_PATH = r'\\octvision.com\CG\Themes'
PROJECT_PATHS=r'Z:\\Themes'
FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\fCopy\FastCopy.exe'
class copyReferenceTool():
    def __init__(self):
        pass
    def copyReference(self,flag):
        freeSV=mm.eval('strip(system("wmic LogicalDisk where Caption=\'E:\' get FreeSpace /value"))')
        freeMV = re.sub("\D", "", freeSV)
        if flag==0:
            if freeMV < 5400000000:
               mc.confirmDialog(message=u"E:盘空间过小将影响性能，建议马上清理磁盘空间", button="OK")
               return 
        allReferences=mc.file(q=True,reference=True)
        for renfence in allReferences:
            renfences=renfence.split("{")[0]
            scrFilePathSplit=renfences.split("/")
            scrFilePathJoin="\\".join(scrFilePathSplit[:-1])
            destFilePath=scrFilePathJoin.replace(PROJECT_PATH,'E:\\REF')
            destFilePath=destFilePath.replace('Z:\Themes','E:\\REF')
            if not os.path.isdir(destFilePath):
                os.makedirs(destFilePath)
            if not os.path.exists(destFilePath+"\\"+scrFilePathSplit[-1]) or (os.path.exists(destFilePath+"\\"+scrFilePathSplit[-1]) and (os.path.getmtime(destFilePath+"\\"+scrFilePathSplit[-1]) != os.path.getmtime(renfences))):  
                fileSize=os.path.getsize(renfences)
                if flag==1 and freeMV<fileSize:
                    mc.confirmDialog(message=u"E:盘空间过小将影响性能，建议马上清理磁盘空间", button="OK")
                    return 
                renfences=renfences.replace("/","\\")
                cmd = '%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\"' % (FCOPY_SPATH, renfences,destFilePath)
                p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
                while True:
                    if not p.poll() is None:
                        del p
                        break

                try:
                    #shutil.copy(renfences,destFilePath)
                    referenceNode=mc.file(renfences,q=True,referenceNode=True)
                    mc.file((destFilePath+"\\"+scrFilePathSplit[-1]),loadReference=referenceNode)
                except:
                    mc.confirmDialog(message=renfence+u"文件拷贝出错!!!",button="OK")
                    return
            if (os.path.exists(destFilePath+"\\"+scrFilePathSplit[-1]) and (os.path.getmtime(destFilePath+"\\"+scrFilePathSplit[-1]) == os.path.getmtime(renfences))) and "E:" not in renfences:
                try:
                    referenceNode=mc.file(renfences,q=True,referenceNode=True)
                    mc.file((destFilePath+"\\"+scrFilePathSplit[-1]),loadReference=referenceNode)
                except:
                    mc.confirmDialog(message=renfence+u"文件设置路径出错！！！",button="OK") 
                    return 
         
                
    def modifyReferencePath(self):
        allReferences=mc.file(q=True,reference=True)
        for renfence in allReferences:
            renfences=renfence.split("{")[0]
            scrFilePathSplit=renfences.split("/")
            scrFilePathJoin="\\".join(scrFilePathSplit)
            
            destFilePath=scrFilePathJoin.replace("E:\\REF","Z:\\Themes")
            
            if os.path.exists(destFilePath):
                referenceNode=mc.file(renfences,q=True,referenceNode=True)
                mc.file(destFilePath,loadReference=referenceNode)
            else:
                mc.confirmDialog(message=destFilePath+u"文件不存在！",button="OK")
               
    def copyReferenceUI(self):
        if mc.window("copyReferenceUI",q=True,exists=True):
            mc.deleteUI("copyReferenceUI")
        mc.window("copyReferenceUI",title=u"拷贝参考物体到本机和修改参考的路径",widthHeight=(200, 100))
        mc.columnLayout(adjustableColumn=True)
        mc.button(label="CopyReferenceToLocal",h=30,c=lambda*args: self.copyReference(0),bgc=[0.5,0.1,0.3])
        mc.button(label="UpdateLocalReference",h=30,c=lambda*args: self.copyReference(1),bgc=[0.1,0.5,0.4])
        mc.button(label="modifyPathReferenceToServer",h=30,c=lambda*args: self.modifyReferencePath(),bgc=[0.2,0.5,0.2])
        mc.showWindow("copyReferenceUI")
     