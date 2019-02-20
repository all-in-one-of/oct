# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import string

def selectTransparency():
	allShape=[]
	allMaterial = mc.ls(type=['blinn','lambert','phong','phongE','surfaceShader','aiStandard','VRayMtl'])
	for mater in allMaterial:
		transpImage=""
		try:
			transpImage=mc.listConnections("%s.transparency"%mater,s=True,d=False,plugs=True)
		except:
			pass
		if not transpImage:
			try:
				transpImage=mc.listConnections("%s.opacity"%mater,s=True,d=False,plugs=True)
			except:
				pass
		if not transpImage:
			try:
				transpImage=mc.listConnections("%s.outTransparency"%mater,s=True,d=False,plugs=True)
			except:
				pass

		if transpImage:
			mc.select(d=True)
			mc.hyperShade(objects=mater)
			allSelect=mc.ls(sl=True)
			for i in allSelect:
				allShape.append(i)
	if allShape:
		mc.select(allShape)
		if mc.objExists("TransparencyImage"):
			mc.sets(cl="TransparencyImage")
			mc.sets(add="TransparencyImage")
		else:
			mc.sets(n="TransparencyImage")
	else:
		if mc.objExists("TransparencyImage"):
			mc.delete("TransparencyImage")