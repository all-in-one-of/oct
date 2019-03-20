#!/usr/bin/env python
# coding=utf-8

import sys
import maya.utils as mu
import maya.cmds as mc
import maya.OpenMaya as om

#sys.path.append(r'D:\MayaSixteenScripts\Python')
#sys.path.append(r'D:\MayaSixteenScripts')
#sys.path.append(r'\\octvision.com\cg\Tech\maya_sixteen\Python')
#sys.path.append(r'\\octvision.com\cg\Tech\maya_sixteen')
# import OCT_about
# #加载摄像机插件
# try:
#     OCT_about.source()
#     mu.executeDeferred("import maya.OpenMaya as om;om.MGlobal.displayInfo(u'Register command complete: IC_getAngle')")
# except:
#     mu.executeDeferred("import maya.OpenMaya as om;om.MGlobal.displayError(u'加载界面时出现异常1,请联系管理员.')")
# 加载PYQT
#sys.path.append(r'F:\Development\octProj\oct\maya_sixteen\Python')
mu.executeDeferred("from Python import *;import custom2016OCTV ")


