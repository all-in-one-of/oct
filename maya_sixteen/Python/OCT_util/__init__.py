#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import sys,os,math,random
# import pu
import maya.utils
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
#不能互相导入（交流导入）
#from Python import OCT_lgt

'''
def ui() :
    if mc.window('PUploader', exists=True):
        mc.deleteUI('PUploader', window=True)

    if mc.windowPref('PUploader', exists=True):
        mc.windowPref('PUploader', remove=True)

    mc.window('PUploader', wh=[216, 419], sizeable=False)

    mc.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=200, adj=False)
    mc.text(label='Project Uploader v1.0')
    mc.text(l=u'上传前请确保所有素材文件')
    mc.text(l=u'都在本地的工程目录中')
    mc.optionMenu('srvList', label='FTP Server')
    mc.menuItem(label='-=Server List=-')
    mc.menuItem(label='Animation')
    mc.menuItem(label='Modeling')
    mc.menuItem(label='VFX')
    mc.menuItem(label='Composition')
    mc.optionMenu('srvList', e=True, sl=3)
    mc.optionMenu('srvList', e=True, en=False)
    mc.checkBox('img', v=True, l="SourceImages")
    mc.checkBox('par', v=True, l="Particle Caches")
    mc.checkBox('nPar', v=True, l="nParticle Caches")
    mc.checkBox('nClo', v=True, l="nCloth Caches")
    mc.checkBox('geo', v=True, l="Geometry Caches")
    mc.checkBox('flu', v=True, l="Fluid Caches")
    mc.checkBox('ibl', v=True, l="MentalRay IBL")
    mc.text(label='Description')
    mc.scrollField('descSF', editable=True, wordWrap=True, h=40)
    mc.checkBox('src', v=False, l="Only source files", onc='mc.scrollField("descSF",e=True,editable=False)', ofc='mc.scrollField("descSF",e=True,editable=True)')
    mc.button('btn', l='Upload Selected', command='OCT_util.submit()')
    mc.setFocus('btn')
    mc.showWindow('PUploader')

def submit():
    OCT_lgt.llCleanUp()

    serverIndex = mc.optionMenu('srvList', q=True, sl=True)
    src = mc.checkBox('src', q=True, v=True)
    if serverIndex == 1:
        mc.confirmDialog(title='Error', message='Please selected one Ftp Server', button=['OK'], defaultButton='OK')
        return

    if serverIndex == 2:
        host = '192.168.80.223'
        port = 21
        user = 'ftp01'
        password = 'ivancheung7'
    elif serverIndex == 3:
        host = '192.168.80.218'
        port = 21
        user = 'ftp01'
        password = 'fTpadMin01'
    elif serverIndex == 4:
        host = '192.168.80.223'
        port = 21
        user = 'ftp01'
        password = 'ivancheung7'
    elif serverIndex == 5:
        host = '192.168.80.223'
        port = 21
        user = 'ftp01'
        password = 'ivancheung7'

    mc.waitCursor(state=True)
    u = pu.PU(host, port, user, password, ["Ly", "An", "Lt", "Cp"], ["Mo", "VFX"], src)
    if mc.checkBox('img',q=True,value=True) :
        u.img()
    if mc.checkBox('par',q=True,value=True) :
        u.par()
    if mc.checkBox('nPar',q=True,value=True) :
        u.nPar()
    if mc.checkBox('nClo',q=True,value=True) :
        u.nClo()
    if mc.checkBox('geo',q=True,value=True) :
        u.geo()
    if mc.checkBox('flu',q=True,value=True) :
        u.flu()
    if mc.checkBox('ibl',q=True,value=True) :
        u.ibl()
    if mc.scrollField('descSF', q=True, tx=True):
        u.desc = mc.scrollField('descSF', q=True, tx=True)
    else:
        u.desc = ' '
    u.finish()
    mc.waitCursor(state=False)
'''

def nameToDag( name ):
    selectionList = om.MSelectionList()
    selectionList.add( name )
    path = om.MDagPath()
    selectionList.getDagPath( 0, path )
    return path

def nameToNode( name ):
    selectionList = om.MSelectionList()
    selectionList.add( name )
    node = om.MObject()
    selectionList.getDependNode( 0, node )
    return node

#返回节点类型,如果有Shape节点,也返回Shape节点类型
def getType(_obj):
    _result = {}
    _result[_obj] = mc.nodeType(_obj)

    _shape = mc.listRelatives(_obj,shapes=True)
    if not _shape == None:
        _result[_shape[0]] = mc.nodeType(_shape[0])

    return _result

def getShapeNameAndType(obj):
    try:
        obj = nameToDag(obj)
    except:
        return None
    try:
        obj.extendToShape()
    except:
        return None

    return [obj.fullPathName(), obj.node().apiTypeStr()]

def getShader(obj):
    mc.select(obj, r=True)
    try:
        mc.hyperShade(smn=True)
    except:
        return None
    else:
        shd = mc.ls(sl=True)
        return shd

def createShd(name, shdType):
    cmd = 'string $temp = `shadingNode -n %s -asShader "%s"`;\n' % (name, shdType)
    resultName = mm.eval(cmd)

    sgName = resultName + 'SG'
    cmd = 'sets -renderable true -noSurfaceShader true -empty -name %s;\n' % sgName
    mm.eval(cmd)

    mc.connectAttr('%s.outColor' % resultName, '%s.surfaceShader' % sgName, f=True)
    return [resultName, sgName]


#计算视域范围：
#width是最终的投影宽度
#distance是距离
def Aov_zwz(width,distance):
	return math.degrees(math.atan2(width/2,distance))*2
	
#计算Aperture Vertical Offset:
#FHeight是最终投影的高度
#CHeight是投影机的高度
#SHeight是银幕底边离地高度
#Distance是距离
#FouceLength是焦距:英寸
def AVOffset_zwz(FHeight,CHeight,SHeight,Distance,FouceLength):
	return math.tan(math.atan2(FHeight/2 - (FHeight-(CHeight-SHeight)), Distance)) * (FouceLength/-25.4)