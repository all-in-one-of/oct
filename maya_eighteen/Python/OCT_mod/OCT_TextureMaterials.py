# -*- coding: utf-8 -*-

import maya.cmds as mc
import os 

class OCT_TextureMaterial():
	def __init__(self):
		self.arnoldOpacity=[]

	def FindArnoldOpacity(self):
		allArnold=mc.ls(type="aiStandard")
		flag = False
		for arn in allArnold:
			if mc.listConnections("%s.opacity"%arn) or mc.getAttr("%s.opacity"%arn)!= [(1.0, 1.0, 1.0)]:
				suferName=mc.listConnections("%s.outColor"%arn,d=True,s=False)
				if not suferName:
					continue
				if suferName:
					for sur in suferName:
						if mc.objectType(sur) == "layeredShader":
							flag = True
							break
				if flag:
					self.arnoldOpacity.append(arn)
				else:
					if mc.objectType(suferName[0])!="shadingEngine" :
						continue
					dagSetMembers=mc.listConnections(suferName[0]+".dagSetMembers")
					if not dagSetMembers:
						continue
					self.arnoldOpacity.append(arn)	
				

		self.textureMaterial(flag)

	def textureMaterial(self,flag):
		if self.arnoldOpacity:
			for arnOpacity in self.arnoldOpacity:
				aiRaySName=mc.listConnections(arnOpacity+".outColor")
				if mc.objectType(aiRaySName[0])=="aiRaySwitch":
					continue
				aiRaySwitchName=mc.shadingNode("aiRaySwitch",asShader=True)
				aiRaySwitchSGName=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(aiRaySwitchName+"SG"))
				mc.connectAttr(("%s.outColor"%aiRaySwitchName),("%s.surfaceShader"%aiRaySwitchSGName))
			
				# mc.hyperShade(objects=arnOpacity)
				# mc.hyperShade(assign=aiRaySwitchName)

				duplicateArnold=mc.duplicate(arnOpacity,inputConnections=True,name=(arnOpacity+"Refraction"))
				mc.connectAttr(("%s.outColor"%duplicateArnold[0]),("%s.refraction"%aiRaySwitchName))

				connectOpacity=mc.listConnections(("%s.Ks"%duplicateArnold[0]),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.Ks"%duplicateArnold[0]))
				
				mc.setAttr(("%s.Ks"%duplicateArnold[0]),0)

				duplicateArnold=mc.duplicate(arnOpacity,inputConnections=True,name=(arnOpacity+"Reflection"))
				mc.connectAttr(("%s.outColor"%duplicateArnold[0]),("%s.reflection"%aiRaySwitchName))

				connectOpacity=mc.listConnections(("%s.Ks"%duplicateArnold[0]),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.Ks"%duplicateArnold[0]))

				mc.setAttr(("%s.Ks"%duplicateArnold[0]),0)

				duplicateArnold=mc.duplicate(arnOpacity,inputConnections=True,name=(arnOpacity+"glossy"))
				mc.connectAttr(("%s.outColor"%duplicateArnold[0]),("%s.glossy"%aiRaySwitchName))
				
				connectOpacity=mc.listConnections(("%s.opacity"%duplicateArnold[0]),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.opacity"%duplicateArnold[0]))
				
				mc.setAttr(("%s.opacity"%duplicateArnold[0]),1,1,1,type="double3")

				connectOpacity=mc.listConnections(("%s.Ks"%duplicateArnold[0]),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.Ks"%duplicateArnold[0]))

				mc.setAttr(("%s.Ks"%duplicateArnold[0]),0)

				duplicateArnold=mc.duplicate(arnOpacity,inputConnections=True,name=(arnOpacity+"diffuse"))
				mc.connectAttr(("%s.outColor"%duplicateArnold[0]),("%s.diffuse"%aiRaySwitchName))
				connectOpacity=mc.listConnections(("%s.opacity"%duplicateArnold[0]),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.opacity"%duplicateArnold[0]))
				mc.setAttr(("%s.opacity"%duplicateArnold[0]),1,1,1,type="double3")


				mc.connectAttr(("%s.outColor"%arnOpacity),("%s.shadow"%aiRaySwitchName))
				mc.connectAttr(("%s.outColor"%arnOpacity),("%s.camera"%aiRaySwitchName))

				connectOpacity=mc.listConnections(("%s.Kr"%arnOpacity),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.Kr"%arnOpacity))
				mc.setAttr(("%s.Kr"%arnOpacity),0)
				mc.setAttr(("%s.enableInternalReflections"%arnOpacity),1)

				connectOpacity=mc.listConnections(("%s.Kt"%arnOpacity),d=False, s=True,plugs=True)
				if connectOpacity:
					mc.disconnectAttr(connectOpacity[0],("%s.Kt"%arnOpacity))

				mc.setAttr(("%s.Kt"%arnOpacity),0)

				if flag:
					allLayert = mc.listConnections(arnOpacity,d=True,s=False,plugs = True,c = True)
					for i in range(len(allLayert)/2):
						if mc.objectType(allLayert[i*2+1].split('.')[0]) == "layeredShader" and ".transparency" in allLayert[i*2+1]:
							print "dddd"
							name = os.path.splitext(allLayert[i*2+1])[0]
							mc.removeMultiInstance(name,b = True)
							mc.connectAttr("%s.outColor"%aiRaySwitchName, "%s.color"%name, f = True)
							mc.connectAttr("%s.outTransparency"%aiRaySwitchName, "%s.transparency"%name, f = True)	
				else:
					connectiRaySwitchMesh=mc.listConnections(aiRaySwitchSGName+".dagSetMembers")
					for con in connectiRaySwitchMesh:
						mc.setAttr(("%s.aiOpaque"%con),0)

#OCT_TextureMaterial().FindArnoldOpacity()
