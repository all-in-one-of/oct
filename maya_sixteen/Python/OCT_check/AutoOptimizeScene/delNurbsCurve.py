# -*- coding: utf-8 -*-
import maya.cmds as mc
import sys

sys.setdefaultencoding('utf8')  

def delNurbsCurve():
	allNurbsCurve=mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
	if allNurbsCurve:
		for i in allNurbsCurve:
			if mc.objectType(i)=='nurbsCurve':
				mc.delete(i)
	else:
		allNurbsCurve=mc.ls(type='nurbsCurve')
		for i in allNurbsCurve:
			mc.delete(i)

	print 'delNurbsCurve() successful...........'