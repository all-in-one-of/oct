# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.OpenMaya as om
import sys, os, string, re
import threading
import maya.mel as mm


def delDefaultRenderLayer():
	layers = mc.ls(exactType='renderLayer')
	count = 0
	pattern = re.compile('^[a-zA-Z0-9_\:-]*defaultRenderLayer$')
	for eachLayer in layers:
		if pattern.match(eachLayer):
			if not eachLayer == 'defaultRenderLayer':
				try:
					mc.delete(eachLayer)
				except:
					om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
				else:
					count += 1
	del pattern
	
	allmylayers = mc.listConnections("renderLayerManager.renderLayerId")
	for layer in layers:
		if not layer in allmylayers:
			try:
				mc.delete(layer)
			except:
				pass
			else:
				count += 1
	om.MGlobal.displayInfo(u'一共清除了%d 个defaultRenderLayer' % count)
	
	print 'delDefaultRenderLayer() successful...........'