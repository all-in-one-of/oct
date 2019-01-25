#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
# -*- coding: cp936 -*- 
# -*- coding: utf-8 -*- 
import maya.cmds as mc
def repWin():
	winName = 'repWindow'
	if mc.window(winName, ex = True):
		mc.deleteUI(winName)
	winWH = [210,100]
	mc.window(winName,wh = winWH)
	mc.columnLayout(adj = True,rs = 10,cat = ['both',5])
	mc.separator(st = 'none')
	mc.text(l = '²Î¿Œ¹ØÁªžŽÖÆ²ÄÖÊÐÞžŽ¹€Ÿß')
	mc.separator()
	mc.rowLayout(nc = 2,cw2 = [100,100])
	# mc.button(l = 'Ñ¡ÔñÐÞžŽ',w = 90,h = 30,c = 'import repairTex;repairTex.repairTexture(ty = 1)')
	# mc.button(l = 'È«²¿ÐÞžŽ',w = 90,h = 30,c = 'import repairTex;repairTex.repairTexture(ty = 0)')
	mc.button(l = 'Ñ¡ÔñÐÞžŽ',w = 90,h = 30,c = 'OCT_mod.repairTex_YJL.repairTexture(ty = 1)')
	mc.button(l = 'È«²¿ÐÞžŽ',w = 90,h = 30,c = 'OCT_mod.repairTex_YJL.repairTexture(ty = 0)')
	
	mc.setParent('..')
	mc.showWindow(winName)
	mc.window(winName,e = True,wh = winWH)
	
def repairTexture(ty = 0):
	if ty:
		selObj = mc.listRelatives(mc.ls(sl = True)[0],c = True,s = True,type = 'mesh',f = True)[0]
		if mc.reference(selObj,inr = True):
			links = mc.ls('%s.instObjGroups[*]'%selObj)
			for link in links:
				linkConAttr = mc.connectionInfo('%s.objectGroups[0]'%link,ges = True)
				sgNode = mc.connectionInfo(linkConAttr,dfs = True)[0]
				mc.disconnectAttr(linkConAttr,sgNode)
				mc.connectAttr(link,sgNode,f = True)
	else:
		objs = [o for o in mc.ls(s = True,l= True,type = 'mesh') if  mc.reference(o,inr = True)]
		for obj in objs:
			if mc.objExists('%s.instObjGroups.objectGroups[0]'%obj):
				lins = mc.ls('%s.instObjGroups[*]'%obj)
				for lin in lins:
					if mc.connectionInfo('%s.objectGroups[0]'%lin,isSource = True):
						linConAttr = mc.connectionInfo('%s.objectGroups[0]'%lin,ges = True)
						sgNod = mc.connectionInfo(linConAttr,dfs = True)[0]
						mc.disconnectAttr(linConAttr,sgNod)
						mc.connectAttr(lin,sgNod,f = True)
	