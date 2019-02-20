#!/usr/bin/python
# -*- coding: utf-8 -*- 
import maya.cmds as mc
import os,re
class changenNetworkPath():
    def __init__(self):
        self.oct_path = r'//octvision.com/CG/Themes'
        self.z_path = r'Z:/Themes'

    #贴图
    def Networkpath_tex(self):
        allFile=mc.ls(type="file") 
        for files in allFile:
            path = mc.getAttr("%s.fileTextureName"%files)
            if "${OCTV_PROJECTS}" in path:
                destPath=path.replace("${OCTV_PROJECTS}","//octvision.com/CG/Themes")
                mc.setAttr("%s.fileTextureName"%files,destPath,type="string")

    def OCTvisonChangZ_tex(self):
        allFile = mc.ls(type = 'file')
        for files in allFile:
            path = mc.getAttr("%s.fileTextureName"%files)
            if self.oct_path.lower() in path.lower():
                destPath = path.replace(self.oct_path, self.z_path)
                mc.setAttr("%s.fileTextureName"%files,destPath,type="string")

            tempPath_oct =  self.oct_path.replace("/","\\")
            if tempPath_oct.lower() in path.lower() :
                tempPath_z =  self.z_path.replace("/","\\")
                destPath = path.replace(tempPath_oct, tempPath_z)
                mc.setAttr("%s.fileTextureName"%files,destPath,type="string")

    def variableChangZ_tex(self):
        allFile = mc.ls(type = 'file')
        for files in allFile:
            path = mc.getAttr("%s.fileTextureName"%files)
            if "${OCTV_PROJECTS}" in path:
                destPath = path.replace("${OCTV_PROJECTS}", self.z_path)
                mc.setAttr("%s.fileTextureName"%files,destPath,type="string")
 
    #参考
    def OCTvisonChangZ_ref(self):
        referenceFiles = mc.file(q=True, reference=True)
        for referenceFile in referenceFiles:
            if self.oct_path.lower() in referenceFile.lower():
                destPath = referenceFile.replace(self.oct_path, self.z_path)
                referenceN = mc.file(referenceFile, q=True, referenceNode=True)
                mc.file(destPath, loadReference = referenceN)

            tempPath_oct =  self.oct_path.replace("/","\\")
            if tempPath_oct.lower() in referenceFile.lower():
                tempPath_z =  self.z_path.replace("/","\\")
                destPath = referenceFile.replace(tempPath_oct, tempPath_z)
                referenceN = mc.file(referenceFile, q=True, referenceNode=True)
                mc.file(destPath, loadReference = referenceN)

    def variableChangZ_ref(self):
        referenceFiles = mc.file(q=True, reference=True)
        for referenceFile in referenceFiles:
            if "${OCTV_PROJECTS}" in referenceFile:
                destPath = referenceFile.replace('${OCTV_PROJECTS}', self.z_path)
                referenceN = mc.file(referenceFile, q=True, referenceNode=True)
                mc.file(destPath, loadReference = referenceN)

    #代理缓存转换成Z:/Themes
    def OCTvisonChangZ_Proxy(self):
        #arnold代理
        allAiStandIns = mc.ls(type = 'aiStandIn')
        tempPath_oct =  self.oct_path.replace("/","\\")
        tempPath_z =  self.z_path.replace("/","\\")
        for aiStand in allAiStandIns:
            path = mc.getAttr('%s.dso'%aiStand)
            if self.oct_path.lower() in path.lower():
                destPath = path.replace(self.oct_path, self.z_path)
                mc.setAttr("%s.dso"%aiStand, destPath, type="string")
            if tempPath_oct.lower() in path.lower():
                destPath = path.replace(tempPath_oct, tempPath_z)
                mc.setAttr('%s.dso'%aiStand, destPath, type="string")

        #vray代理
        allVRayMeshs = mc.ls(type = 'VRayMesh')
        for VRayM in allVRayMeshs:
            path = mc.getAttr('%s.fileName'%VRayM)
            if self.oct_path.lower() in path.lower():
                destPath = path.replace(self.oct_path, self.z_path)
                mc.setAttr('%s.fileName'%VRayM, destPath, type = 'string')
            if tempPath_oct.lower() in path.lower():
                destPath = path.replace(tempPath_oct, tempPath_z)
                mc.setAttr('%s.fileName'%VRayM, destPath, type = 'string')

    def OCTvisonChangZ_Cache(self):
        tempPath_oct =  self.oct_path.replace("/","\\")
        tempPath_z =  self.z_path.replace("/","\\")
        #点缓存
        allCacheFiles = mc.ls(type = 'cacheFile')
        for cacheF in allCacheFiles:
            path = mc.getAttr('%s.cachePath'%cacheF)
            if self.oct_path.lower() in path.lower():
                destPath = path.replace(self.oct_path, self.z_path)
                mc.setAttr('%s.cachePath'%cacheF, destPath, type = 'string')
            if tempPath_oct.lower() in path.lower():
                destPath = path.replace(tempPath_oct, tempPath_z)
                mc.setAttr('%s.cachePath', cacheF, destPath, type = 'string')

        #Abc缓存
        allAlembicNodes = mc.ls(type = 'AlembicNode')
        for alembicN in allAlembicNodes:
            path = mc.getAttr('%s.abc_File'%alembicN)
            if self.oct_path.lower() in path.lower():
                destPath = path.replace(self.oct_path, self.z_path)
                mc.setAttr('%s.abc_File'%alembicN, destPath, type = 'string')
            if tempPath_oct.lower() in path.lower():
                destPath = path.replace(tempPath_oct, tempPath_z)
                mc.setAttr('%s.abc_File'%alembicN, destPath, type = 'string')

        allPgYetiMayas = mc.ls(type = 'pgYetiMaya')
        for pgYetiMaya in allPgYetiMayas:
            path = mc.getAttr('%s.cacheFileName'%pgYetiMaya)
            if self.oct_path.lower() in path.lower():
                destPath = path.replace(self.oct_path, self.z_path)
                mc.setAttr('%s.cacheFileName'%alembicN, destPath, type = 'string')
            if tempPath_oct.lower() in path.lower():
                destPath = path.replace(tempPath_oct, tempPath_z)
                mc.setAttr('%s.cacheFileName'%alembicN, destPath, type = 'string')
  
    def CopyTexture(self):
        allFile=mc.ls(type="file")
        fullPath=mc.workspace(expandName="sourceimages")
        filePath=""
        fileName=""
        fileNames=""
        for files in allFile:
            buf=[]
            path=mc.getAttr("%s.fileTextureName"%files)
            if path=="":
                continue
            path = path.replace('\\','/')
            
            filePath=os.path.dirname(path)
            fileName=os.path.basename(path) 
            
            if mc.getAttr("%s.useFrameExtension"%files):
                fileNames=fileName.split(".")
                buffers=mc.getFileList(filespec=(os.path.dirname(path)+"/*"))
                for buffer in buffers:
                    NewFile = filePath+"/"+buffer
                    if os.path.isfile(NewFile):
                        buf.append(NewFile)
            # ==========2018.12.11===========add by zhangben ========== fix the file nodes use the tilling mode,the tool can't copy all maps=
            elif mc.attributeQuery('uvTilingMode', node=files, exists=True) and mc.getAttr('{}.uvTilingMode'.format(files)) == 3:
                fileNames = fileName.split(".")
                buffers = mc.getFileList(filespec=(os.path.dirname(path) + "/*"))
                for eamap in buffers:
                    map_bnm = re.sub(u'_\d+', '', fileNames[0])
                    if eamap.find(map_bnm) != -1 and eamap.split('.')[-1] == fileNames[-1]:
                        mapPath = filePath + "/" + eamap
                        buf.append(mapPath)
            # ===============================================================================================================================
            else:
                buf.append(path)  
            paths=filePath.split("/")[-1]   
            for i in buf:
                fileNames=os.path.basename(i)
                if not os.path.isdir(fullPath+"/"+paths):
                    os.makedirs(fullPath+"/"+paths)
                    mc.sysFile(i,copy=(fullPath+"/"+paths+"/"+fileNames))
                else:
                    if not os.path.exists(fullPath+"/"+paths+"/"+fileNames) or (os.path.exists(fullPath+"/"+paths+"/"+fileNames) and os.path.getsize(fullPath+"/"+paths+"/"+fileNames) != os.path.getsize(i)):
                        mc.sysFile(i,copy=(fullPath+"/"+paths+"/"+fileNames))
                        
            if os.path.isfile(fullPath+"/"+paths+"/"+fileName):
                print (fullPath+"/"+paths+"/"+fileName)
                mc.setAttr("%s.fileTextureName"%files,(fullPath+"/"+paths+"/"+fileName),type="string")

    def showPath(self):
        mc.textScrollList('path', edit=True, removeAll=True)

        allFile=mc.ls(type="file")
        listPath=[]
        # listPaths=""
        # aa=""
        # hight=""
        for files in allFile:
            path = mc.getAttr("%s.fileTextureName"%files)
            filePath=os.path.dirname(path)
            if not filePath in listPath:
                listPath.append(filePath)
                mc.textScrollList('path', edit=True, append = filePath)

        #     if not listPath:
        #         listPath.append(filePath)
        #         # hight=28
        #         listPaths=filePath
        #     elif filePath not in listPath:
        #         listPath.append(filePath)
        #         # hight=hight+28
        #         # listPaths=listPaths+"\n"+filePath
        #     else:
        #         continue
        # if listPaths:
        #     # mc.textScrollList("path",e=True,h=hight,l=listPaths)
        #     mc.textScrollList('path', edit=True, append = listPaths)

           
    def changenNetworkPathUI(self):
        if mc.window("changenNetworkPathUI",q=True,exists=True):
            mc.deleteUI("changenNetworkPathUI")
        mc.window("changenNetworkPathUI",title=u"改变路径",widthHeight=(400, 100),sizeable=True)
        mc.columnLayout(adjustableColumn=True)
        # mc.text("path",l="",h=1)
        textList = mc.textScrollList('path', numberOfRows=5, allowMultiSelection=True, width=300)
        mc.button(label=u" 显 示 贴 图 的 路 径",h=30,c=lambda*args: self.showPath(),bgc=[0.2,0.2,0.4])
        mc.button(label=u"贴图${OCTV_PROJECTS} 改为//octvision.com/CG/Themes",h=30,c=lambda*args: self.Networkpath_tex(),bgc=[0.4,0.1,0.3])
        mc.button(label=u"贴图${OCTV_PROJECTS} 改为Z:/Themes",h=30,c=lambda*args: self.variableChangZ_tex(),bgc=[0.4,0.5,0.4])
        mc.button(label=u"贴图//octvision.com/CG/Themes 改为Z:/Themes",h=30,c=lambda*args: self.OCTvisonChangZ_tex(),bgc=[0.4,0.5,0.4])
        mc.button(label=u"拷 贝 贴 图 到 工 程 目 录 下 分 文 件 夹",h=30,c=lambda*args: self.CopyTexture(),bgc=[0.4,0.5,0.4])
        mc.button(label=u"参考${OCTV_PROJECTS}改为Z:/Themes",h=30,c=lambda*args: self.variableChangZ_ref(),bgc=[0.4,0.5,0.5])
        mc.button(label=u"参考//octvision.com/CG/Themes 改为Z:/Themes",h=30,c=lambda*args: self.OCTvisonChangZ_ref(),bgc=[0.4,0.5,0.5])
        mc.button(label=u"代理(arnold,VRay)//octvision.com/CG/Themes 改为Z:/Themes",h=30,c=lambda*args: self.OCTvisonChangZ_Proxy(),bgc=[0.4,0.5,0.5])
        mc.button(label=u"缓存(点缓存,abc,yeti)//octvision.com/CG/Themes 改为Z:/Themes",h=30,c=lambda*args: self.OCTvisonChangZ_Cache(),bgc=[0.4,0.5,0.5])
        
        mc.showWindow("changenNetworkPathUI")

    @staticmethod
    def get_seq_texture(path):
        fileNames = path.split(".")
        filePath = os.path.dirname(path)
        fileName = os.path.basename(path)
        fileName_spl = os.path.splitext(fileName)
        buffers = mc.getFileList(filespec=(os.path.dirname(path) + "/*"))
        re_num = re.compile('[_.]\d+')
        if not re_num.search(fileName_spl[0]): return [path]
        map_bnm = re_num.sub('', fileName_spl[0])
        return ["{}/{}".format(filePath, eamap) for eamap in buffers if eamap.find(map_bnm) != -1 and eamap.split('.')[-1] == fileName_spl[-1].split('.')[-1]]

#changenNetworkPath().changenNetworkPathUI()