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

    def close(self, *args):
        if mc.window(self.windowName, q=True, exists=True):
            mc.deleteUI(self.windowName)

    def show(self, *args):
        self.close()

        #make the window
        win = mc.window(self.windowName,
                        t='DeadlineSubmitUI_zwz',
                        wh=self.windowSize,
                        mnb=False, mxb=False, rtf=True, s=True)
        form = mc.formLayout(numberOfDivisions=100)
        oneC = mc.columnLayout('First_Set')
        messageRadio = mc.radioButtonGrp('messagRadioBG', label=u'查看Deadline服务器信息', labelArray2=[u'是', u'否'], sl=2, cl3=['left', 'left', 'left'], cw3=[150, 100, 100], numberOfRadioButtons=2, p=oneC)
        mc.radioButtonGrp('AutoSubmit', label=u'是否全自动提交Deadline', labelArray2=[u'是', u'否'], sl=2, cl3=['left', 'left', 'left'], cw3=[150, 100, 100], numberOfRadioButtons=2, p=oneC)
        mc.textFieldGrp('imgesPool', label=u'输出路径: ', text='', editable=False, cw2=[120, 150], cal=[1, 'left'])
        one = mc.columnLayout('row1', p=form)
        mc.frameLayout('form', l="Servers List", h=20, borderStyle='out', p='row1')
        mc.columnLayout('row2', p='row1', rs=20)
        selectRadio = mc.radioCollection('myselectRadio', p='row2')
        mc.radioButton('one', l=u'#1 (211池)', onc=self.selectServer, p='row2')
        mc.radioButton('two', l=u'#2 (222池)', onc=self.selectServer, p='row2')
        mc.radioButton('three', l=u'#3 (223池)', onc=self.selectServer, p='row2')
        mc.radioButton('four', l=u'#4 (224池)', onc=self.selectServer, p='row2')
        mc.radioButton('five', l=u'#5 (163池)', onc=self.selectServer, p='row2')
        mc.radioButton('six', l=u'#6 (101池)', onc=self.selectServer, backgroundColor=(0.3, 0.1, 0), p='row2')
        mc.radioButton('seven', l=u'#7 (102池)', onc=self.selectServer, backgroundColor=(0.3, 0.1, 0), p='row2')
        two_one = mc.frameLayout('frame2', l="Server Info", h=20, borderStyle='out', p=form)
        two_two = mc.scrollField('serverInfo', tx='', ww=True, ed=False, p=form)
        three_one = mc.button('slButton', l='Submint', c=self.copyFile, p=form, en=False, bgc=[0, 0.7, 0], w=100)
        three_two = mc.button('cancelButton', l='Cancel', c=self.close, p=form, w=100)

        mc.formLayout(form, edit=True,
                      attachForm=[(one, 'left', 5), (two_one, 'right', 5), (two_two, 'right', 5), (one, 'top', 64), (two_one, 'top', 64), (three_one, 'left', 5), (three_one, 'right', 5), (three_two, 'left', 5), (three_two, 'right', 5), (three_two, 'bottom', 5)],
                      attachControl=[(two_one, 'left', 1, one), (two_two, 'left', 1, one), (two_two, 'top', 1, two_one), (one, 'bottom', 1, three_one), (two_two, 'bottom', 1, three_one), (three_one, 'bottom', 1, three_two)],
                      attachNone=[(three_one, 'top')],
                      )

        self.windowName = win
        self.messageRadio = messageRadio
        self.assetRadio = selectRadio
        self.outputFiled = two_two
        self.okButton = three_one

        mc.showWindow(win)

    def selectServer(self, *args):
        global SERVE_PATH
        mc.waitCursor(state=True)
        selectOption = mc.radioCollection(self.assetRadio, q=True, sl=True)
        if selectOption == 'one':
            self.deadlineSereveIp = r'//192.168.80.211'
            SERVE_PATH = r'\\192.168.80.221'
        elif selectOption == 'two':
            self.deadlineSereveIp = r'//192.168.80.222'
            SERVE_PATH = r'\\192.168.80.222'
        elif selectOption == 'three':
            self.deadlineSereveIp = r'//192.168.80.223'
            SERVE_PATH = r'\\192.168.80.223'
        elif selectOption == 'four':
            self.deadlineSereveIp = r'//192.168.80.224'
            SERVE_PATH = r'\\192.168.80.224'
        elif selectOption == 'five':
            self.deadlineSereveIp = r'//192.168.90.163'
            SERVE_PATH = r'\\192.168.90.115'
        elif selectOption == 'six':
            self.deadlineSereveIp = r'//192.168.80.101'
            SERVE_PATH = r'\\192.168.80.205'
        elif selectOption == 'seven':
            self.deadlineSereveIp = r'//192.168.80.102'
            SERVE_PATH = r'\\192.168.80.225'
        path = os.getenv('PATH').split(';')
        addr = ''
        for eachPath in path:
            if 'Deadline/bin' in eachPath:
                addr = eachPath
                if os.path.isfile('%s/deadlinecommand.exe' % addr):
                    break
        if addr == '':
            mc.confirmDialog(title=u'温馨提示：', message=u'找不到Deadline客户端安装目录,请安装Deadline客户端.', button=['OK'], defaultButton='Yes', dismissString='No')
            sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.')
        else:
            try:
                str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository %s/DeadlineRepository' % (addr, self.deadlineSereveIp)).read()
            except:
                sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.')
                mc.button(self.okButton, e=True, en=False)
            else:
                #是否加载服务器信息
                mValue = mc.radioButtonGrp('messagRadioBG', q=True, sl=True)
                if mValue == 1:
                    try:
                        str = os.popen(r'"%s/deadlinecommand.exe" -executescript //octvision.com/cg/Tech/maya/2013/Python/OCT_generel/Deadline/getServerInfo.py' % addr).read()
                    except:
                        mc.confirmDialog(title=u'温馨提示：', message=u'获取Deadline的信息失败，请联系技术管理员！', button=['OK'], defaultButton='Yes', dismissString='No')
                        sys.stderr.write('Error getting Server Info')
                    else:
                        mc.scrollField(self.outputFiled, e=True, tx=str)
                if self.deadlineSereveIp == r'//192.168.90.163':
                    myImagesPaths = ['192.168.90.115', '192.168.90.147']
                    try:
                        address = os.popen(r'"%s/deadlinecommand.exe" -executescript //octvision.com/cg/Tech/maya/2013/Python/OCT_generel/Deadline/getImagesPath.py' % addr).read()
                    except:
                        pass
                    else:
                        minIndex = 0
                        if address:
                            myNum = []
                            for mypath in myImagesPaths:
                                myNum.append(address.count(mypath))
                            minNum = min(myNum)
                            minIndex = myNum.index(minNum)
                        SERVE_PATH = r'\\%s' % myImagesPaths[minIndex]
                mc.button(self.okButton, e=True, en=True)
                mc.textFieldGrp('imgesPool', e=True, text=SERVE_PATH)
        mc.waitCursor(state=False)

    def checkFile(self, copyType):
        '''
        copyType分两种模式
        1 单纯的检查模式
        2 检查并拷贝模式
        '''
        self.copyType = copyType

        if copyType != 2:
            if self.fileSName:
                fileSN = self.fileSName.split('_')
                while '' in fileSN:
                    fileSN.remove('')
                if len(fileSN) >= 3:
                    #判断服务器是否存在该工程
                    serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation', fileSN[1], fileSN[2])
                    if os.path.isdir(serFilePath):
                        if mc.file(q=True, amf=True):
                            if self.copyType == 1:
                                saveFlag = mc.confirmDialog(title=u'温馨提示', message=u'文件已被修改过，请问是否先保存再继续提交？', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                                if saveFlag == 'Yes':
                                    mm.eval("SaveScene")
                    else:
                        mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                        return False
                else:
                    mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                    return False
            else:
                mc.confirmDialog(title=u'警告', message=u'文件名为空！', button=['OK'], defaultButton='Yes', dismissString='No')
                return False

        #设置前缀名
        mc.setAttr("defaultRenderGlobals.imageFilePrefix", "<Scene>/<RenderLayer>/<Camera>/<Camera>", type="string")
        if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True) and mc.objExists('vraySettings'):
            mc.setAttr("vraySettings.fileNamePrefix", "<Scene>/<Layer>/<Camera>/<Camera>", type="string")

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
        allTexFiles = mc.ls(type='file')
        if allTexFiles:
            for texFile in allTexFiles:
                try:
                    texFileName = mc.getAttr('%s.fileTextureName' % texFile)
                except:
                    pass
                else:
                    if texFileName:
                        if texFileName.find('${OCTV_PROJECTS}') >= 0:
                            texFileName = texFileName.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                        elif texFileName.find('z:') >= 0:
                            texFileName = texFileName.replace('z:', OCT_DRIVE)
                        elif texFileName.find('Z:') >= 0:
                            texFileName = texFileName.replace('Z:', OCT_DRIVE)
                        if not os.path.isfile(texFileName):
                            noTexFiles.append(texFile)
                    else:
                        noTexFiles.append(texFile)
        outPutSets(noTexFiles, 'sortNo_TexFiles_sets')

        #检查缓存路径
        noCacheFiles = []
        allCacheFiles = mc.ls(type='cacheFile')
        if allCacheFiles:
            for mycacheFile in allCacheFiles:
                try:
                    cachePath = mc.getAttr('%s.cachePath' % mycacheFile)
                except:
                    pass
                else:
                    if cachePath:
                        if cachePath.find('${OCTV_PROJECTS}') >= 0:
                            cachePath = cachePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                        elif cachePath.find('z:') >= 0:
                            cachePath = cachePath.replace('z:', OCT_DRIVE)
                        elif cachePath.find('Z:') >= 0:
                            cachePath = cachePath.replace('Z:', OCT_DRIVE)
                        cacheName = mc.getAttr('%s.cacheName' % mycacheFile)
                        cacheFilePath = os.path.join(cachePath, cacheName) + '.xml'
                        if not os.path.isfile(cacheFilePath):
                            noCacheFiles.append(mycacheFile)
                    else:
                        noCacheFiles.append(mycacheFile)
        outPutSets(noCacheFiles, 'sortNo_CacheFiles_sets')

        #检查ABC缓存路径
        noAbcCacheFiles = []
        allCacheFiles = mc.ls(type='AlembicNode')
        if allCacheFiles:
            for myAbccacheFile in allCacheFiles:
                try:
                    abcCachePath = mc.getAttr('%s.abc_File' % myAbccacheFile)
                except:
                    pass
                else:
                    if abcCachePath:
                        if abcCachePath.find('${OCTV_PROJECTS}') >= 0:
                            abcCachePath = abcCachePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                        elif abcCachePath.find('z:') >= 0:
                            abcCachePath = abcCachePath.replace('z:', OCT_DRIVE)
                        elif abcCachePath.find('Z:') >= 0:
                            abcCachePath = abcCachePath.replace('Z:', OCT_DRIVE)
                        if not os.path.isfile(abcCachePath):
                            noAbcCacheFiles.append(myAbccacheFile)
                    else:
                        noAbcCacheFiles.append(myAbccacheFile)
        outPutSets(noAbcCacheFiles, 'sortNo_Alembic_CacheFiles_sets')

        #检查粒子缓存
        noParticle = ''
        mydynGlobals = mc.dynGlobals(q=True, a=True)
        if mydynGlobals:
            if mc.getAttr('%s.useParticleDiskCache' % mydynGlobals):
                parPath = mc.workspace(en='particles')
                cacheDirectory = mc.getAttr('%s.cacheDirectory' % mydynGlobals)
                allDirs = os.listdir(parPath)
                if allDirs:
                    particleFlag = False
                    for direach in allDirs:
                        if direach.find(cacheDirectory) >= 0:
                            particleFlag = True
                            break
                    if not particleFlag:
                        noParticle = mydynGlobals
        outPutSets(noParticle, 'sortNo_Particl_sets')

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
                if shavePath.find('${OCTV_PROJECTS}') >= 0:
                    shavePath = shavePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                elif shavePath.find('z:') >= 0:
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
                                if myFileName.find('${OCTV_PROJECTS}') >= 0:
                                    myFileName = myFileName.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                                elif myFileName.find('z:') >= 0:
                                    myFileName = myFileName.replace('z:', OCT_DRIVE)
                                elif myFileName.find('Z:') >= 0:
                                    myFileName = myFileName.replace('Z:', OCT_DRIVE)
                                #print myFileName
                                if fileType == 'file':
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
        numNoAbcCacheFiles = 0
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
        numNoCacheFiles = len(noCacheFiles)
        numNoAbcCacheFiles = len(noAbcCacheFiles)
        numNoParticle = len(noParticle)
        numNorfParFiles = len(norfParFiles)
        numNorfMeshFiles = len(norfMeshFiles)
        numNocamImFiles = len(nocamImFiles)
        numNoShaveCacheFiles = len(noShaveCacheFiles)

        numNoFiles = (numnoTexFiles + numNoCacheFiles + numNoAbcCacheFiles + numNoParticle + numNorfParFiles + numNorfMeshFiles + numNocamImFiles +
                      numNoMrIblFiles + numNoMrTxFiles + numNoVRayMeshFiles + numNoVrIesLFiles + numNoVrIrrMapFiles + numNoVrLightCFiles + numNoVrCausticsFiles + numNoShaveCacheFiles)

        if numNoFiles > 0:
            ErrorText += u'文件存在以下错误：\n在输入的路径下，相应文件或文件夹并不存在!\n有以下类型的节点:\n\n'
            if numnoTexFiles:
                ErrorText += u'有 %s 个 file 贴图文件,并存在"%s"的sets节点下\n' % (numnoTexFiles, 'sortNo_TexFiles_sets')
            if numNoCacheFiles:
                ErrorText += u'有 %s 个 cacheFile 缓存文件,并存在"%s"的sets节点下\n' % (numNoCacheFiles, 'sortNo_CacheFiles_sets')
            if numNoAbcCacheFiles:
                ErrorText += u'有 %s 个 Alembic CacheFile 缓存文件,并存在"%s"的sets节点下\n' % (numNoAbcCacheFiles, 'sortNo_Alembic_CacheFiles_sets')
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
            print ErrorText
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

    def copyFile(self, *args):
        if not mc.radioCollection(self.assetRadio, q=True, sl=True):
            mc.confirmDialog(title=u'温馨提示：', message=u'请选择服务器！', button=['OK'], defaultButton='Yes', dismissString='No')
        else:
            #检查、拷贝、提交
            if self.copyType == 1:
                CopyJob = CopyProject()
                CopyJob.main(1)
                self.close()
            #检查、提交
            elif self.copyType == 2:
                CopyJob = CopyProject()
                CopyJob.main(3)
                self.close()


class CopyJobThread(QtCore.QThread):
    #发射完成比例
    # percent = QtCore.pyqtSignal('int')

    def __init__(self, parent=None):
        super(CopyJobThread, self).__init__(parent)
        self.myLocalFlag = False

    def __del__(self):
        self.wait()

    def ready(self, CpauPath, FcopyPath, source, dest):
        self.myFcopyPath = FcopyPath
        self.myCpauPath = CpauPath
        self.mySourceFile = source
        self.myDestFile = dest
        self.start()

    def run(self):
        if not self.myLocalFlag:
            cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (self.myCpauPath, REMOTE_USER, REMOTE_PWD, self.myFcopyPath, self.mySourceFile, self.myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
            while True:
                if not p.poll() is None:
                    del p
                    break
        else:
            cmd = '%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\"' % (self.myFcopyPath, self.mySourceFile, self.myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
            while True:
                if not p.poll() is None:
                    del p
                    break



class CopyProject(QtGui.QDialog):
    #发射完成比例
    percent = QtCore.pyqtSignal('int')

    def __init__(self, parent=None):
        super(CopyProject, self).__init__(parent)
        self.fileSName = mc.file(q=True, sn=True, shn=True)
        self.CopyLocalPath = self.getCopyPath()
        self.CpauLocalPath = self.getCPauPath()
        self.worker1 = CopyJobThread(self)
        self.worker2 = CopyJobThread(self)
        self.percent.connect(self.EditProgressWindow)
        self.stateMsg = ''
        self.copyType = 1

    def __del__(self):
        del self.worker1, self.worker2

    def EditProgressWindow(self, i):
        mc.progressWindow(edit=True, progress=i)

    #双线程拷贝
    def CopyDataJob(self, myDict):
        i = 0
        for key in myDict.keys():
            if mc.progressWindow(q=True, isCancelled=True):
                while True:
                    if self.worker1.wait() and self.worker2.wait():
                        break
                return False
            mySourceFile = key
            myDestFile = myDict[key]
            if i == 0:
                self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
            elif i == 1:
                self.worker2.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
            else:
                while True:
                    if self.worker1.isFinished():
                        self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                        break
                    elif self.worker2.isFinished():
                        self.worker2.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                        break
            i += 1
            self.percent.emit(i)
        while True:
            if self.worker1.wait() and self.worker2.wait():
                break
        return True

    def fileCountIn(self, dir):
        return sum([len(files) for root, dirs, files in os.walk(dir)])

    #拷贝fastcopy
    def getCopyPath(self):
        FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\fCopy\FastCopy.exe'
        FCOPY_SPATH_BN = os.path.basename(FCOPY_SPATH)
        FCOPY_SPATH_DN = os.path.dirname(FCOPY_SPATH)
        FCOPY_LPATH_DN = r'C:\OCTVTools\fCopy'
        cmd = ''
        if os.path.isdir(FCOPY_LPATH_DN):
            if self.fileCountIn(FCOPY_SPATH_DN) != self.fileCountIn(FCOPY_LPATH_DN):
                cmd = r'%s /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
        else:
            cmd = r'%s /cmd=update /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
        if cmd:
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
            while True:
                if not p.poll() is None:
                    del p
                    break
        return os.path.join(FCOPY_LPATH_DN, FCOPY_SPATH_BN)

    #拷贝Cpau
    def getCPauPath(self):
        CPAY_SPATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
        CPAU_LPATH_DN = r'C:\OCTVTools\CPAU'
        CPAU_LPATH_FP = r'C:\OCTVTools\CPAU\CPAU.exe'
        cmd = ''
        if not os.path.isfile(CPAU_LPATH_FP):
            cmd = r'%s /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (self.CopyLocalPath, CPAY_SPATH, CPAU_LPATH_DN)
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
            while True:
                if not p.poll() is None:
                    del p
                    break
        return CPAU_LPATH_FP

    #创建文件夹命令
    def myCreateFolder(self, address):
        try:
            os.makedirs(address)
        except:
            cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (self.CpauLocalPath, REMOTE_USER, REMOTE_PWD, address)
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
            while True:
                if not p.poll() is None:
                    del p
                    break
                else:
                    time.sleep(0.001)
        time.sleep(0.1)

    #创建相应场景
    def myCreateScenes(self):
        if self.copyType == 1:
            fileSNameSplit = self.fileSName.split('_')
            ProjectName = '_'.join(fileSNameSplit[:3])
            serveProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, fileSNameSplit[0], fileSNameSplit[1], fileSNameSplit[2], USERNAME, ProjectName)
        elif self.copyType == 2:
            result = mc.promptDialog(t=u"拷贝整个工程目录", m=u'请输入路径', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                myPath = mc.promptDialog(q=True, t=True)
                if os.path.isdir(myPath):
                    if myPath[:2] == "z:":
                        myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
                    elif myPath[:2] == "Z:":
                        myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
                    myProjectName = os.path.splitext(self.fileSName)[0]
                    serveProject = os.path.join(myPath, myProjectName)
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
                    return False
            else:
                return False
        if not os.path.isdir(serveProject):
            self.myCreateFolder(serveProject)
            exampleProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, NEWPROJECT_NAME)
            copyData = {exampleProject: serveProject}
            self.CopyDataJob(copyData)
        checkAccessFile = os.path.join(serveProject, 'myTest_TD')
        checkAccessFlag = False
        while(True):
            if os.path.isdir(checkAccessFile):
                checkAccessFile = os.path.join(serveProject, 'myTest_TD')
            else:
                break
        try:
            os.makedirs(checkAccessFile)
        except:
            pass
        try:
            os.removedirs(checkAccessFile)
        except:
            self.worker1.myLocalFlag = False
            self.worker2.myLocalFlag = False
        else:
            self.worker1.myLocalFlag = True
            self.worker2.myLocalFlag = True
        return serveProject

    def myCreateImagesFolder(self):
        fileSNameSplit = self.fileSName.split('_')
        # ProjectName = os.path.splitext(self.fileSName)[0]
        serveProject = os.path.join(SERVE_PATH, IMAGESFLODER_NAME, fileSNameSplit[0], fileSNameSplit[1], fileSNameSplit[2], USERNAME)
        if not os.path.isdir(serveProject):
            self.myCreateFolder(serveProject)
        return serveProject

    #拷贝所有file节点的文件并改变节点
    def myCopyType_Files(self):
        type_file = 'sourceimages'
        serFileName = os.path.join(self.serveProject, type_file)
        allfiles = mc.ls(type='file')
        copyData = {}
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    texFirstFileName = mc.getAttr('%s.fileTextureName' % eachfile)
                except:
                    pass
                else:
                    if texFirstFileName.find('${OCTV_PROJECTS}') >= 0:
                        texFirstFileName = texFirstFileName.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                    elif texFirstFileName.find('z:') >= 0:
                        texFirstFileName = texFirstFileName.replace('z:', OCT_DRIVE)
                    elif texFirstFileName.find('Z:') >= 0:
                        texFirstFileName = texFirstFileName.replace('Z:', OCT_DRIVE)
                    if mc.getAttr('%s.useFrameExtension' % eachfile) == 0:
                        texFileNameGroup = [texFirstFileName]
                    else:
                        myTexDirName = os.path.dirname(texFirstFileName)
                        myTexBaseName = os.path.basename(texFirstFileName)
                        

                    texFileName = os.path.normpath(texFileName)
                    texFileNameS = texFileName.split('\\')
                    try:
                        indexType = texFileNameS.index(type_file)
                    except:
                        texFileNameBN = os.path.basename(texFileName)
                        serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
                        copyFinalTexFilePath = serFileName
                    else:
                        serLastTexFileName = '\\'.join(texFileNameS[indexType+1::])
                        serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
                        copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
                    serFinalTexFileName = os.path.normpath(serFinalTexFileName)
                    copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                    if texFileName != serFinalTexFileName:
                        #加入拷贝字典
                        #设置拷贝标帜
                        tmpCopyFlag = True
                        if os.path.isdir(serFileName):
                            if os.path.isfile(serFinalTexFileName):
                                testMtime = os.path.getmtime(texFileName)
                                tmpMtime = os.path.getmtime(serFinalTexFileName)
                                if int(tmpMtime) >= int(testMtime):
                                    tmpCopyFlag = False
                        if tmpCopyFlag:
                            copyData.update({texFileName: copyFinalTexFilePath})
                        #加入设置字典
                        setData.update({eachfile: serFinalTexFileName})
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 file 贴图!")
                #拷贝文件
                if not self.CopyDataJob(copyData):
                    return False
                #设置路径
                for key in setData.keys():
                    mc.setAttr(u'%s.fileTextureName' % key, setData[key], type='string')
        return True

    #拷贝所有data节点的文件并改变节点
    def myCopy_Data(self):
        type_file = 'data'
        other_file = 'otherCache'
        serFileName = os.path.join(self.serveProject, type_file)
        allfiles = mc.ls(type='cacheFile')
        copyData = {}
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    cachePath = mc.getAttr('%s.cachePath' % eachfile)
                except:
                    pass
                else:
                    if cachePath.find('${OCTV_PROJECTS}') >= 0:
                        cachePath = cachePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                    elif cachePath.find('z:') >= 0:
                        cachePath = cachePath.replace('z:', OCT_DRIVE)
                    elif cachePath.find('Z:') >= 0:
                        cachePath = cachePath.replace('Z:', OCT_DRIVE)
                    cachePath = os.path.normpath(cachePath)
                    cachePathS = cachePath.split('\\')
                    try:
                        indexType = cachePathS.index(type_file)
                    except:
                        copyFinalcachePath = os.path.join(serFileName, other_file)
                    else:
                        serLastcachePath = '\\'.join(cachePathS[indexType+1::])
                        copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
                    copyFinalcachePath = os.path.normpath(copyFinalcachePath)
                    if cachePath != copyFinalcachePath:
                        cacheName = mc.getAttr('%s.cacheName' % eachfile)
                        mylistDir = os.listdir(cachePath)
                        #标志网络路径是否存在
                        tmpPathFlag = os.path.isdir(copyFinalcachePath)
                        #拷贝列表
                        for everydir in mylistDir:
                            if everydir.find(cacheName) >= 0:
                                localFcacheFileName = os.path.join(cachePath, everydir)
                                if os.path.isfile(localFcacheFileName):
                                    if tmpPathFlag:
                                        copyFinalcacheName = os.path.join(copyFinalcachePath, everydir)
                                        copyFinalcacheName = os.path.normpath(copyFinalcachePath)
                                        if os.path.isfile(copyFinalcacheName):
                                            testMtime = os.path.getmtime(localFcacheFileName)
                                            tmpMtime = os.path.getmtime(copyFinalcacheName)
                                            if int(tmpMtime) >= int(testMtime):
                                                continue
                                    copyData.update({localFcacheFileName: copyFinalcachePath})
                        #设置列表
                        setData.update({eachfile: copyFinalcachePath})
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 caChe 缓存!")
                #拷贝文件
                if not self.CopyDataJob(copyData):
                    return False
                #设置路径
                for key in setData.keys():
                    print key
                    print setData[key]
                    mc.setAttr('%s.cachePath' % key, setData[key], type='string')
        return True

    #拷贝所有ABC的data节点的文件并改变节点
    def myCopy_AbcData(self):
        type_file = 'alembic'
        serFileName = os.path.join(self.serveProject, 'cache\\'+type_file)
        allfiles = mc.ls(type='AlembicNode')
        copyData = {}
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    abcCachePath = mc.getAttr('%s.abc_File' % eachfile)
                except:
                    pass
                else:
                    if abcCachePath.find('${OCTV_PROJECTS}') >= 0:
                        abcCachePath = abcCachePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                    elif abcCachePath.find('z:') >= 0:
                        abcCachePath = abcCachePath.replace('z:', OCT_DRIVE)
                    elif abcCachePath.find('Z:') >= 0:
                        abcCachePath = abcCachePath.replace('Z:', OCT_DRIVE)
                    abcCachePath = os.path.normpath(abcCachePath)
                    abcCachePath_S = abcCachePath.split('\\')
                    #多层目录
                    try:
                        indexType = abcCachePath_S.index(type_file)
                    except:
                        abcCachePathBN = os.path.basename(abcCachePath)
                        serFinalAbcCachePath = os.path.join(serFileName, abcCachePathBN)
                        copyFinalAbcCachePath = serFileName
                    else:
                        serLastAbcCachePath = '\\'.join(abcCachePath_S[indexType+1::])
                        copyFinalAbcCachePath = os.path.join(serFileName, serLastAbcCachePath)
                        copyFinalAbcCachePath_dir = os.path.dirname(copyFinalAbcCachePath)
                    copyFinalAbcCachePath = os.path.normpath(copyFinalAbcCachePath)
                    copyFinalAbcCachePath_dir = os.path.normpath(copyFinalAbcCachePath_dir)
                    if abcCachePath != copyFinalAbcCachePath:
                        #拷贝列表
                        #设置拷贝标帜
                        tmpCopyFlag = True
                        if os.path.isdir(serFileName):
                            if os.path.isfile(copyFinalAbcCachePath):
                                testMtime = os.path.getmtime(abcCachePath)
                                tmpMtime = os.path.getmtime(copyFinalAbcCachePath)
                                if int(tmpMtime) >= int(testMtime):
                                    tmpCopyFlag = False
                        if tmpCopyFlag:
                            copyData.update({abcCachePath: copyFinalAbcCachePath_dir})
                        #设置列表
                        setData.update({eachfile: copyFinalAbcCachePath})
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 Alembic caChe 缓存!")
                #拷贝文件
                if not self.CopyDataJob(copyData):
                    return False
                #设置路径
                for key in setData.keys():
                    mc.setAttr('%s.abc_File' % key, setData[key], type='string')
        return True

    #拷贝所有Shave缓存
    def myCopy_Shavedata(self):
        type_file = 'shave'
        serFileName = os.path.join(self.serveProject, 'cache\\'+type_file)
        copyData = {}
        setData = {}
        allOnlyShaveShapes = []
        allShaveShapes = mc.ls(type='shaveHair')
        for eachShape in allShaveShapes:
            allOnlyShaveShapes.append(eachShape.split("|")[-1])
        allShaveOnlyNames = []
        for OnlyShaveShape in allOnlyShaveShapes:
            allShaveOnlyNames.append("shaveStatFile_%s" % OnlyShaveShape)
        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        myshaveGlobals = "shaveGlobals"
        if allShaveShapes and myshaveGlobals:
            shavePath = mc.getAttr("%s.tmpDir" % myshaveGlobals)
            if shavePath:
                if shavePath.find('${OCTV_PROJECTS}') >= 0:
                    shavePath = shavePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                elif shavePath.find('z:') >= 0:
                    shavePath = shavePath.replace('z:', OCT_DRIVE)
                elif shavePath.find('Z:') >= 0:
                    shavePath = shavePath.replace('Z:', OCT_DRIVE)
                if os.path.isdir(shavePath):
                    allSahveDirs = os.listdir(shavePath)
                    if allSahveDirs:
                        #多层目录
                        shavePath = os.path.normpath(shavePath)
                        shaveCachePath_S = shavePath.split('\\')
                        try:
                            indexType = shaveCachePath_S.index(type_file)
                        except:
                            shaveCachePathBN = os.path.basename(shavePath)
                            serFinalShaveCachePath = os.path.join(serFileName, shaveCachePathBN)
                            copyFinalShaveCacheDir = serFileName
                        else:
                            serLastShaveCachePath = '\\'.join(shaveCachePath_S[indexType+1::])
                            copyFinalShaveCacheDir = os.path.join(serFileName, serLastShaveCachePath)
                        copyFinalShaveCacheDir = os.path.normpath(copyFinalShaveCacheDir)
                        #判断文件是否有跟新，有更新就替代
                        tmpCopyFlag = True
                        #判断这个目录网络路径是否存在
                        if os.path.isdir(copyFinalShaveCacheDir):
                            tmpCopyFlag = True
                        for eachDir in allSahveDirs:
                            tmpName = eachDir.split(".")[0]
                            if tmpName in allShaveOnlyNames:
                                eachFullPath = os.path.join(shavePath, eachDir)
                                eachFullPath = os.path.normpath(eachFullPath)
                                copyFinalShaveCachePath = os.path.join(copyFinalShaveCacheDir, eachDir)
                                copyFinalShaveCachePath = os.path.normpath(copyFinalShaveCachePath)
                                if eachFullPath != copyFinalShaveCachePath:
                                    if tmpCopyFlag:
                                        if os.path.isfile(copyFinalShaveCachePath):
                                            testMtime = os.path.getmtime(eachFullPath)
                                            tmpMtime = os.path.getmtime(copyFinalShaveCachePath)
                                            if int(tmpMtime) >= int(testMtime):
                                                tmpCopyFlag = False
                                    if tmpCopyFlag:
                                        copyData.update({eachFullPath: copyFinalShaveCacheDir})
                                    #设置列表
                        setData.update({myshaveGlobals: copyFinalShaveCacheDir})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 Shave caChe 缓存!")
                    #拷贝文件
                    if not self.CopyDataJob(copyData):
                        return False
                    #设置路径
                    for key in setData.keys():
                        mc.setAttr('%s.tmpDir' % key, setData[key], type='string')
        return True
       


    #拷贝粒子缓存
    def myCopy_Particles(self):
        type_file = 'particles'
        serFileName = os.path.join(self.serveProject, type_file)
        mydynGlobals = mc.dynGlobals(q=True, a=True)
        myAllParticles = mc.ls(type='particle')
        copyData = {}
        if mydynGlobals and myAllParticles:
            if mc.getAttr('%s.useParticleDiskCache' % mydynGlobals):
                parPath = mc.workspace(en='particles')
                cacheDirectory = mc.getAttr('%s.cacheDirectory' % mydynGlobals)
                parCachePath = os.path.join(parPath, cacheDirectory)
                parCacheSPath = os.path.join(parPath, cacheDirectory+'_startup')
                fileShortName = os.path.splitext(self.fileSName)[0]
                if os.path.isdir(parCachePath):
                    allParDirs = os.listdir(parCachePath)
                    if cacheDirectory != 'untitled':
                        serFinalPerPath = os.path.join(serFileName, cacheDirectory)
                    else:
                        serFinalPerPath = os.path.join(serFileName, fileShortName+'_'+cacheDirectory)
                    serFinalPerPath = os.path.normpath(serFinalPerPath)
                    #网络盘存在标帜
                    tmpSerPathFlag = os.path.isdir(serFinalPerPath)
                    for dirEach in allParDirs:
                        for parEach in myAllParticles:
                            parFinlName = parEach.replace(':', '_')
                            if dirEach.find(parFinlName) >= 0:
                                copyFinalPerName = os.path.join(parCachePath, dirEach)
                                copyFinalPerName = os.path.normpath(copyFinalPerName)
                                if tmpSerPathFlag:
                                    tmpSerFileName = os.path.join(serFinalPerPath, dirEach)
                                    if os.path.isfile(tmpSerFileName):
                                        testMtime = os.path.getmtime(copyFinalPerName)
                                        tmpMtime = os.path.getmtime(tmpSerFileName)
                                        if int(tmpMtime) >= int(testMtime):
                                            tmpCopyFlag = False
                                if tmpCopyFlag:
                                    copyData.update({copyFinalPerName: serFinalPerPath})
                if os.path.isdir(parCacheSPath):
                    allParSDirs = os.listdir(parCacheSPath)
                    if cacheDirectory != 'untitled':
                        serFinalPerSPath = os.path.join(serFileName, cacheDirectory+'_startup')
                    else:
                        serFinalPerSPath = os.path.join(serFileName, fileShortName+'_'+cacheDirectory+'_startup')
                    serFinalPerSPath = os.path.normpath(serFinalPerSPath)
                    #网络盘存在标帜
                    tmpSerSPathFlag = os.path.isdir(serFinalPerSPath)
                    for dirSEach in allParSDirs:
                        for parSEach in myAllParticles:
                            parFinlSName = parSEach.replace(':', '_')
                            if dirSEach.find(parFinlSName) >= 0:
                                copyFinalPerSName = os.path.join(parCacheSPath, dirSEach)
                                copyFinalPerSName = os.path.normpath(copyFinalPerSName)
                                if tmpSerSPathFlag:
                                    tmpSerFileName = os.path.join(serFinalPerSPath, dirEach)
                                    if os.path.isfile(tmpSerFileName):
                                        testMtime = os.path.getmtime(copyFinalPerName)
                                        tmpMtime = os.path.getmtime(tmpSerFileName)
                                        if int(tmpMtime) >= int(testMtime):
                                            tmpCopyFlag = False
                                if tmpCopyFlag:
                                    copyData.update({copyFinalPerSName: serFinalPerSPath})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 particle缓存!")
                    #拷贝文件
                    if not self.CopyDataJob(copyData):
                        return False
                #设置粒子缓存的新文件名
                if cacheDirectory == 'untitled':
                    parCacheNName = fileShortName+'_'+cacheDirectory
                    mc.setAttr('%s.cacheDirectory' % mydynGlobals, parCacheNName, type='string')
        return True

    #拷贝Vray、Arnold代理、某些贴图节点的文件
    def myCopy_Proxy_OImagesModel(self, myType, mtAttr):
        try:
            allTypeShapes = mc.ls(type=myType)
        except:
            pass
        else:
            if allTypeShapes:
                copyData = {}
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
                            if myFilepath.find('${OCTV_PROJECTS}') >= 0:
                                myFilepath = myFilepath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                            elif myFilepath.find('z:') >= 0:
                                myFilepath = myFilepath.replace('z:', OCT_DRIVE)
                            elif myFilepath.find('Z:') >= 0:
                                myFilepath = myFilepath.replace('Z:', OCT_DRIVE)
                            #获取文件名
                            if os.path.isfile(myFilepath):
                                myFileBaseName = os.path.basename(myFilepath)
                                #最终网络文件名
                                myFinalName = os.path.join(serFileName, myFileBaseName)
                                myFinalName = os.path.normpath(myFinalName)
                                #原始的文件地址
                                myFilepath = os.path.normpath(myFilepath)
                                #服务器地址
                                serFileName = os.path.normpath(serFileName)
                                if myFilepath != myFinalName:
                                    #加入拷贝文件
                                   #设置拷贝标帜
                                    tmpCopyFlag = True
                                    if os.path.isdir(serFileName):
                                        if os.path.isfile(myFinalName):
                                            testMtime = os.path.getmtime(myFilepath)
                                            tmpMtime = os.path.getmtime(myFinalName)
                                            if int(tmpMtime) >= int(testMtime):
                                                tmpCopyFlag = False
                                    if tmpCopyFlag:
                                        copyData.update({myFilepath: serFileName})
                                    #加入设置字典
                                    setData.update({shapeEach: myFinalName})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 %s 文件!" % myType)
                    #拷贝文件
                    if not self.CopyDataJob(copyData):
                        return False
                    for key in setData.keys():
                        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
        return True

    #拷贝Vr光子贴图、焦散贴图
    def myCopy_VrSetFilesModel(self, typeOn, typeModel, typeFuleAttr, numModel):
        copyData = {}
        typeName = ''
        type_file = 'sourceimages'
        serFileName = os.path.join(self.serveProject, type_file)
        try:
            if mc.getAttr("vraySettings.%s" % typeOn):
                if mc.getAttr('vraySettings.%s' % typeModel) == numModel:
                    localFile = mc.getAttr('vraySettings.%s' % typeFuleAttr)
                    if localFile:
                        if localFile.find('${OCTV_PROJECTS}') >= 0:
                            localFile = localFile.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                        elif localFile.find('z:') >= 0:
                            localFile = localFile.replace('z:', OCT_DRIVE)
                        elif localFile.find('Z:') >= 0:
                            localFile = localFile.replace('Z:', OCT_DRIVE)
                        locaFileBaseName = os.path.basename(localFile)
                        serFileFinalName = os.path.join(serFileName, locaFileBaseName)
                        serFileFinalName = os.path.normpath(serFileFinalName)
                        serFileName = os.path.normpath(serFileName)
                        localFile = os.path.normpath(localFile)
                        if os.path.isfile(localFile):
                            if localFile != serFileFinalName:
                                #设置拷贝标帜
                                tmpCopyFlag = True
                                if os.path.isdir(serFileName):
                                    if os.path.isfile(serFileFinalName):
                                        testMtime = os.path.getmtime(localFile)
                                        tmpMtime = os.path.getmtime(serFileFinalName)
                                        if int(tmpMtime) >= int(testMtime):
                                            tmpCopyFlag = False
                                if tmpCopyFlag:
                                    copyData.update({localFile: serFileName})
                                if typeModel == 'imap_mode':
                                    typeName = u'Irradiance map光子贴图'
                                elif typeModel == 'imap_mode':
                                    typeName = u'Light cache map光子贴图'
                                else:
                                    typeName = u'Caustics的焦散贴图'
                                if copyData:
                                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的Vray的 %s!" % typeName)
                                    if not self.CopyDataJob(copyData):
                                        return False
                                mc.setAttr('vraySettings.%s' % typeFuleAttr, serFileFinalName, type='string')
        except:
            pass
        return True

    def myCopy_Mr(self):
        #拷贝mentalrayIblShape节点的贴图
        mrIbType = 'mentalrayIblShape'
        mrIbAttr = 'texture'
        if not self.myCopy_Proxy_OImagesModel(mrIbType, mrIbAttr):
            return False
        #拷贝mentalrayTexture节点的贴图
        mrTxType = 'mentalrayTexture'
        mrTxAttr = 'fileTextureName'
        if not self.myCopy_Proxy_OImagesModel(mrTxType, mrTxAttr):
            return False
        return True

    def myCopy_Vr(self):
        #拷贝Vray的代理
        VrType = 'VRayMesh'
        VrAttr = 'fileName'
        if not self.myCopy_Proxy_OImagesModel(VrType, VrAttr):
            return False
        #检查Vray的VRayLightIESShape灯光贴图
        VrIesLType = 'VRayLightIESShape'
        VrIesLAttr = 'iesFile'
        if not self.myCopy_Proxy_OImagesModel(VrIesLType, VrIesLAttr):
            return False
        #Irradiance map光子贴图
        IrrMap_typeOn = 'giOn'
        IrrMap_typeModel = 'imap_mode'
        IrrMap_typeFuleAttr = 'imap_fileName'
        IrrMap_numModel = 2
        if not self.myCopy_VrSetFilesModel(IrrMap_typeOn, IrrMap_typeModel, IrrMap_typeFuleAttr, IrrMap_numModel):
            return False
        #Light cache map光子贴图
        LightC_typeOn = 'giOn'
        LightC_typeModel = 'mode'
        LightC_typeFuleAttr = 'fileName'
        LightC_numModel = 2
        if not self.myCopy_VrSetFilesModel(LightC_typeOn, LightC_typeModel, LightC_typeFuleAttr, LightC_numModel):
            return False
        #Caustics的焦散贴图
        Caustics_typeOn = 'causticsOn'
        Caustics_typeModel = 'causticsMode'
        Caustics_typeFuleAttr = 'causticsFile'
        Caustics_numModel = 1
        if not self.myCopy_VrSetFilesModel(Caustics_typeOn, Caustics_typeModel, Caustics_typeFuleAttr, Caustics_numModel):
            return False
        return True

    def myCopy_Ar(self):
        #拷贝Arnold代理
        ArType = 'aiStandIn'
        ArAttr = 'dso'
        if not self.myCopy_Proxy_OImagesModel(ArType, ArAttr):
            return False
        #拷贝Arnold的aiPhotometricLight灯光贴图
        ###################
        #改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
        ####################
        ArIesLType = 'aiPhotometricLight'
        ArIesLAttr = 'aiFilename'
        if not self.myCopy_Proxy_OImagesModel(ArIesLType, ArIesLAttr):
            return False
        return True

    #拷贝mrIb贴图、mrTex节点的贴图路径、摄像机投影贴图、检查Vray的VRayLightIESShape灯光贴图
    def myCopy_OtherImages(self):
        #检查摄像机投影贴图
        camImType = 'imagePlane'
        camImAttr = 'imageName'
        if not self.myCopy_Proxy_OImagesModel(camImType, camImAttr):
            return False
        return True

    #拷贝Realflow缓存的模块
    def myCopy_rfCacheModel(self, myType, mtAttr):
        try:
            allRfNodes = mc.ls(type=myType)
        except:
            pass
        else:
            copyData = {}
            setData = {}
            type_file = 'cache'
            type_data = 'realflowCache'
            serFileName = os.path.join(self.serveProject, type_file, type_data)
            if allRfNodes:
                for RfNode in allRfNodes:
                    myFileFullpath = mc.getAttr('%s.%s' % (RfNode, mtAttr))
                    if myFileFullpath:
                        if myFileFullpath.find('${OCTV_PROJECTS}') >= 0:
                            myFileFullpath = myFileFullpath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                        elif myFileFullpath.find('z:') >= 0:
                            myFileFullpath = myFileFullpath.replace('z:', OCT_DRIVE)
                        elif myFileFullpath.find('Z:') >= 0:
                            myFileFullpath = myFileFullpath.replace('Z:', OCT_DRIVE)
                        if myType == 'RealflowEmitter':
                            rfbaseName = 'particles'
                            myFilepath = myFileFullpath
                            myFilePreName = mc.getAttr('%s.Prefixes[0]' % RfNode)
                            myFinalName = os.path.join(serFileName, rfbaseName)
                            myFinalSName = myFinalName
                        else:
                            rfbaseName = 'meshes'
                            myFilepath = os.path.dirname(myFileFullpath)
                            myFileBasePath = os.path.basename(myFileFullpath)
                            FramePadding = mc.getAttr('%s.framePadding' % RfNode)
                            myFileBasePathText = os.path.splitext(myFileBasePath)[0]
                            myFilePreName = myFileBasePathText[:-FramePadding]
                            myFinalName = os.path.join(serFileName, rfbaseName)
                            myFinalSName = os.path.join(myFinalName, myFileBasePath)
                        #获取文件名
                        myFinalName = os.path.normpath(myFinalName)
                        myFinalSName = os.path.normpath(myFinalSName)
                        myFilepath = os.path.normpath(myFilepath)
                        #网络盘存在标帜
                        tmpSerPathFlag = os.path.isdir(myFinalName)
                        if os.path.isdir(myFilepath):
                            if myFilepath != myFinalName:
                                allDirs = os.listdir(myFilepath)
                                for dirEach in allDirs:
                                    if dirEach.find(myFilePreName) >= 0:
                                        copyFinalPerName = os.path.join(myFilepath, dirEach)
                                        copyFinalPerName = os.path.normpath(copyFinalPerName)
                                        if tmpSerPathFlag:
                                            tmpSerFileName = os.path.join(myFinalName, dirEach)
                                            if os.path.isfile(tmpSerFileName):
                                                testMtime = os.path.getmtime(copyFinalPerName)
                                                tmpMtime = os.path.getmtime(tmpSerFileName)
                                                if int(tmpMtime) >= int(testMtime):
                                                    tmpCopyFlag = False
                                        if tmpCopyFlag:
                                            copyData.update({copyFinalPerName: myFinalName})
                                setData.update({RfNode: myFinalSName})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 %s 文件!" % myType)
                    #拷贝文件
                    if not self.CopyDataJob(copyData):
                        return False
                    for key in setData.keys():
                        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
        return True

    #拷贝Realflow的particles粒子和Meshs缓存
    def myCopy_rfCache(self):
        #拷贝particles缓存
        rfParType = 'RealflowEmitter'
        rfParAttr = 'Paths[0]'
        if not self.myCopy_rfCacheModel(rfParType, rfParAttr):
            return False
        #拷贝meshs缓存
        rfMeshType = 'RealflowMesh'
        rfMeshAttr = 'Path'
        if not self.myCopy_rfCacheModel(rfMeshType, rfMeshAttr):
            return False
        return True

    #保存文件
    def mySaveFile(self):
        try:
            mc.deleteUI("hyperShadePanel1Window")
        except:
            pass
        mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
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
        mc.modelEditor(myactivePlane, e=True, da='boundingBox')
        driveFlag = False
        myDrives = ['D:', 'E:', 'C:']
        type_file = 'scenes'
        myFileFullpath = mc.file(q=True, sn=True)
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
            locaoFileName = os.path.join(localTempPath, self.fileSName)
            myTyprName = 'mayaBinary'
            if self.fileSName.find('mb') >= 0:
                myTyprName = 'mayaBinary'
            else:
                myTyprName = 'mayaAscii'
            serFileName = os.path.join(self.serveProject, type_file)
            fileserName = os.path.join(serFileName, self.fileSName)
            if not self.worker1.myLocalFlag:
                mc.file(rename=locaoFileName)
                mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
                time.sleep(1)
                copyData = {locaoFileName: serFileName}
                self.CopyDataJob(copyData)
                # myProjectAddress = self.serveProject.replace('\\', '/')
                # mm.eval('setProject "%s"' % myProjectAddress)
                os.remove(locaoFileName)
            else:
                mc.file(rename=fileserName)
                mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
                time.sleep(1)
            return fileserName
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'本地盘符不够空间来临时存储文件！\n请清理空间', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

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

    def writeInfo(self):
        # 输出job_info文件：
        #       Plugin
        #       Name
        #       Frames
        #       OutputDirectory0
        #       如果界面的Frames里为空的话，这里的Frames会读取渲染设置
        # 输出plugin_info文件：
        #       SceneFile
        #       Renderer
        #       UsingRenderLayers
        #       RenderLayer
        #       ImageWidth
        #       ImageHeight
        #       AspectRatio
        #       ProjectPath
        #       OutputFilePath
        #       OutputFilePrefix
        #       如果没有渲染层的话，Renderer设为File， UsingRenderLayers/RenderLayer/ImageWidth/ImageHeight/AspectRatio可以不写
        layers = mc.ls(exactType='renderLayer')
        pattern = re.compile('^defaultRenderLayer')
        for eachLayer in layers:
            if pattern.match(eachLayer):
                if not eachLayer == 'defaultRenderLayer':
                    try:
                        mc.select(eachLayer, r=True)
                        mc.lockNode(l=False)
                        mc.delete(eachLayer)
                    except:
                        self.stateMsg += u'注意,%s节点无法删除.\n'
                        om.MGlobal.displayWarning(u'注意,%s节点无法删除.\n')
        del pattern

        imgFormat = {23:'avi', 11:'cin', 35:'dds', 9:'eps', 0:'gif', 8:'jpg', 7:'iff', 10:'iff', 31:'psd', 36:'psd', 32:'png', 12:'yuv', 2:'rla', 5:'sgi', 13:'sgi', 1:'pic', 19:'tga', 3:'tif', 4:'tif', 20:'bmp', \
                     2:'rla', 5:'rgb', 51:'tif', 6:'als'}
        getTempFolderScriptFile = r'\\192.168.5.38\td\APP\RenderFarm\getDeadlineTemp.py'
        p = os.popen(r'deadlinecommand -executescript %s' % getTempFolderScriptFile, 'r')
        tempFolder = p.read()
        p.close()
        del p
        tempFolder = tempFolder[:-1]
        key = ['Version', 'Build', 'Name', 'StartFrames', 'EndFrames', 'FrameStep', 'OutputDirectories0', 'SceneFile', 'Renderer', 'RenderLayer', 'ImageWidth',
               'ImageHeight', 'AspectRatio', 'ProjectPath', 'OutputFilePath', 'OutputFilePrefix', 'RenderableLayers']

        renderGlobal = mc.ls(et='renderGlobals')
        resolution = mc.ls(et='resolution')
        if len(renderGlobal) > 1:
            self.stateMsg += u'有多于一个RenderGlobals节点,请检查场景删除多余的节点.\n'
            om.MGlobal.displayError(u'有多于一个RenderGlobals节点,请检查场景删除多余的节点.\n')
            return

        if not len(resolution) == 1 and len(resolution) > 0:
            self.stateMsg += u'有多于一个Resolution节点,请检查场景删除多余的节点.\n'
            om.MGlobal.displayError(u'有多于一个Resolution节点,请检查场景删除多余的节点.\n')
            return

        #filePrefixName = mc.getAttr('%s.imageFilePrefix' % renderGlobal[0])
        fileNameWithExt = mc.file(q=True, sn=True, shn=True)
        fileName = [os.path.splitext(fileNameWithExt)[0]]
        hostFile = ['%s\\scenes\\%s' % (self.serveProject, fileNameWithExt)]
        outputDir = [self.serveImages]
        projPath = [self.serveProject]
        version = [mc.about(version=True)]
        build = ['32bit']
        allCam = mc.ls(et='camera')

        if mc.about(is64=True):
            build[0] = '64bit'

        allLayer = []
        renderable = []

        currentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
        if len(layers):
            for eachLayer in layers:
                if 'defaultRenderLayer' == eachLayer:
                    mc.editRenderLayerGlobals(currentRenderLayer=eachLayer)
                    #continue
                allLayer.append(eachLayer)

        renCam = []
        renderer = []
        filePrefix = []
        # resolveName = []
        format = []
        startFrame = []
        endFrame = []
        frameStep = []
        width = []
        height = []
        ratio = []

        if len(allLayer):
            for eachLayer in allLayer:
                mc.editRenderLayerGlobals(currentRenderLayer=eachLayer)

                if mc.getAttr('%s.renderable' % eachLayer):
                    renderable.append(eachLayer)

                for eachCam in allCam:
                    if mc.getAttr('%s.renderable' % eachCam):
                        renCam.append(eachCam)

                if not len(renCam):
                    #om.MGlobal.displayError(u'%s渲染层没有渲染摄像机,终止操作.' % eachLayer)
                    pass
                currentRenderName = mc.getAttr('%s.currentRenderer' % renderGlobal[0])
                renderer.append(currentRenderName.capitalize())
                if currentRenderName.find('vray') >= 0:
                    prefix = mc.getAttr('vraySettings.fileNamePrefix')
                    frameStep.append(int(mc.getAttr('vraySettings.fileNamePadding')))
                else:
                    prefix = mc.getAttr('%s.imageFilePrefix' % renderGlobal[0])
                    frameStep.append(int(mc.getAttr('defaultRenderGlobals.byFrameStep')))
                filePrefix.append(prefix)
                # prefix = prefix.replace(u'<Scene>', fileName[0])
                # prefix = prefix.replace(u'<RenderLayer>', eachLayer)
                # prefix = prefix.replace(u'<Camera>', renCam[0])
                # resolveName.append(prefix)

                formatIndex = mc.getAttr('%s.imageFormat' % renderGlobal[0])
                format.append(imgFormat[formatIndex])
                startFrame.append(int(mc.getAttr('%s.startFrame' % renderGlobal[0])))
                endFrame.append(int(mc.getAttr('%s.endFrame' % renderGlobal[0])))
                width.append(mc.getAttr('%s.width' % resolution[0]))
                height.append(mc.getAttr('%s.height' % resolution[0]))
                ratio.append(mc.getAttr('%s.deviceAspectRatio' % resolution[0]))

        all = []
        all.append(version)
        all.append(build)
        all.append(fileName)
        all.append(startFrame)
        all.append(endFrame)
        all.append(frameStep)
        all.append(outputDir)
        all.append(hostFile)
        all.append(renderer)
        all.append(allLayer)
        all.append(width)
        all.append(height)
        all.append(ratio)
        all.append(projPath)
        all.append(outputDir)
        all.append(filePrefix)
        all.append(renderable)

        mc.editRenderLayerGlobals(currentRenderLayer=currentLayer)

        writeStr = ''
        for i in range(len(key)):
            writeStr += '[%s]\n' % key[i]
            for eachItem in all[i]:
                writeStr += '%s\n' % eachItem
            writeStr += '[/%s]\n\n' % key[i]

        fPath = os.path.join(tempFolder, 'fileSettings.cfg')
        f = file(fPath, 'w')
        try:
            f.writelines(writeStr)
        except:
            self.stateMsg += u'%s写入信息时出错,终止操作.\n' % fPath
            om.MGlobal.displayError(u'%s写入信息时出错,终止操作.\n' % fPath)
        else:
            f.close()
            self.stateMsg += u'成功写入信息文件.\n'
            om.MGlobal.displayInfo(u'成功写入信息文件.\n')
        del all[:]
        del fileName[:]
        del startFrame[:]
        del endFrame[:]
        del outputDir[:]
        del hostFile[:]
        del renderer[:]
        del allLayer[:]
        del width[:]
        del height[:]
        del ratio[:]
        del projPath[:]
        del filePrefix[:]
        del renderable[:]
        del writeStr

    def executeScript(self):
        try:
            str = os.popen(r'"deadlinecommand.exe" -ExecuteScript \\octvision.com\cg\td\APP\RenderFarm\MayaSubmission.py').read()
        except:
            pass
        else:
            sys.stdout.write(str)

    def changeMrLayer(self):
        if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
            if not mc.getAttr('defaultRenderGlobals.currentRenderer') == 'mentalRay':
                allLayers = mc.listConnections('renderLayerManager.renderLayerId')
                if allLayers:
                    for Layer in allLayers:
                        if mc.getAttr('%s.renderable' % Layer):
                            mc.editRenderLayerGlobals(currentRenderLayer=Layer)
                            if mc.getAttr('defaultRenderGlobals.currentRenderer') == 'mentalRay':
                                break

    def main(self, copeType):
        '''
        copyType分三种模式
        1 单纯拷贝模式
        2 拷贝提交模式
        3 单纯提交模式
        '''
        if mc.file(q=True, reference=True):
            om.MGlobal.displayInfo(u'文件含有参考，请导入后再继续！\n')
            mc.confirmDialog(title=u'温馨提示：', message=u'文件含有参考，请导入后再继续！', button=['OK'], defaultButton='Yes', dismissString='No')
            return False
        self.copyType = copeType
        #创建素材输入文件夹
        if copeType == 1 or copeType == 3:
            self.serveImages = self.myCreateImagesFolder()
        #当模式为1和2时工程目录，3时为读取当前工程目录
        if copeType == 1 or copeType == 2:
            self.serveProject = self.myCreateScenes()
        elif copeType == 3:
            self.serveProject = mc.workspace(q=True, rd=True)
            myFileFullName = mc.file(q=True, sn=True)

        #运行主程序
        if self.serveProject:
            mc.progressWindow(title=u'提交文件', status=u'即将开始', isInterruptable=True)
            if copeType == 1 or copeType == 2:
                i = 0
                j = 1
                k = 9
                mrFlag = False
                vrFlag = False
                arFlag = False
                if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                    mrFlag = True
                    i += 1
                if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
                    vrFlag = True
                    i += 1
                if mc.pluginInfo('mtoa.mll', query=True, loaded=True):
                    arFlag = True
                    i += 1
                k = k + i
                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 file 贴图文件' % (k, j))
                if self.myCopyType_Files():
                    j += 1
                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 cacheFile 缓存文件' % (k, j))
                    if self.myCopy_Data():
                        j += 1
                        mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Alembic cacheFile 缓存文件' % (k, j))
                        if self.myCopy_AbcData():
                            j += 1
                            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Shave cacheFile 缓存文件' % (k, j))
                            if self.myCopy_Shavedata():
                                j += 1
                                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 particle 缓存文件' % (k, j))
                                if self.myCopy_Particles():
                                    j += 1
                                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Realflow 缓存' % (k, j))
                                    if self.myCopy_rfCache():
                                        j += 1
                                        mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传摄像机投影贴图' % (k, j))
                                        if self.myCopy_OtherImages():
                                            if mrFlag:
                                                j += 1
                                                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Mr渲染器的相关文件' % (k, j))
                                                if not self.myCopy_Mr():
                                                    mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                    mc.progressWindow(endProgress=True)
                                                    return False
                                            if vrFlag:
                                                j += 1
                                                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Vr渲染器的相关文件' % (k, j))
                                                if not self.myCopy_Vr():
                                                    mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                    mc.progressWindow(endProgress=True)
                                                    return False
                                            if arFlag:
                                                j += 1
                                                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Ar渲染器的相关文件' % (k, j))
                                                if not self.myCopy_Ar():
                                                    mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                    mc.progressWindow(endProgress=True)
                                                    return False
                                            j += 1
                                            mc.progressWindow(edit=True, progress=1, min=0, max=1, status=u"正在保存文件!", title=u'共%s步, 第 %s 步,正在保存文件' % (k, j))
                                            self.delDefaultRenderLayer()
                                            myFileFullName = self.mySaveFile()
                                            if myFileFullName:
                                                mm.eval('autoUpdateAttrEd;')
                                                om.MGlobal.displayWarning(u'\n文件上传成功！')
                                                j += 1
                                                mc.progressWindow(edit=True, status=u'上传完毕!', title=u'共%s步, 第 %s 步,上传完毕！' % (k, j))
            if copeType == 1 or copeType == 3:
                if copeType == 3:
                    self.delDefaultRenderLayer()
                self.changeMrLayer()
                myfileBaseName = os.path.splitext(self.fileSName)[0]
                mm.eval(r'global string $myFileName = "%s"' % myfileBaseName)
                mm.eval(r'global string $myDeadlineImagesPath = "%s"' % self.serveImages.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineSceneFile = "%s"' % myFileFullName.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineProjectPath= "%s"' % self.serveProject.replace('\\', '/'))
                mm.eval('source "SubmitMayaToDeadline_zwz";')
                mm.eval('SubmitMayaToDeadline_zwz')
                if mc.radioButtonGrp('AutoSubmit', q=True, sl=True) == 1:
                    mm.eval('evalDeferred "SetupSubmission()"')
                # self.writeInfo()
                # self.executeScript()
            mc.progressWindow(endProgress=True)
            return True
