# -*- coding: utf-8 -*-
#!/usr/local/bin/python

from PyQt4 import QtGui, QtCore
import sip
import os
import subprocess
import time
import sys
import re
import shutil
import maya.OpenMayaUI as ui
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om

# CPAU_PATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'
USERNAME = os.environ['USER']
NEWPROJECT_NAME = 'New_Project'
MAYAFOLDER_NAME = 'MayaFiles'
IMAGESFLODER_NAME = 'Images'
PROJECT_PATH = mm.eval('getenv "OCTV_PROJECTS"')
OCT_DRIVE = r'\\octvision.com\cg'
SERVE_PATH = r'\\192.168.80.205'
DEEP_PATH = r'M:\ALL\transfer'
 
class AssetDeadline():
    def __init__(self):
        #UI
        self.windowSize = (600, 350)
        self.windowName = "DeadlineSubmitUI"
        self.assetRadio = ""
        self.outputFiled = ""
        self.okButton = ""
        self.deadlineSereveIp = ""
        self.messageRadio = ''
        self.fileSName = mc.file(q=True, sn=True, shn=True)
        self.copyType = 0
        '''
        copyType分两种模式
        1、单纯的检查模式
        2、检查并打开提交窗口，拷贝提交模式
        3、检查并打开提交窗口，仅提交模式
        '''
        #当存在Arnold时检查各层渲染器
        self.myUseRender = []
        #判断是否有加载

    def checkRender(self, *args):
        MrLayers = []
        ArLayers = []
        VrLayers = []
        OtherLayers = []
        #记录了所有层的渲染器
        AllUsedRender = []
        CurrentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
        allLayers = mc.listConnections('renderLayerManager.renderLayerId')
        if  mc.getAttr('%s.renderable' % CurrentLayer):
            CurrentRender = mc.getAttr('defaultRenderGlobals.currentRenderer')
            if CurrentRender == 'arnold':
                ArLayers.append(CurrentLayer)
            elif CurrentRender == 'mentalRay':
                MrLayers.append(CurrentLayer)
            elif CurrentRender == 'vray':
                VrLayers.append(CurrentLayer)
            else:
                OtherLayers.append(CurrentLayer)
            AllUsedRender.append(CurrentRender)
        if allLayers:
            eachRender = ''
            for Layer in allLayers:
                if Layer != CurrentLayer:
                    if mc.getAttr('%s.renderable' % Layer):
                        mc.editRenderLayerGlobals(currentRenderLayer=Layer)
                        eachRender = mc.getAttr('defaultRenderGlobals.currentRenderer')
                        if eachRender == 'mentalRay':
                            MrLayers.append(Layer)
                        elif eachRender == 'arnold':
                            ArLayers.append(Layer)
                        elif eachRender == 'vray':
                            VrLayers.append(Layer)
                        else:
                            OtherLayers.append(Layer)
                        AllUsedRender.append(eachRender)
            if not ArLayers and MrLayers:
                if eachRender != 'mentalRay':
                    mc.editRenderLayerGlobals(currentRenderLayer=MrLayers[0])
            else:
                mc.editRenderLayerGlobals(currentRenderLayer=CurrentLayer)
        return [OtherLayers, MrLayers, ArLayers, VrLayers, AllUsedRender]

    def myChangeNetPath(self, TempPath):
        if TempPath.find('${OCTV_PROJECTS}') >= 0:
            TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
        elif TempPath.find('z:') >= 0:
            TempPath = TempPath.replace('z:', OCT_DRIVE)
        elif TempPath.find('Z:') >= 0:
            TempPath = TempPath.replace('Z:', OCT_DRIVE)
        return TempPath

    def checkFile(self, copyType):
        '''
        copyType分两种模式
        1、单纯的检查模式
        2、检查并打开提交窗口，拷贝提交模式
        3、检查并打开提交窗口，仅提交模式
        '''
        self.copyType = copyType
        self.OtherLayers = []
        OtherLayers = []
        MrLayers = []
        ArLayers = []
        AllUsedRender = []
        #检查是否存在可渲染的摄像机
        myAllCameras = []
        CameraShape = ''
        AllCameras = AllCameras = mc.listCameras(p=True)
        if AllCameras:
            for Camera in AllCameras:
                try:
                    CameraShape = mc.listRelatives(Camera, s=True)[0]
                except:
                    if mc.getAttr('%s.renderable'%Camera):
                        myAllCameras.append(Camera)
                else:
                    if mc.getAttr('%s.renderable'%CameraShape):
                        myAllCameras.append(Camera)
        if not myAllCameras:
            om.MGlobal.displayInfo(u'无可渲染的摄像机！请设置需要渲染的摄像机\n')
            mc.confirmDialog(title=u'温馨提示：', message=u'无可渲染的摄像机！请设置需要渲染的摄像机', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        if copyType != 1:
            if self.fileSName:
                nameFlag = False
                fileSN = self.fileSName.split('_')
                while '' in fileSN:
                    fileSN.remove('')
                if len(fileSN) >= 3:
                    #判断服务器是否存在该工程
                    serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation', fileSN[1], fileSN[2])
                    if os.path.isdir(serFilePath):
                        if mc.file(q=True, amf=True):
                            if self.copyType == 2 or self.copyType == 4:
                                saveFlag = mc.confirmDialog(title=u'温馨提示', message=u'文件已被修改过，请问是否先保存再继续提交？', button=['Yes', 'SaveAs', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                                if saveFlag == 'Yes':
                                    mm.eval("SaveScene")
                                elif saveFlag == "SaveAs":
                                    mm.eval("SaveSceneAs")
                                    nameFlag = True
                    else:
                        mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                        return False
                else:
                    mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                    return False

                if nameFlag:
                    self.fileSName = mc.file(q=True, sn=True, shn=True)
                    fileSNew = self.fileSName.split('_')
                    while '' in fileSNew:
                        fileSNew.remove('')
                    if len(fileSNew)>=3:
                        #判断服务器是否存在该工程
                        serFilePath = os.path.join(PROJECT_PATH, fileSNew[0], r'Project\scenes\animation', fileSNew[1], fileSNew[2])
                        if not os.path.isdir(serFilePath):
                            mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                            return False
                    else:
                        mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                        return False
                             
            else:
                mc.confirmDialog(title=u'警告', message=u'文件名为空！', button=['OK'], defaultButton='Yes', dismissString='No')
                return False
            #判断Arnold存在时，是否有加载其他渲染器的渲染层
            self.myUseRender = self.checkRender()
            OtherLayers = self.myUseRender[0]
            MrLayers = self.myUseRender[1]
            ArLayers = self.myUseRender[2]
            AllUsedRender = self.myUseRender[4]
            print AllUsedRender
            if len(set(AllUsedRender)) > 1:
                mc.confirmDialog(title=u'警告', message=u'提交的文件仅能使用一种渲染器！\n----------请修改文件---------', button=['OK'], defaultButton='Yes', dismissString='No')
                return False


        #设置前缀名
        mc.setAttr("defaultRenderGlobals.imageFilePrefix", "<Scene>/<RenderLayer>/<Camera>/<Camera>", type="string")
        if mc.pluginInfo("mtoa.mll", q = True, loaded = True) and mc.getAttr("defaultRenderGlobals.currentRenderer")=="arnold":
            mc.setAttr("defaultRenderGlobals.imageFilePrefix", "<Scene>/<RenderLayer>/<Camera>/<RenderPass>/<Camera>", type="string")

        if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True) and mc.objExists('vraySettings'):
            mc.setAttr("vraySettings.fileNamePrefix", "<Scene>/<Layer>/<Camera>/<Camera>", type="string")
            mc.setAttr("defaultRenderGlobals.preMel", "", type ="string")
            mc.setAttr("defaultRenderGlobals.postMel", "", type ="string")

        def outPutSets(nodes, name):
            if nodes:
                mc.select(nodes)
                if mc.objExists(name):
                    mc.sets(cl=name)
                    mc.sets(add=name)
                else:
                    mc.sets(n=name)
            else:
                if mc.objExists(name):
                    mc.delete(name)

        #检查贴图路径
        noTexFiles = []
        #Arnold的Tx贴图
        noArnoldTxTexFiles = []
        ArnoldFlag = False
        if ArLayers:
            ArnoldFlag = True
        allTexFiles = mc.ls(type='file')
        if allTexFiles:
            for texFile in allTexFiles:
                try:
                    texFileName = mc.getAttr('%s.fileTextureName' % texFile)
                except:
                    pass
                else:
                    if texFileName:
                        texFileName = self.myChangeNetPath(texFileName)
                        #当有层使用了Arnold渲染器之后，需要判断是否存在TX文件
                        if ArnoldFlag:
                            PathSplitT = os.path.splitext(texFileName)
                            if len(PathSplitT) > 1:
                                LowerPathType = PathSplitT[1].lower()
                                #序列帧不拷贝tx
                                UseSeqFlag = mc.getAttr('%s.useFrameExtension' % texFile)
                                if (LowerPathType != '.hdr') and ((LowerPathType != '.tx') and (not UseSeqFlag)):
                                    ArnoldTxFileName = PathSplitT[0]+'.tx'
                                    if not os.path.isfile(ArnoldTxFileName):
                                        noArnoldTxTexFiles.append(texFile)
                                else:
                                    if not os.path.isfile(texFileName):
                                        noTexFiles.append(texFile)
                            else:
                                noTexFiles.append(texFile)
                        else:
                            if not os.path.isfile(texFileName):
                                noTexFiles.append(texFile)
                    else:
                        noTexFiles.append(texFile)
        outPutSets(noTexFiles, 'sortNo_TexFiles_sets')
        outPutSets(noArnoldTxTexFiles, 'sortNo_ArnoldTxFiles_sets')

        #检查缓存路径
        wrongCacheFiles = []
        noCacheFiles = []
        allCacheFiles = mc.ls(type='cacheFile')
        LocaDatalPath = mc.workspace(en='data')
        if allCacheFiles:
            for mycacheFile in allCacheFiles:
                try:
                    cachePath = mc.getAttr('%s.cachePath' % mycacheFile)
                except:
                    pass
                else:
                    if cachePath:
                        cachePath = self.myChangeNetPath(cachePath)
                        cacheName = mc.getAttr('%s.cacheName' % mycacheFile)
                        cacheFilePath = os.path.join(cachePath, cacheName) + '.xml'
                        if not os.path.isfile(cacheFilePath):
                            noCacheFiles.append(mycacheFile)
                        LocaDatalPath = self.myChangeNetPath(LocaDatalPath)
                        LocaDatalPath = os.path.normpath(LocaDatalPath)
                        if os.path.isdir(LocaDatalPath):
                            cachePath = os.path.normpath(cachePath)
                            if cachePath.lower().find(LocaDatalPath.lower()) < 0:
                                wrongCacheFiles.append(mycacheFile)
                        else:
                            noCacheFiles.append(wrongCacheFiles)
                    else:
                        noCacheFiles.append(mycacheFile)
        outPutSets(noCacheFiles, 'sortNo_CacheFiles_sets')
        outPutSets(wrongCacheFiles, 'sortWrong_CacheFiles_sets')

        #检查Yeti缓存路径、以及贴图路径下
        noYetiCacheFiles = []
        wrongYetiTexFiles = []
        noYetiTexFiles = []
        allYetiCacheFiles = mc.ls(type='pgYetiMaya')
        if allYetiCacheFiles:
            for myYetiCacheFile in allYetiCacheFiles:
                YetiFileMode = None
                try:
                    YetiFileMode = mc.getAttr('%s.fileMode' % myYetiCacheFile)
                except:
                    pass
                else:
                    if YetiFileMode == 1:
                        YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
                        if YetiCachePath:
                            YetiCachePath = self.myChangeNetPath(YetiCachePath)
                            YetiCacheBasePath = os.path.basename(YetiCachePath)
                            YetiCacheBName = YetiCacheBasePath.split('.')[0]
                            YetiCacheDirPath = os.path.dirname(YetiCachePath)
                            if os.path.isdir(YetiCacheDirPath):
                                allYetiDirs = os.listdir(YetiCacheDirPath)
                                FindYetiFileFlag = False
                                for yetiDir in allYetiDirs:
                                    if yetiDir.find(YetiCacheBName) >= 0:
                                        FindYetiFileFlag = True
                                        break
                                if not FindYetiFileFlag:
                                    noYetiCacheFiles.append(myYetiCacheFile)
                            else:
                                noYetiCacheFiles.append(myYetiCacheFile)
                        YetiTexPath = mc.getAttr('%s.imageSearchPath' % myYetiCacheFile)
                        if YetiTexPath:
                            YetiTexPath = self.myChangeNetPath(YetiTexPath)
                            YetiTexPath=YetiTexPath.replace("\\","/")
                            Textype = YetiTexPath.split('/')[-1]
                            if Textype.lower() != 'yeti':
                                wrongYetiTexFiles.append(myYetiCacheFile)
                            else:
                                if os.path.isdir(YetiTexPath):
                                    allYetiTexFiles = os.listdir(YetiTexPath)
                                    if not allYetiTexFiles:
                                        noYetiTexFiles.append(myYetiCacheFile)
                                else:
                                    noYetiTexFiles.append(myYetiCacheFile)
        outPutSets(noYetiCacheFiles, 'sortNo_pgYetiMaya_CacheFiles_sets')
        outPutSets(wrongYetiTexFiles, 'sortWorng_pgYetiMaya_TexFiles_sets')
        outPutSets(noYetiTexFiles, 'sortNo_pgYetiMaya_TexFiles_sets')

        #检查ABC缓存路径
        wrongAbcCacheFiles = []
        noAbcCacheFiles = []
        type_file = 'alembic'
        myLocaProjectPath= mc.workspace(fn=True)
        allCacheFiles = mc.ls(type='AlembicNode')
        if allCacheFiles:
            for myAbccacheFile in allCacheFiles:
                try:
                    abcCachePath = mc.getAttr('%s.abc_File' % myAbccacheFile)
                except:
                    pass
                else:
                    if abcCachePath:
                        try:
                            indexType = abcCachePath.index("alembic")
                        except:
                            wrongAbcCacheFiles.append(myAbccacheFile)
                        else:
                            abcCachePath = self.myChangeNetPath(abcCachePath)
                            if not os.path.isfile(abcCachePath):
                                abcCachePath = os.path.join(myLocaProjectPath, abcCachePath)
                                abcCachePath = os.path.normpath(abcCachePath)
                                if not os.path.isfile(abcCachePath):
                                    noAbcCacheFiles.append(myAbccacheFile)
                    else:
                        noAbcCacheFiles.append(myAbccacheFile)
        outPutSets(noAbcCacheFiles, 'sortNo_Alembic_CacheFiles_sets')
        outPutSets(wrongAbcCacheFiles, 'sortWorng_Alembic_CacheFiles_sets')

        #检查粒子缓存
        noParticle = ''
        #
        AllIsParFlag = False
        AllPars = mc.ls(type='particle')
        if AllPars:
            for eachP in AllPars:
                if mc.nodeType(eachP) == 'particle':
                    AllIsParFlag = True
                    break
        if AllIsParFlag:
            mydynGlobals = mc.dynGlobals(q=True, a=True)
            parPath = mc.workspace(en='particles')
            if os.path.isdir(parPath):
                allDirs = os.listdir(parPath)
                if mydynGlobals:
                    if mc.getAttr('%s.useParticleDiskCache' % mydynGlobals):
                        cacheDirectory = mc.getAttr('%s.cacheDirectory' % mydynGlobals)
                        if allDirs:
                            particleFlag = False
                            for direach in allDirs:
                                if direach.lower().find(cacheDirectory.lower()) >= 0:
                                    particleFlag = True
                                    break
                            if not particleFlag:
                                noParticle = mydynGlobals
                outPutSets(noParticle, 'sortNo_Particl_sets')
            #检查粒子初始化文件是否存在，不存在需要保存
                fileShortName = os.path.splitext(self.fileSName)[0]
                FindParStartFlag = False
                for perDir in allDirs:
                    if perDir.find(fileShortName) >= 0:
                        if perDir.find('_startup') >= 0:
                            FindParStartFlag = True
                            break
                if not FindParStartFlag:
                    saveFlag = mc.confirmDialog(title=u'警告：', message=u'文件中的粒子没有相应的Startup文件，必须进行保存！', button=[u'保存', u'中断退出'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    if saveFlag == u'\u4fdd\u5b58':
                        mm.eval("SaveScene")
                        time.sleep(1)
                    else:
                        return False
            else:
                mc.confirmDialog(title=u'警告：', message=u'工程目录下不存在particles！\n请完整齐全的工程目录', button='Bye Bye!', defaultButton='Yes', cancelButton='No', dismissString='No')
                return False

        #检查毛发Shave缓存
        noShaveCacheFiles = []
        allOnlyShaveShapes = []
        allShaveShapes = mc.ls(type='shaveHair')
        for eachShape in allShaveShapes:
            allOnlyShaveShapes.append(eachShape.split("|")[-1])
        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        if len(allShaveShapes) > len(allOnlyShaveShapes):
            mc.warning(u"毛发Shave的shapes节点有重名的，将导致同名的Shave使用同一个缓存！")
        myshaveGlobals = "shaveGlobals"
        if allShaveShapes and myshaveGlobals:
            shavePath = mc.getAttr("%s.tmpDir" % myshaveGlobals)
            if shavePath:
                shavePath = self.myChangeNetPath(shavePath)
                if not os.path.isdir(shavePath):
                    proPath = mc.workspace(q=True, rd=True)
                    shavePath = os.path.normpath(os.path.join(proPath, shavePath))
                if shavePath.find('z:') >= 0:
                    shavePath = shavePath.replace('z:', OCT_DRIVE)
                elif shavePath.find('Z:') >= 0:
                    shavePath = shavePath.replace('Z:', OCT_DRIVE)
                if os.path.isdir(shavePath):
                    allSahveDirs = os.listdir(shavePath)
                    if allSahveDirs:
                        shaveNames = []
                        for eachDir in allSahveDirs:
                            shaveNames.append(eachDir.split(".")[0])
                        shaveNames = list(set(shaveNames))
                        for eachShape in allShaveShapes:
                            myName = "shaveStatFile_%s" % eachShape.split("|")[-1]
                            if not myName in shaveNames:
                                eachTran = mc.listRelatives(eachShape, f=True, p=True)[0]
                                noShaveCacheFiles.append(eachTran)
                        if noShaveCacheFiles:
                            noShaveCacheFiles.append(myshaveGlobals)
                    else:
                        noShaveCacheFiles.append(myshaveGlobals)
                else:
                    noShaveCacheFiles.append(myshaveGlobals)
        outPutSets(noShaveCacheFiles, 'sortNo_Shave_CacheFiles_sets')

        #检查代理文件/或路径是否存在的模板
        def myCheck_FileOrFolderModel(myType, mtAttr, fileType, NoTypeSets):
            myLocalSourcePath = mc.workspace(en='sourceimages')
            noFiles = []
            try:
                allFiles = mc.ls(type=myType)
            except:
                pass
            else:
                if allFiles:
                    for fileeach in allFiles:
                        try:
                            myFileName = mc.getAttr('%s.%s' % (fileeach, mtAttr))
                        except:
                            pass
                        else:
                            if myFileName:
                                myFileName = self.myChangeNetPath(myFileName)
                                #print myFileName
                                if fileType == 'file':
                                    #针对Arnold
                                    FileOkFlag = False
                                    if os.path.isfile(myFileName):
                                        FileOkFlag = True
                                    if not FileOkFlag:
                                        myFileName = myLocalSourcePath+'/%s' % myFileName
                                        if not os.path.isfile(myFileName):
                                            noFiles.append(fileeach)
                                else:
                                    if not os.path.isdir(myFileName):
                                        noFiles.append(fileeach)
            outPutSets(noFiles, NoTypeSets)
            return noFiles

        #拷贝某些贴图节点的文件
        def myCheck_VrSetFilesModel(typeOn, typeModel, typeFuleAttr, numModel, NoTypeSets):
            nofile = []
            try:
                if mc.getAttr("vraySettings.%s" % typeOn):
                    if mc.getAttr('vraySettings.%s' % typeModel) == numModel:
                        localFile = mc.getAttr('vraySettings.%s' % typeFuleAttr)
                        if not os.path.isfile(localFile):
                            nofile.append('vraySettings')
                            
            except:
                pass
            outPutSets(nofile, NoTypeSets)
            return nofile

        #错误数量
        numnoTexFiles = 0
        numNoCacheFiles = 0
        numWrongCacheFiles = 0
        numNoYetiCacheFiles = 0
        numWrongYetiTexFiles = []
        numNoYetiTexFiles = []
        numNoAbcCacheFiles = 0
        numWrongAbcCacheFiles=0
        numNoParticle = 0
        numNorfParFiles = 0
        numNorfMeshFiles = 0
        numNocamImFiles = 0
        #Mr
        numNoMrIblFiles = 0
        numNoMrTxFiles = 0
        #Vray
        numNoVRayMeshFiles = 0
        numNoVrIesLFiles = 0
        numNoVrIrrMapFiles = 0
        numNoVrLightCFiles = 0
        numNoVrCausticsFiles = 0
        #Arnold
        numNoAiStandInhFiles = 0
        numNoArIesLFiles = 0
        #Shave
        numNoShaveCacheFiles = 0
        

        #检查摄像机投影贴图
        camImType = 'imagePlane'
        camImAttr = 'imageName'
        camImFileType = 'file'
        camImSets = 'sortNo_imagePlan_set'
        nocamImFiles = myCheck_FileOrFolderModel(camImType, camImAttr, camImFileType, camImSets)
        #检查Realflow的particles粒子和Meshs缓存
        #检查RF的particles缓存
        rfParType = 'RealflowEmitter'
        rfParAttr = 'Paths[0]'
        rfParFileType = 'path'
        rfParSets = 'sortNo_RealflowEmitter_set'
        norfParFiles = myCheck_FileOrFolderModel(rfParType, rfParAttr, rfParFileType, rfParSets)
        #检查RF的meshs缓存
        rfMeshType = 'RealflowMesh'
        rfMeshAttr = 'Path'
        rfMeshFileType = 'file'
        rfMeshSets = 'sortNo_RealflowMesh_set'
        norfMeshFiles = myCheck_FileOrFolderModel(rfMeshType, rfMeshAttr, rfMeshFileType, rfMeshSets)

        if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
            #检查mentalrayIblShape节点的贴图
            mrIblType = 'mentalrayIblShape'
            mrIblAttr = 'texture'
            mrIblFileType = 'file'
            mrIblSets = 'sortNo_mentalrayIblShape_set'
            noMrIblFiles = myCheck_FileOrFolderModel(mrIblType, mrIblAttr, mrIblFileType, mrIblSets)
            #检查mentalrayTexture节点的贴图
            mrTxType = 'mentalrayTexture'
            mrTxAttr = 'fileTextureName'
            mrTxFileType = 'file'
            mrTxSets = 'sortNo_mentalrayTexture_set'
            noMrTxFiles = myCheck_FileOrFolderModel(mrTxType, mrTxAttr, mrTxFileType, mrTxSets)
            #统计错误
            numNoMrIblFiles = len(noMrIblFiles)
            numNoMrTxFiles = len(noMrTxFiles)

        if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
            #检查Vray的代理
            VrType = 'VRayMesh'
            VrAttr = 'fileName'
            VrSets = 'sortNo_VRayMesh_set'
            VrFileType = 'file'
            noVRayMeshFiles = myCheck_FileOrFolderModel(VrType, VrAttr, VrFileType, VrSets)
            #检查Vray的VRayLightIESShape灯光贴图
            VrIesLType = 'VRayLightIESShape'
            VrIesLAttr = 'iesFile'
            VrIesLFileType = 'file'
            VrIesLSets = 'sortNo_VRayLightIESShape_set'
            noVrIesLFiles = myCheck_FileOrFolderModel(VrIesLType, VrIesLAttr, VrIesLFileType, VrIesLSets)
            #Irradiance map光子贴图
            VrIrrMap_typeOn = 'giOn'
            VrIrrMap_typeModel = 'imap_mode'
            VrIrrMap_typeFuleAttr = 'imap_fileName'
            VrIrrMap_numModel = 2
            VrIrrMapSets = 'sortNo_VrayIrradianceMap_set'
            noVrIrrMapFiles = myCheck_VrSetFilesModel(VrIrrMap_typeOn, VrIrrMap_typeModel, VrIrrMap_typeFuleAttr, VrIrrMap_numModel, VrIrrMapSets)
            #Light cache map光子贴图
            VrLightC_typeOn = 'giOn'
            VrLightC_typeModel = 'mode'
            VrLightC_typeFuleAttr = 'fileName'
            VrLightC_numModel = 2
            VrLightCSets = 'sortNo_VrayLightCacheMap_set'
            noVrLightCFiles = myCheck_VrSetFilesModel(VrLightC_typeOn, VrLightC_typeModel, VrLightC_typeFuleAttr, VrLightC_numModel, VrLightCSets)
            #Caustics的焦散贴图
            VrCaustics_typeOn = 'causticsOn'
            VrCaustics_typeModel = 'causticsMode'
            VrCaustics_typeFuleAttr = 'causticsFile'
            VrCaustics_numModel = 1
            VrCausticsSets = 'sortNo_CausticsMap_set'
            noVrCausticsFiles = myCheck_VrSetFilesModel(VrCaustics_typeOn, VrCaustics_typeModel, VrCaustics_typeFuleAttr, VrCaustics_numModel, VrCausticsSets)
            #统计错误
            numNoVRayMeshFiles = len(noVRayMeshFiles)
            numNoVrIesLFiles = len(noVrIesLFiles)
            numNoVrIrrMapFiles = len(noVrIrrMapFiles)
            numNoVrLightCFiles = len(noVrLightCFiles)
            numNoVrCausticsFiles = len(noVrCausticsFiles)
            
        if mc.pluginInfo('mtoa.mll', query=True, loaded=True):
            #检查Arnold的代理
            ArType = 'aiStandIn'
            ArAttr = 'dso'
            ArSets = 'sortNo_AiStandIn_set'
            ArFileType = 'file'
            noAiStandInhFiles = myCheck_FileOrFolderModel(ArType, ArAttr, ArFileType, ArSets)
            #检查Arnold的aiPhotometricLight灯光贴图
            ###################
            #改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
            ####################
            ArIesLType = 'aiPhotometricLight'
            ArIesLAttr = 'aiFilename'
            ArIesLFileType = 'file'
            ArIesLSets = 'sortNo_aiPhotometricLight_set'
            noArIesLFiles = myCheck_FileOrFolderModel(ArIesLType, ArIesLAttr, ArIesLFileType, ArIesLSets)
            #统计错误
            numNoAiStandInhFiles = len(noAiStandInhFiles)
            numNoArIesLFiles = len(noArIesLFiles)

        ErrorText = u''
        numnoTexFiles = len(noTexFiles)
        numnoArnoldTxFiles = len(noArnoldTxTexFiles)
        numNoCacheFiles = len(noCacheFiles)
        numWrongCacheFiles = len(wrongCacheFiles)
        numNoYetiCacheFiles = len(noYetiCacheFiles)
        numWrongYetiTexFiles = len(wrongYetiTexFiles )
        numNoYetiTexFiles = len(noYetiTexFiles )
        numNoAbcCacheFiles = len(noAbcCacheFiles)
        numWrongAbcCacheFiles=len(wrongAbcCacheFiles)
        numNoParticle = len(noParticle)
        numNorfParFiles = len(norfParFiles)
        numNorfMeshFiles = len(norfMeshFiles)
        numNocamImFiles = len(nocamImFiles)
        numNoShaveCacheFiles = len(noShaveCacheFiles)

        numNoFiles = (numnoTexFiles + numnoArnoldTxFiles + numNoCacheFiles + numWrongCacheFiles + numNoYetiCacheFiles + numWrongYetiTexFiles + numNoYetiTexFiles + numNoAbcCacheFiles +
                      numWrongAbcCacheFiles+numNoParticle + numNorfParFiles + numNorfMeshFiles + numNocamImFiles + numNoMrIblFiles + numNoMrTxFiles + numNoVRayMeshFiles + numNoVrIesLFiles +
                      numNoVrIrrMapFiles + numNoVrLightCFiles + numNoVrCausticsFiles + numNoAiStandInhFiles + numNoArIesLFiles + numNoShaveCacheFiles)

        if numNoFiles > 0:
            ErrorText += u'文件存在以下错误：\n在输入的路径下，相应文件或文件夹并不存在!\n有以下类型的节点:\n\n'
            if numnoTexFiles:
                ErrorText += u'有 %s 个 file 贴图文件,并存在"%s"的sets节点下\n' % (numnoTexFiles, 'sortNo_TexFiles_sets')
            if numnoArnoldTxFiles:
                ErrorText += u'有 %s 个 file Arnold的Tx贴图文件,并存在"%s"的sets节点下\n' % (numnoArnoldTxFiles, 'sortNo_ArnoldTxFiles_sets')
            if numNoCacheFiles:
                ErrorText += u'有 %s 个 cacheFile 缓存文件,并存在"%s"的sets节点下\n' % (numNoCacheFiles, 'sortNo_CacheFiles_sets')
            if numWrongCacheFiles:
                ErrorText += u'有 %s 个 cacheFile 缓存文件没有放在本工程的data目录下,并存在"%s"的sets节点下\n' % (numWrongCacheFiles, 'sortWrong_CacheFiles_sets')
            if numNoYetiCacheFiles:
                ErrorText += u'有 %s 个 pgYetiMaya Yeti毛发缓存文件,并存在"%s"的sets节点下\n' % (numNoYetiCacheFiles, 'sortWrong_pgYetiMaya_CacheFiles_sets')
            if numWrongYetiTexFiles:
                ErrorText += u'有 %s 个 pgYetiMaya Yeti毛发贴图路径为空或最终不在“yeti”文件夹里,并存在"%s"的sets节点下\n' % (numWrongYetiTexFiles, 'sortWorng_pgYetiMaya_TexFiles_sets')
            if numNoYetiTexFiles:
                ErrorText += u'有 %s 个 pgYetiMaya Yeti指定的路径下找不到贴图,并存在"%s"的sets节点下\n' % (numNoYetiTexFiles, 'sortNo_pgYetiMaya_TexFiles_sets')
            if numNoAbcCacheFiles:
                ErrorText += u'有 %s 个 Alembic CacheFile 缓存文件,并存在"%s"的sets节点下\n' % (numNoAbcCacheFiles, 'sortNo_Alembic_CacheFiles_sets')
            if numWrongAbcCacheFiles:
                ErrorText += u'有 %s 个 Alembic CacheFile 缓存文件最终文件不在“alembic”文件夹里,并存在"%s"的sets节点下\n' % (numWrongAbcCacheFiles, 'sortWrong_CacheFiles_sets')
            if numNoShaveCacheFiles:
                if numNoShaveCacheFiles == 1:
                    ErrorText += u'有 %s 个 Shave shaveGlobals 缓存设置找不到相应文件,并存在"%s"的sets节点下\n' % (numNoShaveCacheFiles, 'sortNo_Shave_CacheFiles_sets')
                else:
                    ErrorText += u'在Shave shaveGlobals的指定路径下有 %s 个  Shave节点找不到相应的缓存文件,并存在"%s"的sets节点下\n' % (numNoShaveCacheFiles-1, 'sortNo_Shave_CacheFiles_sets')
            if numNoParticle:
                ErrorText += u'有 %s 个 particle 缓存文件,并存在"%s"的sets节点下\n' % (numNoParticle, 'sortNo_Particl_sets')
            if numNorfParFiles:
                ErrorText += u'有 %s 个 RealflowEmitter 缓存文件,并存在"%s"的sets节点下\n' % (numNorfParFiles, rfParSets)
            if numNorfMeshFiles:
                ErrorText += u'有 %s 个 RealflowMesh 缓存文件,并存在"%s"的sets节点下\n' % (numNorfMeshFiles, rfMeshSets)
            if numNocamImFiles:
                ErrorText += u'有 %s 个 imagePlane 摄像机投影文件,并存在"%s"的sets节点下\n' % (numNocamImFiles, camImSets)
            if numNoMrIblFiles:
                ErrorText += u'有 %s 个 mentalrayIblShape MR的Image Base Lighting的环境球贴图文件,并存在"%s"的sets节点下\n' % (numNoMrIblFiles, mrIblSets)
            if numNoMrTxFiles:
                ErrorText += u'有 %s 个 mentalrayTexture MR的贴图文件,并存在"%s"的sets节点下\n' % (numNoMrTxFiles, mrTxSets)
            if numNoVRayMeshFiles:
                ErrorText += u'有 %s 个 VRayMesh Vray的代理文件,并存在"%s"的sets节点下\n' % (numNoVRayMeshFiles, VrSets)
            if numNoVrIesLFiles:
                ErrorText += u'有 %s 个 VRayLightIESShape Vray的灯光贴图,并存在"%s"的sets节点下\n' % (numNoVrIesLFiles, VrIesLSets)
            if numNoVrIrrMapFiles:
                ErrorText += u'有 %s 个 vraySettings Vray的Irradiance map光子贴图,并存在"%s"的sets节点下\n' % (numNoVrIrrMapFiles, VrIrrMapSets)
            if numNoVrLightCFiles:
                ErrorText += u'有 %s 个 vraySettings Vray的Light cache map光子贴图,并存在"%s"的sets节点下\n' % (numNoVrLightCFiles, VrLightCSets)
            if numNoVrCausticsFiles:
                ErrorText += u'有 %s 个 vraySettings Vray的Caustics的焦散贴图,并存在"%s"的sets节点下\n' % (numNoVrCausticsFiles, VrCausticsSets)
            if numNoAiStandInhFiles:
                ErrorText += u'有 %s 个 aiStandIn Arnold的代理文件,并存在"%s"的sets节点下\n' % (numNoAiStandInhFiles, ArSets)
            if numNoArIesLFiles:
                ErrorText += u'有 %s 个 aiPhotometricLight Arnold的灯光贴图,并存在"%s"的sets节点下\n' % (numNoArIesLFiles, ArIesLSets)
        if ErrorText:
            mc.warning(ErrorText)
            mc.confirmDialog(title=u'警告', message=u'%s' % ErrorText, button=['OK'], defaultButton='Yes', dismissString='No')
            try:
                mc.outlinerEditor('outlinerPanel1', e=True, ssm=True)
            except:
                pass
            return False
        try:
            mc.outlinerEditor('outlinerPanel1', e=True, ssm=False)
        except:
            pass
        return True

    #modelEditor的show改为none
    def NonePlane(self):
        a=['', 'F', 'B']
        b=['UL_panel', 'U_panel', 'UR_panel', 'L_panel', 'M_panel', 'R_panel', 'DL_panel', 'D_panel', 'DR_panel']
        for i in a:
            for j in b:
                if i=='F' or i=='B':
                    planeName='%s_%s' %(i, j)
                else:
                    planeName=j
                if mc.modelPanel(planeName, ex=True):
                    mc.modelEditor(planeName,e=True, allObjects=False)
        i=1
        while(i):
            try:
                tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
            except:
                pass
            else:
                if tmp:
                    myactivePlane = 'modelPanel%d' % i
                    break
            i+=1
        if myactivePlane:
            mc.modelEditor(myactivePlane, e=True, allObjects=False)

    def copyFile(self, *args):
        self.NonePlane()
        if not mc.radioCollection(self.assetRadio, q=True, sl=True):
            mc.confirmDialog(title=u'温馨提示：', message=u'请选择服务器！', button=['OK'], defaultButton='Yes', dismissString='No')
        else:
            #检查、拷贝、提交
            #CopyJob 2 为拷贝提交模式 3为仅提交模式
            if self.copyType == 2:
                CopyJob = CopyProject()
                CopyJob.main(2, self.myUseRender)
                self.close()
            #检查、提交
            elif self.copyType == 3:
                CopyJob = CopyProject()
                CopyJob.main(3)
                self.close()

            #检查，拷贝，提交(deep)
            elif self.copyType==4:
                CopyJob = CopyProject()
                CopyJob.main(4, self.myUseRender)
                self.close()

#特效渲染deep改路径为\\file2.nas\share\ALL\transfer
class SetProjectPath():
    def __init__(self, parent=None):
        self.fileSName = mc.file(q = True, sn = True, shn=True)
        self.copyType = 1
        self.serveProject = ""

        #记录渲染层
        self.myUseRender = []
        self.ArnoldFlag = False

        self.copyData = {}

    def myChangeNetPath(self,TempPath):
        if TempPath.find('${OCTV_PROJECTS}')>=0:
            TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
        elif TempPath.find('z:') >= 0:
            TempPath = TempPath.replace('z:', OCT_DRIVE)
        elif TempPath.find('Z:') >= 0:
            TempPath = TempPath.replace('Z:', OCT_DRIVE)
        return TempPath

    #改变所有file节点
    def mySetType_Files(self):
        tmpCopyFlag = True
        #判断是否有使用Arnold层
        type_file = "sourceimages"
        serFileName = os.path.join(self.serveProject, type_file)
        allfiles = mc.ls(type = 'file')
        setData = {}

        if allfiles:
            for eachfile in allfiles:
                texFileNameGroup = []
                try:
                    texFirstFileName = mc.getAttr('%s.fileTextureName'%eachfile)
                except:
                    pass
                else:
                    texFirstFileName = self.myChangeNetPath(texFirstFileName)
                    #判断贴图是否开了序列帧模式
                    #序列标识
                    UseSeqFlag = mc.getAttr('%s.useFrameExtension'%eachfile)
                    if not UseSeqFlag:
                        # #当存在Arnold渲染器时
                        # if self.ArnoldFlag:
                        texFileNameGroup.append(texFirstFileName)
                    #当开启了序列时
                    else:
                        myTexDirName = os.path.dirname(texFirstFileName)
                        myTexBaseName = os.path.basename(texFirstFileName)
                        myTexFileTopName = re.findall(r'\D+', myTexBaseName)[0]
                        myAllFileName = os.listdir(myTexDirName)
                        for eachDirFileName in myAllFileName:
                            if eachDirFileName.find(myTexFileTopName) >= 0:
                                IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                                texFileNameGroup.append(IndexTexName)

                    if  texFileNameGroup:
                        for texFileName in texFileNameGroup:
                            texFileName = os.path.normpath(texFileName)
                            texFileNameS = texFileName.split('\\')
                            try:
                                indexType = texFileNameS.index(type_file)
                            except:
                                texFileNameBN = os.path.basename(texFileName)
                                copyFinalTexFilePath = serFileName
                                serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
                            else:
                                serLastTexFileName = '\\'.join(texFileNameS[indexType+1::])
                                serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
                                copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
                            serFinalTexFileName = os.path.normpath(serFinalTexFileName)
                            copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)

                            self.copyData.update({texFileName:['file',copyFinalTexFilePath]})

                        if not UseSeqFlag:
                            setData.update({eachfile:serFinalTexFileName})
                        else:
                            mySetTexDirName = os.path.dirname(serFinalTexFileName)
                            serFinalSetTexFileName = os.path.join(mySetTexDirName, myTexBaseName)
                            serFinalSetTexFileName = os.path.normpath(serFinalSetTexFileName)
                            setData.update({eachfile: serFinalSetTexFileName})
            if setData:
                #设置路径
                for key in setData.keys():
                    mc.setAttr('%s.fileTextureName'%key, setData[key], type = 'string')

            #临时拷贝Arnold贴图文件夹
            if mc.ls(type = 'aiStandIn'):
                myLocalArnoldSourcePath = mc.workspace(en = 'sourceimages')+'/arnoldTex'
                ArnoldProxyCopyData = {}
                if os.path.isdir(myLocalArnoldSourcePath):
                    myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
                    serFileFinalName = serFileName + '\\arnoldTex'
                    self.copyData.update({myLocalArnoldSourcePath:['dir',serFileFinalName]})
        return True

    #改变所有cacheFile节点
    def mySetType_Data(self):
        type_file = 'data'
        other_file = 'otherCache'
        setSercachePath = ''
        serFileName = os.path.join(self.serveProject, type_file)
        allfiles = mc.ls(type = "cacheFile")
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    cachePath = mc.getAttr("%s.cachePath"%eachfile)
                except:
                    pass
                else:
                    cachePath = self.myChangeNetPath(cachePath)
                    cachePath = os.path.normpath(cachePath)
                    cachePathS = cachePath.split("\\")
                    try:
                        indexType = cachePathS.index(type_file)
                    except:
                        copyFinalcachePath = os.path.join(serFileName, other_file)
                    else:
                        serLastcachePath = "\\".join(cachePathS[indexType+1::])
                        copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
                    setSercachePath = "\\".join(cachePathS[indexType::])
                    copyFinalcachePath = os.path.normpath(copyFinalcachePath)
                    if cachePath != copyFinalcachePath:
                        #整理文件夹拷贝
                        self.copyData.update({cachePath:['dir', copyFinalcachePath]})
                        setData.update({eachfile: setSercachePath})
            if setData:
                for key in setData.keys():
                    try:
                        mc.setAttr('%s.cachePath' % key, setData[key], type='string')
                    except:
                        mc.warning(u'cacheFile设置文件出错！')
                        return False
        return True

    #改变所有ABC的data节点
    def mySetAbc_Data(self):
        type_file = 'alembic'
        serFileName = os.path.join(self.serveProject, 'cache\\'+type_file)
        allfiles = mc.ls(type = 'AlembicNode')
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    abcCachePath = mc.getAttr("%s.abc_File"%eachfile)
                except:
                    pass
                else:
                    abcCachePath = self.myChangeNetPath(abcCachePath)
                    abcCachePath = os.path.normpath(abcCachePath)
                    abcCachePath_S = abcCachePath.split("\\")
                    copyFinalAbcCachePath = ""
                    try:
                        indexType = abcCachePath_S.index(type_file)
                    except:
                        abcCachePathBN = os.path.basename(abcCachePath)
                        serFinalAbcCachePath = os.path.join(serFileName, abcCachePathBN)
                        copyFinalAbcCachePath = serFinalAbcCachePath
                        copyFinalAbcCachePath_dir = serFileName
                    else:
                        serLastAbcCachePath = "\\".join(abcCachePath_S[indexType+1::])
                        copyFinalAbcCachePath = os.path.join(serFileName, serLastAbcCachePath)
                        copyFinalAbcCachePath_dir = os.path.dirname(copyFinalAbcCachePath)
                    if copyFinalAbcCachePath:
                        copyFinalAbcCachePath = os.path.normpath(copyFinalAbcCachePath)
                        copyFinalAbcCachePath_dir = os.path.normpath(copyFinalAbcCachePath_dir)
                        if abcCachePath != copyFinalAbcCachePath:
                            self.copyData.update({abcCachePath:['file', copyFinalAbcCachePath_dir]})
                            setData.update({eachfile:copyFinalAbcCachePath})
            if setData:
                for key in setData.keys():
                    mc.setAttr("%s.abc_File"%key, setData[key], type = 'string')
        return True 

    #改变所有Shave缓存节点
    def mySet_Shavedata(self):
        type_file = 'shave'
        serFileName = os.path.join(self.serveProject, 'cache\\'+type_file)
        setData = {}
        allOnlyShaveShapes = []
        allShaveShapes = mc.ls(type = 'shaveHair')
        for eachShape in allShaveShapes:
            allOnlyShaveShapes.append(eachShape.split("|")[-1])

        allShaveOnlyNames =[]
        for OnlyShaveShape in allOnlyShaveShapes:
            allShaveOnlyNames.append("shaveStatFile_%s" %OnlyShaveShape)

        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        myshaveGlobals = 'shaveGlobals'
        if allShaveShapes and myshaveGlobals:
            shavePath = mc.getAttr("%s.tmpDir"%myshaveGlobals)
            if shavePath:
                shavePath = self.myChangeNetPath(shavePath)
                if not os.path.isdir(shavePath):
                    proPath = mc.workspace(q = True, rd = True)
                    shavePath = os.path.normpath(os.path.join(proPath,shavePath))
                shavePath = self.myChangeNetPath(shavePath)
                if os.path.isdir(shavePath):
                    allSahveDirs = os.listdir(shavePath)
                    if allSahveDirs:
                        shavePath = os.path.normpath(shavePath)
                        shaveCachePath_S = shavePath.split("\\")
                        try:
                            indexType = shaveCachePath_S.index(type_file)
                        except:
                            shaveCachePathBN = os.path.basename(shavePath)
                            serFinalShaveCachePath = os.path.join(serFileName, shaveCachePathBN)
                            copyFinalShaveCacheDir = serFileName
                        else:
                            serLastShaveCachePath = '\\'.join(shaveCachePath_S[indexType+1::])
                            copyFinalShaveCacheDir =os.path.join(serFileName, serLastShaveCachePath)
                        copyFinalShaveCacheDir = os.path.normpath(copyFinalShaveCacheDir)
                        self.copyData.update({shavePath:['dir', copyFinalShaveCacheDir]})
                        setData.update({myshaveGlobals :copyFinalShaveCacheDir})
        if setData:
            for key in setData.keys():
                mc.setAttr("%s.tmpDir"%key, setData[key], type = 'string')
        return True

    def mySet_Particles(self):
        type_file = 'particle'
        serFileName = os.path.join(self.serveProject, type_file)
        AllIsParFlag = False
        myAllParticles = mc.ls(type = 'particle')
        for eachP in myAllParticles:
            if mc.nodeType(eachP) == 'particle':
                AllIsParFlag = True
                break
        mydynGlobals= mc.dynGlobals(q = True, a = True)
        if mydynGlobals and AllIsParFlag:
            fileShortName = os.path.splitext(self.fileSName)[0]
            parPath = mc.workspace(en = 'particle')
            cacheDirectory = mc.getAttr("%s.cacheDirectory"%mydynGlobals)
            if not cacheDirectory:
                cacheDirectory = fileShortName
            parCachePath = os.path.join(parPath, cacheDirectory)
            parCachePath = os.path.normpath(parCachePath)
            parCacheSPath = os.path.join(parPath, cacheDirectory+'_startup')
            parCacheSPath = os.path.normpath(parCacheSPath)
            #粒子缓存文件
            if mc.getAttr("%s.useParticleDiskCache"%mydynGlobals):
                if os.path.isdir(parCachePath):
                    if cacheDirectory != "untitled":
                        serFinalPerPath = os.path.join(serFileName,cacheDirectory)
                    else:
                        serFinalPerPath = os.path.join(serFileName, fileShortName+'_'+cacheDirectory)
                    serFinalPerPath = os.path.normpath(serFinalPerPath)
                    #整个文件拷贝方式
                    if parCachePath != serFinalPerPath:
                        self.copyData.update({parCachePath:['dir', serFinalPerPath]})
            #拷贝初始化缓存方案
            if not os.path.isdir(parCacheSPath):
                cacheDirectory = fileShortName
                parCacheSPath = os.path.join(parPath, cacheDirectory+'_startup')
            #粒子初始化文件
            if os.path.isdir(parCacheSPath):
                if cacheDirectory != 'untitled':
                    serFinalPerSPath = os.path.join(serFileName,cacheDirectory+'_startup')
                else:
                    serFinalPerSPath = os.path.join(serFileName, fileShortName+'_'+cacheDirectory+'_startup')
                serFinalPerSPath = os.path.normpath(serFinalPerSPath)
                #整个文件拷贝方式
                if parCacheSPath != serFinalPerSPath:
                    self.copyData.update({parCacheSPath:['dir', serFinalPerSPath]})
            #设置粒子缓存的新文件名
            if cacheDirectory == 'untitled':
                parCacheNName = fileShortName+'_'+cacheDirectory
                mc.setAttr('%s.cacheDirectory'%mydynGlobals, parCacheNName, type = 'string')
        return True

    #设置Realflow的particles粒子和Meshs缓存
    def mySet_rfCacheModel(self, myType, mtAttr):
        tmpCopyFlag = True
        try:
            allRfNodes = mc.ls(type = myType)
        except:
            pass
        else:
            setData = {}
            type_file = 'cache'
            type_data = 'realflowCache'
            serFileName = os.path.join(self.serveProject, type_file, type_data)
            if allRfNodes:
                for RfNode in allRfNodes:
                    myFileFullpath = mc.getAttr('%s.%s'%(RfNode, mtAttr))
                    if myFileFullpath:
                        myFileFullpath = self.myChangeNetPath(myFileFullpath)
                        if myType == 'RealflowEmitter':
                            rfbaseName = 'particle'
                            myFilepath = myFileFullpath
                            myFilePreName = mc.getAttr('%s.Prefixes[0]'%RfNode)
                            myFinalName = os.path.join(serFileName, rfbaseName)
                            myFinalSName = myFinalName
                        else:
                            rfbaseName = 'meshes'
                            myFilepath = os.path.dirname(myFileFullpath)
                            myFileBasePath = os.path.basename(myFileFullpath)
                            FramePadding = mc.getAttr('%s.framePadding'%RfNode)
                            myFileBasePathText = os.path.splitext(myFileBasePath)[0]
                            myFilePreName = myFileBasePathText[:-FramePadding]
                            myFinalName = os.path.join(serFileName, rfbaseName)
                            myFinalSName = os.path.join(myFinalName, myFileBasePath)
                        #获取文件名
                        myFinalName = os.path.normpath(myFinalName)
                        myFinalSName = os.path.normpath(myFinalSName)
                        myFilepath = os.path.normpath(myFilepath)
                        #网络盘存在标识
                        tmpSerPathFlag = os.path.isdir(myFinalName)
                        if os.path.isdir(myFilepath):
                            if myFilepath != myFinalName:
                                #整体文件夹拷贝
                                if myType == 'RealflowEmitter':
                                    self.copyData.update({myFilepath:['dir', myFinalName]})
                                    setData.update({RfNode:myFinalSName})
                                else:
                                    self.copyData.update({myFilepath:['file', myFinalName]})
                                    setData.update({RfNode:myFinalSName})
                if setData:
                    for key in setData.keys():
                        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type = 'string')
        return True
    #设置VRay、Arnold代理、某些贴图节点的文件
    def mySet_Proxy_OImagesModel(self, myType, mtAttr):
        myLocalSourcePath = mc.workspace(en = 'sourceimages')
        try:
            allTypeShapes = mc.ls(type = myType)
        except:
            pass
        else:
            if allTypeShapes:
                setData = {}
                type_file = 'sourceimages'
                serFileName = os.path.join(self.serveProject, type_file)
                for shapeEach in allTypeShapes:
                    try:
                        myFilepath = mc.getAttr('%s.%s' % (shapeEach, mtAttr))
                    except:
                        pass
                    else:
                        if myFilepath:
                            myFilepath = self.myChangeNetPath(myFilepath)
                            #获取文件名
                            FileOkFlag = False
                            if os.path.isfile(myFilepath):
                                FileOkFlag = True
                            if not FileOkFlag:
                                myFilepath = myLocalSourcePath+"/%s"%myFilepath
                                if os.path.isfile(myFilepath):
                                    FileOkFlag = True
                            if FileOkFlag:
                                myFileBaseName = os.path.basename(myFilepath)
                                #最终网络文件名
                                myFinalName = os.path.join(serFileName, myFileBaseName)
                                myFinalName = os.path.normpath(myFinalName)
                                #原始文件地址
                                myFilepath = os.path.normpath(myFilepath)
                                #服务器地址
                                serFileName = os.path.normpath(serFileName)
                                if myFilepath != myFinalName:
                                    self.copyData.update({myFilepath:['file', serFileName]})
                                    setData.update({shapeEach:myFinalName})
                if setData:
                    for key in setData.keys():
                        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type = 'string')
        return True


    #mrIb贴图、mrTex节点的贴图路径、摄像机投影贴图、检查Vray的VRayLightIESShape灯光贴图
    def mySet_OtherImages(self):
        #检查摄像机投影贴图
        camImType = 'imagePlane'
        camImAttr = 'imageName'
        if not self.mySet_Proxy_OImagesModel(camImType, camImAttr):
            return False
        return True


    #设置Yeti缓存和贴图
    def mySet_YetiCache(self):
        type_file = 'cache'
        other_file = 'otherCache'
        setSercachePath = ''
        serFileName = os.path.join(self.serveProject, type_file)
        serFileName = os.path.normpath(serFileName)
        #贴图
        type_TexFile = 'sourceimages'
        serTexFileName = os.path.join(self.serveProject, type_TexFile)
        serFileName = os.path.normpath(serFileName)
        allYetiCacheFiles = mc.ls(type = 'pgYetiMaya')
        setTexData = {}
        #进行
        setSerTexPath = ''
        setData = {}
        if allYetiCacheFiles:
            for myYetiCacheFile in allYetiCacheFiles:
                YetiFileMode = None
                try:
                    YetiFileMode =mc.getAttr('%s.fileMode' % myYetiCacheFile)
                except:
                    pass
                else:
                    if YetiFileMode == 1:
                        YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
                        if YetiCachePath:
                            YetiCachePath = self.myChangeNetPath(YetiCachePath)
                            YetiCachePath = os.path.normpath(YetiCachePath)
                            cachePathS = YetiCachePath.split("\\")
                            try:
                                indexType = cachePathS.index(type_file)
                            except:
                                copyFinalcachePath = os.path.join(serFileName, other_file, '%s'%myYetiCacheFile)
                            else:
                                serLastcachePath = '\\'.join(cachePathS[indexType+1:-1])
                                copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
                            YetiCacheBasePath = os.path.basename(YetiCachePath)
                            YetiCacheDirPath = os.path.dirname(YetiCachePath)
                            setSercachePath = os.path.join(copyFinalcachePath,YetiCacheBasePath)
                            copyFinalcachePath = os.path.normpath(copyFinalcachePath)
                            #整体文件夹设置
                            if YetiCacheDirPath != copyFinalcachePath:
                                self.copyData.update({YetiCacheDirPath:['dir', copyFinalcachePath]})
                                setSercachePath = setSercachePath.replace("\\", "/")
                                setData.update({myYetiCacheFile:setSercachePath})
                        #设置贴图
                        YetiTexPath = mc.getAttr('%s.imageSearchPath' % myYetiCacheFile)
                        if YetiTexPath:
                            YetiTexPath = self.myChangeNetPath(YetiTexPath)
                            if os.path.isdir(YetiTexPath):
                                copyFinalTexPath = os.path.join(serTexFileName, 'Yeti')
                                YetiTexPath = os.path.normpath(YetiTexPath)
                                self.copyData.update({YetiTexPath:['dir', copyFinalTexPath]})
                                setTexData.update({myYetiCacheFile: copyFinalTexPath})
                    for key in setData.keys():
                        try:
                            mc.setAttr("%s.cacheFileName" % key, setData[key], type = 'string')
                        except:
                            mc.warning(u'Yeti的缓存设置文件出错！')
                            return False
                    for key in setTexData.keys():
                        try:
                            mc.setAttr('%s.imageSearchPath' % key, setTexData[key], type = 'string')
                        except:
                            mc.warning(u'Yeti的贴图设置文件出错！')
                            return False
        return True

    #设置Vr光子贴图、焦散贴图
    def mySet_VrSetFilesModel(self, typeOn, typeModel, typeFuleAttr, numModel):
        typeName = ''
        type_file = 'sourceimages'
        serFileName = os.path.join(self.serveProject, type_file)
        try:
            if mc.getAttr('vraySettings.%s' %typeOn):
                if mc.getAttr('vraySettings.%s' % typeModel) == 'numModel':
                    localFile = mc.getAttr('vraySettings.%s' % typeFuleAttr)
                    if localFile:
                        localFile = self.myChangeNetPath(localFile)
                        locaFileBaseName = os.path.basename(localFile)
                        serFileFinalName = os.path.join(serFileName, locaFileBaseName)
                        serFileFinalName = os.path.normpath(serFileFinalName)
                        serFileName = os.path.normpath(serFileName)
                        localFile = os.path.normpath(localFile)
                        if os.path.isfile(localFile):
                            if localFile != serFileFinalName:
                                self.copyData.update({localFile:['file', serFileName]})
                            if typeModel == 'imap_mode':
                                typeName = u'Irradiance map光子贴图'
                            elif typeModel == 'imap_mode':
                                typeName = u'Light cache map光子贴图'
                            else:
                                typeName = u'Caustics的焦散贴图'
                            mc.setAttr('vraySettings.%s' % typeFuleAttr, serFileFinalName, type='string')
        except:
            pass
        return True

    def mySet_Mr(self):
        #设置mentalrayIblShape节点的贴图
        mrIbType = 'mentalrayIblShape'
        mrIbAttr = 'texture'
        if not self.mySet_Proxy_OImagesModel(mrIbType, mrIbAttr):
            return False
        #设置mentalrayTexture节点的贴图
        mrTxType = 'mentalrayTexture'
        mrTxAttr = 'fileTextureName'
        if not self.mySet_Proxy_OImagesModel(mrTxType, mrTxAttr):
            return False
        return True

    def mySet_Vr(self):
        #设置Vray的代理
        VrType = 'VRayMesh'
        VrAttr = 'fileName'
        if not self.mySet_Proxy_OImagesModel(VrType, VrAttr):
            return False
        #检查Vray的VRayLightIESShape灯光贴图
        VrIesLType = 'VRayLightIESShape'
        VrIesLAttr = 'iesFile'
        if not self.mySet_Proxy_OImagesModel(VrIesLType, VrIesLAttr):
            return False
        #Irradiance map光子贴图
        IrrMap_typeOn = 'giOn'
        IrrMap_typeModel = 'imap_mode'
        IrrMap_typeFuleAttr = 'imap_fileName'
        IrrMap_numModel = 2
        if not self.mySet_VrSetFilesModel(IrrMap_typeOn, IrrMap_typeModel, IrrMap_typeFuleAttr, IrrMap_numModel):
            return False
        #Light cache map光子 贴图
        LightC_typeOn = 'giOn'
        LightC_typeModel = 'mode'
        LightC_typeFuleAttr = 'fileName'
        LightC_numModel = 2
        if not self.mySet_VrSetFilesModel(LightC_typeOn, LightC_typeModel, LightC_typeFuleAttr, LightC_numModel):
            return False
        #Caustics的焦散贴图
        Caustics_typeOn = 'causticsOn'
        Caustics_typeModel = 'causticsMode'
        Caustics_typeFuleAttr = 'causticsFile'
        Caustics_numModel = 1
        if not self.mySet_VrSetFilesModel(Caustics_typeOn, Caustics_typeModel, Caustics_typeFuleAttr, Caustics_numModel):
            return False
        return True

    def mySet_Ar(self):
        #设置arnold代理
        ArType = 'aiStandIn'
        ArAttr = 'dso'
        if not self.mySet_Proxy_OImagesModel(ArType, ArAttr):
            return False
        #设置Arnold的aiPhotometricLight灯光贴图
        ###################
        #改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
        ArIesLType = 'aiPhotometricLight'
        ArIesLAttr = 'aiFilename'
        if not self.mySet_Proxy_OImagesModel(ArIesLType, ArIesLAttr):
            return False
        return True

    #设置RealFlow的particles粒子和Mesh缓存
    def mySet_rfCache(self):
        #设置particles缓存
        rfParType = 'RealflowEmitter'
        rfParAttr = 'Paths[0]'
        if not self.mySet_rfCacheModel(rfParType, rfParAttr):
            return False

        #设置meshs缓存
        rfMeshType = 'RealflowMesh'
        rfMeshAttr = 'Path'
        if not self.mySet_rfCacheModel(rfMeshType, rfMeshAttr):
            return False
        return True

    #保存文件
    def mySaveFile(self):
        type_file = 'scenes'
        myFileFullpath = mc.file(q=True, sn=True)
        localTempPath = os.path.splitext(myFileFullpath)
        locaoFileName = localTempPath[0]+"_deep"+ localTempPath[1]
        myTyprName = 'mayaBinary'
        if self.fileSName.lower().find('mb') >= 0:
            myTyprName = 'mayaBinary'
        else:
            myTyprName = 'mayaAscii'

        serFileName = os.path.join(self.serveProject, type_file)
        fileserName = os.path.join(serFileName, self.fileSName)

        #判断是否有用Vray渲染器和是否是渲染动画帧
        VrayFlag = False
        VrayAnimationFlag = False
        ChangeFlag = False
        if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
            if mc.objExists('vraySettings'):
                VrayFlag = True
                VrayAnimationFlag = mc.getAttr("defaultRenderGlobals.animation")
        if VrayFlag and VrayAnimationFlag:
            try:
                mc.setAttr("defaultRenderGlobals.animation", False)
            except:
                pass
            else:
                ChangeFlag = True
                time.sleep(1)

        mc.file(rename=locaoFileName)
        mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
        time.sleep(1)
        self.copyData.update({locaoFileName:['file', serFileName]})

        # myProjectAddress = self.serveProject.replace('\\', '/')
        # mm.eval('setProject "%s"' % myProjectAddress)
        if ChangeFlag:
            try:
                mc.setAttr("defaultRenderGlobals.animation", True)
            except:
                pass
        return fileserName
    

    def delDefaultRenderLayer(self):
        layers = mc.ls(exactType='renderLayer')
        count = 0
        pattern = re.compile('^[a-zA-Z0-9_\:-]*defaultRenderLayer$')
        for eachLayer in layers:
            if pattern.match(eachLayer):
                if not eachLayer == 'defaultRenderLayer':
                    try:
                        mc.delete(eachLayer)
                    except:
                        om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                    else:
                        count += 1
        del pattern

        resolutions = mc.ls(exactType='resolution')
        count = 0
        patternS = re.compile('^[a-zA-Z0-9_\:-]*defaultResolution$')
        for each in resolutions:
            if patternS.match(each):
                if not each == 'defaultResolution':
                    try:
                        mc.delete(each)
                    except:
                        om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                    else:
                        count += 1
        del patternS

        allmylayers = mc.listConnections("renderLayerManager.renderLayerId")
        for layer in layers:
            if not layer in allmylayers:
                try:
                    mc.delete(layer)
                except:
                    pass
                else:
                    count += 1
        om.MGlobal.displayInfo(u'一共清除了%d 个defaultRenderLayer' % count)

    def Cancelsimulation(self):
        #关闭布料和毛发动力解算
        try:
            AllNucleus= mc.ls(type='nucleus')
        except:
            pass
        else:
            if AllNucleus:
                for eachNucleu in AllNucleus:
                    try:
                        mc.setAttr('%s.enable' % eachNucleu, 0)
                    except:
                        pass
        #Yeti毛发缓存
        try:
            AllYetiCahces= mc.ls(type='pgYetiGroom')
        except:
            pass
        else:
            if AllYetiCahces:
                for eachYetiCahce in AllYetiCahces:
                    try:
                        mc.setAttr('%s.doSimulation' % eachYetiCahce, 0)
                    except:
                        pass


    def setPath(self, *args):
        self.ArnoldFlag = False
        if len(args) > 1:
            self.myUseRender = args[1]
            if len(self.myUseRender[2])>0:
                self.ArnoldFlag = True
        if mc.file(q = True, reference = True):
            mc.confirmDialog(title=u'温馨提示：', message=u'文件含有参考，请导入后再继续！', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        #项目路径
        fileSN = self.fileSName.split('_')
        self.serveProject = os.path.join(DEEP_PATH, fileSN[0], fileSN[1], fileSN[2])
        flag = False
        mc.progressWindow(title=u'设置路径', status=u'即将开始', isInterruptable=True)
        i = 0
        j = 1
        k = 10
        mrFlag = False
        vrFlag = False
        arFlag = False
        if mc.pluginInfo('Mayatomr.mll', query = True, loaded = True):
            mrFlag = True
            i += 1
        if mc.pluginInfo('vrayformaya.mll', query = True, loaded = True):
            vrFlag = True
            i += 1
        if mc.pluginInfo('mtoa.mll', query = True, loaded = True):
            arFlag = True
            i += 1
        k = k + i
       
        mc.progressWindow(edit = True, title = u'共%s步，第 %s 步,正在设置file贴图文件'%(k, j))
        if self.mySetType_Files():
            j += 1
            mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置 cacheFile 缓存文件' % (k, j))
            if self.mySetType_Data():
                j += 1
                mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置 Alembic cacheFile 缓存文件' % (k, j))
                if self.mySetAbc_Data():
                    j += 1
                    mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置 Shave cacheFile  缓存文件' % (k, j))
                    if self.mySet_Shavedata():
                        j += 1
                        mc.progressWindow(edit = True,title = u'共%s步, 第 %s 步,正在设置 particle 缓存文件' % (k, j))
                        if self.mySet_Particles():
                            j += 1
                            mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置 Realflow 缓存' % (k, j))
                            if self.mySet_rfCache():
                                j += 1
                                
                                mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置Yeti毛发缓存' % (k, j))
                                if self.mySet_YetiCache():
                                    j += 1
                                    mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置摄像机投影贴图' % (k, j))
                                    if self.mySet_OtherImages():
                                        if mrFlag:
                                            j += 1
                                            mc.progressWindow(edit = True, title = u'共%s步, 第 %s 步,正在设置Mr渲染器的相关文件' % (k, j))
                                            if not self.mySet_Mr():
                                                mc.confirmDialog(title=u'警告：', message=u'设置文件路径被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                mc.progressWindow(endProgress=True)
                                                return False
                                        if vrFlag:
                                            j += 1
                                            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在设置Vr渲染器的相关文件' % (k, j))
                                            if not self.mySet_Vr():
                                                mc.confirmDialog(title=u'警告：', message=u'设置文件路径被中断', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                mc.progressWindow(endProgress=True)
                                                return False
                                        if arFlag:
                                            j += 1
                                            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在设置Ar渲染器的相关文件' % (k, j))
                                            if not self.mySet_Ar():
                                                mc.confirmDialog(title=u'警告：', message=u'设置文件路径被中断', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                mc.progressWindow(endProgress=True)
                                                return False
                                        j += 1
                                        mc.progressWindow(edit=True, progress=1, min=0, max=1, status=u"正在保存文件!", title=u'共%s步, 第 %s 步,正在保存文件' % (k, j))
                                        self.delDefaultRenderLayer()
                                        self.Cancelsimulation()
                                        myFileFullName = self.mySaveFile()
                                        if myFileFullName:
                                           mm.eval('autoUpdateAttrEd;')
                                           flag = True
                                           

        if flag:
            if self.copyData:
                #localTempPath = os.path.splitext(self.fileSName)[0]+".txt"
                #myProjecttxt = os.path.join(r"D:\FileCopyTool", localTempPath)
                myProjecttxt = r"D:\FileCopyTool\path.txt"
                if not os.path.isdir(r"D:\FileCopyTool"):
                    os.makedirs(r"D:\FileCopyTool")
                f1 = 1
                d1 = 1
                f=open(myProjecttxt,'a')
                
                f.seek(0)
                for key in self.copyData.keys():
                    if self.copyData[key][0] == 'file':
                        fileCopy = 'file%s,%s;%s\r\n' %(str(f1),key, self.copyData[key][1])
                        print fileCopy

                        f.write(fileCopy)
                        f1 = f1 + 1
                    elif self.copyData[key][0] == 'dir':
                        fileCopy = 'dir%s,%s;%s\r\n' %(str(d1),key, self.copyData[key][1])
                        print fileCopy
                        f.write(fileCopy)
                        d1 = d1 + 1
                f.close()
                # myProjecttxt = r"D:\FileCopyTool\path.txt"
                # f=open(myProjecttxt,'a')
                # f.seek(0)
                # for i in range(3):
                #     f.write("fffff\r\n")
                # f.close()

            mc.progressWindow(endProgress=True)
            mc.confirmDialog(title=u'温馨提示：', message=u'文件设置完成！', button=['OK'], defaultButton='Yes', dismissString='No')
            

# i = AssetDeadline()
# i.checkFile(2) 
# SetProjectPath().setPath(i.myUseRender)

