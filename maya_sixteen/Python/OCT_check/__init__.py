#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc

def AutoOptimizeScenes():
    import setup
    i = setup.AutoOptimizeScene()

def CheckTXSize():
    import OCT_TextureSizeForm_YH
    i=OCT_TextureSizeForm_YH.checkTextureSize()
    i.checkTextureSizeFormUI()

def checkUnusedRefence(num):
    import OCT_CheckRefence
    i = OCT_CheckRefence.OCT_CheckRefence()
    if num == 1:
        i.checkReference()
    elif num == 2:
        i.deleteUnusedReference()

def disconnectSGNode():
    allSelect = mc.ls(sl = True, dag = True,ni = True, shapes = True)
    for obj in allSelect:
        cons = mc.listConnections(obj,s = True, d = True,c = True, p = True)
        for j in range(0,len(cons),2):
            if mc.objectType(cons[j+1].split('.')[0]) == 'shadingEngine' or mc.objectType(cons[j].split('.')[0]) == 'shadingEngine':
                try:
                    mc.disconnectAttr(cons[j],cons[j+1])
                except:
                    pass

