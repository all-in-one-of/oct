#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
import shutil,os,re

class OCT_VRayProxyChangeModel():
	def __init__(self):
		pass
	def VRayChangeModel(self):
		allVRayMeshs=mc.ls(type='VRayMesh')
		for VRaymeshs in allVRayMeshs:
			try:
				Trans=mc.listConnections("%s"%VRaymeshs,s=False,d=True)
				if mc.objectType(Trans[0])=="transform":
					mc.setAttr("%s.showBBoxOnly"%VRaymeshs,0)
					mc.setAttr("%s.showWholeMesh"%VRaymeshs,1)
					mm.eval('vray restoreMesh %s;'%VRaymeshs)
					getTranslate=mc.getAttr("%s.translate"%Trans[0])[0]
					getRotate=mc.getAttr("%s.rotate"%Trans[0])[0]
					getScale=mc.getAttr("%s.scale"%Trans[0])[0]

					mc.setAttr('%s_restored.translate'%VRaymeshs,getTranslate[0],getTranslate[1],getTranslate[2])
					mc.setAttr('%s_restored.rotate'%VRaymeshs,getRotate[0],getRotate[1],getRotate[2])
					mc.setAttr('%s_restored.scale'%VRaymeshs,getScale[0],getScale[1],getScale[2])
					mc.delete(Trans)
					mc.delete(VRaymeshs)
					mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
		
			except ValueError:
				print "The %s node is missing"
#OCT_VRayProxyChangeModel().VRayChangeModel()