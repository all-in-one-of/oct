#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mm
import random
class delMaterials():
    def __init__(self):
        self.allMeshs = ""
    def delMaterial(self):
        self.allMeshs = mc.ls(long=True,type="mesh",noIntermediate=True)

        createLambertShader = mc.shadingNode("lambert",asShader=True)
        createLambertShaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = "%sSG"%createLambertShader)
        mc.connectAttr("%s.outColor"%createLambertShader, "%s.surfaceShader"%createLambertShaderSG, f=True)
        
        #mc.select(d = True)
        #mc.select(self.allMeshs)
        mc.sets(self.allMeshs, forceElement = createLambertShaderSG,e=True)
        #mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')
        #self.delFace();
     
    def delFace(self):
        for meshs in self.allMeshs:
            numFace=mc.polyEvaluate(meshs,face=True)
            for num in range(numFace/2):
                randFace=random.randint(0,numFace)
                mc.select(meshs+'.f['+str(randFace)+']')
                mc.delete()

#delMaterials().delMaterial()