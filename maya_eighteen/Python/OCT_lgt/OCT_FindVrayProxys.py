#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
class findVrayProxys():
    def __init__(self):
        pass
    def mySelectVray(self):
       
        allMyVrayMeshs = mc.ls(type="VRayMesh", l=True)
        myFilaNames = []
        allOnlyVrayMeshs = []
        allOnlyParents = []
        if allMyVrayMeshs:
            for eachMesh in allMyVrayMeshs:
                allOnlyVrayMeshs.append(eachMesh)
            if allOnlyVrayMeshs:
                for eachOnlySVrayMesh in allOnlyVrayMeshs:
                    eachmeshCons = mc.listConnections(eachOnlySVrayMesh)
                    if eachmeshCons:
                        flag=True
                        for eachCon in eachmeshCons:
                            if mc.nodeType(eachCon) == "transform":
                                allOnlyParents.append(mc.ls(eachCon, l=True)[0])
                                break
                                
                            if mc.nodeType(eachCon) == "transformGeometry":
                                eachmeshCons = mc.listConnections(eachCon)
                                for eachCon in eachmeshCons:
                                    if mc.nodeType(eachCon) == "transform":
                                        allOnlyParents.append(mc.ls(eachCon, l=True)[0])
                                        flag=False
                                        break
                                    elif mc.nodeType(eachCon) == "transformGeometry":
                                        eachmeshCons = mc.listConnections(eachCon)
                                        for eachCon in eachmeshCons:
                                            if mc.nodeType(eachCon) == "transform":
                                                allOnlyParents.append(mc.ls(eachCon, l=True)[0])
                                                flag=False
                                                break
                                    if not flag:
                                        break
                            
                                
            mc.select(allOnlyParents)
        else:
            mc.warning(u"没有Vray代理物体")
    
    
    
    def SelectsameVrayMesh(self):
        myTrans = mc.ls(sl=True, l=True, tr=True)
        if myTrans:
            allMySelectShapes = []
            for eachTran in myTrans:
                myTanS = mc.listRelatives(eachTran, s=True)[0]
                allMySelectShapes.append(myTanS)
                
        allMySelectShapes = list(set(allMySelectShapes))
        
        myFilaNames = []
        allMySelectShapes = mc.ls(allMySelectShapes, l=True)
        for eachSShape in allMySelectShapes:
            myAllHistorys = mc.listHistory(eachSShape)
            for myHistory in myAllHistorys:
                myHistoryType = mc.nodeType(myHistory)
                if myHistoryType == 'VRayMesh':
                    tmpName = mc.getAttr('%s.fileName' % myHistory)
                    if tmpName:
                        myFilaNames.append(myHistory)
        if myFilaNames:
             mySelectVrayMesh = []
             allSameVrayTran = []
             allMyVrayMeshs = mc.ls(type="VRayMesh")
             if allMyVrayMeshs:
                 for eachMesh in allMyVrayMeshs:
                     if eachMesh in myFilaNames:
                         mySelectVrayMesh.append(eachMesh)
                                
                 for eachMySVrayMesh in mySelectVrayMesh:
                    eachmeshCons = mc.listConnections(eachMySVrayMesh, sh=True)
                    if eachmeshCons:
                        flag=True
                        for eachCon in eachmeshCons:
                            if mc.nodeType(eachCon) == "mesh":
                                allSameVrayTran += mc.listRelatives(eachCon, f=True, ap=True)
                                break
                            elif mc.nodeType(eachCon) == "transformGeometry":
                                eachmeshCons = mc.listConnections(eachCon,sh=True)
                                for eachCon in eachmeshCons:
                                    if mc.nodeType(eachCon) == "mesh":
                                        allSameVrayTran += mc.listRelatives(eachCon, f=True, ap=True)
                                        flag=False
                                        break
                                    elif mc.nodeType(eachCon) == "transformGeometry":
                                        eachmeshCons = mc.listConnections(eachCon,sh=True)
                                        for eachCon in eachmeshCons:
                                            if mc.nodeType(eachCon) == "mesh":
                                                allSameVrayTran += mc.listRelatives(eachCon, f=True, ap=True)
                                                flag=False
                                                break
                                    if not flag:
                                        break     
                            
                 if allSameVrayTran:
                     mc.select(allSameVrayTran)
             else:
                 mc.warning(u"选择为空！")
                 
    def  findVrayProxysUI(self):
        if mc.window("findVrayProxysUI",q=True,exists=True):
            mc.deleteUI("findVrayProxysUI")
        mc.window("findVrayProxysUI",title=u"查找VrayMesh的代表物体",widthHeight=(200, 70))
        mc.columnLayout(adjustableColumn=True)
        mc.button(label=u"选择所有VrayMesh的代表物体",h=30,c=lambda*args: self.mySelectVray(),bgc=[0.7,0.5,0.3])
        mc.button(label=u"选择相同VrayMesh的所有物体",h=30,c=lambda*args: self.SelectsameVrayMesh(),bgc=[0.7,0.6,0.4])
        mc.showWindow("findVrayProxysUI")
     
    
    