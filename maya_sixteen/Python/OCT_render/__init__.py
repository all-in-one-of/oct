#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import threading
import maya.cmds as mc
import maya.mel as mm


import OCT_QuantityRender_zwz
import OCT_SuperFixFram_zwz
from zxy_resizeImage import ReSizeDialog
from OCT_ChangeNodePath_Tool import File_Tools


def replaceViewportProxyPath():
    import ReplaceVRayViewport
    dialog = ReplaceVRayViewport.ReplaceVRayViewport()
    dialog.showWindow()

#abc缓存管理工具
def run_AlembicNodeFile_Tools_YH():
    fileType = 'AlembicNode' #节点类型
    nodeAttr = 'abc_File'    #节点属性
    dirName = 'alembic'     #文件夹

    if mc.window("%sDialog"%fileType, exists=True):
        mc.deleteUI("%sDialog"%fileType, window=True)
    dialog = File_Tools(fileType, nodeAttr, dirName)
    t = threading.Thread(None, dialog.show())
    t.start()

def run_VRayMeshFile_Tools_YH():
    fileType = 'VRayMesh' #节点类型
    nodeAttr = 'fileName'    #节点属性
    dirName = 'sourceimages'     #文件

    if mc.window("%sDialog"%fileType, exists=True):
        mc.deleteUI("%sDialog"%fileType, window=True)
    dialog = File_Tools(fileType, nodeAttr, dirName)
    t = threading.Thread(None, dialog.show())
    t.start()
def run_YetiTexture_Tools():
    from OCT_YetiTextureTool import YetiFile_Tools
    fileType = 'pgYetiMaya' #节点类型
    nodeAttr = 'imageSearchPath'    #节点属性
    dirName = 'sourceimages'     #文件

    if mc.window("%sDialog"%fileType, exists=True):
        mc.deleteUI("%sDialog"%fileType, window=True)

    dialog = YetiFile_Tools(fileType, nodeAttr, dirName)
    t = threading.Thread(None, dialog.show())
    t.start()

def run_shaveCache_Tools():
    from OCT_YetiTextureTool import YetiFile_Tools
    fileType = 'shaveGlobals' #节点类型
    nodeAttr = 'tmpDir'    #节点属性
    dirName = 'cache'     #文件

    if mc.window("%sDialog"%fileType, exists=True):
        mc.deleteUI("%sDialog"%fileType, window=True)

    dialog = YetiFile_Tools(fileType, nodeAttr, dirName)
    t = threading.Thread(None, dialog.show())
    t.start()

def run_AiStandIn_Tools():
    from OCT_YetiTextureTool import YetiFile_Tools
    fileType = 'aiStandIn' #节点类型
    nodeAttr = 'dso'    #节点属性
    dirName = 'sourceimages'     #文件

    if mc.window("%sDialog"%fileType, exists=True):
        mc.deleteUI("%sDialog"%fileType, window=True)

    dialog = YetiFile_Tools(fileType, nodeAttr, dirName)
    t = threading.Thread(None, dialog.show())
    t.start()
    
def ClearUseRanderDefer():
    import OCT_ClearUseRanderAndDefer
    i = OCT_ClearUseRanderAndDefer.OCT_ClearUseRander()
    i.clearUseRender_UI()
    
def batchRender_Tools():
    import batchRender_Tool
    i=batchRender_Tool.BatchRender_Tools()
    i.window_Reader()

def run_zxy_resizeImage():
    if mc.window("resize_dialog", exists=True):
        mc.deleteUI("resize_dialog", window=True)
    dialog = ReSizeDialog()
    t = threading.Thread(None, dialog.show())
    t.start()

def OCT_RenderDeepSets():
    import OCT_RenderDeepSet
    i=OCT_RenderDeepSet.OCT_RenderDeepSet()
    i.OCT_ProjectPathSet()

def newPreRender_YH():
	import DY_New_RenderToolsUI_YH
	DY_New_RenderToolsUI_YH.DY_New_PreRendersUI_YH()

def OpenRenderLayerTools():
	import OCT_RenderLayers_zwz
	OCT_RenderLayers_zwz.OCT_RenderLayers_Menum_zwz()


def cameraConnetPlace3d():
    import OCT_cameraConnetPlace3dTexture
    i=OCT_cameraConnetPlace3dTexture.cameraConnetPlace3dTexture()
    i.cameraConnetPlace3d()

def cameraConnetPlace3darnold():
    import OCT_cameraConnetPlace3dTexture
    i=OCT_cameraConnetPlace3dTexture.cameraConnetPlace3dTexture()
    i.cameraConnetPlace3dArnold()
    
def cameraConnetPlace3dImp():
    import OCT_cameraConnetPlace3dTexture
    i=OCT_cameraConnetPlace3dTexture.cameraConnetPlace3dTexture()
    i.shaderImp()

def OCT_materialChanges():
    import OCT_materialChange
    OCT_materialChange.OCT_materialChangeUI()

def changeShaderIMP():
    import OCT_changeShaderIMP
    i=OCT_changeShaderIMP.changeShaderIMPs()
    i.changeShaderUI()



def deleteSGNode_YH():
	mm.eval('''
		global proc deleteSGNode(){
			string $allShading[]=`ls -type shadingEngine`;
			for($i in $allShading){
				catch(`delete $i`);
			}
    	}
    	deleteSGNode();
    ''')