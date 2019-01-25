# -*- coding: utf-8 -*-
#!/usr/bin/env python

import maya.cmds as mc
import maya.mel as mm
import os
import re

class ExportImportSGNode():
    def __init__(self):
        self.allShapes = []

    def ExportImportSGNodeUI(self):
        if mc.window("ExportImportSGNodeUI", exists = True):
            mc.deleteUI("ExportImportSGNodeUI", window=True)
        getWindow = mc.window("ExportImportSGNodeUI", wh = (300,200), resizeToFitChildren=1, sizeable=True)
        mc.columnLayout('First_Set',columnAttach=('both', 5), rowSpacing=10, columnWidth=300 )
        mc.button('btn1', h = 30, label = u"选择物体导出物体相连的SG节点和材质", c = lambda*args: self.ExportSG())
        mc.button('btn3', h = 30, label = u"导入文件连接材质(fbx文件的材质和原SG节点名字相同)", c = lambda*args: self.FbxAndSGCon())
        mc.button('btn4', h = 30, label = u"导入文件连接材质(abc文件的mesh和原SG节点名字相同)", c = lambda*args: self.AbcAndSGCon())
        mc.button('btn2', h = 30, label = u"导入文件连接材质(根据houdini引擎mesh和原SG节点相似)", c = lambda*args: self.GetNewMaterial())
       
        mc.showWindow()

    #根据houdini引擎mesh和原SG节点相似
    def GetNewMaterial(self):
        myList = []

        self.allShapes = mc.ls(sl = True, dagObjects=True, ni=True, shapes=True)
        if not self.allShapes:
            mc.confirmDialog(message = u"请选择要赋材质的物体！")
            return
        allMeshs = {}
        allMats = mc.ls(type  = "shadingEngine")

        for shape in self.allShapes:
            if mc.objectType(shape) == "mesh":
                name = shape.split("_fxSG")[0]
                if "u_" in name:
                    name = "_".join(name.split("_")[1:-2])
                    # print name
                else:
                    name = "_".join(shape.split("_")[0:-1])
                allMeshs.update({name:shape})
        for meshs in allMeshs.keys():
            materialName = ""
            for mat in allMats:
                pattern1 = re.compile('^(\w+)(:%s)$'%meshs)
                pattern2 = re.compile('^(\w+)(_%s)$'%meshs)
                m = pattern1.match(mat)
                if m == None:
                    m = pattern2.match(mat)
                if m:
                    materialName = m.group()
                    break
                elif mat == meshs:
                    materialName = mat
                    break

            if mc.objExists(materialName):
                mc.sets(allMeshs[meshs], e = True, forceElement = materialName)
            else:
                myList.append(allMeshs[meshs])

        if myList:
            mc.confirmDialog(message = u"%s节点文件中没有找到与之相匹配的SG点"%myList)
            return

    #导入文件连接材质(fbx文件的材质和原SG节点名字相同)
    def FbxAndSGCon(self):
        #查找fbx中的材质
        #self.allMats = mc.ls(mat = True)
        myList = []
        self.allMats = []
        self.allShapes = mc.ls(sl = True, dagObjects=True, ni=True, shapes=True)
        if not self.allShapes:
            mc.confirmDialog(message = u"请选择要赋材质的物体！")
            return
        for shap in self.allShapes:
            shapSG = mc.listConnections(shap, s = True, d = True)
            shapSGs = list(set(shapSG))
            for SG in shapSGs:
                if mc.objectType(SG) == "shadingEngine":
                    materal = mc.listConnections("%s.surfaceShader"%SG, s = True, d = False)
                    self.allMats.append(materal[0])

        #查找导入的sg节点
        self.allShadings = mc.ls(type = "shadingEngine")
        for mats in self.allMats :
            materialName = ""
            for shading in self.allShadings:
                pattern1 = re.compile('^(\w+)(:%s)$'%mats)
                pattern2 = re.compile('^(\w+)(_%s)$'%mats)
                pattern3 = re.compile('^(%s)(\d)$'%shading)
                pattern4 = re.compile('^(%s)(\d)$'%name)
                m = pattern1.match(shading)
                if m == None:
                    m = pattern2.match(shading)
                    if m == None:
                        m = pattern4.match(shading)
                if m:
                    materialName = m.group()
                    break
                elif mat ==  shading:
                    materialName = shading
                    break
                else:
                    m = pattern3.match(name)
                    if m:
                        materialName = shading

            if materialName:
                cons = mc.listConnections("%s.outColor"%mats,s = False, d = True)
                if cons:
                    ConMeshs = mc.sets(cons[0], q = True)
                    if ConMeshs:
                        for mesh in ConMeshs:
                            mc.sets(mesh, e = True, forceElement = materialName)
                else:
                    myList.append(mats)
                    print(u"%s没有连接SG节点！"%mats)
            else:
                myList.append(mats)
        if myList:
            mc.confirmDialog(message = u"%s节点文件中没有找到与之相匹配的SG点"%myList)
            return

    #导入文件连接材质(abc文件的mesh和原SG节点名字相同)
    def AbcAndSGCon(self):
        myList = []
        #查询所选择的所有物体
        self.allShapes = mc.ls(sl = True, dagObjects=True, ni=True, shapes=True)
        if not self.allShapes:
            mc.confirmDialog(message = u"请选择要赋材质的物体！")
            return
        #查找导入的sg节点
        self.allShadings = mc.ls(type = "shadingEngine")
        for shapes in self.allShapes:
            name = ""
            if "|" in shapes:
                name = shapes.split("|")[-1]
            else:
                name = shapes
                
            materialName = ""
        
            for shading in self.allShadings:
                pattern1 = re.compile('^(\w+)(:%s)$'%name)
                pattern2 = re.compile('^(\w+)(_%s)$'%name)
                pattern3 = re.compile('^(%s)(\d)$'%shading)
                pattern4 = re.compile('^(%s)(\d)$'%name)
                m = pattern1.match(shading)
                if m == None:
                    m = pattern2.match(shading)
                    if m == None:
                        m = pattern4.match(shading)
                if m:
                    materialName = m.group()
                    break
                elif shading == name:
                    materialName = shading
                    break
                else:
                    m = pattern3.match(name)
                    if m:
                        materialName = shading

            if materialName:
                mc.sets(shapes, e = True, forceElement = materialName)
            else:
                myList.append(shapes)
                
        if myList:
            mc.confirmDialog(message = u"%s节点文件中没有找到与之相匹配的SG点"%myList)
            return


    def ExportSG(self):
        self.allShapes = mc.ls(sl = True, dagObjects=True, ni=True, shapes=True)
        if not self.allShapes:
            mc.confirmDialog(message = u"请选择要赋材质的物体！")
            return
        allSG = []
        for shape in self.allShapes:
            ShapeShadings = mc.listConnections(shape, s = True, d = True)
            for shading in ShapeShadings:
                if mc.objectType(shading) == "shadingEngine":
                    if not shading in allSG:
                        allSG.append(shading)
  
        if allSG:
            mc.select(allSG, ne = True)
            fileName = mc.file(sn = True, q = True)
            fileNames = os.path.splitext(fileName)[0]+"_SG.mb"
            mc.file(fileNames, op = "v=0;",typ = "mayaBinary",pr = True, es = True)

#ExportImportSGNode().ExportImportSGNodeUI()
