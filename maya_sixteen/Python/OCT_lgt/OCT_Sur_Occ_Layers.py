# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

class OCT_Sur_Occ_Layers():
	def __init__(self):
		self.allMaterial=[]
	def LS_All_Material(self):
		allShadingEngine=mc.ls(type="shadingEngine")
		for shading in allShadingEngine:
			if shading!="initialParticleSE" and shading!="initialShadingGroup":
				conn=mc.listConnections("%s.surfaceShader"%shading)
				if conn:
					self.allMaterial.append(conn[0])

		mc.setAttr("miDefaultOptions.maxRayDepth",20)
		mc.setAttr("miDefaultOptions.maxRefractionRays",10)
		mc.setAttr("miDefaultOptions.finalGather",1)
		mc.setAttr("miDefaultOptions.finalGatherRays",100)
		mc.setAttr("miDefaultOptions.finalGatherPresampleDensity",1)
		mc.setAttr("miDefaultOptions.finalGatherPoints",10)
		self.surfaceShader_Occ()

	def surfaceShader_Occ(self):
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
				surfaceNode=mc.shadingNode("surfaceShader",asShader=True)
				surfaceNodeSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(surfaceNode+"SG"))
				mc.connectAttr("%s.outColor"%surfaceNode,"%s.surfaceShader"%surfaceNodeSG,f=True)

				mib_fg_occlNode=mc.shadingNode("mib_fg_occlusion",asShader=True)
				mc.connectAttr("%s.outValue"%mib_fg_occlNode,"%s.outColor"%surfaceNode,f=True)

				mib_transpNode=mc.shadingNode("mib_transparency",asShader=True)
				mc.connectAttr("%s.outValue"%mib_transpNode,"%s.miMaterialShader"%surfaceNodeSG)

				mc.connectAttr("%s.outValueA"%mib_fg_occlNode,"%s.inputA"%mib_transpNode)
				mc.connectAttr("%s.outValue"%mib_fg_occlNode,"%s.input"%mib_transpNode)

				tran=transp.split(".")[0]
				mc.connectAttr("%s.outColor"%tran,"%s.transp"%mib_transpNode)
				mc.connectAttr("%s.outAlpha"%tran,"%s.transpA"%mib_transpNode)

				mc.setAttr("%s.invert"%tran,1)

				mc.hyperShade(objects=Mater)
				mc.hyperShade(assign=surfaceNode)
			else:
				surfaceNode=mc.shadingNode("surfaceShader",asShader=True)
				surfaceNodeSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(surfaceNode+"SG"))
				mc.connectAttr("%s.outColor"%surfaceNode,"%s.surfaceShader"%surfaceNodeSG,f=True)

				mib_fg_occlNode=mc.shadingNode("mib_fg_occlusion",asShader=True)
				mc.connectAttr("%s.outValue"%mib_fg_occlNode,"%s.outColor"%surfaceNode,f=True)

				try:
					mc.hyperShade(objects=Mater)
					mc.hyperShade(assign=surfaceNode)

				except:
					pass
				

#OCT_Sur_Occ_Layers().LS_All_Material()				
