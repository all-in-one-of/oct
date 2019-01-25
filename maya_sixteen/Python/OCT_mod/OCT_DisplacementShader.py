#!/usr/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

class DisplacementShaderAndShading():
	def __init__(self):
		pass
	def disconnectDisPlacement(self):
		allDisplacementShader=mc.ls(type="displacementShader")
		flag=0
		if allDisplacementShader:
			for displacement in allDisplacementShader:
				connect=mc.listConnections("%s.displacement"%displacement,s=False,d=True)
				if connect:
					displacementName=displacement.split("_")
					if len(displacementName)>1 and "disSG" in displacementName[-1]:
						connectName=mc.listConnections("%s.displacement"%displacement,s=False,d=True)
						mc.disconnectAttr("%s.displacement"%displacement,"%s.displacementShader"%connectName[0])
					else:
						flag=flag+1
						newDisPlace=mc.rename(displacement,"%s_disSG%s"%(displacement,flag))
						connectName=mc.listConnections("%s.displacement"%newDisPlace,s=False,d=True)
						newShading=mc.rename(connectName[0],"%s_disSG%s"%(connectName[0],flag))		
						mc.disconnectAttr("%s.displacement"%newDisPlace,"%s.displacementShader"%newShading)
					
	def connectDisPlacement(self):
		allDisplacementShader=mc.ls(type="displacementShader")
		if allDisplacementShader:
			for displacement in allDisplacementShader:
				displacementName=displacement.split("_")
				if len(displacementName)>1 and "disSG" in displacementName[-1]:
					allShadingEngine=mc.ls(type="shadingEngine")
					for shadings in allShadingEngine:
						shadingsName=shadings.split("_")
						if displacementName[-1]==shadingsName[-1]:
							mc.connectAttr("%s.displacement"%displacement,"%s.displacementShader"%shadings)
	def deleteDisplacement(self):
		allDisplacementShader=mc.ls(type="displacementShader")
		if allDisplacementShader:
			for displacement in allDisplacementShader:
				mc.delete(displacement)
							
	def DisplacementShaderAndShadingUI(self):
		if mc.window("DisplacementShaderAndShadingUI",q=True,exists=True):
			mc.deleteUI("DisplacementShaderAndShadingUI")
		mc.window("DisplacementShaderAndShadingUI",title=u"断开与连接材质节点",widthHeight=(400, 100),sizeable=False)
		mc.columnLayout(adjustableColumn=True)
		mc.button(label=u"断开置换贴图",h=30,c=lambda*args: self.disconnectDisPlacement(),bgc=[0.4,0.1,0.3])
		mc.button(label=u"连接置换贴图",h=30,c=lambda*args: self.connectDisPlacement(),bgc=[0.4,0.5,0.4])
		mc.button(label=u"删除置换节点",h=30,c=lambda*args: self.deleteDisplacement(),bgc=[0.2,0.1,0.4])
		mc.showWindow("DisplacementShaderAndShadingUI")
