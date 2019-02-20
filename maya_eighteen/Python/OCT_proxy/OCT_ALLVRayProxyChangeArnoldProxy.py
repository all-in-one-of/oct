# -*- coding: UTF-8 -*-  
import maya.cmds as mc
import maya.mel as mm 
import os 
def proxyChange():
	allVRayMesh=mc.ls(type='VRayMesh')
	allArnoldProxy=[]
	for VRays in allVRayMesh:
		mc.setAttr("%s.showBBoxOnly"%VRays,0)
		mc.setAttr("%s.showWholeMesh"%VRays,1)
		mc.select(d=True)
		mc.select(VRays,r=True)
		mm.eval("vray restoreMesh %s;"%VRays)
		path_VRay=mc.getAttr("%s.fileName2"%VRays)
		path_ArnoldName=os.path.splitext(path_VRay)[0]
		mc.select("%s_restored"%VRays)
		path_ArnoldName=mc.file(path_ArnoldName,force=True,options="-mask 25;-lightLinks 0;-shadowLinks 0",type="ASS Export",pr=True,es=True)
		mc.file(path_ArnoldName,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")
		allArnold=mc.ls(type="aiStandIn")
		name=mc.listConnections("ArnoldStandInDefaultLightSet.dagSetMembers")[-1]
		shapes=mc.listConnections(VRays,s=False,d=True)
		for sh in shapes:
			if mc.objectType(sh)=='transform' or mc.objectType(sh)=='mesh':
				transX=mc.getAttr("%s.translateX"%sh)
				transY=mc.getAttr("%s.translateY"%sh)
				transZ=mc.getAttr("%s.translateZ"%sh)

				rotateX=mc.getAttr("%s.rotateX"%sh)
				rotateY=mc.getAttr("%s.rotateY"%sh)
				rotateZ=mc.getAttr("%s.rotateZ"%sh)

				scaleX=mc.getAttr("%s.scaleX"%sh)
				scaleY=mc.getAttr("%s.scaleY"%sh)
				scaleZ=mc.getAttr("%s.scaleZ"%sh)

				mc.setAttr("%s.translateX"%name,transX)
				mc.setAttr("%s.translateY"%name,transY)
				mc.setAttr("%s.translateZ"%name,transZ)

				mc.setAttr("%s.rotateX"%name,rotateX)
				mc.setAttr("%s.rotateY"%name,rotateY)
				mc.setAttr("%s.rotateZ"%name,rotateZ)

				mc.setAttr("%s.scaleX"%name,scaleX)
				mc.setAttr("%s.scaleY"%name,scaleY)
				mc.setAttr("%s.scaleZ"%name,scaleZ)
				mc.delete(sh)

		try:
			mc.delete(VRays)
			mc.delete("%s_restored"%VRays)
		except:
			pass

proxyChange()	