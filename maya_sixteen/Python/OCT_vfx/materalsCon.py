# -*- coding: utf-8 -*-
#!/usr/bin/env python

import maya.cmds as mc
import maya.mel as mm
import os
import re
#特效破碎文件把材质名改成和mesh节点名字相似
def materalsCon():
    allShapes = mc.ls(sl = True, dagObjects=True, ni=True, shapes=True)
    if not allShapes:
        mc.confirmDialog(message = u"请选择要赋材质的物体！")
        return
    allMats = mc.ls(mat = True)
    
    for shapes in allShapes :
        shapeName = ""
        materialName = ""
        if "_fxSG" in shapes:
            name = shapes.split("_fxSG")[0]
            names = name.split("_")
            n = 0
            for i in range(len(names)-1,-1,-1):
                if names[i] != "":   
                    n = i
                    break
            shapeName = "_".join(names[0:n+1])

        if shapeName:
            for mats in allMats:
                pattern1 = re.compile('^(\w+)(:%s)$'%shapeName)
                pattern2 = re.compile('^(\w+)(_%s)$'%shapeName)
                m = pattern1.match(mats)
                if m == None:
                    m = pattern2.match(mats)
                if m:
                    materialName = m.group()
                    continue
                #print materialName

            if mc.objExists(materialName):
                print materialName
                SGNodes = mc.listConnections("%s.outColor"%materialName, s = False, d = True)
                if SGNodes:
                    for SG in SGNodes:
                        if mc.objectType(SG) == "shadingEngine":
                            mc.sets(shapes, e = True, forceElement = SG)
                else:
                    SGName = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = materialName+"SG")
                    mc.connectAttr("%s.outColor"%materialName, "%s.surfaceShader"%SGNodes, f = True)

                    mc.sets(shapes, e = True, forceElement = SGName)
materalsCon()