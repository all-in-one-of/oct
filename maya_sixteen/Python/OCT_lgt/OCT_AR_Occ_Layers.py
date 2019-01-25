# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import string
import maya.OpenMaya as om

class OCT_Ar_Occ_Layers():
	def __init__(self):
		self.allMaterial=[]
		self.defaultMaterial=""
	def LS_All_Material(self):
		allShadingEngine=mc.ls(type="shadingEngine")
		for shading in allShadingEngine:
			if shading!="initialParticleSE" and shading!="initialShadingGroup":
				conn=mc.listConnections("%s.surfaceShader"%shading)
				if conn:
					self.allMaterial.append(conn[0])
			elif shading=="initialShadingGroup":
				conn=mc.listConnections("%s.surfaceShader"%shading)
				self.defaultMaterial=shading

		self.arnoldShader_Occ()

	def arnoldShader_Occ(self):
		for Mater in self.allMaterial:
			transp=""
			try:
				transp=mc.listConnections("%s.transparency"%Mater,s=True,d=False,plugs=True)[0]
			except:
				pass
			try:
				transp=mc.listConnections("%s.opacity"%Mater,s=True,d=False,plugs=True)[0]
			except:
				pass
			if transp:
				try:
					mc.disconnectAttr(transp,"%s.transparency"%Mater)
				except:
					pass
				try:
					mc.disconnectAttr(transp,"%s.opacity"%Mater)
				except:
					pass
				
				aiAmbienNode=mc.shadingNode("aiAmbientOcclusion",asShader=True)
				tran=transp.split(".")[0]
				mc.connectAttr("%s.outColor"%tran,"%s.opacity"%aiAmbienNode,f=True)
				connections = mc.listConnections(Mater,s=False,d=True,connections=True,plugs=True)
				if connections:
					for i in range(0,len(connections),2):
						origPlug = connections[i]
						dstPlug = connections[i+1]
						replacePlug = string.replace(origPlug,Mater,aiAmbienNode)
						try:
							mc.disconnectAttr(origPlug,dstPlug)
							mc.connectAttr(replacePlug,dstPlug)
						except:
							om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
			else:
				aiAmbienNode=mc.shadingNode("aiAmbientOcclusion",asShader=True)
				connections = mc.listConnections(Mater,s=False,d=True,connections=True,plugs=True)
				if connections:
					for i in range(0,len(connections),2):
						origPlug = connections[i]
						dstPlug = connections[i+1]
						replacePlug = string.replace(origPlug,Mater,aiAmbienNode)

						try:
							mc.disconnectAttr(origPlug,dstPlug)
							mc.connectAttr(replacePlug,dstPlug)
						except:
							om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))

		if self.defaultMaterial:
			aiAmbienNode=mc.shadingNode("aiAmbientOcclusion",asShader=True)
			aiAmbienNodeSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(aiAmbienNode+"SG"))
			try:
				mc.hyperShade(objects=Mater)
				mc.hyperShade(assign=surfaceNode)
			except:
				pass
				
		allMeshs=mc.ls(type="mesh")
		for m in allMeshs:
			mc.setAttr("%s.aiOpaque"%m,0)

				
#OCT_Ar_Occ_Layers().LS_All_Material()