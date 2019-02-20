# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

class cameraConnetPlace3dTexture():
    def __init__(self):
        pass
    def cameraConnetPlace3d(self):
        allMesh=mc.ls(ap=True,type="mesh",ni=True)
        allSelect=mc.ls(sl=True)
        flag=False
        if allSelect and len(allSelect)<2:
            shapesNodes=mc.listRelatives(allSelect[0],c=True,s=True,ni=True)
            if mc.objectType(shapesNodes[0])=="camera":
                flag=True
        if flag:
            lambertShader=mc.shadingNode("lambert",asShader=True)
            lambertShadesSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(lambertShader+"SG"))
            mc.connectAttr((lambertShader+".outColor"),(lambertShadesSG+".surfaceShader"),f=True)
            
            projectShader=mc.shadingNode("projection",asUtility=True)
            mc.connectAttr((projectShader+".outColor"),(lambertShader+".color"),f=True)
            
            rampName=mc.shadingNode("ramp",asTexture=True)
            place2dTextureName=mc.shadingNode("place2dTexture",asUtility=True)
            mc.connectAttr((place2dTextureName+".outUV"),(rampName+".uv"),f=True)
            mc.connectAttr((place2dTextureName+".outUvFilterSize"),(rampName+".uvFilterSize"),f=True)
            mc.removeMultiInstance((rampName+".colorEntryList[1]"),b=True)
            mc.setAttr((rampName+".colorEntryList[2].color"),1,1,1,type="double3")
            mc.setAttr((rampName+".colorEntryList[0].color"),0,0,0,type="double3")
            
            mc.setAttr((rampName+".colorEntryList[2].position"),1)
            mc.setAttr((rampName+".colorEntryList[0].position"),0)
            
            mc.connectAttr((rampName+".outColor"),(projectShader+".image"),f=True)
            place3dTextureName=mc.shadingNode("place3dTexture",asUtility=True)
            mc.connectAttr((place3dTextureName+".worldInverseMatrix[0]"),(projectShader+".placementMatrix"),f=True)
       
            
            mc.setAttr((rampName+".type"),1)
            mc.select(allSelect[0],r=True)
            mc.select(place3dTextureName,add=True)
            mm.eval('doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };')
            place3dTexture2_point=mc.pointConstraint(offset=[0,0,0],weight=1)
            mm.eval('doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };')
            place3dTexture2_orien=mc.orientConstraint(offset=[0,0,0],weight=1)
            mc.delete(place3dTexture2_point)
            mc.delete(place3dTexture2_orien)
            mc.select(place3dTextureName,r=True)
            mc.select(allSelect[0],add=True)
            mc.parent()
            
            mc.setAttr((projectShader+".wrap"),0)
            mc.setAttr((place3dTextureName+".rotateY"),90)
            mc.setAttr((lambertShader+".ambientColor"),1,1,1,type="double3")
            mc.setAttr((lambertShader+".diffuse"),0)
            mc.select(d=True)
            mc.select(allMesh)
            mc.hyperShade(assign=lambertShader)
            ctx=mc.currentCtx()
            if ctx!="shadingProjectionContext":
                mc.select(place3dTextureName,r=True)
                mc.setToolTo("shadingProjectionContext")
            else:
                mc.select(place3dTextureName,r=True)
            mc.projectionManip(fb=True)
           
        else:
            mc.confirmDialog(message=u"请选择一个相机！")
            return 
      
            
    def cameraConnetPlace3dArnold(self):
        allMesh=mc.ls(ap=True,type="mesh",ni=True)
        allArnold=mc.ls(type="aiStandIn")
        allSelect=mc.ls(sl=True)
        flag=False
        if allSelect and len(allSelect)<2:
            shapesNodes=mc.listRelatives(allSelect[0],c=True,s=True,ni=True)
            if mc.objectType(shapesNodes[0])=="camera":
                flag=True
        if flag:
            aiUtilityShader=mc.shadingNode("aiUtility",asShader=True)
            aiUtilityShaderSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(aiUtilityShader+"SG"))
            mc.connectAttr((aiUtilityShader+".outColor"),(aiUtilityShaderSG+".surfaceShader"),f=True)
            
            projectShader=mc.shadingNode("projection",asUtility=True)
            mc.connectAttr((projectShader+".outColor"),(aiUtilityShader+".color"),f=True)
            
            rampName=mc.shadingNode("ramp",asTexture=True)
            place2dTextureName=mc.shadingNode("place2dTexture",asUtility=True)
            mc.connectAttr((place2dTextureName+".outUV"),(rampName+".uv"),f=True)
            mc.connectAttr((place2dTextureName+".outUvFilterSize"),(rampName+".uvFilterSize"),f=True)
            mc.removeMultiInstance((rampName+".colorEntryList[1]"),b=True)
            mc.setAttr((rampName+".colorEntryList[2].color"),1,1,1,type="double3")
            mc.setAttr((rampName+".colorEntryList[0].color"),0,0,0,type="double3")
            
            mc.setAttr((rampName+".colorEntryList[2].position"),1)
            mc.setAttr((rampName+".colorEntryList[0].position"),0)
            
            mc.connectAttr((rampName+".outColor"),(projectShader+".image"),f=True)
            place3dTextureName=mc.shadingNode("place3dTexture",asUtility=True)
            mc.connectAttr((place3dTextureName+".worldInverseMatrix[0]"),(projectShader+".placementMatrix"),f=True)
       
            
            mc.setAttr((rampName+".type"),1)
            mc.select(allSelect[0],r=True)
            mc.select(place3dTextureName,add=True)
            mm.eval('doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };')
            place3dTexture2_point=mc.pointConstraint(offset=[0,0,0],weight=1)
            mm.eval('doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };')
            place3dTexture2_orien=mc.orientConstraint(offset=[0,0,0],weight=1)
            mc.delete(place3dTexture2_point)
            mc.delete(place3dTexture2_orien)
            mc.select(place3dTextureName,r=True)
            mc.select(allSelect[0],add=True)
            mc.parent()
            
            mc.setAttr((projectShader+".wrap"),0)
            mc.setAttr((place3dTextureName+".rotateY"),90)
            mc.setAttr((aiUtilityShader+".shadeMode"),2)
           
            mc.select(d=True)
            if allMesh:
                mc.select(allMesh)
                mc.hyperShade(assign=aiUtilityShader)
            if allArnold:
                mc.select(allArnold)
                mc.hyperShade(assign=aiUtilityShader)
            ctx=mc.currentCtx()
            if ctx!="shadingProjectionContext":
                mc.select(place3dTextureName,r=True)
                mc.setToolTo("shadingProjectionContext")
            else:
                mc.select(place3dTextureName,r=True)
            mc.projectionManip(fb=True)
           
        else:
            mc.confirmDialog(message=u"请选择一个相机！")
            return  


    def shaderImp(self):
        allSelect=mc.ls(sl=True)
        flag=False
        if allSelect:
            for sel in allSelect:
                if mc.objectType(sel):
                    flag=True
                    break
                shapesNodes=mc.listRelatives(sel,c=True,s=True,ni=True)
                if mc.objectType(shapesNodes[0])=="mesh":
                    flag=True
                    break
        if flag:
            lambertShader=mc.shadingNode("lambert",asShader=True)
            lambertShadesSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(lambertShader+"SG"))
            mc.connectAttr((lambertShader+".outColor"),(lambertShadesSG+".surfaceShader"),f=True)
            
            projectShader=mc.shadingNode("projection",asUtility=True)
            mc.connectAttr((projectShader+".outColor"),(lambertShader+".color"),f=True)
            
            rampName=mc.shadingNode("ramp",asTexture=True)
            place2dTextureName=mc.shadingNode("place2dTexture",asUtility=True)
            mc.connectAttr((place2dTextureName+".outUV"),(rampName+".uv"),f=True)
            mc.connectAttr((place2dTextureName+".outUvFilterSize"),(rampName+".uvFilterSize"),f=True)
            mc.removeMultiInstance((rampName+".colorEntryList[1]"),b=True)
            mc.setAttr((rampName+".colorEntryList[2].color"),1,1,1,type="double3")
            mc.setAttr((rampName+".colorEntryList[0].color"),0,0,0,type="double3")
            
            mc.setAttr((rampName+".colorEntryList[2].position"),1)
            mc.setAttr((rampName+".colorEntryList[0].position"),0)
            
            mc.connectAttr((rampName+".outColor"),(projectShader+".image"),f=True)
            place3dTextureName=mc.shadingNode("place3dTexture",asUtility=True)
            mc.connectAttr((place3dTextureName+".worldInverseMatrix[0]"),(projectShader+".placementMatrix"),f=True)
            
            mc.setAttr((rampName+".type"),0)
            mc.setAttr((projectShader+".wrap"),0)
            mc.setAttr((place3dTextureName+".rotateY"),90)
            mc.setAttr((lambertShader+".ambientColor"),1,1,1,type="double3")
            mc.setAttr((lambertShader+".diffuse"),0)
            
            mc.setAttr((projectShader+".defaultColorR"),0)
            mc.setAttr((projectShader+".defaultColorG"),0)
            mc.setAttr((projectShader+".defaultColorB"),0)

            mc.select(d=True)
            print allSelect
            for sel in allSelect:
                mc.select(sel,add=True)
            mc.hyperShade(assign=lambertShader)
            ctx=mc.currentCtx()
            if ctx!="shadingProjectionContext":
                mc.select(place3dTextureName,r=True)
                mc.setToolTo("shadingProjectionContext")
            else:
                mc.select(place3dTextureName,r=True)
            mc.projectionManip(fb=True)
           
        else:
            mc.confirmDialog(message=u"请选择物体！")
            return 
            
             