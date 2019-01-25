#!/usr/bin/env python
# coding=utf-8

from PyQt4 import QtGui, QtCore
import sip
import os
import subprocess
import time
import sys
import re
import maya.OpenMayaUI as ui
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om


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

serProjectName = mm.eval('getenv "OCTV_PROJECTS"')
fileLongName = mc.file(q=True, sn=True, shn=True)
if fileLongName:
    fileSN = fileLongName.split('_')
    while '' in fileSN:
        fileSN.remove('')
    if len(fileSN) >= 3:
        #判断服务器是否存在该工程
        serFilePath = os.path.join(serProjectName, fileSN[0], r'Project\scenes\animation', fileSN[1], fileSN[2])
        if not os.path.isdir(serFilePath):
            mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
            pass
    else:
        mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
        pass
else:
    mc.confirmDialog(title=u'警告', message=u'文件名为空！', button=['OK'], defaultButton='Yes', dismissString='No')
    pass

#检查贴图路径
noTexFiles = []
ErrorTexPaths = []
allTexFiles = mc.ls(type='file')
if allTexFiles:
    for texFile in allTexFiles:
        try:
            texFileName = mc.getAttr('%s.fileTextureName' % texFile)
        except:
            pass
        else:
            if texFileName.find('${OCTV_PROJECTS}') >= 0:
                texFileName = texFileName.replace('${OCTV_PROJECTS}', serProjectName)
            if not os.path.isfile(texFileName):
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
            if cachePath.find('${OCTV_PROJECTS}') >= 0:
                cachePath = cachePath.replace('${OCTV_PROJECTS}', serProjectName)
            if not os.path.isdir(cachePath):
                noCacheFiles.append(mycacheFile)
outPutSets(noCacheFiles, 'sortNo_CacheFiles_sets')

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

#检查代理文件/货路径是否存在的模板
def myCheck_ProxyModel(myType, mtAttr, fileType, NoTypeSets):
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
                    if myFileName.find('${OCTV_PROJECTS}') >= 0:
                        myFileName = myFileName.replace('${OCTV_PROJECTS}', serProjectName)
                    if fileType == 'file':
                        if not os.path.isfile(myFileName):
                            noFiles.append(fileeach)
                    else:
                        if not os.path.isdir(myFileName):
                            noFiles.append(fileeach)
    outPutSets(noFiles, NoTypeSets)
    return noFiles

#检查Vray的代理
VrType = 'VRayMesh'
VrAttr = 'fileName'
VrSets = 'sortNo_VRayMesh_set'
VrFileType = 'file'
noVRayMeshFiles = myCheck_ProxyModel(VrType, VrAttr, VrFileType, VrSets)
#检查Arnold的代理
ArType = 'aiStandIn'
ArAttr = 'dso'
ArSets = 'sortNo_AiStandIn_set'
ArFileType = 'file'
noAiStandInhFiles = myCheck_ProxyModel(ArType, ArAttr, ArFileType, ArSets)
#检查mentalrayIblShape节点的贴图
mrIblType = 'mentalrayIblShape'
mrIblAttr = 'texture'
mrIblFileType = 'file'
mrIblSets = 'sortNo_mentalrayIblShape_set'
noMrIblFiles = myCheck_ProxyModel(mrIblType, mrIblAttr, mrIblFileType, mrIblSets)
#检查mentalrayTexture节点的贴图
mrTxType = 'mentalrayTexture'
mrTxAttr = 'fileTextureName'
mrTxFileType = 'file'
mrTxSets = 'sortNo_mentalrayTexture_set'
noMrTxFiles = myCheck_ProxyModel(mrTxType, mrTxAttr, mrTxFileType, mrTxSets)
#检查摄像机投影贴图
camImType = 'imagePlane'
camImAttr = 'imageName'
camImFileType = 'file'
camImSets = 'sortNo_imagePlan_set'
nocamImFiles = myCheck_ProxyModel(camImType, camImAttr, camImFileType, camImSets)
#检查Vray的VRayLightIESShape灯光贴图
VrIesLType = 'VRayLightIESShape'
VrIesLAttr = 'iesFile'
VrIesLFileType = 'file'
VrIesLSets = 'sortNo_VRayLightIESShape_set'
noVrIesLFiles = myCheck_ProxyModel(VrIesLType, VrIesLAttr, VrIesLFileType, VrIesLSets)
#检查Arnold的aiPhotometricLight灯光贴图
###################
#改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
####################
ArIesLType = 'aiPhotometricLight'
ArIesLAttr = 'aiFilename'
ArIesLFileType = 'file'
ArIesLSets = 'sortNo_aiPhotometricLight_set'
ArIesLFiles = myCheck_ProxyModel(ArIesLType, ArIesLAttr, ArIesLFileType, ArIesLSets)
