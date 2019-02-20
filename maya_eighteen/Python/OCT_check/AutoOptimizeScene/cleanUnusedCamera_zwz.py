# -*- coding: utf-8 -*-
#import maya.OpenMaya as om
import maya.cmds as mc


def cleanUnusedCamera_zwz():
	allLight = mc.ls(type='light')
	for myLight in allLight:
		myTLights = mc.listRelatives(myLight, p=True, path=True)
		for myTLight in myTLights:
			myAllSLights = mc.listRelatives(myTLight, c=True, path=True)
			for mySLight in myAllSLights:
				if mc.objectType(mySLight) == 'camera':
					mc.delete(mySLight)
					
	print 'cleanUnusedCamera_zwz() successful...........'