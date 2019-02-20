#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm

class ProxyChange():
    def __init__(self):
        pass
    def VrayProxyChangeArnoldProxy(self):
        allVrayMesh=mc.ls(type="VRayMesh")
        allArnoldProxy=mc.ls(type="aiStandIn")
        listVrayMesh=[]
        for vraypro in allVrayMesh:
            VrayFilePath=mc.getAttr(vraypro+".fileName")
            VrayProFile=VrayFilePath.split("/")[-1].split(".")[0]
            for arnoldPro in allArnoldProxy:
                arnoldDso=mc.getAttr(arnoldPro+".dso")
                ArnoldProFile=arnoldDso.split("/")[-1].split(".")[0]
                flag=False
                if VrayProFile==ArnoldProFile:
                    transformsArnold=mc.listRelatives(arnoldPro,p=True)
                    translateArnold=mc.getAttr(transformsArnold[0]+".translate")
                
                    rotateArnold=mc.getAttr(transformsArnold[0]+".rotate")
                    scaleArnold=mc.getAttr(transformsArnold[0]+".scale")
                    
                    connects=mc.listConnections(vraypro,s=False,d=True,connections=True,plugs=True)
                    transformsVray=""
                    for con in connects:
                        if "inMesh" in con:
                            nodes=con.split(".")[0]
                            transformsVray=mc.listRelatives(nodes,p=True)
                    if transformsVray:
                        translateVray=mc.getAttr(transformsVray[0]+".translate")
                        rotateVray=mc.getAttr(transformsVray[0]+".rotate")
                        scaleVray=mc.getAttr(transformsVray[0]+".scale")
                        if translateArnold==translateVray and rotateArnold==rotateVray and scaleArnold==scaleVray:
                            flag=True
                            if mc.objExists(transformsVray[0]):
                                mc.delete(transformsVray[0])
                    if flag:
                        for con in connects:
                            nodes=con.split(".")[0]
                            if mc.objExists(nodes):
                                mc.delete(con.split(".")[0])
                                
                                
    def ArnoldProxyChangeVrayProxy(self):
        allVrayMesh=mc.ls(type="VRayMesh")
        allArnoldProxy=mc.ls(type="aiStandIn")
        listVrayMesh=[]
        for vraypro in allVrayMesh:
            VrayFilePath=mc.getAttr(vraypro+".fileName")
            VrayProFile=VrayFilePath.split("/")[-1].split(".")[0]
            for arnoldPro in allArnoldProxy:
                arnoldDso=mc.getAttr(arnoldPro+".dso")
                ArnoldProFile=arnoldDso.split("/")[-1].split(".")[0]
                flag=False
                if VrayProFile==ArnoldProFile:
                    transformsArnold=mc.listRelatives(arnoldPro,p=True)
                    translateArnold=mc.getAttr(transformsArnold[0]+".translate")
                
                    rotateArnold=mc.getAttr(transformsArnold[0]+".rotate")
                    scaleArnold=mc.getAttr(transformsArnold[0]+".scale")
                    
                    connects=mc.listConnections(vraypro,s=False,d=True,connections=True,plugs=True)
                    transformsVray=""
                    for con in connects:
                        if "inMesh" in con:
                            nodes=con.split(".")[0]
                            transformsVray=mc.listRelatives(nodes,p=True)
                    if transformsVray:
                        translateVray=mc.getAttr(transformsVray[0]+".translate")
                        rotateVray=mc.getAttr(transformsVray[0]+".rotate")
                        scaleVray=mc.getAttr(transformsVray[0]+".scale")
                        if translateArnold==translateVray and rotateArnold==rotateVray and scaleArnold==scaleVray:
                            if mc.objExists(transformsArnold[0]):
                                mc.delete(transformsArnold[0])
                    
    def ProxyChangeUI(self):
        if mc.window("ProxyChangeUI",q=True,exists=True):
            mc.deleteUI("ProxyChangeUI")
        mc.window("ProxyChangeUI",title=u"代理替换",widthHeight=(200, 70))
        mc.columnLayout(adjustableColumn=True)
        mc.button(label="VrayProxyChangeArnoldProxy",h=30,c=lambda*args: self.VrayProxyChangeArnoldProxy(),bgc=[0.4,0.1,0.3])
        mc.button(label="ArnoldProxyChangeVrayProxy",h=30,c=lambda*args: self.ArnoldProxyChangeVrayProxy(),bgc=[0.4,0.5,0.4])
        mc.showWindow("ProxyChangeUI")
     





 