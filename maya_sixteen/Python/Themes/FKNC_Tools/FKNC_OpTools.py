#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

from __future__ import with_statement #only needed for maya 2008 & 2009


import maya.cmds as mc
import maya.mel as mm


import OCT_generel

def FKNC_Optimize():
    OCT_generel.removeNamespace()

    PROJECT_PATH = r"\\octvision.com\cg\Themes"
    OCT_DRIVE = r"\\octvision.com\cg"
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
                    mc.setAttr('%s.fileTextureName' % texFile, texFileName, type="string")

    myMat = mc.ls(mat=True)
    mc.select(myMat)
    mm.eval('removeDuplicateShadingNetworks( 1 );')

def SelectRootFolder():
    a=mc.ls('Root')
    if a:
        mc.select(a)
    b = mc.ls('root')
    if b:
        mc.select(b,add=True)


def DeleteConAndOptimize():
    myAllContainers = mc.ls(type=['parentConstraint', 'pointConstraint', 'aimConstraint', 'orientConstraint', 'scaleConstraint'])
    mc.delete(myAllContainers)
    mm.eval("OptimizeScene;cleanUpScene 1;")