#!/usr/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import re
import os 

class OCT_ChangeFrameRate():
	def __init__(self):
		pass

	def frameRate(self):
		mc.currentUnit(time='film')
		startTime=mc.playbackOptions(q=True,min=True)
		if startTime%1>0:
			startTime=startTime//1+1
			startTime=mc.playbackOptions(min=startTime)
				
		endTime=mc.playbackOptions(q=True,max=True)
		if endTime%1>0:
			endTime=endTime//1+1
			endTime=mc.playbackOptions(max=endTime)
			
		animCurves=mc.ls(type="animCurve")
		for animCurve in animCurves:
			connections=mc.listConnections(animCurve,source=True,destination=False)
			#排除set driven keyframeCount
			#设置第一个帧为关键帧
			if not connections:
				#startLoction=mc.keyframe(animCurve,q=True,t=(startTime,startTime),eval=True)
				#mc.setKeyframe(animCurve,v=startLoction[0],t=startTime)
				keyframeCount=mc.keyframe(animCurve,q=True,keyframeCount=True)
		    	for num in range(keyframeCount):
		    		Frames=mc.keyframe(animCurve,index=(num,num),q=True)
		    		if Frames and Frames[0]%1>0:
		    			myFrame=Frames[0]//1+1
		    			frameLocation=mc.keyframe(animCurve,q=True,t=(Frames[0],Frames[0]),eval=True)
		    			mc.setKeyframe(animCurve,v=frameLocation[0],t=myFrame)
		    			mc.cutKey(animCurve,time=(Frames[0],Frames[0]))
		    		else:
		    			continue
	  		else:
	  			continue

#OCT_ChangeFrameRate().frameRate()