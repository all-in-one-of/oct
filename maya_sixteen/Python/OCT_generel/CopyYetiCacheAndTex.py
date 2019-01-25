#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import maya.cmds as mc
import shutil

OCT_DRIVE = r'\\octvision.com\cg'

sourcePath=mc.workspace(expandName="sourceimages")
CachePath=mc.workspace(expandName="cache")
type_file = 'cache'

def myChangeNetPath(TempPath):
    if TempPath.find('${OCTV_PROJECTS}') >= 0:
        TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
    elif TempPath.find('z:') >= 0:
        TempPath = TempPath.replace('z:', OCT_DRIVE)
    elif TempPath.find('Z:') >= 0:
        TempPath = TempPath.replace('Z:', OCT_DRIVE)
    return TempPath
def copyYetiCacheAndTex():
	allYetiCacheFiles = mc.ls(type='pgYetiMaya')
	if allYetiCacheFiles:
	    for myYetiCacheFile in allYetiCacheFiles:
	    	#yeti缓存
	        YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
	        if YetiCachePath:
	            YetiCachePath = myChangeNetPath(YetiCachePath)
	            YetiCachePath = os.path.normpath(YetiCachePath)

	            YetiCacheBasePath=os.path.basename(YetiCachePath)

	            oldPathCache=os.path.dirname(YetiCachePath)
	            YetiPath=oldPathCache.split(type_file)[-1]
	            YetiPath=CachePath+YetiPath
	            YetiPath=YetiPath.replace("/","\\")
	            cacheFiles=mc.getFileList(fld=(oldPathCache+"\\"))
	            if not os.path.isdir(YetiPath):
	            	os.makedirs(YetiPath)
	            print YetiPath
	            for caches in cacheFiles:
	            	print(oldPathCache+"\\"+caches)
	            	shutil.copy((oldPathCache+"\\"+caches),YetiPath)
	            	#mc.sysFile((oldPathCache+"\\"+caches),copy=YetiPath)

	            mc.setAttr('%s.cacheFileName' % myYetiCacheFile, (YetiPath+"\\"+YetiCacheBasePath),type='string')
	            os.startfile(YetiPath)
	        #yeti贴图
	        YetiTexPath = mc.getAttr('%s.imageSearchPath' % myYetiCacheFile)
	        if YetiTexPath:
	        	YetiCachePath = myChangeNetPath(YetiCachePath)
	        	YetiTexPath=YetiTexPath.replace("/","\\")
	        	YetiTexPath =os.path.normpath(YetiTexPath)
	        	YetiPath=YetiTexPath.split("sourceimages")[-1]
	        	YetiPath=sourcePath+YetiPath
	        	YetiPath=YetiPath.replace("/","\\")
	        	YetiTexFiles=mc.getFileList(fld=(YetiTexPath+"\\"))
	        	print YetiTexFiles
	        	if not os.path.isdir(YetiPath):
	        		os.makedirs(YetiPath)
	        	for Tex in YetiTexFiles:
	        		print(YetiTexPath+"\\"+Tex)
	        		shutil.copy((YetiTexPath+"\\"+Tex),YetiPath)

	        	mc.setAttr('%s.imageSearchPath' % myYetiCacheFile, YetiPath,type='string')
	        	os.startfile(YetiPath)