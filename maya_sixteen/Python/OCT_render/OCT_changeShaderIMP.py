# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om

class changeShaderIMPs():
    def __init__(self):
        pass
    def changeShaderBlinn(self):
        allSelect=mc.ls(sl=True)
        if allSelect:
            if len(allSelect)>1:
                mc.confirmDialog(message="请选择一个材质！")
                return
            else:
                connections = mc.listConnections(allSelect[0],s=True,d=False,connections=True,plugs=True)
                blinnShader=mc.shadingNode("blinn",asShader=True)
                blinnShaderSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(blinnShader+"SG"))
                try:
                    mc.connectAttr((blinnShader+".outColor"),(blinnShaderSG+".surfaceShader"),f=True)
                    mc.connectAttr(connections[1],(blinnShader+".color"),f=True)
                except:
                    om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.cloor' %(connections[1],blinnShader))
                else:
                    mc.setAttr((blinnShader+".ambientColor"),1,1,1,type="double3")
                    mc.setAttr((blinnShader+".diffuse"),0)
                    mc.setAttr((blinnShader+".specularColor"),0,0,0,type="double3")
                    mc.setAttr((blinnShader+".reflectivity"),0)
                    
    def changeShaderPhong(self):
        allSelect=mc.ls(sl=True)
        if allSelect:
            if len(allSelect)>1:
                mc.confirmDialog(message="请选择一个材质！")
                return
            else:
                connections = mc.listConnections(allSelect[0],s=True,d=False,connections=True,plugs=True)
                phongShader=mc.shadingNode("phong",asShader=True)
                phongShaderSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(phongShader+"SG"))
                try:
                    mc.connectAttr((phongShader+".outColor"),(phongShaderSG+".surfaceShader"),f=True)
                    mc.connectAttr(connections[1],(phongShader+".color"),f=True)
                except:
                    om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.cloor' %(connections[1],phongShader))
                else:
                    mc.setAttr((phongShader+".ambientColor"),1,1,1,type="double3")
                    mc.setAttr((phongShader+".diffuse"),0)
                    mc.setAttr((phongShader+".specularColor"),0,0,0,type="double3")
                    mc.setAttr((phongShader+".reflectivity"),0)
        
    def changeShaderPhongE(self):
        allSelect=mc.ls(sl=True)
        if allSelect:
            if len(allSelect)>1:
                mc.confirmDialog(message="请选择一个材质！")
                return
            else:
                connections = mc.listConnections(allSelect[0],s=True,d=False,connections=True,plugs=True)
                phongEShader=mc.shadingNode("phongE",asShader=True)
                phongEShaderSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(phongEShader+"SG"))
                try:
                    mc.connectAttr((phongEShader+".outColor"),(phongEShaderSG+".surfaceShader"),f=True)
                    mc.connectAttr(connections[1],(phongEShader+".color"),f=True)
                except:
                    om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.cloor' %(connections[1],phongShader))
                else:
                    mc.setAttr((phongEShader+".ambientColor"),1,1,1,type="double3")
                    mc.setAttr((phongEShader+".diffuse"),0)
                    mc.setAttr((phongEShader+".specularColor"),0,0,0,type="double3")
                    mc.setAttr((phongEShader+".reflectivity"),0)            
        
    def changeShaderUI(self):
         if mc.window("changeShaderUI",q=True,exists=True):
            mc.deleteUI("changeShaderUI")
         mc.window("changeShaderUI",title=u"imp连接各种材质",widthHeight=(200, 120),sizeable=False)
         mc.columnLayout(adjustableColumn=True)
         mc.button(label="Blinn",h=35,w=200,c=lambda*args: self.changeShaderBlinn(),bgc=[0.4,0.1,0.3])
         mc.button(label="Phong",h=35,w=200,c=lambda*args: self.changeShaderPhong(),bgc=[0.4,0.5,0.4])
         mc.button(label="PhongE",h=35,w=200,c=lambda*args: self.changeShaderPhongE(),bgc=[0.4,0.7,0.5])
         mc.showWindow("changeShaderUI")
        